---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "InformationItem"
observedEndpointOccurrences: 388
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — InformationItem

## Source identity

- **EA Object_Type:** `InformationItem`
- **Observed relationship-endpoint occurrences:** 388

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_InformationItem\|No stereotype]] | 388 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 121 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 25 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - Document]] | 24 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 22 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 21 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 14 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Software Component]] | 14 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 9 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 7 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 7 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 6 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Module]] | 6 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - Hardware Component]] | 5 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[README_UseCase]] | 5 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - requirement]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 4 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 3 | 13 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - System State]] | 3 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Function]] | 3 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 3 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[README_Object]] | 3 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[README_Issue]] | 3 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[README_Action]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Connector | [[EA Element - No Stereotype]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Dependency «refine» | [[README_Action]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - Hardware Function]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - System Function]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component + block]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Nesting | [[README_InformationItem]] | 2 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 1 | 13 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[README_Actor]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Text]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Physical System Variant]] | 1 | 7 | Settled | Map: describes / describedBy |
| Incoming | Dependency | [[EA Stereotype - testCase]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «refine» | [[EA Stereotype - Module]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - Software Component]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - extendedRequirement]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Actor]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[README_Change]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Module]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Actor]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Platform]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - block]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[README_Text]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Nesting | [[EA Stereotype - Webasto Requirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |

## Canvas

[[CANVAS_InformationItem]]
