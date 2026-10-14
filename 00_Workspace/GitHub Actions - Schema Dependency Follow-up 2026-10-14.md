# Branch Cleanup — CI Dependency Follow-up (2026-10-14)

## Verified regression
At run [38647533105](https://github.com/spencerskelly/Test_Vault_/actions/runs/38647533105), seven jobs completed success and `importer-static-contract` failed at `Source profile and v0.8.19 headless compile-only`. Job log 116138004226 shows `ENOENT` for `99_System/03_Schemas/local-model.yaml` when `taxonomy_local_model_05_static_test.js` executed. The earlier absent Source Profile was resolved enough for execution to advance, but the taxonomy test also depends on the schema directory.

## Applied
Validation branch `integration/p03-legacy-compat-tests-20261013` commit `b2e7d52d8e37c82521817af2e31c614061b6fc19` adds `99_System/03_Schemas` to `importer-static-contract` sparse checkout, retaining previously restored `Importer/Definition`, `Importer/Testing`, `Importer/Tools`, and `Base Vault/Tools`.

## Evidence boundary and prevention
Commit confirmed; follow-up Actions run not registered at immediate query. Do not report pass until job outcome is verified. This is the second omitted runtime data dependency from a too-narrow checkout; a comprehensive static dependency inventory should precede further optimization. The GitHub Actions Node20 deprecation warnings are unrelated to the ENOENT failure and should be addressed separately. Real QEAX and GUI gates remain open; no main edits, merge, release or branch deletion.
