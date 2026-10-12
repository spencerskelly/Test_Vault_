# Branch cleanup — checkpoint BR-05: first six integration branches

Date: 2026-10-12
Status: PASS for ancestry triage; divergent branch content NOT yet reviewed
Comparison head: `consolidation/step22-single-repo-cutover-2026-10-11`

## Live GitHub comparisons

GitHub compare uses each integration branch as `base`, Step 22 as `head`. Accordingly `ahead` counts commits exclusive to Step 22, and `behind` counts commits exclusive to the integration branch.

| Branch | Comparison status | Step 22 ahead | Integration-only commits | Disposition |
|---|---|---:|---:|---|
| `integration/bom-a14-reconciliation-2026-10-09` | diverged | 128 | 2 | HOLD: inspect two commits and tree effect |
| `integration/bom-a14-source-step15-2026-10-09` | ahead | 54 | 0 | Included in Step 22 |
| `integration/bom-governance-step16-2026-10-09` | ahead | 49 | 0 | Included in Step 22 |
| `integration/bom-real-qeax-step17-2026-10-09` | ahead | 48 | 0 | Included in Step 22 |
| `integration/importer-persisted-2026-10-09` | ahead | 133 | 0 | Included in Step 22 |
| `integration/importer-reconciliation-2026-10-09` | diverged | 644 | 6 | HOLD: inspect six commits and tree effect |

## Findings

Four branches have their committed histories wholly included in Step 22. Two diverged branches contain eight branch-exclusive commits combined, **not** necessarily eight unique features or useful changes. Commit-level and content-level reconciliation must precede promotion, closure or deletion.

Branch head comparison is not evidence of current effective source equivalence, external data security review, or GUI acceptance. No change to `main`, no merge/deletion/archival action.

## Handoff

STEP: BR-05
STATUS: PASS — first six integration branch ancestry checks
SOURCE: live GitHub compare on 2026-10-12
OUTPUT: this file on PR #41
CHECK: 4 included / 2 diverged, branch-only counts 2 and 6
NEXT: BR-06 — remaining six integration branches; BR-07 should inspect diverged branch-only commits and files
OPEN: all divergent content, PR approval, local unpublished work, QEAX safety, GUI testing
