# MDSE v2 — Tools

**Status:** Scaffolding; no executable v2 release claimed.

Store source translators, SysML textual emitters/parsers, validation and Workbench v2 implementation in clearly versioned subdirectories. Reuse shared **source ingestion** where possible, but keep v1 and v2 transformation profiles and output schema versions separate.

## Intended modules
- `source-adapter/`: normalized EA CSV / QEAX evidence input; shared rules must be governed before extraction into common code.
- `translation/`: v1-to-v2 rules and explicitly approved MDSE corrections.
- `sysml/`: standards-valid text generation, symbol ownership and reference resolution.
- `workbench/`: Obsidian editing, navigation and visual interaction for authoritative SysML declarations.
- `bom/`: BOM source adaptation, effective configuration and source ledger.

Folders above are **planned module names**, not current completed tools. Never check production models, extracted company BOMs, or QEAX databases into this tooling workspace.
