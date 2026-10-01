# MDSE Base Vault — relationship schema 1.32

Clean base-vault snapshot for the native EA → MDSE importer v0.4.

Source workspace commit: 230a7846ca115971b9b46326229b547cde604607
Relationship schema: 1.32
Importer: 99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.4.html

This package contains the approved W-250 base-vault contents only. It intentionally excludes the EA evidence bundle, translator governance/decision files, import outputs, archive, and MDSE Workbench.

## First use

1. Make a disposable copy before every import test.
2. Initialize `.vault.yaml` once for that copy; never reuse another vault's real `vault_uid`.
3. Open the vault in Obsidian and let MDSE Bootstrap/plugin setup complete as applicable.
4. Run importer v0.4 against the QEAX.
5. For the first acceptance run use package path `02 Product Context`.
6. Treat v0.4 output as structural acceptance only until the remaining renderer gaps are implemented and reviewed.

The importer refuses a base vault whose `99_System/03_Schemas/relationships.yaml` is not schemaVersion 1.32.
