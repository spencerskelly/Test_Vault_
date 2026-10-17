# Golden Import Step 2 — Unstereotyped EA Class

Decision date: 2026-10-17. Status: APPROVED; implementation and per-row review checks pending.

- EA `Class` elements without a stereotype default to a reusable native SysML v2 `PartDefinition`.
- Preserve `eaType: Class`, EA stereotype (empty when absent), and MDSE type/subtype in YAML, with source identity and provenance.
- If explicit source evidence establishes another semantic kind, flag for review rather than silently forcing PartDefinition.
- Each definition has one MDSE note; usages are represented in owning models and do not generate additional notes.
- Preserve explicitly modeled relationships under their own approved connector rules. Native parser and reimport checks still apply.
