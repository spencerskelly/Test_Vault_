---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "State"
observedEndpointOccurrences: 3582
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — State

## Source identity

- **EA Object_Type:** `State`
- **Observed relationship-endpoint occurrences:** 3582

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Element - No Stereotype\|No stereotype]] | 872 |
| [[EA Stereotype - Fault State\|Fault State]] | 2 |
| [[EA Stereotype - System State\|System State]] | 2708 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 540 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 400 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 312 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 267 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 265 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 123 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | StateFlow | [[EA Element - No Stereotype]] | 110 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 98 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 91 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Aggregation | [[EA Stereotype - System State]] | 75 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 59 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Usage | [[README_UseCase]] | 58 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 53 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 51 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | StateFlow | [[README_StateNode]] | 43 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 38 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 34 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 30 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 29 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | StateFlow | [[README_StateNode]] | 25 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 24 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 19 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 16 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 13 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[EA Stereotype - block]] | 12 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 12 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 11 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Hardware Function]] | 9 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 9 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 9 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 8 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 8 | 14 | Review | Review: State allocation/context evidence |
| Incoming | NoteLink | [[README_Note]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | StateFlow | [[EA Stereotype - System State]] | 8 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - designConstraint]] | 7 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Electrical & Material Interface]] | 6 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - requirement]] | 6 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - block]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | StateFlow | [[README_Synchronization]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Incoming | StateFlow | [[README_Synchronization]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component + block]] | 4 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - designConstraint]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Module Function]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 4 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - System State]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 3 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Generalization | [[EA Stereotype - Hardware Function]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Function]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | ControlFlow | [[README_Action]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Action]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - Software Function]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[README_UseCase]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Regulatory Requirement]] | 2 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - System State]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Webasto Requirement]] | 2 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Software Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[README_Issue]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | StateFlow | [[EA Stereotype - Fault State]] | 2 | 47 | Deferred | Deferred: transition evidence |
| Incoming | Usage | [[README_Issue]] | 2 | 49 | Review | Review: Issue→State Usage |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - block]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Mechanical Interface]] | 1 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Decision]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Issue]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - Regulatory Requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Module]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «refine» | [[EA Stereotype - requirement]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Document]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - performanceRequirement]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Document]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | NoteLink | [[README_Note]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | StateFlow | [[README_Event]] | 1 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | StateFlow | [[README_Event]] | 1 | 47 | Deferred | Deferred: transition evidence |

## Canvas

[[CANVAS_State]]
