---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Change"
observedEndpointOccurrences: 109
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Change

## Source identity

- **EA Object_Type:** `Change`
- **Observed relationship-endpoint occurrences:** 109

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Change\|No stereotype]] | 109 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Abstraction «allocate» | [[README_Issue]] | 42 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[README_Change]] | 12 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Nesting | [[README_Change]] | 6 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Realisation | [[EA Element - No Stereotype]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Issue]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Object]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Actor]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - functionalRequirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - testCase]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |

## Canvas

[[CANVAS_Change]]
