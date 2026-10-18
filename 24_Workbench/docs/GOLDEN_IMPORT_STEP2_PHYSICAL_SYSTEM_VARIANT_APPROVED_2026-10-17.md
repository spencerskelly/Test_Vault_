# Golden Import Step 2 — Physical System Variant

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- EA `Class:Physical System Variant` maps directly to a reusable native SysML v2 `PartDefinition`.
- Preserve the EA stereotype and type, MDSE type and subtype, plus source provenance in YAML.
- Import its explicitly modeled EA relationships according to existing relationship-specific rules and evidence gates; do not infer specialization, variation, redefinition, or subtype from the stereotype or name alone.
- Relationships requiring unresolved translation remain explicitly reviewable in the connector ledger, without blocking definition creation.
- Revisit relationship modeling later as directed by the model owner; no broad relationship redesign in Step 2.
- One MDSE note per defined element; usages reference the definition without separate notes.
