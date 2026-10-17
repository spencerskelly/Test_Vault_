# Golden Import — State aggregation as nested StateUsage

Decision date: 2026-10-17. Status: APPROVED translation rule; implementation and native parser validation pending.

- For each semantically valid EA State → State Aggregation, represent the child as a native SysML v2 `StateUsage` nested within the owning parent state, referencing a reusable state definition where available.
- Preserve **every distinct EA connector** as a distinct nested usage declaration; matching endpoint pairs are not sufficient evidence of duplication.
- Maintain one MDSE note per reusable state definition, not per usage. Preserve original EA connector identities, source roles, aggregation flags, directions, multiplicities and provenance.
- Prefer explicit EA role/name; otherwise generate stable child-derived usage names with deterministic collision suffixes.
- Preserve explicit applicable child-end multiplicity only where semantically and syntactically valid; absent multiplicity stays unspecified.
- Ensure source relationship genuinely denotes state nesting rather than mere grouping or transition; incompatible cases remain reviewable. Detect ownership cycles and exclude affected usages from native output until resolved.
- Provide structural and visual Workbench containment/navigation using distinct StateUsage semantics, never physical PartUsage or Activity ActionUsage. Retain round-trip/provenance and validator diagnostics.
- Native parser/conformance testing is outstanding; no translated connector is claimed accepted yet.

Source audit context: 76 State → State aggregation connectors in the reduced QEAX broad endpoint classification; count is not a successful-conversion count.
