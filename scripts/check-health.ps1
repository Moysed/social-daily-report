<#
.SYNOPSIS
    Hourly health check for social-daily-report. Posts to Discord on issues.

.DESCRIPTION
    Wraps `python -m social_report.monitor`. Same resolution logic as
    run-daily.ps1: finds the venv from $PSScriptRoot, logs to logs/, returns
    the monitor's exit code so Task Scheduler reflects unhealthy state.

    Exit codes:
        0 = healthy (or healthy + no webhook configured)
        2 = issues detected (alert was posted)
        3 = webhook POST failed
#>

[CmdletBinding()]
param(
    [switch]$Status   # forces a heartbeat post even when healthy
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $VenvPython)) {
    $VenvPython = (Get-Command python -ErrorAction Stop).Source
}

$LogDir = Join-Path $RepoRoot "logs"
if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir | Out-Null }
$LogFile = Join-Path $LogDir ("monitor-{0}.log" -f (Get-Date).ToString("yyyy-MM-dd"))

$MonitorArgs = @("-m", "social_report.monitor")
if ($Status) { $MonitorArgs += "--status" }

Add-Content -Path $LogFile -Value "----- $(Get-Date -Format o) -----" -Encoding UTF8
& $VenvPython @MonitorArgs 2>&1 | Tee-Object -FilePath $LogFile -Append
exit $LASTEXITCODE
