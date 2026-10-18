---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: ""
observedEndpointOccurrences: 2506
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — No Stereotype

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** none
- **Observed relationship-endpoint occurrences:** 2506

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 336 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 196 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 173 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 160 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 139 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 123 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 113 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 109 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 75 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 61 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 58 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 54 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 49 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 48 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 41 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 39 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 35 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Usage | [[README_UseCase]] | 32 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 25 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | ControlFlow | [[README_Decision]] | 21 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 20 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | ControlFlow | [[README_Decision]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Synchronization]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Generalization | [[EA Stereotype - Hardware Function]] | 17 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Hardware Function]] | 14 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 12 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | ControlFlow | [[README_StateNode]] | 10 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Synchronization]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Module Function]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 6 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 5 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | ControlFlow | [[README_Action]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 4 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Generalization | [[EA Stereotype - Software Function]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - testCase]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[README_Change]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Software Parameter]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - functionalRequirement]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 3 | 13 | Settled | Map: describes / describedBy |
| Incoming | ControlFlow | [[README_Object]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - System Function]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Association | [[README_Actor]] | 2 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | ControlFlow | [[README_Action]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System Function]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Object]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - System Function]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_UseCase]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Platform]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Partner]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Hardware Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency | [[README_Change]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Module Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Software Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - designConstraint]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Hardware Function]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | ControlFlow | [[EA Stereotype - Module Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_UseCase]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - Hardware Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Object]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Software Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Boundary]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_UseCase]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «verify» | [[EA Stereotype - requirement]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Electrical & Material Interface]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[README_Object]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Usage | [[EA Stereotype - System Function]] | 1 | 59 | Review | Review: Usage endpoint pattern |

## Canvas

[[CANVAS_Activity - No Stereotype]]
