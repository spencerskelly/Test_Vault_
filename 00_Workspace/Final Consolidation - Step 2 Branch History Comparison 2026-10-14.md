# Final Consolidation — Step 2 Branch History Comparison (2026-10-14)

**Evidence scope:** GitHub compare API against `main` for eight sampled branches, not yet a full 48-branch ledger. Figures are branch-ahead commit counts, *not* change requests or proof of missing live files. Both main and sampled consolidation descendants are divergent; compare results had truncated file listings at 300 for Step22 and P03. Do not use those file lists for exhaustive preservation.

| Branch | Compare status | Ahead | Behind | Classification |
| --- | --- | ---: | ---: | --- |
| `ai/importer-v0.8-folder-cap-75` | behind | 0 | 212 | Potential retire, subject to local work/reference checks |
| `mdse-workbench-dashboard-definition-20260930` | behind | 0 | 502 | Potential retire, subject to local work/reference checks |
| `integration/lean-test-infrastructure-20261013` | diverged | 8 | 2 | Reconcile unique changes |
| `wb106-release-integration` | diverged | 8 | 145 | Reconcile unique changes |
| `recovery/repository-consolidation-2026-10-09` | diverged | 24 | 2 | Preserve recovery evidence |
| `consolidate/test-vault-single-authority-20261012` | diverged | 175 | 2 | Active audit branch; preserve notes |
| `consolidation/step22-single-repo-cutover-2026-10-11` | diverged | 1809 | 2 | Engineering cutover input; history includes imported work |
| `integration/p03-legacy-compat-tests-20261013` | diverged | 1942 | 2 | Engineering validation candidate; exact head requires new CI |

Merge base for seven branches compared to main was `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e`. Behind-only branches had older merge bases. None of the sampled comparisons authorizes deletion.

## Next action
Complete a scoped comparison of remaining branch tips against the *candidate integration head*, not only main; record exact tip SHAs and any unique changes. Prioritize eight previously-held divergent branches and open PR heads; preserve work as exact refs before an owner-approved deletion batch. Then build a reviewed clean integration target. Do not bulk-merge historical steps, delete branches, change main, issue releases, or accept real QEAX until independent gates are met.
