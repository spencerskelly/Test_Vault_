# Golden Import — EA ControlFlow

Decision date: 2026-10-17. Status: APPROVED translation policy; native parser and source-level validation pending.

- EA `ControlFlow` between compatible actions/activities translates to native SysML v2 `Succession`, preserving the source-defined execution order.
- Preserve explicitly modeled guard conditions as native guard semantics only where context and parser validity support them; otherwise retain their exact source evidence for review, without silently dropping guards.
- `Succession` establishes control order, not item/data transfer. Do not convert ordinary ControlFlow to generic Flow or SuccessionFlow without explicit transfer evidence.
- Normalize trusted source and target orientation, owning workflow context and participant action usages. Flag unresolved endpoints, direction or guards rather than inventing semantics.
- Preserve original EA connector identity, type/stereotype, guard expression and source provenance. No separate MDSE note for succession usages.
- Validate against pinned official SysML v2 grammar/library and repeat-import stability before native acceptance.
