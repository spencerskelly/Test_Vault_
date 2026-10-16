# GitHub Consolidation — Step 14: BOM A-01–A-14 Original Source Recovery Completed

**Date:** 2026-10-09 (PDT)
**Outcome:** **PASS — all 31 historical BOM artifacts persisted in GitHub and independently SHA-256 verified.**
**Release status:** BOM implementation and MDSE controlled release **NOT APPROVED**.
**Prior:** [[GitHub Consolidation Step 13 Original BOM Archive Verification 2026-10-09]]

## Verified immutable source

The four original files missing in Step 13 were uploaded by the user to `spencerskelly/MDSE_Workbench` on branch `recovery/bom-a01-a14-artifacts-2026-10-09` under `docs/bom/a01-a14/`:
`BOM_A06_Fixtures.zip`, `BOM_A11_Canonical_Examples.zip`, `BOM_A14_Disposable_Obsidian_Vault.zip` and historical `BOM_RUN_LOG.md`.

They join the prior 27 originals. Current `docs/bom/a01-a14/` contains **31 frozen-inventory files**. The source SHA inventory predates these uploads: `docs/bom/A01-A14_ARTIFACT_SHA256.md` on the existing BOM proposal branch.

### Passing original-file evidence (from GitHub Actions, not just a local archive)

- [First complete GitHub audit 38008742547](https://github.com/spencerskelly/MDSE_Workbench/actions/runs/38008742547), at user upload commit `160f1066b7fac47d7879c252b5e69f2e0d66249e`: **31/31 exact original SHA-256, 0 missing, 0 mismatches**.
- The audit's existing partial-recovery allowance was replaced with a **fail-closed** requirement for exactly 31 inventory entries and exactly 31 matching Git-backed source files. It rejects a missing original or altered bytes.
- [Hardened independent CI rerun 38008828655](https://github.com/spencerskelly/MDSE_Workbench/actions/runs/38008828655), at `83ba924dc98c8d10a3790d3dfe15743e6a5452dc`: **success, 31/31 exact, 0 missing, 0 mismatches**.
- [Workbench artifact recovery status](https://github.com/spencerskelly/MDSE_Workbench/blob/recovery/bom-a01-a14-artifacts-2026-10-09/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md) and [uploaded original archive evidence](https://github.com/spencerskelly/MDSE_Workbench/blob/recovery/bom-a01-a14-artifacts-2026-10-09/docs/bom/A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md) have been updated to distinguish the completed Git original-file gate from BOM feature/release gates.

Historical original TAR.GZ size **76,602 bytes**, SHA-256 `afec22098e7a6aa8c84a392c51d8ab4e04485708cdc04fe4642f507cd022f5af`. Archive audit also covered 17 disposable vault members. All 3 original ZIPs passed CRC tests. The archived historical log, not the later Library version, is committed and matched.

## Safe changes and exclusions

- The artifact-recovery **draft [Workbench PR #15](https://github.com/spencerskelly/MDSE_Workbench/pull/15)** targets `proposal/bom-a14-readonly-quantity-uom` rather than `main`. Do not merge this PR into the production default branch without review.
- The Test_Vault_ staging branch `integration/release-contract-step10-2026-10-09` still holds accepted importer v0.8.19 and WB-129 Local Model 0.5 source; the **BOM source feature remains separate**.
- [Step 11 isolated BOM reconciliation](https://github.com/spencerskelly/Test_Vault_/actions/runs/37978500005) had a **clean non-squashed temporary subtree merge** and **462 passing Workbench tests after an ephemeral historical future-version negative-test fix**. Its workflow failed deliberately on missing source artifacts; this original-source blocker is now resolved, but a fresh end-to-end BOM integration test is still needed.
- All old branches and source histories are retained; no controlled release, numbered-directory migration, Bootstrap candidate promotion or manual Obsidian startup/edit acceptance occurred here.

## Next bounded task — Step 15

1. Review the complete artifact-recovery PR #15 against the BOM proposal. Decide whether to integrate the verified originals into the proposal, **not default main**, preserving original history.
2. Prepare the BOM source reconciliation into the combined `Test_Vault_` staging tree. Update **committed**, not ephemeral, historic future-schema negative test to 0.7 only when read-only 0.6 is approved.
3. Govern Local Model 0.6 read-only quantity/UOM and Object→Object `variantOf` in authoritative `99_System/03_Schemas`; retain the 0.5 writer, verify importer+Workbench acceptance and existing release invariants, then separately perform manual Obsidian tests.

**Artifact preservation: COMPLETE. BOM implementation/release: NOT YET APPROVED.**
