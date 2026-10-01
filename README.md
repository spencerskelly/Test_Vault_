# Test_Vault_

A workspace, not the vault that will be built. It defines the EA-to-MDSE translator and the conventions the real vault will follow (W-01). The real vault is generated later from the Sparx EA file.

## Start here

1. `99_System/10_Docs/EA Native Importer Comprehensive Handoff - 2026-10-01.md`: current importer/occurrence/repository audit and next-chat continuation point.
2. `99_System/10_Docs/Handoff - Continue Here.md`: ongoing workspace handoff and reading order.
3. `99_System/10_Docs/Translator Definition.md`: what the stage 1 translator must do. Kept current.
4. `99_System/10_Docs/Workspace Decision Log.md`: every decision, and the Open list at the end.

## Folders

- `99_System/03_Schemas`: the class, relationship, element, connector, field, tag and package rules, as YAML.
- `99_System/05_Templates`, `08_Scripts`: the class templates and the id and uid snippets.
- `99_System/10_Docs`: the decision log, handoff, Translator Definition, Post-Import Tasks and Ruleset 1.22.
- `99_System/CSV_EA`: evidence extracted from the EA file, used to define the rules. The import reads the EA file itself (W-247).
- `Definitions`: the note layout and the `Source: EA` section.
- `MDSE Workbench`: a separate product-definition workspace. It is not authoritative for model semantics.
