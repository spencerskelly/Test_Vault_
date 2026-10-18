# V2 executable selector recovery — 2026-10-18

Status: candidate-selector inspection only. Approved October 17 mappings remain unchanged.

## Result
The exact 60 approved EA element families were compared to `sysml_v2_semantic_rules.v0.2.json` and `project_v2_element_candidates.py`:
- 2 exact registry selectors.
- 26 families selected only by generic type-wide wildcard.
- 32 families not selected at all.
- 26 relationship families have exact registry keys, but the relationship projector returns deferred review counts and generates no native semantics.

The machine-readable row-by-row snapshot is `26_Definitions/v2_executable_candidate_crosswalk.v0.1.json`. A regression test recomputes every match and is included in main CI.

## Critical integration warning
Registry membership does not imply alignment with later approved semantic decisions. For example, the provisional `InformationItem` selector targets `ItemDefinition`, whereas the approved October 17 reconciliation makes it a descriptive MDSE note, not a native ItemDefinition. This is a candidate-registry implementation divergence, **not a reason to revisit the approved decision**.

Some wildcard selectors are especially risky: a generic Class or Activity selector must not bypass exact source-family decisions. Maintain exact approved-family precedence and no silent fallback.

## Next engineering unit
Inventory existing canonical graph, Phase 3/8/9 runtime entrypoints and native serializers, then implement a **read-only approved-rule resolution verifier** and golden fixtures. Do not directly mutate the pinned provisional registry, expand native emission, or repeat family policy debates. Independently verify CI and run a scoped end-to-end dry-run once the approved resolver exists.

No real source row data belongs in this repository.
