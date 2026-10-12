# Branch cleanup — checkpoint BR-10: old importer, recovery, Base Vault and CI probes

Date: 2026-10-12
Status: PASS — ancestry triage only; no approval to merge or delete
Target: `consolidation/step22-single-repo-cutover-2026-10-11`

## Live GitHub compare results

Each source branch is the `base`; Step 22 is `head`. Accordingly `ahead` means commits exclusive to Step 22; `behind` means commits exclusive to the source branch.

| Source branch | Comparison status | Step22 ahead | Source branch-only | Disposition |
|---|---|---:|---:|---|
| `ai/importer-v0.8-folder-cap-75` | ahead | 2019 | 0 | Included in Step 22 |
| `importer/baseline-contract-2026-10-05` | ahead | 1334 | 0 | Included in Step 22 |
| `recovery/repository-consolidation-2026-10-09` | diverged | 1804 | 19 | Hold, inspect |
| `base-vault-2026-09-30-rel132-v04` | diverged | 2242 | 1 | Hold, inspect |
| `base-vault-2026-09-30-rel133-v05` | diverged | 2232 | 1 | Hold, inspect |
| `base-vault-2026-09-30-rel133-v051` | diverged | 2225 | 1 | Hold, inspect |
| `ci-probe-bootstrap-031` | diverged | 1897 | 3 | Hold, inspect |
| `ci-probe-bootstrap-artifact` | diverged | 1896 | 1 | Hold, inspect |

The six diverged branches contain 26 branch-exclusive commit *counts* summed across branches. They are not necessarily 26 distinct changes because branches may share commits. Net comparison files listing hit a 300-file response cap in these comparisons; source-level content analysis remains OPEN.

## Cumulative progress

- 21 earlier consolidation branch tips included in Step22 (BR-02–04).
- 9 integration branch tips included; 3 diverged with net effects reviewed (BR-05–09).
- 2 further old importer branches included (this step).
- New six diverged branches held for content/ancestry review.

DO NOT bulk-merge old recovery, Base Vault or CI branches. Before deletion, confirm unique commits and any needed fixtures/scripts are independently preserved. Avoid reactivating historical workflows.

## Next step

BR-11: compare the remaining miscellaneous branch heads (`mdse-workbench-dashboard-definition-20260930`, `wb106-release-integration`) and the 2026-10-12 PR #41 branch with Step22. Reconcile the branch inventory and decide which branch serves as the surviving cleanup ledger before any PR closure or deletion.

## Handoff
STEP: BR-10
STATUS: PASS — 8 branch ancestry checks
SOURCE: GitHub compare results 2026-10-12
OUTPUT: this file on PR #41
CHECK: 2 included, 6 diverged; 300-file listing cap means no content-level clearance
NEXT: BR-11
OPEN: legacy branch content, PR disposition, independent local work, data security and governance acceptance, GUI release testing.
