# Golden Import — Multiplicity on owned usages

Decision date: 2026-10-17. Status: APPROVED; source extraction and native SysML v2 parser validation pending.

- Import explicitly defined EA multiplicity onto the corresponding owned, typed SysML v2 usage (for physical assembly containment, `PartUsage`).
- Multiple identical occurrences within one assembly may be represented by a **single usage with multiplicity** (e.g. `part powerModules : PowerModule[4];`), rather than an individual usage per unit.
- Different owning assemblies retain independent PartUsages referencing the same reusable PartDefinition; no duplicate definition notes.
- Preserve original source connector identity, association-end cardinality, direction and provenance. Normalize which EA cardinality applies to the child usage from trusted source-role evidence; never guess or default to four.
- Preserve EA multiplicity ranges when explicit; absent or ambiguous cardinality remains unspecified or flagged, never invented.
- Keep BOM-specific quantity and unit-of-measure evidence distinct from native usage multiplicity, per the approved BOM contract.
- Validate parser syntax, allowed multiplicity, ownership, stable identity and reimport behavior.

## Follow-up approval — missing multiplicity

Decision date: 2026-10-17. **Unspecified is the default** when the EA source has no explicit multiplicity. Do not populate `[1]` or any other numeric multiplicity by assumption. Preserve the distinction between source-absent cardinality and explicitly specified `[1]` in the source ledger/YAML provenance. Native serializer must omit the multiplicity annotation when absent, subject to native grammar validation.
