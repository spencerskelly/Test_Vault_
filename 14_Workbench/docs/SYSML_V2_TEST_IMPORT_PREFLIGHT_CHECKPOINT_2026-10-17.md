# SysML v2 test-import preflight checkpoint

Read-only source assessment of the reduced QEAX with a local Python SQLite preflight (not a translated vault). The source SHA256 is `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`. `PRAGMA quick_check` returned `ok`.

Inventory: 11,447 elements, 14,688 connectors, 1,389 packages, 2,208 diagrams; 60 observed (EA Object_Type,Stereotype) combinations. 203 missing or blank EA Author values require the previously governed fallback author code. Zero invalid/missing EA CreatedDate values. No duplicate/missing element EA GUIDs or dangling connector endpoints detected by this first gate. No native SysML v2 output or parser validation has happened: **native accepted = 0**.

This supports **GO for a non-destructive source dry run**, not production import. Next gates are exact machine-readable ruleset embedding, typed source-to-native mapping, per-row outcome ledger, deterministic UID allocation, note bottom syntax/YAML and flagLink generation, official pinned SysML parser verification, reimport and Obsidian tests. Avoid confusing the 17 raw Connector_Type/SubType pairs in the simplified preflight with the 26 semantic relationship families previously reviewed (which include additional stereotypes).

The current standalone local preflight script and raw diagnostics are provided as a conversation artifact; neither source-row evidence nor raw model contents are committed here. Bring the preflight module into the offline single-file HTML importer; its embedded rulesets must be generated from versioned core rules rather than transcribed separately. Input counts and diagnostics belong in the interface's Analysis and Errors panes, exportable offline.
