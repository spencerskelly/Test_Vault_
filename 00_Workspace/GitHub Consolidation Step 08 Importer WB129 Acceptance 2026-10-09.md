# GitHub Consolidation — Step 8 Importer and Workbench 0.5 Integrated Acceptance

**Recorded:** 2026-10-09
**Status:** **PASS — paired source/regression, deterministic full-QEAX import, topology/BindingConnector and Workbench Local Model 0.5 headless real-vault candidate acceptance.** Full controlled release and manual Obsidian UI acceptance remain pending.
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

**Final verified real-QEAX result: PASS.** GitHub Actions [run 37974532073](https://github.com/spencerskelly/Test_Vault_/actions/runs/37974532073) is `completed` / `success` (job `113969334862`); every job step, including `Full import and WB-129 read/edit acceptance`, completed successfully. Source QEAX checksum was validated before executing the import, including **35,969 objects** and **21,822 connectors**.

**Deterministic replay:** two fresh import inventories each contained **28,273 nonvolatile files**; `onlyA=0`, `onlyB=0`, `changed=0`, `DETERMINISM PASS`.

**Importer semantic / topology checks:** IMP-009 headless result **25 checks / 0 warnings**, transaction status `IMPORT_COMPLETE`, write `WRITE_PASS`, pending (not falsely approved) semantic acceptance, **1,051 definitionless Interfaces**, all **1,545 Local Model endpoint block references** resolving. IMP-010 hierarchy/interface-flow and IMP-011 BindingConnector acceptance passed: **249** source/review bindings, **209** `Interface.equals` pairs (418 directed links), **23** `Connection.exposes` relationships, and **803** Local Model regions.

**Workbench Local Model 0.5 candidate:** log result `status=PASS`, `acceptance=candidate-only`, `localModelVersion=0.5`, `sourceVaultUnmodified=true`, `failures=[]`; **27,813 Markdown files**, **803** Local Model regions; counts match expected: **2,055 parts**, **4,387 endpoints**, **552 connections**, **72 flows**. **0 parsed errors**, **4 no-op samples**, **0 no-op drifts**. It did not write to the source vault.

**Remaining manual/UI acceptance:** the importer reported an explicit manual Obsidian scenario on a definitionless Interface: inspect and edit only its contextual identifier in the controlled Workbench UI, restart Obsidian, confirm persistence and no reusable Interface note. The headless gate does not perform this graphical Obsidian interaction. The log also reports **3 moderate npm audit vulnerabilities**, requiring separate dependency triage; this was not a failing gate.

No generated QEAX/model output was uploaded to the Git repository. No release manifest, generated plugin lock, BOM feature, persistent importer source merge or `main` branch was changed.

## Remaining release gates

- Confirm real-QEAX outcome and resolve any semantic/model defects; if passed, separately review a full importer history-preserving merge into WB-129 feature staging.
- Preserve and integrate BOM A-14 development from the divergent Workbench branch.
- Address release-checker document registration, Bootstrap pin/lock mismatch and issue a tested controlled Base.
- Migrate approved numbered folder paths with dependency-aware CI/runtime updates.
- Verify Obsidian first-open and end-user interactions plus workstation-local uncommitted/unpushed changes.

**Step 8 verdict:** Headless full real-QEAX pairing PASSED. **Next bounded unit (Step 9):** preserve and non-squash stage the importer v0.8.19 history atop Workbench 0.5 on a dedicated proposal branch, while retaining all original PRs; rerun the source gate after persistence. Do not promote the release until document registration, Bootstrap lock alignment, manual Obsidian check, BOM reconciliation, local-work audit and numbered path migration are resolved.
