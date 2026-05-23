<#
.SYNOPSIS
    One-shot setup for the social-daily-report on a Windows host that will
    run the pipeline 24/7 (e.g. the company computer).

.DESCRIPTION
    Performs these steps interactively:
      1. Verify Python 3.11+ available.
      2. Create .venv and install the package (with the [mcp] extra).
      3. Verify `claude` is on PATH; offer to install/login.
      4. Verify .env has LLM_BACKEND + (XQUIK_API_KEY or ANTHROPIC_API_KEY).
      5. Sanity test the chosen backend.
      6. Register the daily Task Scheduler task at 10:00 local time.
      7. Test-trigger the task once and tail the log.

    Re-runnable: idempotent on steps that have already completed.

.NOTES
    Must be run from an elevated PowerShell ONLY if you need to register the
    task for All Users. Default registers under the current user (no admin).
#>

[CmdletBinding()]
param(
    [switch]$SkipTaskRegister,
    [string]$TaskName = "SocialDailyReport"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

function Step($n, $msg) { Write-Host "`n[$n] $msg" -ForegroundColor Cyan }
function Ok($msg)       { Write-Host "  ok: $msg"   -ForegroundColor Green }
function Warn($msg)     { Write-Host "  warn: $msg" -ForegroundColor Yellow }
function Fail($msg)     { Write-Host "  fail: $msg" -ForegroundColor Red; exit 1 }

# ---- 1. Python ----
# Find a real Python 3.11+, skipping Windows' Microsoft Store stub
# (which lives under %LOCALAPPDATA%\Microsoft\WindowsApps\python.exe and
# launches the Store instead of running). Order: py launcher (`py -3`),
# python3.exe, python.exe — first one that reports Python 3.11+ wins.
Step 1 "Verifying Python"
function Find-RealPython {
    $candidates = @()
    # `py -3` is the official launcher on Windows, never the Store stub.
    if (Get-Command py -ErrorAction SilentlyContinue) {
        $candidates += @{ Cmd = "py"; Args = @("-3") }
    }
    foreach ($name in @("python3", "python")) {
        $cmds = Get-Command -Name $name -All -ErrorAction SilentlyContinue
        foreach ($c in $cmds) {
            if ($c.Source -like "*WindowsApps\python*.exe") { continue } # store stub
            $candidates += @{ Cmd = $c.Source; Args = @() }
        }
    }
    foreach ($cand in $candidates) {
        $ver = & $cand.Cmd @($cand.Args + @("--version")) 2>&1
        if ($ver -match "Python 3\.(1[1-9]|[2-9]\d)") {
            return @{ Source = $cand.Cmd; Args = $cand.Args; Version = $ver }
        }
    }
    return $null
}
$pyInfo = Find-RealPython
if (-not $pyInfo) {
    Fail "Need Python 3.11+ on PATH. If `python.exe` opens the Microsoft Store: install Python from https://www.python.org/downloads/ (check 'Add to PATH'), then re-run. Or disable the Store stub in Settings -> Apps -> Advanced app settings -> App execution aliases."
}
$py = $pyInfo.Source
$pyArgs = $pyInfo.Args
Ok "$($pyInfo.Version) at $py $($pyArgs -join ' ')"

# ---- 2. venv + install ----
Step 2 "Creating venv + installing"
$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $VenvPython)) {
    & $py @($pyArgs + @("-m", "venv", ".venv"))
    Ok ".venv created"
} else {
    Ok ".venv exists"
}
& $VenvPython -m pip install --upgrade pip --quiet
& $VenvPython -m pip install -e ".[mcp]" --quiet
Ok "dependencies installed (with [mcp] extra)"

# ---- 3. Claude CLI ----
Step 3 "Verifying claude CLI"
$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
    Warn "claude not on PATH. Install Claude Code from https://claude.com/claude-code then re-run."
    Fail "missing dependency"
}
$claudeVer = & claude --version 2>&1
Ok "$claudeVer at $($claude.Source)"

