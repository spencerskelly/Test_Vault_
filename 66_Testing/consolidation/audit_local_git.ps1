# Step 05 — READ ONLY. Windows PowerShell 5.1+; no fetch, reset, clean, stage, commit, or push.
# Run separately for every local clone, e.g. .\audit_local_git.ps1 -Path 'C:\Vaults\MDSE_Workbench'
[CmdletBinding()]
param([string]$Path = '.')
$ErrorActionPreference = 'Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'git is not installed' }
$root = (& git -C $Path rev-parse --show-toplevel 2>$null)
if ($LASTEXITCODE -ne 0 -or -not $root) { throw 'path is not inside a Git worktree' }
$root = [string]($root | Select-Object -First 1)
$head = & git -C $root rev-parse HEAD
$branch = & git -C $root symbolic-ref --quiet --short HEAD 2>$null
if ($LASTEXITCODE -ne 0 -or -not $branch) { $branch = 'DETACHED' }
$status = @(& git -C $root status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0) { throw 'git status failed' }
$tracked = 0; $untracked = 0
foreach ($line in $status) {
  if (-not $line) { continue }
  if ($line.StartsWith('??')) { $untracked++ } else { $tracked++ }
}
$refs = @(& git -C $root for-each-ref '--format=%(refname:short)|%(upstream:short)|%(objectname)' refs/heads)
if ($LASTEXITCODE -ne 0) { throw 'git for-each-ref failed' }
$stashes = @(& git -C $root stash list '--format=%H' | Where-Object { $_ })
$worktrees = @(& git -C $root worktree list --porcelain | Where-Object { $_ -match '^worktree ' })
$shallow = & git -C $root rev-parse --is-shallow-repository
'READ_ONLY=true'; 'FETCH_PERFORMED=false'; 'MDSE_LOCAL_GIT_AUDIT=v1'
'REPOSITORY_DIRECTORY=' + [IO.Path]::GetFileName($root.TrimEnd('\','/'))
'HEAD_SHA=' + $head
'CURRENT_BRANCH=' + $branch
'TRACKED_DIRTY_ENTRIES=' + $tracked
'UNTRACKED_ENTRIES=' + $untracked
'LOCAL_BRANCH_COUNT=' + @($refs | Where-Object { $_ }).Count
'STASH_COUNT=' + @($stashes).Count
'WORKTREE_COUNT=' + @($worktrees).Count
'SHALLOW=' + $shallow
'BRANCH_AHEAD_BEHIND_BEGIN'
foreach ($line in $refs) {
  if (-not $line) { continue }
  $fields = $line -split '\|',3
  $name = $fields[0]; $upstream = $fields[1]
  if (-not $upstream) { 'BRANCH=' + $name + ' UPSTREAM=NONE AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_LOCAL_ONLY'; continue }
  $counts = & git -C $root rev-list --left-right --count "refs/heads/$name...$upstream" 2>$null
  if ($LASTEXITCODE -ne 0 -or -not $counts) { 'BRANCH=' + $name + ' UPSTREAM=' + $upstream + ' AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=UNRESOLVED'; continue }
  $parts = ([string]($counts | Select-Object -First 1)).Trim() -split '\s+'
  'BRANCH=' + $name + ' UPSTREAM=' + $upstream + ' AHEAD=' + $parts[0] + ' BEHIND=' + $parts[1] + ' STATUS=LOCAL_REMOTE_TRACKING_ONLY'
}
'BRANCH_AHEAD_BEHIND_END'
'NOTE=Remote-tracking refs may be stale: no network access or fetch was performed.'
'NOTE=Ignored files, other clones, remote-only branches, and stash contents are not audited.'
'NOTE=Output includes local branch names; review locally and redact before sharing.'
