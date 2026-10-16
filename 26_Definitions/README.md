# MDSE v2 — Definition

**Status:** Development / proposed until approved.

This is the v2 authoritative design workspace for mapping, structure, relationships, SysML textual ownership, and BOM integration. It complements the existing `README_SysMLv2_Translator_Workbench.md` rather than overriding its history.

## Start here
1. [Structural mapping contract](Structural%20Mapping%20Contract.md) — next Gate A working definition of definitions, usages, ownership, ports, connectors and BOM structure.
2. [Architecture decisions](Architecture Decisions.md) — adopted v2 direction versus open decisions.
3. [BOM integration](BOM Integration.md) — manufacturing structure, alternates, configuration and traceability.
4. [Mapping and conformance](Mapping and Conformance.md) — OMG-first mapping reviews and exceptions.
5. [V2 delivery plan](V2 Delivery Plan.md) — gated roadmap and acceptance criteria.

## Rules
- **Only v2 files govern v2 outputs**; do not modify v1 mappings as a side effect.
- Main approved MDSE element-to-note mappings remain the default.
- SysML v2 text is the authority for formal structure and relationships; Workbench is its interface, not a second authoring authority.
- Shared EA input semantics, source identity and evidence stay reusable across both lines.
- Exceptional transformations require explicit disposition, source evidence and review.
- BOM-specific revision/effectivity records are distinct from structural assertions.
