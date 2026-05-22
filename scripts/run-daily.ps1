<#
.SYNOPSIS
    Daily wrapper for social-daily-report. Designed for Windows Task Scheduler.

.DESCRIPTION
    Resolves repo root from this script's location, activates the venv,
    runs the pipeline for all topics, logs everything to logs/YYYY-MM-DD.log,
    and propagates the exit code so Task Scheduler can flag failures.

.PARAMETER Topic
    Restrict to a single topic. Defaults to all topics in config/sources.yaml.

.PARAMETER Date
    Override the report date label. 'today' | 'yesterday' | 'YYYY-MM-DD'.

.NOTES
    Requires .env on the company PC with at least:
        LLM_BACKEND=cli         (or 'api' with ANTHROPIC_API_KEY)
        XQUIK_API_KEY=xq_...    (only if any topic enables connector: x)

    Run from Task Scheduler with "Run only when user is logged on" — the CLI
    backend needs the OAuth keychain populated by `claude login`, which is
    bound to the interactive Windows user session.
#>

[CmdletBinding()]
param(
    [string]$Topic = $null,
    [string]$Date  = "today"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

# Resolve venv python; fall back to system python if missing.
$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $VenvPython)) {
    $VenvPython = (Get-Command python -ErrorAction Stop).Source
    Write-Warning ".venv not found; using $VenvPython"
}

# Logs dir is sibling of data/; gitignored.
$LogDir = Join-Path $RepoRoot "logs"
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}
$Today  = (Get-Date).ToString("yyyy-MM-dd")
$LogFile = Join-Path $LogDir "$Today.log"

# Build args
$Args = @("-m", "social_report.cli", "run", "--date", $Date)
if ($Topic) { $Args += @("--topic", $Topic) }

$Header = @(
    "===== social-daily-report run @ $(Get-Date -Format o) ====="
    "  repo:    $RepoRoot"
    "  python:  $VenvPython"
    "  args:    $($Args -join ' ')"
    "============================================================"
) -join "`n"

Add-Content -Path $LogFile -Value $Header -Encoding UTF8

# Tee output to log AND stdout so Task Scheduler "Last Run Result" gets the exit code,
# while a human can tail the log.
$ExitCode = 0
try {
    & $VenvPython @Args 2>&1 | Tee-Object -FilePath $LogFile -Append
    $ExitCode = $LASTEXITCODE
} catch {
    Add-Content -Path $LogFile -Value "FATAL: $_" -Encoding UTF8
    $ExitCode = 1
}

# Auto-commit + push today's reports so Vercel redeploys without manual work.
# Only runs on a clean pipeline (exit 0); skips silently if there's nothing to
# commit or `git` is unavailable. Failure here doesn't fail the whole task —
# the reports are already on disk; deploy is a nice-to-have.
if ($ExitCode -eq 0 -and (Get-Command git -ErrorAction SilentlyContinue)) {
    try {
        $Changed = git -C $RepoRoot status --porcelain "content/reports/$Today" 2>$null
        if ($Changed) {
            git -C $RepoRoot add "content/reports/$Today" 2>&1 | Out-Null
            $Commit = "Daily reports $Today (auto)"
            git -C $RepoRoot commit -m $Commit 2>&1 | Tee-Object -FilePath $LogFile -Append
            git -C $RepoRoot push origin main 2>&1 | Tee-Object -FilePath $LogFile -Append
            Add-Content -Path $LogFile -Value "deploy: pushed to origin/main" -Encoding UTF8
        } else {
            Add-Content -Path $LogFile -Value "deploy: no report changes to commit" -Encoding UTF8
        }
    } catch {
        Add-Content -Path $LogFile -Value "deploy: git push skipped ($_)" -Encoding UTF8
    }
}

$Footer = "===== exit $ExitCode @ $(Get-Date -Format o) =====`n"
Add-Content -Path $LogFile -Value $Footer -Encoding UTF8
exit $ExitCode
