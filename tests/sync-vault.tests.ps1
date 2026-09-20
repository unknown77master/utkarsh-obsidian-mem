[CmdletBinding()]
param(
    [string]$ScriptUnderTest,
    [string[]]$Only
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($ScriptUnderTest)) {
    $ScriptUnderTest = Join-Path (Split-Path -Parent $PSScriptRoot) 'sync-vault.ps1'
}

function Assert-That {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw $Message }
}

function Invoke-TestGit {
    param([Parameter(Mandatory)][string]$Repository, [Parameter(Mandatory)][string[]]$Arguments)
    $previousErrorAction = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        $output = & git -c "safe.directory=$Repository" -C $Repository @Arguments 2>$null
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorAction
    }
    if ($exitCode -ne 0) {
        throw "Git command failed: git -C $Repository $($Arguments -join ' ')`n$($output -join [Environment]::NewLine)"
    }
    return @($output | ForEach-Object { "$_" })
}

function Write-FixtureFile {
    param([string]$Root, [string]$RelativePath, [string]$Content)
    $path = Join-Path $Root $RelativePath
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $path) | Out-Null
    Set-Content -LiteralPath $path -Value $Content -NoNewline
}

function New-Fixture {
    $base = Join-Path ([System.IO.Path]::GetTempPath()) ("sync-vault-tests-" + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $base | Out-Null
    $remote = Join-Path $base 'origin.git'
    Invoke-TestGit -Repository $base -Arguments @('init', '--bare', '--initial-branch=main', $remote) | Out-Null
    $seed = Join-Path $base 'seed'
    Invoke-TestGit -Repository $base -Arguments @('clone', $remote, $seed) | Out-Null
    Invoke-TestGit -Repository $seed -Arguments @('config', 'user.name', 'Sync Vault Test') | Out-Null
    Invoke-TestGit -Repository $seed -Arguments @('config', 'user.email', 'sync-vault@example.test') | Out-Null
    Write-FixtureFile $seed 'chatgpt-to-obsidian/utkarsh-vault/AGENTS.md' "# Test vault`nRaw exports are protected."
    Write-FixtureFile $seed 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "first`nsecond`nthird`n"
    Write-FixtureFile $seed 'chatgpt-to-obsidian/utkarsh-vault/Raw/Export/seed.json' '{}'
    Write-FixtureFile $seed 'chatgpt-to-obsidian/utkarsh-vault/.chatgpt-migration-state.json' '{}'
    Write-FixtureFile $seed 'chatgpt-to-obsidian/utkarsh-vault/.export-mirror-manifest.json' '{}'
    Invoke-TestGit -Repository $seed -Arguments @('add', '-A') | Out-Null
    Invoke-TestGit -Repository $seed -Arguments @('commit', '-m', 'seed') | Out-Null
    Invoke-TestGit -Repository $seed -Arguments @('push', 'origin', 'main') | Out-Null
    $client = Join-Path $base 'client'
    Invoke-TestGit -Repository $base -Arguments @('clone', $remote, $client) | Out-Null
    Invoke-TestGit -Repository $client -Arguments @('config', 'user.name', 'Sync Vault Test') | Out-Null
    Invoke-TestGit -Repository $client -Arguments @('config', 'user.email', 'sync-vault@example.test') | Out-Null
    return [pscustomobject]@{ Base = $base; Remote = $remote; Client = $client }
}

function Remove-Fixture {
    param([Parameter(Mandatory)]$Fixture)
    if ($Fixture.Base -notmatch 'sync-vault-tests-[0-9a-f]+$') { throw "Refusing to remove unexpected test path: $($Fixture.Base)" }
    Remove-Item -LiteralPath $Fixture.Base -Recurse -Force
}

function Add-RemoteCommit {
    param([Parameter(Mandatory)]$Fixture, [Parameter(Mandatory)][scriptblock]$Change, [string]$Message = 'remote change')
    $editor = Join-Path $Fixture.Base ("editor-" + [guid]::NewGuid().ToString('N'))
    Invoke-TestGit -Repository $Fixture.Base -Arguments @('clone', $Fixture.Remote, $editor) | Out-Null
    Invoke-TestGit -Repository $editor -Arguments @('config', 'user.name', 'Sync Vault Test') | Out-Null
    Invoke-TestGit -Repository $editor -Arguments @('config', 'user.email', 'sync-vault@example.test') | Out-Null
    & $Change $editor
    Invoke-TestGit -Repository $editor -Arguments @('add', '-A') | Out-Null
    Invoke-TestGit -Repository $editor -Arguments @('commit', '-m', $Message) | Out-Null
    Invoke-TestGit -Repository $editor -Arguments @('push', 'origin', 'main') | Out-Null
}

function Invoke-Sync {
    param([Parameter(Mandatory)][string]$Repository, [switch]$Preview)
    Push-Location $Repository
    try {
        $arguments = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $ScriptUnderTest)
        if ($Preview) { $arguments += '-Preview' }
        $previousErrorAction = $ErrorActionPreference
        try {
            $ErrorActionPreference = 'Continue'
            $output = & powershell.exe @arguments 2>&1
            $exitCode = $LASTEXITCODE
        } finally {
            $ErrorActionPreference = $previousErrorAction
        }
        return [pscustomobject]@{ ExitCode = $exitCode; Output = @($output | ForEach-Object { "$_" }) }
    } finally { Pop-Location }
}

