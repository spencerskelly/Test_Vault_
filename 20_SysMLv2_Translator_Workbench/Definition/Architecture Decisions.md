# MDSE v2 — Architecture Decisions

**Status:** Recorded user direction, implementation not yet approved or verified. **Date:** 2026-10-15.

## Accepted direction
- New development goes into the **v2 workspace**. Version 1 is maintained separately and used as historical migration/reference evidence.
- Retain main MDSE element-to-Markdown-note mappings.
- **SysML v2 language is authoritative** for formal structure and relationships.
- Workbench is the principal user interface for editing and visualization, and must edit the one authoritative model.
- Standard OMG SysML v1-to-v2 transformation is the default. Existing approved MDSE source-interpretation rules may override it when documented with evidence and standards-valid output.
- Unexpected source concepts remain review findings until resolved rather than silently inventing relationships.
- Shared data should include source semantics, provenance and utilities that do not embed v1- or v2-specific meaning.
- Any v2 improvement applicable to v1 is a **proposal for approval**, not an automatic cross-version change.

## Open architecture decisions
1. Whether authoritative SysML textual declarations live in Markdown code regions or linked `.sysml` files; the standard extract must preserve namespace and ownership independently from folder placement.
2. Fragment ownership, cross-note symbol identity, and safe two-way Workbench editing.
3. Qualified nonstandard extension approach for metadata and genuinely unsupported relationships.
4. Mapping of Local Model occurrences to native v2 usages and relationships without information loss.
5. External parser and release conformance gates.

## Version boundary
A change in v2 never modifies `10_*`, `11_*` or any other v1-prefixed area without an explicit cross-version approval. Shared changes must demonstrate compatibility with both pipelines.
