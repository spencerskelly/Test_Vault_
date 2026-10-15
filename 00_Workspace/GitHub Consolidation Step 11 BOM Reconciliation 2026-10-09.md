# GitHub Consolidation — Step 11: BOM A-14 Read-Only Reconciliation

**Recorded:** 2026-10-09
**Status:** **Code-level merge rehearsal CLEAN and component tests PASS after ephemeral regression-test expectation update. Release/integration promotion intentionally BLOCKED by missing original BOM artifacts and unapproved 0.6 schema proposal.**
**Original source unaffected:** `spencerskelly/MDSE_Workbench`, `proposal/bom-a14-readonly-quantity-uom`.
**Working monorepo staging unaffected:** no BOM source committed to `Test_Vault_`.
**Review:** [Test_Vault_ draft PR #14](https://github.com/spencerskelly/Test_Vault_/pull/14).
**Prior:** [[GitHub Consolidation Step 10 Release Registry and Fixture 2026-10-09]]

## Inputs and divergence

- Accepted combined source baseline `spencerskelly/Test_Vault_/integration/release-contract-step10-2026-10-09` at `c922067c7aa0cf6ae2dbc1035527f1a7c4ee27ad`. This includes importer v0.8.19, WB-129 Local Model 0.5, and verified pre-release documentation / Workbench schema fixture repair.
- BOM source branch `spencerskelly/MDSE_Workbench/proposal/bom-a14-readonly-quantity-uom` at `87cb615876c342a34ce794beee8b5fad80b80520`.
- Original WB-129 source `8097f383c41617f879eac8e4ca19fab1d0cb7657`; branch divergence comparison shows **32 BOM-unique** and **23 WB-129-unique** commits since Local Model 0.5 ancestor `7052c07b4c95212522ba4b5d274c95be0860bda3`.
- The independent `proposal/bom-a14-baseline-check` head `2667965cdff6e2db8cf3129fdd0b50d4f9fd8d04` contains one non-BOM-test workflow commit relative to LM 0.5; preserve it as historical verification evidence. The richer BOM proposal contains `.github/workflows/bom-a14-verify.yml`.

## Actual BOM proposal features — *not* yet approved as governed schemas

1. Workbench `src/core/localmodel.ts` adds a **readable** Local Model **0.6** and allows part-level `quantity` and `unitOfMeasure` next to existing `multiplicity`. **WRITABLE_VERSION remains `0.5`**, and 0.5 rejects 0.6-only fields. New 0.6 proposal enforces paired positive quantity/unit, known unit vocabulary, and prevents double-counting with `ea`.
2. Read-only `variantOf` is an **optional, single-target Object→Object** frontmatter relationship, *distinct* from subtype/generalization and with no inverse stored. It reports invalid YAML shape, unresolved/multiple links, duplicate links, self-reference, invalid endpoint types, missing target, and cycles through existing Review/assurance paths.
3. Modified `src/core/cache.ts`, `src/core/model.ts`, `src/core/review.ts`, Obsidian indexer/assurance/review to preserve/query these candidate additions. BOM-focused test files are `test/bom-localmodel-06.test.ts` and `test/bom-variantof.test.ts`, plus cache tests.
4. **Not yet created/approved:** governed schema 0.6 and `variantOf` relationship declarations in `99_System/03_Schemas`, BOM quantity notes/units/variantOf contract artifacts listed below, Base/Importer support for schema 0.6, and controlled user-facing Obsidian runtime acceptance. Do not represent a read-only extension as a released writer format.

## CI evidence — two reproducible non-writing merge rehearsals

The new `.github/workflows/bom-a14-merge-rehearsal.yml` on isolated `integration/bom-a14-reconciliation-2026-10-09` does a pinned `git subtree pull --prefix=55_Workbench ... --no-squash` **inside an ephemeral GitHub Actions runner**. Both source lineages remain reachable; **zero Git merge conflicts** occurred; **no merge commit was pushed**.

- [Initial run 37978351156](https://github.com/spencerskelly/Test_Vault_/actions/runs/37978351156): non-squashed subtree merge **CLEAN**, typecheck and BOM tests advanced, but full legacy suite **461 pass / 1 fail**. Exact failing test: `test/localmodel.test.ts`, `unsupported future schema: readable as Markdown, structured use off, no records guessed`. It uses `canonical().replace("schema=0.2", "schema=0.6")`. With proposed BOM reader 0.6 this is now an obsolete negative expectation, **not a runtime crash**. The promotion gate also correctly rejected missing handoff artifact files.
- [Follow-up run 37978500005](https://github.com/spencerskelly/Test_Vault_/actions/runs/37978500005): in the ephemeral runner only, the single obsolete negative fixture replaces `schema=0.6` with unsupported **`schema=0.7`**. Result: **30/30 BOM-focused tests PASS**, full suite **462/462 tests PASS**, TypeScript typecheck and production build PASS. Writer remains 0.5. The workflow intentionally finishes **FAILED** on the final missing-artifact gate. This is correct; a green component suite must not imply complete BOM provenance.
- CI uploaded [merge-diagnosis artifact for run 37978500005](https://github.com/spencerskelly/Test_Vault_/actions/runs/37978500005) containing an ephemeral test adjustment diff and merge status, not original BOM source/model files.
- The legacy test **has not been modified or committed in the original Workbench or the merged Test_Vault_ source**. Any future BOM promotion requires a reviewed implementation/test update and central schema/decision approval.

## Explicit source recovery blocker

BOM source branch includes [`docs/bom/A01-A14_GIT_PERSISTENCE_AUDIT.md`](https://github.com/spencerskelly/MDSE_Workbench/blob/proposal/bom-a14-readonly-quantity-uom/docs/bom/A01-A14_GIT_PERSISTENCE_AUDIT.md) and [`A01-A14_ARTIFACT_SHA256.md`](https://github.com/spencerskelly/MDSE_Workbench/blob/proposal/bom-a14-readonly-quantity-uom/docs/bom/A01-A14_ARTIFACT_SHA256.md). Its audit expressly states **the authored specs, fixture ZIPs and test-vault ZIP were produced as local artifacts but were not committed**. A direct GitHub contents request confirms `docs/bom/a01-a14/` is **absent** from the proposal branch.

The proposal inventory lists original source manifest, semantic/decision records, Local Model unit/schema proposal, A-06/A-08/A-11 fixtures/tests, `variantOf` and variant-comparison contracts, Object subtype decision, Ruleset and AI/template amendments, A-14 preflight, runtime-acceptance evidence, disposable vault, master plan and run log, plus archive-internal files. **The GitHub checksum inventory is not a substitute for those bytes.** Do not fabricate or paraphrase exact historical artifacts to match an old SHA. Recover exact files through prior ChatGPT artifact/file library or the originating workstation and compare SHA-256 checksums before committing, or explicitly document unrecoverable provenance.

The current CI fail-closed gate checks `55_Workbench/docs/bom/a01-a14/BOM_SOURCE_MANIFEST.json` and blocks absent files; this **cannot alone prove the entire artifact set has been transferred and verified**. A subsequent audited manifest must enumerate every item and verify each hash.

## Next atomic unit — Step 12

**Prioritize recovering the exact original A-01–A-14 assets** and recording which are present, inaccessible, or hash-unverified. In parallel, plan approved proposal schemas (readable Local Model 0.6, optional Object→Object `variantOf`), a reviewed fix of the legacy negative test, and a cross-tool compatibility check for importer 0.5. Do **not** stage/push the BOM source merge into the release integration branch until evidence is complete and tests on committed source pass.

**Release still pre-release.** Importer/Workbench QEAX headless candidate acceptance passed independently, but manual Obsidian, Bootstrap first-open, local Git dirty/unpushed review and numbered folder migration remain unverified.