function Test-Scenario {
    param([string]$Name, [scriptblock]$Body)
    if (@($Only).Count -gt 0 -and $Name -notin $Only) { return }
    $fixture = New-Fixture
    try {
        & $Body $fixture
        Write-Host "PASS $Name"
    } finally { Remove-Fixture $fixture }
}

if (-not (Test-Path -LiteralPath $ScriptUnderTest)) { throw "Script under test does not exist: $ScriptUnderTest" }

Test-Scenario 'A clean local repo + remote update' {
    param($f)
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/A.md' 'remote update' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That (Test-Path (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/A.md')) 'Remote update did not arrive.'
}

Test-Scenario 'B remote creates a new note' {
    param($f)
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/New Remote Note.md' 'new note' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That ((Get-Content -Raw (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/New Remote Note.md')) -eq 'new note') 'New remote note content is wrong.'
}

Test-Scenario 'C remote modifies an existing note' {
    param($f)
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "first`nremote second`nthird`n" }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That ((Get-Content -Raw (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md')) -match 'remote second') 'Remote modification did not arrive.'
}

Test-Scenario 'D local tracked file accidentally deleted' {
    param($f)
    $note = Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md'
    Remove-Item -LiteralPath $note
    $preview = Invoke-Sync $f.Client -Preview
    Assert-That ($preview.ExitCode -eq 0) ($preview.Output -join "`n")
    Assert-That (-not (Test-Path $note)) 'Preview changed the working tree.'
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That ((Get-Content -Raw $note) -match 'second') 'Missing tracked file was not restored.'
}

Test-Scenario 'E local file modified, remote unrelated file modified' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "local first`nsecond`nthird`n"
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote E.md' 'remote E' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That ((Get-Content -Raw (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md')) -match 'local first') 'Local edit was lost.'
    Assert-That (Test-Path (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote E.md')) 'Remote unrelated change was missing.'
}

Test-Scenario 'F same file changed locally and remotely on different lines' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "local first`nsecond`nthird`n"
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "first`nsecond`nremote third`n" }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    $content = Get-Content -Raw (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md')
    Assert-That ($content -match 'local first' -and $content -match 'remote third') 'Different-line edits did not merge.'
}

Test-Scenario 'G same lines changed locally and remotely conflict' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "first`nlocal second`nthird`n"
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' "first`nremote second`nthird`n" }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -ne 0) 'Conflicting changes unexpectedly succeeded.'
    $conflicts = Invoke-TestGit $f.Client @('diff', '--name-only', '--diff-filter=U')
    Assert-That ($conflicts -contains 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md') 'Expected Git conflict was not left for the user.'
    Assert-That ((Invoke-TestGit $f.Client @('stash', 'list')) -match 'vault-sync-') 'Temporary sync stash was not retained after conflict.'
}

Test-Scenario 'H existing staged local changes abort' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' 'staged change'
    Invoke-TestGit $f.Client @('add', 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md') | Out-Null
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -ne 0) 'Staged changes did not abort sync.'
    Assert-That ((Invoke-TestGit $f.Client @('diff', '--cached', '--name-only')) -contains 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md') 'Staged change was altered.'
}

Test-Scenario 'I existing unrelated Git stash is left untouched' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' 'user stash'
    Invoke-TestGit $f.Client @('stash', 'push', '--message', 'user stash') | Out-Null
    $before = Invoke-TestGit $f.Client @('stash', 'list', '--format=%s')
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote I.md' 'remote I' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    $after = Invoke-TestGit $f.Client @('stash', 'list', '--format=%s')
    Assert-That (($before -join "`n") -eq ($after -join "`n")) 'Existing user stash changed.'
}

Test-Scenario 'J untracked local file is preserved' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/local-only.md' 'keep me'
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote J.md' 'remote J' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -eq 0) ($result.Output -join "`n")
    Assert-That ((Get-Content -Raw (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/local-only.md')) -eq 'keep me') 'Untracked file was lost.'
}

Test-Scenario 'K diverged local and remote history aborts' {
    param($f)
    Write-FixtureFile $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Note.md' 'local commit'
    Invoke-TestGit $f.Client @('add', '-A') | Out-Null
    Invoke-TestGit $f.Client @('commit', '-m', 'local commit') | Out-Null
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote K.md' 'remote K' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -ne 0) 'Diverged history unexpectedly synced.'
    Assert-That (-not (Test-Path (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Projects/Remote K.md'))) 'Remote commit was merged despite divergence.'
}

Test-Scenario 'L protected incoming Raw Export path aborts' {
    param($f)
    Add-RemoteCommit $f { param($r) Write-FixtureFile $r 'chatgpt-to-obsidian/utkarsh-vault/Raw/Export/incoming.json' '{}' }
    $result = Invoke-Sync $f.Client
    Assert-That ($result.ExitCode -ne 0) 'Protected incoming change unexpectedly synced.'
    Assert-That (-not (Test-Path (Join-Path $f.Client 'chatgpt-to-obsidian/utkarsh-vault/Raw/Export/incoming.json'))) 'Protected remote file was applied.'
}

Write-Host 'All sync-vault scenarios passed.'
