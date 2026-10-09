# GitHub Consolidation — Step 8 Importer and Workbench 0.5 Integrated Acceptance

**Recorded:** 2026-10-09
**Status:** Compatibility/regression gate **PASS**; real-QEAX acceptance run awaiting final result at time of this initial record.
**Promotion status:** Candidate only, no persistent importer merge, no changes to main.
**Predecessor:** [[GitHub Consolidation Step 07 WB129 Local Model 05 Staging 2026-10-09]]

## Frozen integration input

- Test_Vault_ WB-129 feature source: `integration/workbench-lm05-2026-10-09` at `5b761f14477afaba2177d157587c43f846aeee67`.
- Original Workbench WB-129 recovery commit: `8097f383c41617f879eac8e4ca19fab1d0cb7657`.
- Importer 0.8.19 candidate: `importer/baseline-contract-2026-10-05` at `0494354ec40378e119b17c61fdf6e828844035e4`.
- Acceptance implementation branch: `integration/importer-wb129-acceptance-2026-10-09`; reviewed in [draft PR #11](https://github.com/spencerskelly/Test_Vault_/pull/11).
- Importer changes merged **only with `git merge --no-ff --no-commit` inside ephemeral CI runners**, preserving the frozen originals. Do not interpret this PR as a persisted importer merge.

## Passing source-level compatibility and component checks

[Run 37974395307](https://github.com/spencerskelly/Test_Vault_/actions/runs/37974395307) completed **success**. The same fail-closed `66_Testing/check_importer_workbench_localmodel.py` that correctly rejected the older 0.4-only Workbench source in Step 6 now confirms the actual WB-129 source reads 0.1–0.5 and writes Local Model 0.5, matching the importer candidate's schema.

The run also passed importer v0.8.19 governed source-profile check, release-gate regression tests, IMP-009 acceptance selftest, fresh Base Vault build, Workbench TypeScript typecheck, complete **448-test** suite with **zero failures**, and production build. This is a **component/integration-source PASS**, not yet a release or real-model acceptance.

## Full real-QEAX acceptance under evaluation

[Run 37974532073](https://github.com/spencerskelly/Test_Vault_/actions/runs/37974532073) was launched on the same branch using separate read-only scripts in `66_Testing/real_qeax_prepare.sh` and `66_Testing/real_qeax_execute.sh`. The runner:
- recreates the frozen noncommitting merge and runs the source/schema gate;
- checks the governed source zip's QEAX SHA-256 `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c` and source counts 35,969 objects / 21,822 connectors;
- builds three initialized disposable base vaults;
- attempts the full deterministic import + injected-failure scenario, output hash equality, IMP-009/010/011 topology and BindingConnector acceptance and WB-129 `accept:real-vault:05` read/edit/reload acceptance with source-vault mutation prohibited.

**Do not assume the real-QEAX run succeeded until its final job conclusion and steps are verified.** No model/QEAX output is uploaded into the repo. No release manifest, generated lock, BOM feature, importer source or main branch has been changed.

## Remaining release gates

- Confirm real-QEAX outcome and resolve any semantic/model defects; if passed, separately review a full importer history-preserving merge into WB-129 feature staging.
- Preserve and integrate BOM A-14 development from the divergent Workbench branch.
- Address release-checker document registration, Bootstrap pin/lock mismatch and issue a tested controlled Base.
- Migrate approved numbered folder paths with dependency-aware CI/runtime updates.
- Verify Obsidian first-open and end-user interactions plus workstation-local uncommitted/unpushed changes.

**Next:** update this record with actual real-QEAX job outcome before moving to persistent importer merge.
