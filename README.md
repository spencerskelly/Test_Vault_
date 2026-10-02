# Test_Vault_

A workspace, not the vault that will be built. It defines the EA-to-MDSE translator and the conventions the real vault will follow (W-01). The real vault is generated later from the Sparx EA file.

## Start here

1. `99_System/10_Docs/00 - Current State.md`: the registry. It lists what is current, what is historical or superseded, tool status and where each rule lives. Start here.
2. `99_System/10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`: current cross-repository authority and implementation contract.
3. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`: current modeling/import governance.
4. `99_System/10_Docs/Translator Definition.md`: current Stage-1/native importer contract.
5. `99_System/10_Docs/Workspace Decision Log.md`: decisions through W-322.
6. `99_System/10_Docs/Handoff Prompt - MDSE v0.8 Implementation.md`: copy-ready continuation prompt for a new AI chat.

Current target: MDSE/base/importer 0.8.0, relationships 1.35, element-types 1.17, Local Model 0.2. Machine-readable manifest: `99_System/03_Schemas/mdse-release.yaml`. Build the lean base with `build-base.py`; verify authority/Workbench/base alignment with `check-release.py`.

## Folders

- `99_System/03_Schemas`: the class, relationship, element, connector, field, tag and package rules, as YAML.
- `99_System/05_Templates`, `08_Scripts`: the class templates and the id and uid snippets.
- `99_System/10_Docs`: Current State registry, decision log, handoffs, Translator Definition, Post-Import Tasks and Ruleset 1.23.
- `99_System/archive`: retired material with no authority; see its README.
- `99_System/CSV_EA`: evidence extracted from the EA file, used to define the rules. The import reads the EA file itself (W-247).
- `Definitions`: the note layout and the `Source: EA` section.
- `MDSE Workbench`: a separate product-definition workspace. It is not authoritative for model semantics.
- `MDSE Bootstrap`: the Bootstrap plugin source and its docs (controlled plugin release, author registration, base test sheet; W-322).
- `99_System/06_Fileclasses`: generated Fileclass schemas (do not edit).
