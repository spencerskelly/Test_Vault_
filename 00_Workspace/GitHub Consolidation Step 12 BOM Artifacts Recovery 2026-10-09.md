# GitHub Consolidation — Step 12: BOM A-01–A-14 Original Artifact Recovery

**Date:** 2026-10-09
**Status:** **PARTIALLY RECOVERED, GIT INTEGRITY VERIFIED FOR ALL 27 ORIGINAL TEXT FILES; FOUR HISTORICAL ARTIFACTS REMAIN. DO NOT PROMOTE BOM.**
**Previous:** [[GitHub Consolidation Step 11 BOM Reconciliation 2026-10-09]]

## Critical discovery and primary source

The original BOM A-01–A-14 text documents, fixture ZIP files and the source `BOM_A01_A14_Git_Handoff.tar.gz` (**76,602 bytes**) are located in the user's ChatGPT Library **`/BOM Work`**. That path also includes `BOM_MDSE_Vault_Implementation_Plan.md` and `BOM_RUN_LOG.md`. Therefore these originals are **located**, rather than known permanently lost. The Library's raw-byte materialization for the Project's archive/ZIP files failed with an authorization-path warning; do not confuse *located* with *byte-verified*.

## Recovery verification performed

- Inspected the authoritative SHA-256 inventory `spencerskelly/MDSE_Workbench/docs/bom/A01-A14_ARTIFACT_SHA256.md` on BOM proposal head `87cb615876c342a34ce794beee8b5fad80b80520`.
- Recovered **28 readable text documents** through Library text materialization. Each text extraction omitted a terminal newline. After restoring that original newline, **27/28** text files matched their **independent frozen SHA-256 values** exactly.
- **One unmatched text file:** `BOM_RUN_LOG.md`: expected original `0142c0c616cf17f745d3d499629b70a998bebfc75334c9d980c00bcbce331514`, current Library text `63ee9d799c78403a4b2c131fa75257ad8ed17b21fd1b76578de3d9b03094ae2f`. Preserve both and recover the frozen archived source without silently substituting a later/different revision.
- Three original binary ZIP files were found by filename and metadata, but could not be raw-materialized for SHA verification: `BOM_A06_Fixtures.zip`, `BOM_A11_Canonical_Examples.zip`, `BOM_A14_Disposable_Obsidian_Vault.zip`. The 76,602-byte TAR.GZ was also located, not byte-verified.
- Built a separate **27-file, byte-verified text transfer packet** `BOM_A01_A14_Verified_Text_Recovery_27_Files.zip`, with SHA-256 `e757a96df4b4d62c4d152f0c01c5bcb5bc62c39ad2581f1fe2b7d0f34d0194a1`, plus checksum manifest and four missing-file notices. This is a ChatGPT conversation artifact, **not the original handoff archive**. It is not yet on GitHub.

## Verified persistent GitHub work

Created new source-preserving branch `spencerskelly/MDSE_Workbench/recovery/bom-a01-a14-artifacts-2026-10-09` from original BOM proposal SHA `87cb615876c342a34ce794beee8b5fad80b80520`. **All 27** checksum-confirmed text originals were committed under `docs/bom/a01-a14/`. A read-only GitHub Action `.github/workflows/bom-artifact-recovery-audit.yml` verifies every present file against the frozen SHA inventory and deliberately does not claim completion when other files are missing.

- [Final checksum audit 37980681944](https://github.com/spencerskelly/MDSE_Workbench/actions/runs/37980681944): **31 frozen inventory entries, 27 exact Git byte matches, 4 missing, 0 hash errors**.
- [Detailed Workbench recovery record](https://github.com/spencerskelly/MDSE_Workbench/blob/recovery/bom-a01-a14-artifacts-2026-10-09/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md).
- [Draft Workbench PR #15](https://github.com/spencerskelly/MDSE_Workbench/pull/15) targets `proposal/bom-a14-readonly-quantity-uom`, **not `main`**; do not merge until 31/31 original source artifacts are accounted for.
- The 4 missing from remote Git consist of **3 unrecovered raw binary ZIPs** and **1 differently hashed historical BOM run log**. All 27 text originals have passed GitHub SHA validation.

## Important exclusions and next atomic step

No BOM source-code merge was persisted to Test_Vault_ in Step 12. The read-only 0.6 reader and Object `variantOf` governance remain proposals; `WRITABLE_VERSION` remains 0.5 on the BOM source. Step 11's [isolated BOM merge rehearsal](https://github.com/spencerskelly/Test_Vault_/actions/runs/37978500005) had **462/462 tests passing** after an ephemeral obsolete-negative-test update, but **failed intentionally** on incomplete source archive provenance; that fail-closed disposition is unchanged.

**Step 13:** Recover the three untouched original ZIPs and archived BOM run log by an approved raw-byte path (Library UI/workstation or raw conversation attachment) and require **31/31 frozen checksums** before merging Workbench artifact recovery into the BOM proposal or merging BOM source into Test_Vault_. Separately retain all release, first-open Obsidian, importer pin, Bootstrap, and numbered-directory gates.
