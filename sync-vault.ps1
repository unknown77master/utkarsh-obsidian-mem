[CmdletBinding()]
param(
    [switch]$Preview
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Find-RepositoryCandidate {
    $candidate = (Resolve-Path -LiteralPath (Get-Location).Path).Path
    while ($true) {
        if (Test-Path -LiteralPath (Join-Path $candidate '.git')) {
            return $candidate
        }

        $parent = Split-Path -Parent $candidate
        if ([string]::IsNullOrWhiteSpace($parent) -or $parent -eq $candidate) {
            throw 'Run sync-vault.ps1 from inside the obsidian_mem Git working tree.'
        }
        $candidate = $parent
    }
}

$script:RepoRoot = Find-RepositoryCandidate

function Format-CommandOutput {
    param([object[]]$Output)
    return (@($Output | ForEach-Object { "$_" }) -join [Environment]::NewLine)
}

function Invoke-Git {
    param([Parameter(Mandatory)][string[]]$Arguments)

    $previousErrorAction = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        $output = & git -c "safe.directory=$script:RepoRoot" @Arguments 2>$null
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorAction
    }
    if ($exitCode -ne 0) {
        throw "Git command failed (exit $exitCode): git $($Arguments -join ' ')"
    }
    return @($output | ForEach-Object { "$_" })
}

function Invoke-GitResult {
    param([Parameter(Mandatory)][string[]]$Arguments)

    $previousErrorAction = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        $output = & git -c "safe.directory=$script:RepoRoot" @Arguments 2>$null
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorAction
    }
    return [pscustomobject]@{
        ExitCode = $exitCode
        Output   = @($output | ForEach-Object { "$_" })
    }
}

function Test-Git {
    param([Parameter(Mandatory)][string[]]$Arguments)

    & git -c "safe.directory=$script:RepoRoot" @Arguments 1>$null 2>$null
    return $LASTEXITCODE -eq 0
}

function Get-GitLines {
    param([Parameter(Mandatory)][string[]]$Arguments)

    return @(Invoke-Git $Arguments | Where-Object {
        -not [string]::IsNullOrWhiteSpace($_) -and
        "$_" -notmatch '^warning: unable to access .+[\\/]\.config[\\/]git[\\/]ignore'
    })
}

