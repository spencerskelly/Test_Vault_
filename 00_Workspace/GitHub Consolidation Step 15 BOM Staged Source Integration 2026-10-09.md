# GitHub Consolidation — Step 15: BOM A-14 Source Integrated on Isolated Staging

**Recorded:** 2026-10-09 PDT
**Result:** **PASS — fully history-preserved BOM proposal with all 31 original artifacts staged, importer/source gate and 462 tests PASS.**
**Controlled release:** NOT ISSUED. **Governing Local Model 0.6 and `variantOf`: proposals, not approved.**
**Previous:** [[GitHub Consolidation Step 14 BOM Original Git Integrity Complete 2026-10-09]]

## Workbench recovery PR #15 review

[Original BOM handoff recovery PR #15](https://github.com/spencerskelly/MDSE_Workbench/pull/15) was inspected against `proposal/bom-a14-readonly-quantity-uom`. The compare shows **34 added files, no removals or modifications of implementation or schema source**. It restores 31 frozen historical documents/ZIPs with the independent `docs/bom/A01-A14_ARTIFACT_SHA256.md` manifest, adds a fail-closed checksum workflow, and retains recovery provenance notes.

[Hardened BOM artifact GitHub CI 38008906573](https://github.com/spencerskelly/MDSE_Workbench/actions/runs/38008906573) verified all original **31/31 SHA-256**, 0 missing and 0 mismatches. PR #15 remains **draft** against the BOM proposal (not `main`); reviewed test integration below does **not** imply it was merged.

## Isolated Test Vault BOM proposal integration

- Destination: `spencerskelly/Test_Vault_`, branch `integration/bom-a14-source-step15-2026-10-09`.
- Starting tested importer/WB-129 source and release-contract staging: `integration/release-contract-step10-2026-10-09` at `c922067c7aa0cf6ae2dbc1035527f1a7c4ee27ad`. Its original importer v0.8.19 and WB-129 Workbench Local Model 0.5 histories are retained.
- Original BOM A-14 recovered source branch: `spencerskelly/MDSE_Workbench/recovery/bom-a01-a14-artifacts-2026-10-09` at `50e78c6924a1615d865e763ffdb39d1d2f338bad`, built above frozen BOM source head `87cb615876c342a34ce794beee8b5fad80b80520`.
- **Actual persisted non-squashed subtree merge** [`5d34b3898d7c0a56719435c75b2993b876fca3d6`](https://github.com/spencerskelly/Test_Vault_/commit/5d34b3898d7c0a56719435c75b2993b876fca3d6), with verified ordered Git parents:
  - `24abdb7b570675989cdf8b2d0e23ebd6afafc9c6` — Test Vault integrated staging, including one reviewed negative-test expectation change.
  - `50e78c6924a1615d865e763ffdb39d1d2f338bad` — full BOM proposal plus 31 original recovery files/history.
- Review: [Test_Vault_ draft PR #15](https://github.com/spencerskelly/Test_Vault_/pull/15), targeting the **isolated release-contract integration branch**, not `main`.

## Full gated CI evidence

[GitHub Actions run 38011203998](https://github.com/spencerskelly/Test_Vault_/actions/runs/38011203998) **completed SUCCESS**. The merge occurred in the runner and was only non-forced pushed to the isolated feature branch **after** these gates passed:

1. Frozen original BOM branch commit and WB-129 ancestry are both reachable; non-squashed merge has correct two-parent commit.
2. **31/31 BOM original historical files match their frozen SHA-256** (original Markdown hard-break whitespace was not altered).
3. Read-only Local Model **0.6** recognized by the Workbench BOM reader. **Actual Workbench writer is still 0.5** and the **approved importer schema and release manifest remain Local Model 0.5, `pre-release`**. This is source compatibility, not governance approval.
4. Existing `66_Testing/check_importer_workbench_localmodel.py` and importer profile / regression checks: PASS.
5. Fresh Base Vault built; authoritative `Base Vault/Testing/check-release.py`: **0 FAIL, 4 WARN**, preserving bootstrap candidate / missing controlled release / legacy importer directory warnings.
6. Focused BOM/cache suite: **30 tests passed, 0 failed**. Full merged Workbench suite: **462 tests passed, 0 failed**. TypeScript typecheck and production build: PASS.
7. The historical WB-129 `test/localmodel.test.ts` future-schema negative expectation was committed as a **single-line** isolated Test Vault test patch: unsupported `schema=0.6` changed to unsupported `schema=0.7`, reflecting candidate read support for 0.6. **No waiver or temporary-runner-only patch was used this time.**

**Important first-run diagnostic:** [run 38011165731](https://github.com/spencerskelly/Test_Vault_/actions/runs/38011165731) stopped at `git diff --check` because the exact SHA-frozen historical markdown originals include author-intended trailing spaces (Markdown hard line breaks). The stage workflow was corrected to check **only changed executable and test source paths**, while enforcing full byte-by-byte original-file integrity separately. No source files were normalized or modified to make the check pass.

## Proposed model semantics and open governance

- **A-04/A-05:** `quantity` and `unitOfMeasure` belong on **parent-owned local Part occurrences**, optionally alongside `multiplicity`; both quantity/unit present as a pair, positive exact decimal, governed UOM, no `ea` double counting. Product quantity totals must be derived from parent occurrences; child-side where-used redundancy remains prohibited.
- **A-07/A-08:** `variantOf` proposed as an optional **single-target directed Object→Object** relationship for family/related builds. It is **not** `subtypeOf`, `partOf`, substitutability or a derived inverse YAML field. Prevent self/cycles/unknown/invalid types and ensure raw source evidence provenance.
- The historic A-05 proposal sketches a future **0.6 writer**, whereas the current BOM code **only reads 0.6 and still writes 0.5**. Do not prematurely modify active `99_System/03_Schemas/local-model.yaml`, `relationships.yaml`, or `mdse-release.yaml` to pretend writer/read-only contract alignment is complete. A W-decision and associated schema, ruleset, template, editor, validator, unit vocabulary and cross-tool acceptance are needed.
- Local Model 0.5 importer full real-QEAX regression passed at Step 8 **before the BOM source extension**. A new full source-model run against this merged BOM candidate is **not yet verified**. Nor is Obsidian real interactive editing/restart or Bootstrap first-open.
- Do not merge Workbench PR #15 or Test_Vault_ draft PR #15 into any `main` by treating source SHA integrity / component tests as a release authorization.

## Next atomic unit — Step 16

1. Write and review a coherent **schema governance proposal** that resolves readable-vs-writable Local Model 0.6, controlled UOM exact decimal policy and Object `variantOf` cardinality/cycles against the current authoritative MDSE schemas.
2. Run the full pinned real-QEAX import and WB-129 read/edit candidate acceptance on the *persisted BOM source stage*, verifying 0.5 model compatibility while BOM 0.6 remains read-only.
3. Separately schedule Obsidian UI first-open and BOM `variantOf`/quantity note tests in a disposable vault and address release/Bootstrap warnings before any controlled promotion.

**Original handoff recovery: COMPLETE. Source-level BOM integration on staging: PASS. Governance, real model/UI and release: OPEN.**
