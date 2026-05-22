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

$Footer = "===== exit $ExitCode @ $(Get-Date -Format o) =====`n"
Add-Content -Path $LogFile -Value $Footer -Encoding UTF8
exit $ExitCode
