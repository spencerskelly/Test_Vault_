# Step 65 — Regression coverage and CI gate separation (2026-10-14)

Status: **CI gate change committed; run outcome not yet verified**. PR #43 validation branch only.

## CI change

Commit `890166131e5f301685fad2da5c1b67d1f4805456` updates `.github/workflows/p04-workbench-readonly.yml`:
- Previously `sha256sum --check artifact-sha256.txt` ran **after** rebuilding `main.js` and failed whenever an intentional new candidate differed from the historical governed bundle.
- New integrity gate compares the committed Git object for each of `main.js`, `manifest.json`, `styles.css` against the existing controlled `artifact-sha256.txt`. Any tampering still fails.
- Separate report records the fresh candidate SHA and historical SHA as either MATCH or DIFFERENT. DIFFERENT is explicitly **not release approval**. Two-clean-build consistency, typecheck, npm tests, original historical reproduction and every other gate remain intact.
- No binary, hash manifest, model, QEAX data or frozen branch was changed.

## Bounded regression-test review

The following **existing** test files were inspected by textual signal scan (not a comprehensive suite-wide coverage audit):
- `55_Workbench/test/localmodel.test.ts`: 33 `test(` occurrences, references to reciprocal/`equals`, but no direct occurrence of `quantity`, `unitOfMeasure`, `variantOf` or literal `schema 0.6`.
- `55_Workbench/test/localmodel-edit.test.ts`: 68 `test(` occurrences, references to `equals` and reciprocal. No direct occurrence of quantity/unit fields or variantOf.
- `55_Workbench/test/cache.test.ts`: 23 `test(` occurrences; several references to `variantOf`, no direct `quantity` or `unitOfMeasure` occurrences.

These are *lexical observations*, not proof that test cases are missing globally. Additional test files and actual behavior assertions must be evaluated before claiming complete coverage.

## Release governance

The validated original Workbench source reproduces governed `main.js` SHA256 `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`. New candidate output may differ due to the 8 modified and 2 added sources. The revised P04 check separates **governed artifact integrity** from **new candidate identity**. Even if CI passes, candidate packaging, approval, real-QEAX and GUI validation, and PR #39/#41 reviews remain held independently.

## Step 66

Inspect completed P04 CI run, confirm integrity and candidate classification gates both execute; expand missing coverage specifically for 0.6 part quantities, unitOfMeasure, cache roundtrips, and variantOf. Do not promote or delete refs.
