[CmdletBinding()]
param([switch]$Remove, [switch]$ReadOnly)
$ErrorActionPreference = 'Stop'
$taskName = 'Obsidian Memory Sync'
if ($Remove) {
    Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host 'Removed automatic startup. A manually started preview must be stopped separately.'
    exit
}
$python = (Get-Command python.exe -ErrorAction Stop).Source
$pythonWindowless = Join-Path (Split-Path -Parent $python) 'pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) {
    throw 'pythonw.exe is missing. Install Python 3.10 or newer with its windowless launcher.'
}
$scriptPath = Join-Path $PSScriptRoot 'vault-sync.py'
$arguments = '"' + $scriptPath + '" --interval 120 --port 8765'
if ($ReadOnly) { $arguments += ' --read-only' }
$userId = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$action = New-ScheduledTaskAction -Execute $pythonWindowless -Argument $arguments -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $userId
$principal = New-ScheduledTaskPrincipal -UserId $userId -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit ([TimeSpan]::Zero) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force | Out-Null
Start-ScheduledTask -TaskName $taskName
Write-Host 'Startup installed. Dashboard: http://127.0.0.1:8765'
Write-Host 'If the port is occupied by a preview, stop that preview before starting this task.'