function Test-ProtectedPath {
    param([AllowEmptyString()][string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return $false
    }

    $normalized = $Path.Replace('\', '/')
    return (
        $normalized -match '^chatgpt-to-obsidian/utkarsh-vault/Raw/Export(?:/|$)' -or
        $normalized -match '(^|/)\.chatgpt-migration-state\.json$' -or
        $normalized -match '(^|/)\.export-mirror-manifest\.json$'
    )
}

function Get-ProtectedPaths {
    param([string[]]$Paths)
    return @($Paths | Where-Object { Test-ProtectedPath $_ } | Sort-Object -Unique)
}

function Get-OperationInProgress {
    $markers = @('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'BISECT_LOG', 'rebase-apply', 'rebase-merge')
    $active = foreach ($marker in $markers) {
        $gitPath = (Get-GitLines @('rev-parse', '--git-path', $marker) | Select-Object -First 1)
        $absolutePath = if ([System.IO.Path]::IsPathRooted($gitPath)) { $gitPath } else { Join-Path $script:RepoRoot $gitPath }
        if (Test-Path -LiteralPath $absolutePath) { $marker }
    }
    return @($active)
}

function Write-NameStatusList {
    param([Parameter(Mandatory)][string]$Title, [string[]]$Entries)

    Write-Host "${Title}:"
    if (@($Entries).Count -eq 0) {
        Write-Host '  none'
        return
    }
    foreach ($entry in $Entries) {
        $parts = $entry -split "`t", 2
        $prefix = switch -Regex ($parts[0]) {
            '^A' { '+'; break }
            '^D' { '-'; break }
            default { '~'; break }
        }
        $path = if ($parts.Count -gt 1) { $parts[1] } else { $entry }
        Write-Host "  $prefix $path"
    }
}

function Write-PathList {
    param([Parameter(Mandatory)][string]$Title, [Parameter(Mandatory)][string]$Prefix, [string[]]$Paths)

    Write-Host "${Title}:"
    if (@($Paths).Count -eq 0) {
        Write-Host '  none'
        return
    }
    foreach ($path in $Paths) { Write-Host "  $Prefix $path" }
}

function Find-SyncStash {
    param([Parameter(Mandatory)][string]$Identifier)

    foreach ($line in Get-GitLines @('stash', 'list', '--format=%H%x09%gd%x09%s')) {
        $parts = $line -split "`t", 3
        if ($parts.Count -eq 3 -and $parts[2] -like "*$Identifier*") {
            return [pscustomobject]@{ Commit = $parts[0]; Ref = $parts[1]; Subject = $parts[2] }
        }
    }
    return $null
}

function Stop-Sync {
    param([Parameter(Mandatory)][string]$Message)
    Write-Error $Message
    exit 1
}

try {
    $gitRoot = (Get-GitLines @('rev-parse', '--show-toplevel') | Select-Object -First 1)
    $resolvedGitRoot = (Resolve-Path -LiteralPath $gitRoot).Path.TrimEnd('\', '/')
    $resolvedCandidate = (Resolve-Path -LiteralPath $script:RepoRoot).Path.TrimEnd('\', '/')
    if ($resolvedGitRoot -ne $resolvedCandidate) {
        Stop-Sync 'The discovered Git root does not match the working-tree root.'
    }
    $script:RepoRoot = $resolvedGitRoot

    $vaultAgents = Join-Path $script:RepoRoot 'chatgpt-to-obsidian\utkarsh-vault\AGENTS.md'
    if (-not (Test-Path -LiteralPath $vaultAgents)) {
        Stop-Sync 'This is not the expected obsidian_mem repository: vault AGENTS.md is missing.'
    }

    $currentBranch = (Get-GitLines @('branch', '--show-current') | Select-Object -First 1)
    if ($currentBranch -ne 'main') {
        Stop-Sync "Vault sync only operates from main; current branch is '$currentBranch'."
    }

    $operations = @(Get-OperationInProgress)
    if ($operations.Count -gt 0) {
        Stop-Sync "A Git operation is already in progress ($($operations -join ', ')). Resolve or abort it before syncing."
    }

    if (-not ((Get-GitLines @('remote')) -contains 'origin')) {
        Stop-Sync 'Remote "origin" is not configured. Configure it before running vault sync.'
    }

    Invoke-Git @('fetch', 'origin') | Out-Null
    if (-not (Test-Git @('rev-parse', '--verify', 'refs/remotes/origin/main'))) {
        Stop-Sync 'origin/main does not exist after fetch; vault sync can only sync against origin/main.'
    }

    $headIsAncestor = Test-Git @('merge-base', '--is-ancestor', 'HEAD', 'origin/main')
    $originIsAncestor = Test-Git @('merge-base', '--is-ancestor', 'origin/main', 'HEAD')
    $divergence = if ($headIsAncestor -and $originIsAncestor) {
        'none'
    } elseif ($headIsAncestor) {
        'none'
    } elseif ($originIsAncestor) {
        'local branch is ahead of origin/main'
    } else {
        'local and origin/main histories have diverged'
    }

    $stagedChanges = @(Get-GitLines @('diff', '--cached', '--name-status', '--no-renames'))
    $missingTracked = @(Get-GitLines @('diff', '--name-only', '--diff-filter=D', '--no-renames'))
    $allTrackedWorkingChanges = @(Get-GitLines @('diff', '--name-only', '--no-renames'))
    $modifiedTracked = @($allTrackedWorkingChanges | Where-Object { $_ -notin $missingTracked })
    $untracked = @(Get-GitLines @('ls-files', '--others', '--exclude-standard'))
    $localProtected = @(Get-ProtectedPaths @($allTrackedWorkingChanges + $untracked))

    $remoteChanges = @(if ($headIsAncestor) {
        Get-GitLines @('diff', '--name-status', '--no-renames', 'HEAD', 'origin/main')
    } else { @() }
    )
    $remotePaths = @(if ($headIsAncestor) {
        Get-GitLines @('diff', '--name-only', '--no-renames', 'HEAD', 'origin/main')
    } else { @() }
    )
    $protectedIncoming = @(Get-ProtectedPaths $remotePaths)

    if ($Preview) {
        Write-NameStatusList -Title 'Remote' -Entries $remoteChanges
        Write-Host 'Local:'
        if ($modifiedTracked.Count -eq 0 -and $untracked.Count -eq 0 -and $missingTracked.Count -eq 0) {
            Write-Host '  none'
        } else {
            foreach ($path in $modifiedTracked) { Write-Host "  ~ $path" }
            foreach ($path in $untracked) { Write-Host "  ? $path" }
            foreach ($path in $missingTracked) { Write-Host "  - $path" }
        }
        Write-PathList -Title 'Missing tracked files to restore' -Prefix '-' -Paths $missingTracked
        Write-NameStatusList -Title 'Staged changes' -Entries $stagedChanges
        Write-PathList -Title 'Protected-path changes' -Prefix '!' -Paths @($localProtected + $protectedIncoming | Sort-Object -Unique)
        Write-Host "Branch divergence: $divergence"
        $safe = $stagedChanges.Count -eq 0 -and $localProtected.Count -eq 0 -and $protectedIncoming.Count -eq 0 -and $divergence -eq 'none'
        Write-Host "Safe to sync: $(if ($safe) { 'YES' } else { 'NO' })"
        exit $(if ($safe) { 0 } else { 1 })
    }

    if ($stagedChanges.Count -gt 0) {
        Stop-Sync "Sync aborted because staged changes are present. Commit, unstage, or otherwise resolve them first; this script will not guess whether they are intentional.`n$(Format-CommandOutput $stagedChanges)"
    }
    if ($localProtected.Count -gt 0) {
        Stop-Sync "Sync aborted because protected vault paths have local changes. The script will not stash or restore protected files:`n$($localProtected -join [Environment]::NewLine)"
    }
    if ($protectedIncoming.Count -gt 0) {
        Stop-Sync "Sync aborted because origin/main changes protected vault paths. Review and merge these manually:`n$($protectedIncoming -join [Environment]::NewLine)"
    }
    if ($divergence -ne 'none') {
        Stop-Sync "Sync aborted: $divergence. Resolve the history deliberately with normal Git commands before running this script again."
    }

    if ($missingTracked.Count -gt 0) {
        Invoke-Git (@('restore', '--source=HEAD', '--worktree', '--') + $missingTracked) | Out-Null
        Write-Host "Restored $($missingTracked.Count) accidentally missing tracked file(s) from HEAD."
    }

    $localEdits = @(Get-GitLines @('diff', '--name-only', '--no-renames'))
    $untrackedAfterRestore = @(Get-GitLines @('ls-files', '--others', '--exclude-standard'))
    $stash = $null
    if ($remoteChanges.Count -gt 0 -and ($localEdits.Count -gt 0 -or $untrackedAfterRestore.Count -gt 0)) {
        $stashId = "vault-sync-$((Get-Date).ToUniversalTime().ToString('yyyyMMddHHmmss'))-$([guid]::NewGuid().ToString('N'))"
        Invoke-Git @('stash', 'push', '--include-untracked', '--message', $stashId) | Out-Null
        $stash = Find-SyncStash $stashId
        if ($null -eq $stash) {
            Stop-Sync "Local work may have been stashed, but its unique sync stash could not be identified. No remote changes were applied. Run 'git stash list' and recover the stash before retrying."
        }
        Write-Host "Temporarily preserved local edits in $($stash.Ref)."
    }

    if ($remoteChanges.Count -gt 0) {
        try {
            Invoke-Git @('merge', '--ff-only', 'origin/main') | Out-Null
        } catch {
            if ($null -ne $stash) {
                Stop-Sync "Fast-forward failed. Your local work remains safely stored in $($stash.Ref) ($($stash.Commit)). No automatic recovery was attempted. Details: $($_.Exception.Message)"
            }
            throw
        }
        Write-Host "Fast-forwarded main from origin/main ($($remoteChanges.Count) remote change(s))."
    } else {
        Write-Host 'origin/main is already current.'
    }

    if ($null -ne $stash) {
        $apply = Invoke-GitResult @('stash', 'apply', $stash.Commit)
        if ($apply.ExitCode -ne 0) {
            Stop-Sync "The temporary stash could not be reapplied cleanly. Git left normal conflict state and retained the stash ($($stash.Ref), $($stash.Commit)); resolve conflicts with Git, then drop that exact stash only after confirming your work is present.`n$(Format-CommandOutput $apply.Output)"
        }

        $identifier = $stash.Subject.Substring($stash.Subject.IndexOf('vault-sync-'))
        $stashToDrop = Find-SyncStash $identifier
        if ($null -eq $stashToDrop -or $stashToDrop.Commit -ne $stash.Commit) {
            Stop-Sync "Local edits were reapplied, but the temporary stash could not be verified for safe removal. It was retained intentionally; inspect 'git stash list' before dropping it manually."
        }
        Invoke-Git @('stash', 'drop', $stashToDrop.Ref) | Out-Null
        Write-Host 'Reapplied local edits and removed only the temporary sync stash.'
    }

    $conflicts = @(Get-GitLines @('diff', '--name-only', '--diff-filter=U'))
    if ($conflicts.Count -gt 0) {
        Stop-Sync "Sync stopped with Git conflicts:`n$($conflicts -join [Environment]::NewLine)"
    }
    $remainingMissing = @(Get-GitLines @('diff', '--name-only', '--diff-filter=D', '--no-renames'))
    $unexpectedMissing = @($remainingMissing | Where-Object { -not (Test-ProtectedPath $_) })
    if ($unexpectedMissing.Count -gt 0) {
        Stop-Sync "Sync stopped because normal tracked files are still missing:`n$($unexpectedMissing -join [Environment]::NewLine)"
    }
    $finalProtected = @(Get-ProtectedPaths (Get-GitLines @('diff', '--name-only', '--no-renames')))
    if ($finalProtected.Count -gt 0) {
        Stop-Sync "Sync stopped because protected paths unexpectedly changed:`n$($finalProtected -join [Environment]::NewLine)"
    }
    if (-not (Test-Git @('diff', '--quiet', 'HEAD', 'origin/main'))) {
        Stop-Sync 'Sync stopped because HEAD is not aligned with origin/main after the fast-forward.'
    }

    $status = @(Get-GitLines @('status', '--short'))
    Write-Host 'Post-sync verification:'
    Write-Host '  HEAD matches origin/main: yes'
    Write-Host '  Conflicts: none'
    Write-Host '  Unexpected missing tracked files: none'
    Write-Host '  Protected files: untouched'
    Write-Host "  Working-tree entries remaining: $($status.Count) (preserved local edits may be listed)"
} catch {
    Stop-Sync $_.Exception.Message
}
