# Golden Import — Use Case aggregation as nested usage

Decision date: 2026-10-17. Status: APPROVED mapping policy; source-row conformance and native parser verification pending.

- Translate a semantically valid EA Use Case → Use Case Aggregation that represents genuine decomposition into a native nested SysML v2 `UseCaseUsage` in the owning parent use case, typed by a reusable `UseCaseDefinition` where available.
- Keep this ownership/decomposition mapping semantically distinct from approved EA `include` (required use) and `extend` (conditional optional extension). Do not reinterpret aggregation as either include or extend.
- Preserve **each independently modeled EA aggregation connector** as a separate nested usage declaration even where parent and child endpoints repeat. Keep only one MDSE note per reusable definition, not per usage.
- Preserve source connector ID, endpoint orientation, aggregate flag, explicit end-role naming, multiplicity and provenance. Missing multiplicity remains unspecified. If role name is absent, derive a stable usage name from the child and add deterministic suffixes on collisions.
- Confirm source relationship denotes actual nested use-case decomposition, not merely diagram grouping or dependency. Flag ambiguous/incompatible relationships and ownership cycles instead of forcing a native usage.
- Workbench structural view shows nested UseCaseUsage and parent containment; visual view displays an independently navigable, typed nested usage, with traceability to source connector and validation messages. Distinguish include/extend links visually and semantically.
- Native syntax/parser, round-trip identity and the ten fixture connectors are still pending validation; approval does not imply ten successful translations.

Audit context: 10 EA Use Case → Use Case aggregation connectors in the reduced QEAX endpoint classification.
