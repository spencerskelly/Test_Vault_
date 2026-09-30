---
uid:
type: EA Element
status: Working
eaMetaclass: "State"
eaStereotype: ""
observedEndpointOccurrences: 872
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA State — No Stereotype

## Source identity

- **EA Object_Type:** `State`
- **EA stereotype:** none
- **Observed relationship-endpoint occurrences:** 872

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 176 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | StateFlow | [[EA Element - No Stereotype]] | 110 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 68 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 60 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | StateFlow | [[README_StateNode]] | 41 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 35 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | StateFlow | [[README_StateNode]] | 24 | 47 | Deferred | Deferred: transition evidence |
| Incoming | Generalization | [[EA Stereotype - System State]] | 23 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 22 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 21 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 20 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 16 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 12 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 8 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 8 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 8 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 7 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 7 | 24 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 6 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | StateFlow | [[README_Synchronization]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Incoming | StateFlow | [[README_Synchronization]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Incoming | Usage | [[README_UseCase]] | 4 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - designConstraint]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - requirement]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 3 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | NoteLink | [[README_Note]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Hardware Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[README_Issue]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | StateFlow | [[EA Stereotype - Fault State]] | 2 | 47 | Deferred | Deferred: transition evidence |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - System State]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Issue]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - Regulatory Requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Webasto Requirement]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | StateFlow | [[EA Stereotype - System State]] | 1 | 47 | Deferred | Deferred: transition evidence |

## Canvas

[[CANVAS_State - No Stereotype]]
