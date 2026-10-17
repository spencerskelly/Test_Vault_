# Golden Import — Activity aggregation as nested ActionUsage

Decision date: 2026-10-17. Status: APPROVED translation rule; implementation and native parser validation pending.

- For each semantically valid EA Activity → Activity Aggregation, represent the nested activity as a native SysML v2 `ActionUsage` owned in its parent activity, typed by a reusable `ActionDefinition` when an appropriate definition exists.
- Preserve **each distinct source Aggregation connector as a separate ActionUsage declaration** in the parent. Do not collapse connectors because their endpoints or child definitions match.
- Maintain one MDSE note per reusable ActionDefinition; owned usages remain in the parent's definition, with no standalone usage notes.
- Source role names take precedence; otherwise use stable deterministic child-derived usage names and suffixes to avoid collisions. Preserve connector IDs, aggregate-end flags, orientation and source provenance.
- Transfer explicitly modeled EA child-end multiplicity where semantically and syntactically valid. Missing multiplicity is unspecified.
- Confirm that the endpoints really represent nested execution/ownership rather than mere dependency or organizational grouping; flag incompatible or ambiguous relationships for review.
- Detect and exclude ownership cycles from native output; do not reverse or silently discard invalid edges.
- Verify the generated native SysML v2 syntax and source-to-output traceability before claiming accepted translation.

Source audit context: 148 Activity → Activity aggregation connectors in the reduced QEAX broad endpoint classification; this count is not an acceptance count.
