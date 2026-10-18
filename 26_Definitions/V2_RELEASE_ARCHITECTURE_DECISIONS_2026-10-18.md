# V2 release architecture — approved decisions

Date: 2026-10-18. Status: USER APPROVED. These are product architecture decisions, not new semantic mappings.

## ADR-V2-01 — Phased release
First usable release: validated EA import and read-only Workbench. Graphical editing and BOM importer are subsequent phases. Do not represent work from later phases as required for first viewing, but retain their interfaces and recovery requirements now.

## ADR-V2-02 — Model authority
Authoritative formal model is SysML v2 text in the final governed `## SysML v2` section of a Markdown note. Structural, visual, table and other Workbench editing actions must eventually issue parser-validated, transactional changes to that text. Read-only initial Workbench must not introduce independent semantic state. YAML and diagrams are derived navigation/provenance/evidence, not separate native authority.

## ADR-V2-03 — Hybrid managed configuration
Core plugin and schema compatibility is centrally governed. Approved personal preferences are retained through updates. Develop versioned configuration ownership, migration, dry-run diff, rollback and validation before distribution. Do not overwrite user-customized settings indiscriminately.

## ADR-V2-04 — Cross-vault sequencing
Design IDs, links, resolver interfaces and lifecycle for cross-vault use now. Ship operational cross-vault support after single-vault validation; avoid a first-release dependency on it.

## ADR-V2-05 — Defer all EA diagrams until after toolchain and golden import completion
**Approved October 18, 2026.** EA diagram tables, diagrams, layout, Canvas generation from EA, diagram-based source normalization and any requirement to verify diagram fidelity are **out of scope** for all active V2 tools and golden import tests. Use EA elements/connectors and other non-diagram source evidence only. Native SysML-derived Workbench views remain in scope and must not need EA diagrams. [Detailed STEP-02A scope lock](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md). Reopen only after the golden import is accepted, all planned tools are complete/tested, and the user approves a diagram phase.

## Non-negotiable retained rules
- Approved mappings remain approved and are not reopened because implementation is incomplete.
- Native OMG SysML v2 semantics only; non-native MDSE evidence and explicit review flags remain distinct.
- One reusable definition note; owning-context usages are not duplicate definition notes.
- Source QEAX/BOM and row-level data stay outside the public repository.
- V2 is independently buildable and does not depend on archived V1 runtime.
- Each source element/connector receives an auditable disposition; zero hidden drops.
- Syntax parsing, semantic validation, end-user UI, and package/release acceptance are different gates.

## Current release acceptance targets
R1: read-only source fingerprint/schema and ledger coverage for reduced QEAX.
R2: deterministic canonical source mapping with native/extension/deferred outcomes.
R3: valid native SysML output for eligible scoped rows, separately parser tested.
R4: generated notes in a fresh disposable v2 Base, no overwrite of source/approved vault.
R5: read-only Workbench shows definition/usage distinction, navigation, provenance and diagnostics consistently.
R6: independent Windows/macOS/offline packaging and locked release dependencies.
R7: no claim of golden import until outcome and UI checks are complete.

## Next recovery actions
Build a traceability catalog linking decision → source authority → executable implementation → synthetic tests → real-source verification → parser verification → read-only Workbench coverage → release gate. Classify each field as approved, implemented, validated synthetic, validated real-source, parser accepted, GUI accepted, released, or gap. Reuse Phase 8/9 bridge and October 17 aggregation/family decisions rather than recoding them.
