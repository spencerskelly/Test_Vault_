# Golden Import Step 2 — Verification Case relationships

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser validation pending.

- EA `Activity:testCase` maps to a reusable native SysML v2 `VerificationCaseDefinition`.
- Preserve explicitly modeled EA verification relationships to requirements using native SysML v2 verification semantics, only when source connector type, direction, endpoints and roles support that mapping.
- Do not infer verification relationships from names, proximity, notes or organizational package containment.
- Where source relationships are ambiguous, preserve evidence and flag review rather than inventing a native verify relationship.
- One MDSE note per VerificationCaseDefinition; contextual usages do not create additional notes.
- Preserve `type`, `subtype`, `eaType`, `eaStereotype`, and source provenance in YAML; test execution/results remain separate from verification case definitions.
- Verify native serialization, requirement target resolution, provenance and idempotent reimport.
