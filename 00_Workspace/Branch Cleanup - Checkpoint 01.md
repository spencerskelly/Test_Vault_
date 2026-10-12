# Branch cleanup — checkpoint 01: inventory and triage

Date: 2026-10-12
Status: COMPLETE for naming-family inventory; NOT permission to merge/delete
Source: live GitHub branch and open PR search for `spencerskelly/Test_Vault_` on 2026-10-12.
Target: three durable branches maximum (`main`, `develop`, `test`); short-lived feature branches only as needed. These targets are proposals; `develop` and `test` have not been created.

## Observed inventory

46 remote branches:
- `main`: 1
- `consolidation/*`: 22 (original single-authority 2026-10-10 and sequential step02 through step22, ending 2026-10-11)
- `integration/*`: 12 (Workbench import, Local Model, importer, BOM, release and acceptance staging)
- `consolidate/*`: 1 (2026-10-12 single-authority proposal, PR #41)
- `ai/*`: 1 (importer folder cap)
- `importer/*`: 1 (importer baseline contract)
- `recovery/*`: 1 (repository consolidation)
- `base-vault-*`: 3
- `ci-probe-*`: 2
- `mdse-workbench-dashboard-definition-20260930`: 1
- `wb106-release-integration`: 1

36 open PRs (#5–#39, #41; #40 absent from open results). 2 merged PRs were identified in the preceding checkpoint. Verify complete closed PR history separately.

## Preliminary disposition (NOT merge/deletion approval)

- **KEEP:** `main` as the approved baseline.
- **CANDIDATE:** `consolidation/step22-single-repo-cutover-2026-10-11` for preserving the most recent *stacked* consolidation sequence. Comparison from prior checkpoint: 1809 commits ahead of main, 0 behind; huge history includes imported Workbench commits, not necessarily 1809 independent changes.
- **REVIEW/DEDUPE:** 21 earlier `consolidation/*` branches; the PR descriptions say they're stacked. Before cleanup prove their unique commits and accepted artifacts are reachable from the selected candidate.
- **REVIEW/DEDUPE:** 12 `integration/*` branches; preserve unique source and test artifacts not found in selected consolidation head.
- **REVIEW:** `consolidate/test-vault-single-authority-20261012` (this branch / PR #41) duplicates consolidation direction; its single documentation commit may be incorporated into the existing consolidation candidate, after review, rather than forming a second roadmap.
- **REVIEW:** 9 other non-main/non-consolidation/non-integration branches (importer, AI, recovery, base, CI probes, dashboard, WB106). Check merge status, unique commits, PR associations and release dependencies before proposing deletion.
- **HOLD:** all branches/PRs pending provenance, approvals and independent verification. No mergers, ref deletions, source rewrites, schema promotions or standalone repo archival made in this checkpoint.

## Risks found in existing PR descriptions

- PR #39 indicates Workbench source was staged under `55_Workbench/` and notes approval/security/local-clone prerequisites remain.
- PR #37 states Mac/Windows Obsidian GUI acceptance NOT RUN and Local Model 0.6 writer / variantOf proposal not enabled.
- PR #35 flags document-control classification pending despite passing technical CI.
- Branch existence is not evidence of independent useful work, but neither is age evidence of safe deletion.

## Next bounded task (02)

Compare `consolidation/step22-single-repo-cutover-2026-10-11` with representative earlier consolidation heads for ahead/behind, and inspect the PR base/head stack. Produce a branch-specific KEEP/INCLUDED/UNIQUE/UNKNOWN ledger. Do not merge or delete. Repeat in batches of at most 6–8 branches.

## Handoff

STEP: BR-01
STATUS: PASS — family inventory, no content-level clearance
SOURCE: GitHub live branch and open-PR lists, 2026-10-12
OUTPUT: this document (PR #41 feature branch)
CHECK: 1+22+12+1+1+1+1+3+2+1+1 = 46; open PRs=36
NEXT: BR-02 — first 6–8 ancestry checks
OPEN: all unique-change proof; unpushed local branches/worktrees; PR disposition; security and GUI approvals
