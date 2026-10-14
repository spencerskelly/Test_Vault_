# Final Consolidation — Preservation-First Branch Reduction Inventory

Date: 2026-10-14
Authority target: `spencerskelly/Test_Vault_`
Status: **classification proposal, not deletion/merge approval**.

## Live GitHub snapshot
- **48 remote branches**, including `main`.
- **18 open PRs**: #5–#18 (14), #39, #41, #42, #43.
- PR #39 is a draft cutover (`consolidation/step22-single-repo-cutover-2026-10-11` -> `consolidation/step21-gui-evidence-sessions-2026-10-11`); head `58ab10870f11757cf1bf367ecd5868be9b60933d`.
- PR #43 is draft integration validation (`integration/p03-legacy-compat-tests-20261013` -> Step22); head `f84869f7d69b975125297b3f8d31d212c65f2759`.
- PR #41 is draft documentation and preservation audit (consolidation audit branch -> main); head `3b4eb881fdb4a787c8ba51443e8bf1a257153a9c`.
- PR #42 is draft isolated infrastructure validation (`integration/lean-test-infrastructure-20261013` -> main).
- The previously verified 8/8 CI green baseline was `298271bee000cc3a4820e134ad81778dcb0a56d5`. Later commits on #43 require separate CI confirmation; do not extrapolate baseline success.
- Real QEAX database passed SQLite integrity and 249 BindingConnector cardinality; tested generated vault contains schema 0.2 and fails 0.5 contract; real acceptance remains open. This is not a precondition to a *development* baseline, but it blocks a golden-model/release declaration.

## Work queues — classification is provisional
| Group | Branches | Proposed disposition | Before deletion |
| --- | --- | --- | --- |
| Authority | `main` | Keep stable, protected | No deletion |
| Current consolidation audit | `consolidate/test-vault-single-authority-20261012` | Carry forward documentation, then close review | Verify all unique audit records represented and PR disposition |
| Frozen engineering cutover | `consolidation/step22-single-repo-cutover-2026-10-11` | Candidate integration ancestor, not yet new main | Compare against main, current validation head, all live feature branches |
| Current CI validation | `integration/p03-legacy-compat-tests-20261013` | Candidate engineering baseline input | Exact-head CI; reviewed PR #43; real gate recorded as pending |
| Prior consolidation steps | `consolidation/single-authority-2026-10-10`; `consolidation/step02-...` through `step21-...` | Historical candidates for tag-and-retire | Unique commits/files, preservation and contributor signoff |
| Recovery & migration branches | `recovery/repository-consolidation-2026-10-09`, `integration/workbench-*`, `integration/importer-*`, `integration/release-contract-*`, `integration/bom-*`, `integration/obsidian-ui-*`, `importer/baseline-contract-2026-10-05` | Reconcile with integrated content, then consider retirement | PR #5–18 closure plan and unique-work validation |
| Independently divergent / ancillary | `ai/importer-v0.8-folder-cap-75`, `mdse-workbench-dashboard-definition-20260930`, `wb106-release-integration`, `base-vault-*`, `ci-probe-*`, `integration/lean-test-infrastructure-20261013` | **Hold** until proven represented or intentionally archived | Individually review missing commits, payloads and CI consumers |
| New long-lived branch | `develop` | Proposed after approved integration baseline | Create once, from reviewed/green authoritative commit |

## Cutover gates in priority order
1. **Preservation ledger:** capture every branch's exact SHA, merge base with candidate, unique commits / tree diff, historical PR disposition, and possible unpublished local contributor work. The 48 names above are an inventory, **not proof of safe deletion**.
2. **One target tree:** construct one clean candidate on a *new* integration branch with Workbench, importer, base, schemas, Bootstrap, BOM documents and controlled checks. Avoid accidentally retaining multiple competing copies as live authority.
3. **Exact-head reproducibility:** run consolidated CI and source-only build, verify release/reference paths and do Mac/Windows smoke as feasible. Track real-QEAX schema 0.2 mismatch as open engineering issue, not a false passing gate.
4. **Explicit human approval:** compare exact candidate against main and submit reviewed PR. Only with approval promote to stable main, then create develop at approved commit.
5. **Cleanup batches:** tag or archive source tips by SHA, close obsolete PRs with successor references, and delete only reviewed, explicitly authorized branches in small batches. Never bulk-delete by prefix or age.
6. **Future operating practice:** main = controlled stable; develop = current development; task branches short-lived. Keep release and model acceptance separate.

## Immediate next atomic task
Build a machine-readable `branch -> exact SHA -> merge-base -> unique commit count -> diff paths -> PR -> action` ledger from repository branch tips. Do not issue deletions, merges, release publication or pretend that the current generated vault passed.
