# CI Dependency Closure — 2026-10-14

## Evidence
The consolidated integration workflow at commit `b2e7d52d8e37c82521817af2e31c614061b6fc19`, run [38647723952](https://github.com/spencerskelly/Test_Vault_/actions/runs/38647723952), had seven successful jobs and one failed `importer-static-contract` job. The failure was specifically in `IMP-005 fresh-base initialization regression`, with the log for job 116138638311 reporting `FileNotFoundError: Base Vault/Definition/mdse-release.yaml`.

Earlier missing source-profile and Local Model schema data dependencies were corrected. This failure confirms another omitted runtime dependency in the sparse checkout; it is not direct evidence of an importer function defect.

## Action
Committed `8d0be59e3e02b535dc4876661414779239f9fdfe` to validation branch `integration/p03-legacy-compat-tests-20261013`. The `importer-static-contract` checkout includes `Importer/Testing`, `Importer/Tools`, `Importer/Definition`, **complete `Base Vault`**, and `99_System/03_Schemas`. Complete Base Vault is chosen instead of adding one dependency at a time because the fresh-base builder requires governed definitions and may require other assets. The source QEAX ZIP remains excluded. Other jobs and testing commands unchanged.

## Verification boundary
Change committed but not yet CI-verified. Inspect the new pinned run before saying the importer/static job passes. No real QEAX import acceptance, GUI signoff, merge, branch deletion, or release promotion.
