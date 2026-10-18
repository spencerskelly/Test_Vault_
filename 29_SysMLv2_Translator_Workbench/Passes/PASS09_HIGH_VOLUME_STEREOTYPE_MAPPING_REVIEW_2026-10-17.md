# Phase 9 — High-volume generalization stereotype review

Status: proposals only. No approved/native eligibility changes; no private source rows.

| EA source pattern (observed count) | Native candidate | Evidence needed |
|---|---|---|
| Hardware Component → Hardware Component (767) | PartDefinition specialization | reusable definitions, not installed occurrences or decomposition |
| Physical Component → Physical Component (181) | PartDefinition specialization | distinguish definition from actual assembly usage |
| Module → Module (150) | PartDefinition specialization | reusable type-to-type specialization |
| Logical Signal → Logical Signal (579) | ItemDefinition specialization candidate | signal/item versus event, port, flow or occurrence |
| System State → System State (218) | StateDefinition specialization candidate | exclude nested substates within a state usage |
| System Function → System Function (187) | ActionDefinition specialization candidate | exclude nested subactivities and performer allocations |
| UseCase → UseCase (216) | CaseDefinition specialization candidate | exclude include, extend and required steps |
| Data Interface → Electrical & Material Interface (108) | InterfaceDefinition cross-kind review | validate boundary and interface semantics; no binding-port collapse |

Counts are observed aggregate stereotype patterns, not a claim of accepted valid specialization. They are not a comprehensive partition of all 3,531 review cases.

## Workbench implementation contract

Structural: keep definition generalization distinct from usage typing, redefinition, containment and nested state/activity usages. Visual: directed subtype-to-supertype specialization edge distinguishable from connections/ownership; ports-as-parts still appear on internal views, while Binding Port stays distinct. Navigation: both endpoint definitions and EA evidence. Validation: kind compatibility, direction, cycle and provenance checks; deferred links remain visible as review. Round-trip: preserve source endpoints, connector direction, stereotype, rule revision and local evidence; no source GUIDs in public repo.

## Qualification

Confirm standard native syntax and semantics, document EA conventions, add negative examples for states/actions/ports, run independent matrix tests and visual/structural assertions. No translator or native emitter enabled by this proposal.