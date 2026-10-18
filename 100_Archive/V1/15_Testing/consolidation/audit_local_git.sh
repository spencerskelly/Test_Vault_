#!/bin/sh
# MDSE consolidation Step 06. Offline, read-only Git *inventory*, NOT archival sign-off.
# git status is run with GIT_OPTIONAL_LOCKS=0 to avoid optional index refresh writes.
set -eu
export LC_ALL=C
export GIT_OPTIONAL_LOCKS=0
input=${1:-.}
command -v git >/dev/null 2>&1 || { echo 'ERROR: git is not installed' >&2; exit 2; }
root=$(git -C "$input" rev-parse --show-toplevel 2>/dev/null) || { echo 'ERROR: not a Git worktree' >&2; exit 2; }
head=$(git -C "$root" rev-parse --verify HEAD 2>/dev/null) || { echo 'ERROR: unborn/invalid HEAD; review manually' >&2; exit 2; }
status=$(git -C "$root" -c core.quotePath=true status --porcelain=v1 --untracked-files=all) || { echo 'ERROR: git status failed' >&2; exit 2; }
counts=$(printf '%s\n' "$status" | awk 'NF {if(substr($0,1,2)=="??") u++; else t++} END{printf "%d %d",t+0,u+0}')
set -- $counts
tracked=${1:-0}; untracked=${2:-0}
branch=$(git -C "$root" symbolic-ref --quiet --short HEAD 2>/dev/null || true)
refs=$(git -C "$root" for-each-ref --format='%(refname:short)' refs/heads) || { echo 'ERROR: cannot read branch refs' >&2; exit 2; }
branch_count=$(printf '%s\n' "$refs" | awk 'NF{n++}END{print n+0}')
stash_count=$(git -C "$root" stash list --format='%H' | awk 'NF{n++}END{print n+0}')
worktree_count=$(git -C "$root" worktree list --porcelain | awk '/^worktree /{n++}END{print n+0}')
remote_count=$(git -C "$root" remote | awk 'NF{n++}END{print n+0}')
shallow=$(git -C "$root" rev-parse --is-shallow-repository)
printf '%s\n' 'MDSE_LOCAL_GIT_AUDIT=v2' 'READ_ONLY_INTENT=true' 'GIT_OPTIONAL_LOCKS=0' 'FETCH_PERFORMED=false'
printf 'REPOSITORY_DIRECTORY=%s\n' "$(basename "$root")"
printf 'HEAD_SHA=%s\nCURRENT_BRANCH=%s\n' "$head" "${branch:-DETACHED}"
printf 'TRACKED_DIRTY_ENTRIES=%s\nUNTRACKED_ENTRIES=%s\nLOCAL_BRANCH_COUNT=%s\n' "$tracked" "$untracked" "$branch_count"
printf 'STASH_COUNT=%s\nWORKTREE_COUNT=%s\nREMOTE_COUNT=%s\nSHALLOW=%s\n' "$stash_count" "$worktree_count" "$remote_count" "$shallow"
if [ -z "$branch" ]; then
  # Do not infer that detached HEAD is covered by another local branch.
  printf '%s\n' 'DETACHED_HEAD_REVIEW=REQUIRED'
else
  printf '%s\n' 'DETACHED_HEAD_REVIEW=NOT_APPLICABLE'
fi
printf '%s\n' 'BRANCH_AHEAD_BEHIND_BEGIN'
# Avoid delimited fields from Git refs; a valid ref can contain "|".
# Git branch refs cannot contain newlines, so read one branch name per line.
if [ -n "$refs" ]; then
  printf '%s\n' "$refs" | while IFS= read -r name; do
    [ -n "$name" ] || continue
    upref=$(git -C "$root" for-each-ref --format='%(upstream)' "refs/heads/$name")
    if [ -z "$upref" ]; then
      printf 'BRANCH=%s UPSTREAM=NONE AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_NO_UPSTREAM\n' "$name"
      continue
    fi
    upstream=$(git -C "$root" for-each-ref --format='%(upstream:short)' "refs/heads/$name")
    case "$upref" in
      refs/remotes/*) upkind=REMOTE_TRACKING ;;
      *) upkind=LOCAL_OR_OTHER ;;
    esac
    pair=$(git -C "$root" rev-list --left-right --count "refs/heads/$name...$upref" 2>/dev/null || true)
    if [ -z "$pair" ]; then
      printf 'BRANCH=%s UPSTREAM=%s UPSTREAM_TYPE=%s AHEAD=UNKNOWN BEHIND=UNKNOWN STATUS=REVIEW_UPSTREAM_UNRESOLVED\n' "$name" "$upstream" "$upkind"
      continue
    fi
    set -- $pair
    ahead=${1:-UNKNOWN}; behind=${2:-UNKNOWN}
    if [ "$upkind" != REMOTE_TRACKING ]; then
      result=REVIEW_LOCAL_UPSTREAM
    elif [ "$ahead" -gt 0 ] && [ "$behind" -gt 0 ]; then
      result=REVIEW_DIVERGED
    elif [ "$ahead" -gt 0 ]; then
      result=REVIEW_AHEAD
    elif [ "$behind" -gt 0 ]; then
      result=REVIEW_BEHIND
    else
      result=REMOTE_TRACKING_ONLY_NOT_VERIFIED
    fi
    printf 'BRANCH=%s UPSTREAM=%s UPSTREAM_TYPE=%s AHEAD=%s BEHIND=%s STATUS=%s\n' \
      "$name" "$upstream" "$upkind" "$ahead" "$behind" "$result"
  done
fi
printf '%s\n' 'BRANCH_AHEAD_BEHIND_END' 'ARCHIVE_SIGNOFF=NOT_CERTIFIED'
printf '%s\n' 'NOTE=Remote-tracking refs may be stale; GitHub synchronization is NOT verified.'
printf '%s\n' 'NOTE=Ignored files, lost/unreferenced commits, other clones, submodule contents and stash contents are NOT audited.'
printf '%s\n' 'NOTE=Only run on trusted local paths; redact repository and branch names before sharing.'
