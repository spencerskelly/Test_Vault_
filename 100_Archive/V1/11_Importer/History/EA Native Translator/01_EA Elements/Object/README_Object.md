---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Object"
observedEndpointOccurrences: 868
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Object

## Source identity

- **EA Object_Type:** `Object`
- **Observed relationship-endpoint occurrences:** 868

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Object\|No stereotype]] | 868 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Aggregation | [[README_Object]] | 195 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Sequence | [[README_Object]] | 77 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Association | [[README_UseCase]] | 39 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 27 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 27 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 22 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 18 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Association | [[README_UseCase]] | 17 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 15 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 14 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 13 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 8 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Dependency «trace» | [[README_Text]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Sequence | [[EA Stereotype - Hardware Component]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Connector | [[README_Object]] | 6 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | ControlFlow | [[README_Action]] | 6 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_StateNode]] | 5 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Abstraction «allocate» | [[README_Change]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[README_Action]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - testCase]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 4 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Sequence | [[EA Stereotype - Hardware Component]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 3 | 24 | Settled | Map: describes / describedBy |
| Incoming | Aggregation | [[EA Stereotype - Electrical & Material Interface]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Decision]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Decision]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Synchronization]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency «trace» | [[README_Change]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - block]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[README_Text]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - block]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - Physical System Variant]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[README_Object]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Realisation | [[EA Element - No Stereotype]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Sequence | [[README_Sequence]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Object]]
