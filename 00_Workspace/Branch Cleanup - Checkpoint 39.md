# Branch Cleanup — Checkpoint BR-39: Exact Divergent-Commit Audit Packet

**Date:** 2026-10-12
**Repository:** `spencerskelly/Test_Vault_`
**Audit PR:** #41
**Comparison reference:** `consolidation/step22-single-repo-cutover-2026-10-11` @ `58ab10870f11757cf1bf367ecd5868be9b60933d`
**Status:** FOUR BRANCHES HELD; commit enumeration required before branch retirement.

## Verified GitHub history counts (refreshed BR-39)

| Held historical branch | Exclusive commits | Step22-exclusive commits | Git merge base SHA |
|---|---:|---:|---|
| `wb106-release-integration` | **8** | 1952 | `bfdcecafefc5a35f894d3eb8541e676b9f8165b4` |
| `integration/importer-reconciliation-2026-10-09` | **6** | 644 | `75eff6007af46e19f36f76b38df44658ac381ba5` |
| `integration/bom-a14-reconciliation-2026-10-09` | **2** | 128 | `c922067c7aa0cf6ae2dbc1035527f1a7c4ee27ad` |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | **1** | 1806 | `bfefb8ee0c03dd613a8695662fbcc25112bc90c2` |

**Total: 17 branch-exclusive commits across these four held branches.** This is not the global total across every held branch (recovery and Base Vault snapshots still require their own held-ref resolution).

GitHub connector compare exposes counts/merge base and branch-side file statistics but not a complete branch-exclusive SHA list. Direct local `git ls-remote` in this execution environment failed DNS resolution for GitHub; therefore exact exclusive commit SHAs were **not** obtained in this pass. Do not fabricate identities or claim reviewed 17 commits. The historical-only CI files and tip-content checks are recorded in BR-33–BR-35.

## Deterministic, READ-ONLY Git SHA enumeration

Run from an *approved local clone* after confirming remote origin is the intended repository. This performs a fetch (updates **remote-tracking refs only**, not local working files/branches), plus read-only comparisons; do not use it on a locally modified reference without contributor consent.

```bash
set -euo pipefail
git remote get-url origin
git status --short --branch
git fetch --no-tags origin \
 '+refs/heads/consolidation/step22-single-repo-cutover-2026-10-11:refs/remotes/origin/consolidation/step22-single-repo-cutover-2026-10-11' \
 '+refs/heads/wb106-release-integration:refs/remotes/origin/wb106-release-integration' \
 '+refs/heads/integration/importer-reconciliation-2026-10-09:refs/remotes/origin/integration/importer-reconciliation-2026-10-09' \
 '+refs/heads/integration/bom-a14-reconciliation-2026-10-09:refs/remotes/origin/integration/bom-a14-reconciliation-2026-10-09' \
 '+refs/heads/integration/workbench-monorepo-rehearsal-2026-10-09:refs/remotes/origin/integration/workbench-monorepo-rehearsal-2026-10-09'
base='origin/consolidation/step22-single-repo-cutover-2026-10-11'
test "$(git rev-parse "$base")" = '58ab10870f11757cf1bf367ecd5868be9b60933d'
for b in \
 'origin/wb106-release-integration' \
 'origin/integration/importer-reconciliation-2026-10-09' \
 'origin/integration/bom-a14-reconciliation-2026-10-09' \
 'origin/integration/workbench-monorepo-rehearsal-2026-10-09'
do
  printf '\nBRANCH %s\n' "$b"
  git rev-list --count "$base..$b"
  git log --reverse --format='%H | %cs | %s' "$base..$b"
  git diff --name-status "$base" "$b"
done
```

**Do not paste raw output into a public PR until reviewed for confidential paths, private commit messages and model contents.** Send sanitized exact SHAs and commit subjects privately to the owner/auditor, then record classifications only.

## Per-commit classification form

For each of 17 branch-exclusive commits, record privately: full SHA; parent SHA(s); summary; relevant paths; whether the commit is a historical CI fixture, superseded implementation, necessary source-only change, provenance/documentation, or uncertain; exact corresponding Step22 blob/test evidence if preserved; reviewer; and disposition (PRESERVED, HISTORICAL_EVIDENCE, MIGRATE_REVIEW_REQUIRED, or HOLD). Do not cherry-pick history simply because a commit is exclusive. Recheck tip-to-tip trees and code behavior before concluding equivalence.

## Stops and independent requirements

- `wb106-release-integration`: an old workflow has `contents: write` and push behavior; **do not reactivate**. The older manifest version 0.1.17 must not replace Step22 version 0.1.18 without review.
- Importer validator was previously proven byte-identical on Step22 (BR-33); historical CI workflows on 3 integration branches must not be restored automatically (BR-33/34).
- S1: QEAX archive publication classification and potential response remain security owner-only, pending (BR-37).
- S2: contributor clones, local branches, stashes, worktrees and unpublished state remain unverified; private signoff procedure in BR-38.
- W/document-control, actual Mac/Windows Obsidian GUI acceptance, pinned release/checker and latest PR review evidence remain separate holds.

**BR-39 completed:** Frozen four-branch exact ancestry baseline, delivered executable read-only evidence acquisition commands and per-commit decision rubric, documented tool network boundary. **Not completed:** actual SHA enumeration or owner signoffs.

**NEXT BR-40:** Work an independent evidence gate that is verifiable through GitHub (PR #39 latest CI/approval state and governance cross-check), or ingest a privately reviewed sanitized 17-commit SHA list from authorized workstation; do not repeat these counts without new evidence.

**NO destructive action:** No PR closure, branch deletion, merge, history rewrite, release promotion or model export.
