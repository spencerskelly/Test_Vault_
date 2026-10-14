# Final Consolidation — Step 3 Candidate-Ancestry Review

Date: 2026-10-14
Compared against `integration/p03-legacy-compat-tests-20261013` using GitHub compare API. **Sampling: 16 branches, not all 48.** Commit-ahead counts are ancestry differences; they are not proof of missing production functionality. No branch deletion is authorized.

## Behind candidate (0 commits ahead)
| Branch | Behind |
|---|---:|
| `consolidation/step22-single-repo-cutover-2026-10-11` | 133 |
| `integration/bom-real-qeax-step17-2026-10-09` | 181 |
| `integration/obsidian-ui-acceptance-step18-2026-10-09` | 174 |
| `integration/workbench-lm05-2026-10-09` | 748 |
| `integration/importer-persisted-2026-10-09` | 266 |
| `integration/bom-governance-step16-2026-10-09` | 182 |
| `integration/workbench-subtree-2026-10-09` | 777 |
| `consolidation/step21-gui-evidence-sessions-2026-10-11` | 135 |
| `importer/baseline-contract-2026-10-05` | 1467 |

## Diverged (unique commits ahead)
| Branch | Ahead | Behind | Disposition |
|---|---:|---:|---|
| `consolidate/test-vault-single-authority-20261012` | 176 | 1942 | Preserve documentation/review decisions |
| `recovery/repository-consolidation-2026-10-09` | 19 | 1937 | Reconcile evidence, no blanket merge |
| `integration/lean-test-infrastructure-20261013` | 8 | 1942 | Review test changes |
| `wb106-release-integration` | 8 | 2085 | Review release provenance and code |
| `base-vault-2026-09-30-rel133-v051` | 1 | 2358 | Historical release archive candidate |
| `ci-probe-bootstrap-031` | 3 | 2030 | Probe artifact candidate, inspect dependencies |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | 1 | 1939 | Verify rehearsal evidence |

## Interpretation
The frozen cutover, multiple importer/BOM/Workbench integration steps, and prior UI acceptance preparation are ancestral to the active validation branch. This supports choosing a new reviewed consolidated integration target **based on the active candidate**, but does not mean the entire repository's work has been exhaustively preserved. The exact current candidate HEAD and CI need re-verification before promotion. Real-QEAX 0.2-era generated-vault mismatch stays an open model issue rather than a reason to retain 48 development branches.

## Next
Finish the comparison of unsampled branches; obtain exact branch-tip IDs, differences for all non-ancestral heads, and PR owner decisions. Preserve evidence and approved outputs by SHA or tag before deletion. No merges, deletions, main edits, or release promotion.
