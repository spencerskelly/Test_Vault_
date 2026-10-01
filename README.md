# MDSE Base Vault — relationship schema 1.33

Clean base-vault snapshot for the native EA → MDSE importer v0.5 whole-model assessment.

Source workspace commit: 0978773fd3db77b76cf0e822b6dc6016b1ee8a43
Relationship schema: 1.33
Importer: 99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.5.html

This package contains the approved W-250 base-vault contents only. It intentionally excludes the EA evidence bundle, translator governance/decision files, import outputs, archive, and MDSE Workbench.

## First use

1. Make a disposable copy before every import test.
2. Initialize `.vault.yaml` once for that copy; never reuse another vault's real `vault_uid`.
3. Open the vault in Obsidian and let MDSE Bootstrap/plugin setup complete as applicable.
4. Run importer v0.5 against the QEAX.
5. For the full assessment, check **Whole model** before generating.
6. Do not point v0.5 at an already-populated model vault; it will refuse model-root folders that already exist.
7. Treat v0.5 output as assessment-only until the remaining renderer gaps are implemented and reviewed.

The importer requires `99_System/03_Schemas/relationships.yaml` schemaVersion 1.33.
