# MDSE consolidation Step 06. Offline, read-only Git inventory; NOT archival sign-off.
# Windows PowerShell 5.1+; run per clone with -Path. No fetch, reset, clean, stage, commit or push.
[CmdletBinding()]
param([string]$Path = '.')
$ErrorActionPreference = 'Stop'
$env:GIT_OPTIONAL_LOCKS = '0'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'git is not installed' }
$root = (& git -C $Path rev-parse --show-toplevel 2>$null)
if ($LASTEXITCODE -ne 0 -or -not $root) { throw 'not a Git worktree' }
$root = [string]($root | Select-Object -First 1)
$head = & git -C $root rev-parse --verify HEAD 2>$null
if ($LASTEXITCODE -ne 0 -or -not $head) { throw 'unborn/invalid HEAD; review manually' }
$status = @(& git -C $root -c core.quotePath=true status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0) { throw 'git status failed' }
$tracked = 0; $untracked = 0
foreach ($line in $status) {
    if (-not $line) { continue }
    if ($line.StartsWith('??')) { $untracked++ } else { $tracked++ }
}
$branch = & git -C $root symbolic-ref --quiet --short HEAD 2>$null
if ($LASTEXITCODE -ne 0 -or -not $branch) { $branch = 'DETACHED' }
$refs = @(& git -C $root for-each-ref '--format=%(refname:short)' refs/heads | Where-Object { $_ })
if ($LASTEXITCODE -ne 0) { throw 'cannot read branch refs' }
$stashes = @(& git -C $root stash list '--format=%H' | Where-Object { $_ })
$worktrees = @(& git -C $root worktree list --porcelain | Where-Object { $_ -match '^worktree ' })
$remotes = @(& git -C $root remote | Where-Object { $_ })
$shallow = & git -C $root rev-parse --is-shallow-repository
'MDSE_LOCAL_GIT_AUDIT=v2'
'READ_ONLY_INTENT=true'; 'GIT_OPTIONAL_LOCKS=0'; 'FETCH_PERFORMED=false'
'REPOSITORY_DIRECTORY=' + (Split-Path -Path $root -Leaf)
'HEAD_SHA=' + $head
'CURRENT_BRANCH=' + $branch
'TRACKED_DIRTY_ENTRIES=' + $tracked
'UNTRACKED_ENTRIES=' + $untracked
'LOCAL_BRANCH_COUNT=' + $refs.Count
'STASH_COUNT=' + $stashes.Count
'WORKTREE_COUNT=' + $worktrees.Count
'REMOTE_COUNT=' + $remotes.Count
'SHALLOW=' + $shallow
if ($branch -eq 'DETACHED') { 'DETACHED_HEAD_REVIEW=REQUIRED' }
else { 'DETACHED_HEAD_REVIEW=NOT_APPLICABLE' }
'BRANCH_AHEAD_BEHIND_BEGIN'
foreach ($name in $refs) {
    $upref = & git -C $root for-each-ref '--format=%(upstream)' "refs/heads/$name"
    if ($LASTEXITCODE -ne 0) { throw 'cannot read upstream refs' }
    $upref = [string]($upref | Select-Object -First 1)
    if (-not $upref) {
        'BRANCH=' + $name + ' UPSTREAM=NONE AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_NO_UPSTREAM'
        continue
    }
    $upstream = & git -C $root for-each-ref '--format=%(upstream:short)' "refs/heads/$name"
    $upstream = [string]($upstream | Select-Object -First 1)
    if ($upref.StartsWith('refs/remotes/')) { $upkind = 'REMOTE_TRACKING' }
    else { $upkind = 'LOCAL_OR_OTHER' }
    $pair = & git -C $root rev-list --left-right --count "refs/heads/$name...$upref" 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $pair) {
        'BRANCH=' + $name + ' UPSTREAM=' + $upstream + ' UPSTREAM_TYPE=' + $upkind + ' AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_UPSTREAM_UNRESOLVED'
        continue
    }
    $parts = ([string]($pair | Select-Object -First 1)).Trim() -split '\s+'
    $ahead = [int]$parts[0]; $behind = [int]$parts[1]
    if ($upkind -ne 'REMOTE_TRACKING') { $result = 'REVIEW_LOCAL_UPSTREAM' }
    elseif ($ahead -gt 0 -and $behind -gt 0) { $result = 'REVIEW_DIVERGED' }
    elseif ($ahead -gt 0) { $result = 'REVIEW_AHEAD' }
    elseif ($behind -gt 0) { $result = 'REVIEW_BEHIND' }
    else { $result = 'REMOTE_TRACKING_ONLY_NOT_VERIFIED' }
    'BRANCH=' + $name + ' UPSTREAM=' + $upstream + ' UPSTREAM_TYPE=' + $upkind + ' AHEAD=' + $ahead + ' BEHIND=' + $behind + ' STATUS=' + $result
}
'BRANCH_AHEAD_BEHIND_END'
'ARCHIVE_SIGNOFF=NOT_CERTIFIED'
'NOTE=Remote-tracking refs may be stale; GitHub synchronization is NOT verified.'
'NOTE=Ignored files, lost/unreferenced commits, other clones, submodule contents and stash contents are NOT audited.'
'NOTE=Only run on trusted local paths; redact repository and branch names before sharing.'
