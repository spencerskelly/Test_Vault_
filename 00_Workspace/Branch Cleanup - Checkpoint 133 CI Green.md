# Branch Cleanup — CI Stabilization Verified (2026-10-14)

## Verified successful run
Validation branch `integration/p03-legacy-compat-tests-20261013`, commit `298271bee000cc3a4820e134ad81778dcb0a56d5`, [consolidated integration run 38648119715](https://github.com/spencerskelly/Test_Vault_/actions/runs/38648119715): completed **success**.

The job API confirms **all eight** completed successfully: `importer-static-contract`, `workbench-source-build`, `synthetic-gui-evidence-preflight`, `base-and-document-governance`, `governance-provenance-regressions`, `historical-authority-regressions`, `controlled-python-checks`, `importer-and-governance-smoke`. No job reports a failed step.

## What fixed the prior failures
The importer-only sparse checkout was aligned to source paths declared in `Base Vault/Definition/mdse-release.yaml`, including `.obsidian`, `Definitions`, importer code/definitions/testing, `Base Vault`, and required `99_System` folders. The previously reported `FileNotFoundError` failures for importer Source Profile, `local-model.yaml`, `mdse-release.yaml`, and `.obsidian/app.json` are absent in this successful CI run.

## Remaining boundaries
This passing synthetic/static CI is not a completed real QEAX import, generated-vault acceptance, human Obsidian GUI acceptance, or approved release. Node.js Actions runtime deprecation warnings and potential duplicate push/PR CI runs remain separate cleanup candidates, but do not undermine the successful jobs shown here. Continue to require explicit approval and evidence before merge, branch retirement or release promotion.

## Next
Move back to missing real-QEAX/generated-vault acceptance and gate evidence. Address action-major-version upgrades separately after a dependency-inventory preflight; avoid unnecessary modifications to this now-green workflow.
