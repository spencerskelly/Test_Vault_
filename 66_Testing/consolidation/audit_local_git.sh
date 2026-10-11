#!/bin/sh
# Step 05 — READ ONLY. Never fetches, resets, cleans, stages, commits, or pushes.
# Run separately for every local clone, e.g. sh audit_local_git.sh "/path/to/MDSE_Workbench"
set -eu
export LC_ALL=C
input=${1:-.}
if ! command -v git >/dev/null 2>&1; then
  echo 'ERROR: git is not installed' >&2
  exit 2
fi
if ! root=$(git -C "$input" rev-parse --show-toplevel 2>/dev/null); then
  echo 'ERROR: path is not inside a Git worktree' >&2
  exit 2
fi
printf '%s\n' 'MDSE_LOCAL_GIT_AUDIT=v1' 'READ_ONLY=true' 'FETCH_PERFORMED=false'
printf 'REPOSITORY_DIRECTORY=%s\n' "$(basename "$root")"
head=$(git -C "$root" rev-parse HEAD)
printf 'HEAD_SHA=%s\n' "$head"
branch=$(git -C "$root" symbolic-ref --quiet --short HEAD 2>/dev/null || true)
printf 'CURRENT_BRANCH=%s\n' "${branch:-DETACHED}"
status=$(git -C "$root" status --porcelain=v1 --untracked-files=all)
printf '%s\n' "$status" | awk 'NF {if (substr($0,1,2)=="??") untracked++; else tracked++} END {printf "TRACKED_DIRTY_ENTRIES=%d\nUNTRACKED_ENTRIES=%d\n",tracked+0,untracked+0}'
git -C "$root" for-each-ref --format='%(refname)' refs/heads | awk 'END {printf "LOCAL_BRANCH_COUNT=%d\n",NR+0}'
git -C "$root" stash list --format='%H' | awk 'END {printf "STASH_COUNT=%d\n",NR+0}'
git -C "$root" worktree list --porcelain | awk '/^worktree / {n++} END {printf "WORKTREE_COUNT=%d\n",n+0}'
printf 'SHALLOW=%s\n' "$(git -C "$root" rev-parse --is-shallow-repository)"
printf '%s\n' 'BRANCH_AHEAD_BEHIND_BEGIN'
git -C "$root" for-each-ref --format='%(refname:short)|%(upstream:short)|%(objectname)' refs/heads | while IFS='|' read -r name upstream sha; do
  [ -n "$name" ] || continue
  if [ -z "$upstream" ]; then
    printf 'BRANCH=%s UPSTREAM=NONE AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_LOCAL_ONLY\n' "$name"
  else
    counts=$(git -C "$root" rev-list --left-right --count "refs/heads/$name...$upstream" 2>/dev/null || true)
    if [ -z "$counts" ]; then
      printf 'BRANCH=%s UPSTREAM=%s AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=UNRESOLVED\n' "$name" "$upstream"
    else
      set -- $counts
      printf 'BRANCH=%s UPSTREAM=%s AHEAD=%s BEHIND=%s STATUS=LOCAL_REMOTE_TRACKING_ONLY\n' "$name" "$upstream" "${1:-UNKNOWN}" "${2:-UNKNOWN}"
    fi
  fi
done
printf '%s\n' 'BRANCH_AHEAD_BEHIND_END' 'NOTE=Remote-tracking refs may be stale: no network access or fetch was performed.' 'NOTE=Ignored files, other clones, remote-only branches, and the content of stashes are not audited.' 'NOTE=Output includes local branch names; review locally and redact before sharing.'
