# Final Consolidation — Step 4 Complete Branch Ancestry Classification

Date: 2026-10-14. Reference `integration/p03-legacy-compat-tests-20261013`.

**Complete ancestry coverage:** GitHub reported 48 remote branches. All 47 other branch names were compared to the integration candidate (16 in Step 3, 30 in this step, plus `main` reference status previously compared indirectly). Of the **46 non-main, non-candidate** branches: **34 had zero ahead commits**; **12 were divergent**. `main` itself is 2 commits ahead of the integration candidate by prior compare, and thus counts as **13 divergent branches including main**, which must never be a deletion candidate. Totals: 34 + 13 + 1 = 48. Counts represent ancestry, not unmerged content or authorization to delete.

## Divergent branches requiring disposition
| Branch | Ahead of integration | Handling |
|---|---:|---|
| `main` | 2 (inferred from prior reciprocal comparison) | **Protect; explicitly reconcile** |
| `consolidate/test-vault-single-authority-20261012` | 176 at Step3 capture | Carry audit documentation |
| `recovery/repository-consolidation-2026-10-09` | 19 | Preserve recovery evidence |
| `integration/lean-test-infrastructure-20261013` | 8 | Compare CI/test improvements |
| `wb106-release-integration` | 8 | Review runtime source/provenance |
| `base-vault-2026-09-30-rel133-v051` | 1 | Release archive candidate |
| `ci-probe-bootstrap-031` | 3 | Probe archive candidate |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | 1 | Rehearsal evidence |
| `integration/bom-a14-reconciliation-2026-10-09` | 2 | Inspect BOM reconciliation |
| `integration/importer-reconciliation-2026-10-09` | 6 | Inspect importer reconciliation |
| `base-vault-2026-09-30-rel132-v04` | 1 | Release archive candidate |
| `base-vault-2026-09-30-rel133-v05` | 1 | Release archive candidate |
| `ci-probe-bootstrap-artifact` | 1 | Probe archive candidate |

**34 other branches were strictly behind the candidate** on Git ancestry, including consolidation Step 01–22, earlier Workbench subtree, importer persisted, BOM governance, Obsidian acceptance preparation, `ai/importer-v0.8-folder-cap-75`, and the historical Workbench dashboard. Do not delete without local unpublished-work check and PR/reference review.

## Critical boundaries
- Comparison results are branch-history facts at query time; candidate and audit tips can advance.
- 300-file API result limit prevents treating compare file lists on giant branches as exhaustive.
- Active PRs remain drafts. Exact candidate tip must pass CI, be reviewed, and reconcile main's own two commits before stable promotion.
- Real QEAX output with schema 0.2 is not approved as a current schema 0.5 golden model.
- No branch tags, merges, deletions, release approvals or main changes in this step.

## Step 5
Inspect the unique changed paths and semantics of `integration/bom-a14-reconciliation-2026-10-09`, `integration/importer-reconciliation-2026-10-09`, and main's two commits first. Then freeze an exact integration candidate and prepare a concise owner approval gate for merging. Treat historical probe/release heads as preserve-or-tag candidates, not silent cherry-pick requests.
