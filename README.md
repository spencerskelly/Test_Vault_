# MDSE Base Vault — relationship schema 1.33

Clean base-vault snapshot for the native EA → MDSE importer v0.5.1 whole-model assessment.

Source workspace commit: 3e7d696b75793dbf46f09f573ab8c3ca7f4dfc70
Relationship schema: 1.33
Importer: 99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.5.1.html

This package contains the approved W-250 base-vault contents only. It intentionally excludes the EA evidence bundle, translator governance/decision files, import outputs, archive, and MDSE Workbench.

## First use

1. Make a disposable copy before every import test.
2. Initialize `.vault.yaml` once for that copy; never reuse another vault's real `vault_uid`.
3. Do not open the target vault in Obsidian until generation is finished.
4. Run importer v0.5.1 against the QEAX.
5. Run Analyze QEAX, then Build whole-model plan.
6. Only after the plan passes, choose this fresh base copy as output.
7. Check **Whole model**, then Generate assessment vault.
8. Never select `Test_Vault_` or an existing imported vault as the output target.

The importer requires `99_System/03_Schemas/relationships.yaml` schemaVersion 1.33.
