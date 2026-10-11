# GitHub Consolidation — Step 13: Original BOM Archive Verified

**Historical checkpoint:** This Step 13 record describes the state *before* the user uploaded the final four originals to GitHub. The [Step 14 completion record](GitHub%20Consolidation%20Step%2014%20BOM%20Original%20Git%20Integrity%20Complete%202026-10-09.md) supersedes its 27/31 Git-persistence status: **31/31 original files are now in GitHub and both the initial and hardened SHA-256 audits passed.**

**Recorded:** 2026-10-09
**Status:** **Original source archive verified 31/31 against frozen SHA-256 inventory, all ZIP CRC checks PASS. GitHub source files remain 27/31 until the final four are uploaded.**
**Predecessor:** [[GitHub Consolidation Step 12 BOM Artifacts Recovery 2026-10-09]]

## User-provided original source archive

The user attached `BOM_A01_A14_Git_Handoff.tar.gz` at a verified conversation sandbox path. The raw original TAR.GZ bytes were inspected directly, not inferred from a text snippet or reconstructed from prior chat.

- Archive size: **76,602 bytes**.
- SHA-256: **`afec22098e7a6aa8c84a392c51d8ab4e04485708cdc04fe4642f507cd022f5af`**.
- Archive contents: **48 regular files** — **31 top-level historical BOM artifacts** from the immutable `A01-A14_ARTIFACT_SHA256.md` inventory plus **17** original disposable-Obsidian-vault files.
- **All 31 historical original artifacts matched their frozen inventory SHA-256 exactly.** There were zero mismatches or missing inventory items in the archive.
- ZIP CRC validation passed for all three originally missing ZIPs: **4** A-06 fixture entries, **8** A-11 canonical examples, **17** A-14 disposable vault entries.
- Original `BOM_RUN_LOG.md` from the archive is **18,936 bytes**, hash `0142c0c616cf17f745d3d499629b70a998bebfc75334c9d980c00bcbce331514`. This resolves the prior mismatch with a later Library revision (not used for archival restoration).

### Four original files recovered and verified

| Original | Size | SHA-256 |
|---|---:|---|
| `BOM_A06_Fixtures.zip` | 3,319 | `a2fd27132588ad5c343efed0bccfb653f72bb715eb4345165d0fa3fb2e2d040f` |
| `BOM_A11_Canonical_Examples.zip` | 3,876 | `7219f43f29a409ba321f076d5e23a5e388ba3deb334f30359359b7918e457afa` |
| `BOM_A14_Disposable_Obsidian_Vault.zip` | 6,061 | `28cabfaebed97629732ad39f94f2f786251c002388ef1cd4456549254d81932c` |
| `BOM_RUN_LOG.md` | 18,936 | `0142c0c616cf17f745d3d499629b70a998bebfc75334c9d980c00bcbce331514` |

These original bytes were repackaged unmodified into a user-visible **`BOM_Final_Four_Verified_for_GitHub.zip`** for handoff. The separate full inventory JSON is `BOM_A01_A14_Original_Archive_Integrity_Report.json`. The package is not a substitute for checking the individual original hashes after GitHub upload.

## Verified GitHub state and remaining transport

- [Original BOM recovery source branch](https://github.com/spencerskelly/MDSE_Workbench/tree/recovery/bom-a01-a14-artifacts-2026-10-09) contains **27** exact original text files under `docs/bom/a01-a14/`, SHA-checked by [Actions run 37980805384](https://github.com/spencerskelly/MDSE_Workbench/actions/runs/37980805384): **27/31, 0 failures, 4 missing**.
- A [new source archive verification note](https://github.com/spencerskelly/MDSE_Workbench/blob/recovery/bom-a01-a14-artifacts-2026-10-09/docs/bom/A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md) documents **31/31 historical archive matches**, and existing `A01-A14_RECOVERY_STATUS_2026-10-09.md` now distinguishes archive verification from Git persistence.
- [Draft Workbench PR #15](https://github.com/spencerskelly/MDSE_Workbench/pull/15) remains **draft**, based on the original BOM proposal branch, not `main`; no BOM implementation merge.
- Due to the GitHub connector not accepting a local mounted binary file path, **the 3 original binary ZIPs and historic `BOM_RUN_LOG.md` have NOT been uploaded to the GitHub recovery branch**.
- The user can download/extract `BOM_Final_Four_Verified_for_GitHub.zip` and use GitHub's **Add file → Upload files** on the recovery branch, folder `docs/bom/a01-a14/`. Then rerun `.github/workflows/bom-artifact-recovery-audit.yml` and require **31/31 matches, zero missing and zero hash mismatches**.

**Do not report source Git recovery complete or merge PR #15 before GitHub independently confirms 31/31.** No Test_Vault_ or Workbench default-branch updates or controlled release promotion occurred.

## Follow-up

Next bounded step: finish GitHub transfer of those exact four raw-byte originals, verify GitHub Actions at **31/31**, then separately review the BOM A-14 read-only schema 0.6 and `variantOf` against the approved Local Model 0.5 writer and Workbench/importer acceptance. Manual Obsidian first-open remains pending.
