# Branch Cleanup — Checkpoint BR-43: Actual Release Checker and Exact-Tip Validation Matrix

**Date:** 2026-10-12
**Repository:** `spencerskelly/Test_Vault_`
**Audit PR:** #41
**Engineering candidate:** `consolidation/step22-single-repo-cutover-2026-10-11` @ `58ab10870f11757cf1bf367ecd5868be9b60933d`
**Status:** Inspection of checker and Step22 workflow complete; full release validation NOT EXECUTED in this checkpoint.

## Source files directly inspected

| Source | Git blob SHA | Scope |
|---|---|---|
| `Base Vault/Testing/check-release.py` | `aae6d70357fbeea2c56aac7c3307604750dfdefe` | Broader W-320/321/322 controlled-release consistency checker |
| `.github/workflows/consolidation-step22-cutover.yml` | `e23e950f81ea5dcdc88789fbd7a3eddfe05ad478` | Branch-scoped retirement audit, sparse checkout that excludes QEAX archive |
| `66_Testing/consolidation/test_step22_retirement.py` | `dc009e86bf411f682d65548cfdc2e0ac17780568` | Fourteen `unittest` assertions about historical branch inventory, SHA preservation and explicit holds |

The source code is the basis of the matrix; the historical run's successful job was verified in BR-41.

## Matrix: what the actual checker enforces

| Domain | Source-observed check | Scope of execution evidence |
|---|---|---|
| Filesystem governance | Requires null total generated path and folder file-count limits, global imported filename scope, nested element folders | Implemented in `check-release.py`; no full exact-tip run verified |
| Lean runtime Base inputs | Requires builder, included source files/trees, mapped sources, valid `sh -n` init scripts, and no include/forbid conflicts | Implemented; no exact-tip run verified |
| Schemas | Reads schemaVersion from relationships, element-types and local-model YAML, compares against release manifest | Implemented; no exact-tip run verified |
| Document authority | All registered docs exist; obsolete banners refer to successor; current docs cannot have superseded banner; workspace/tool docs are registered | Implemented; no exact-tip run verified |
| W decision chain | Translator Definition marker cannot claim beyond latest W in Workspace Decision Log; Current State references versions and latest W; stale text checks | Implemented; no exact-tip run verified |
| Controlled plugin packaging | Runs plugin configuration/lock generators with `--check`; verifies enabled plugins exactly match lock and SHA-256 content hashes match runtime payloads | Implemented; no exact-tip run verified |
| Bootstrap and Workbench | Checks pinned versions against lock, source manifests and candidate allowances; distinguishes pre-release warnings from release failures | Implemented; no exact-tip run verified |
| Importer candidate | Static contract tokens, forbidden legacy literals, source-profile model ID, path planner/attachment reconciliation call-site checks | Implemented; no exact-tip run verified |
| Retired standalone Workbench coverage | 14 retirement tests and branch-scoped workflow check source SHA/inventory, prior BOM workflow archive, pre-release status and explicit unfinished signoffs | Historical CI job `114628807255` conclusion success, NOT complete release checker |

**Evidence boundary:** The direct release-checker text reviewed in this pass was its initial portion through importer contract logic. This matrix is limited to those observed sections and does not claim to inventory any later code branches in the checker. To certify the complete checker, review remaining code and execute full test suite on an approved exact promotion SHA.

## Commands for a controlled disposable staging checkout

Only after confirming security-approved access to source material, and use a safe sparse checkout or approved environment that **does not materialize sensitive QEAX blobs**:

```bash
# In a verified clean checkout of the exact authorized candidate SHA:
python3 -m pip install pyyaml
python3 'Base Vault/Testing/check-release.py'
python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step22_retirement.py' -v
```

Optional checker flags from its usage are `--workbench PATH_TO_MDSE_WORKBENCH` and `--base PATH_TO_GENERATED_BASE`; the generated Base should be a disposable, independently checked output, not a live user vault. Check that warning handling, negative/fail-closed test suites and actual importer/Workbench/Bootstrap integration are independently covered. Do not call a release READY merely because this checker returns 0.

## Exact release acceptance gaps

1. Final approved tip SHA fixed and documented; ensure full CI runs on exactly that tip.
2. Run comprehensive controlled-release checker, dependencies, lock hash and generated Base consistency with captured logs and results.
3. Independently verify importer/Workbench/Bootstrap end-to-end and fail-closed/negative tests, plus real QEAX cases where specifically authorized and confidential handling is established.
4. Obtain actual Mac and Windows Obsidian UI acceptance rather than synthetic model fixtures.
5. Obtain written W/document-control authority for proposed registrations and any schema change.
6. Resolve QEAX public-history confidentiality/exposure and contributor-local unpublished work signoff before promotion/retirement.
7. Inspect GitHub PR head/base, required checks and review approvals, then authorize any merge/archival/deletion as separately scoped steps.

## Decision / handoff

**BR-43 result:** Release checker and Step22 CI source evidence reviewed, critical test-coverage mismatch recorded. All release readiness and cleanup deletion gates remain OPEN.

**NEXT BR-44:** Inspect the remaining checker implementation for optional Workbench/Base validation and final exit semantics; create a precise promotion gate plan grounded in full source code. No checker or release manifest edits without governed approval.

**No destructive action:** No merge, closure, branch deletion, archive, workflow rerun or release promotion.
