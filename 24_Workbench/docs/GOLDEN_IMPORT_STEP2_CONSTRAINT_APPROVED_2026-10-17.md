# Golden Import Step 2 — Constraint

Decision date: 2026-10-17. Status: APPROVED; implementation and parser validation pending.

- EA `Constraint` maps to reusable native SysML v2 `ConstraintDefinition`.
- Contextual applications are native `ConstraintUsage` in the owning element, referencing the definition; no separate MDSE note per usage.
- Each definition has one MDSE note with `type`, `subtype`, `eaType`, `eaStereotype` and source provenance in YAML.
- Preserve explicitly provided constraint expressions and parameters; do not infer expressions or owners when absent.
- Missing expression/owner/typing evidence remains reviewable, never silently fabricated.
- Validate serialization and type-checking with a pinned SysML v2 parser, source links and reimport stability.
