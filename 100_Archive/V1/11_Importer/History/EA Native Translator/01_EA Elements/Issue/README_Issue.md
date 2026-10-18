---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Issue"
observedEndpointOccurrences: 355
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Issue

## Source identity

- **EA Object_Type:** `Issue`
- **Observed relationship-endpoint occurrences:** 355

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Issue\|No stereotype]] | 355 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Abstraction «allocate» | [[README_Change]] | 42 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 41 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 27 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 26 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[README_UseCase]] | 26 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[README_Action]] | 20 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 16 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 11 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «trace» | [[README_UseCase]] | 11 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | ControlFlow | [[README_Decision]] | 10 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - functionalRequirement]] | 8 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 6 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 6 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - testCase]] | 5 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | ControlFlow | [[README_StateNode]] | 5 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 4 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 3 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 3 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Actor]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_ProxyConnector]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[README_UseCase]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[README_Change]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Software Function]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - testCase]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Generalization | [[README_Issue]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Realisation | [[EA Element - No Stereotype]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Usage | [[EA Stereotype - System State]] | 2 | 49 | Review | Review: Issue→State Usage |
| Outgoing | UseCase «extend» | [[README_UseCase]] | 2 | 60 | Review | Review: extend endpoint pattern |
| Incoming | Abstraction «Derive» | [[EA Stereotype - functionalRequirement]] | 1 | 67 | Review | Review: StandardProfile Derive endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 1 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Association | [[README_Actor]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Outgoing | Association | [[EA Stereotype - Module]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Outgoing | Association | [[EA Stereotype - Physical System Variant]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Outgoing | ControlFlow | [[README_Action]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - testCase]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Partner]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Dependency «trace» | [[README_ProxyConnector]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Sequence | [[EA Stereotype - System Partner]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Issue]]