# ---- 4. .env sanity ----
Step 4 "Checking .env"
$envPath = Join-Path $RepoRoot ".env"
if (-not (Test-Path $envPath)) {
    Copy-Item (Join-Path $RepoRoot ".env.example") $envPath
    Warn ".env created from .env.example -- edit it to set keys, then re-run"
    Fail "edit .env first"
}
$envText = Get-Content $envPath -Raw
$backend = if ($envText -match 'LLM_BACKEND\s*=\s*(\w+)') { $Matches[1] } else { "api" }
Ok "LLM_BACKEND = $backend"

if ($backend -eq "api" -and $envText -notmatch 'ANTHROPIC_API_KEY\s*=\s*\S+') {
    Fail "LLM_BACKEND=api but ANTHROPIC_API_KEY is empty in .env"
}

# ---- 5. Backend sanity ----
Step 5 "Sanity testing $backend backend"
if ($backend -eq "cli") {
    Push-Location ([System.IO.Path]::GetTempPath())
    $reply = & claude -p "Reply with only: OK" --model opus --output-format json --no-session-persistence 2>&1
    Pop-Location
    if ($reply -match '"result":"OK"') {
        Ok "claude -p subscription path works"
    } else {
        Warn "claude -p did not return OK -- you may need: claude login"
        Write-Host $reply
        $ans = Read-Host "Run 'claude login' now? (y/N)"
        if ($ans -eq "y") { claude login }
    }
} else {
    & $VenvPython -c "from social_report.analyze.client import make_llm_client; c = make_llm_client(); print('enabled:', c.enabled, 'backend:', c.backend)"
}

# ---- 6. Register Task Scheduler task ----
if (-not $SkipTaskRegister) {
    Step 6 "Registering Task Scheduler entry"
    $xmlTemplate = Join-Path $RepoRoot "scripts\social-daily-report.xml"
    $xmlFilled   = Join-Path $env:TEMP "social-daily-report-task.xml"
    (Get-Content $xmlTemplate -Raw) -replace '\{\{REPO_ROOT\}\}', $RepoRoot |
        Set-Content -Path $xmlFilled -Encoding Unicode

    schtasks.exe /Create /TN $TaskName /XML $xmlFilled /F | Out-Null
    Ok "task '$TaskName' registered (10:00 + 22:00 local (every 12h))"
    Remove-Item $xmlFilled

    # Optional: also register hourly Discord monitor if webhook is set.
    if ($envText -match 'MONITOR_DISCORD_WEBHOOK\s*=\s*https://') {
        $monXml      = Join-Path $RepoRoot "scripts\social-daily-report-monitor.xml"
        $monFilled   = Join-Path $env:TEMP "social-daily-report-monitor-task.xml"
        (Get-Content $monXml -Raw) -replace '\{\{REPO_ROOT\}\}', $RepoRoot |
            Set-Content -Path $monFilled -Encoding Unicode
        schtasks.exe /Create /TN "${TaskName}Monitor" /XML $monFilled /F | Out-Null
        Ok "task '${TaskName}Monitor' registered (hourly 09:00-00:00)"
        Remove-Item $monFilled
    } else {
        Warn "MONITOR_DISCORD_WEBHOOK not set in .env -- skipping hourly monitor task"
    }
} else {
    Warn "skipping task register (-SkipTaskRegister)"
}

# ---- 7. Test trigger ----
Step 7 "Test trigger -- runs the pipeline once now (ai-devtools only)"
$ans = Read-Host "Run a one-topic test now? (Y/n)"
if ($ans -ne "n") {
    & (Join-Path $RepoRoot "scripts\run-daily.ps1") -Topic "ai-devtools"
    Ok "see logs\$((Get-Date).ToString('yyyy-MM-dd')).log for output"
}

Write-Host "`nSetup complete." -ForegroundColor Green
Write-Host "Pipeline fires at 10:00 and 22:00 local (every 12h). Inspect with: schtasks /Query /TN $TaskName /V /FO LIST"
