---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: "testCase"
observedEndpointOccurrences: 361
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — testCase

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** `testCase`
- **Observed relationship-endpoint occurrences:** 361

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «verify» | [[EA Stereotype - requirement]] | 272 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «verify» | [[EA Stereotype - designConstraint]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «verify» | [[EA Stereotype - functionalRequirement]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Nesting | [[EA Stereotype - testCase]] | 6 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 5 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency | [[README_Object]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Nesting | [[EA Element - No Stereotype]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Dependency «trace» | [[README_Text]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency | [[EA Stereotype - Image]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_InformationItem]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Change]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - Hardware Function]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - extendedRequirement]] | 1 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Generalization | [[EA Stereotype - testCase]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |

## Canvas

[[CANVAS_Activity - testCase]]
