---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Activity"
observedEndpointOccurrences: 6230
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Activity

## Source identity

- **EA Object_Type:** `Activity`
- **Observed relationship-endpoint occurrences:** 6230

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Element - No Stereotype\|No stereotype]] | 2506 |
| [[EA Stereotype - Hardware Function\|Hardware Function]] | 815 |
| [[EA Stereotype - Module Function\|Module Function]] | 119 |
| [[EA Stereotype - Software Function\|Software Function]] | 237 |
| [[EA Stereotype - System Function\|System Function]] | 2192 |
| [[EA Stereotype - testCase\|testCase]] | 361 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 404 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 361 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 336 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 275 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «verify» | [[EA Stereotype - requirement]] | 272 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 269 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 239 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 196 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 160 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 150 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 139 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Usage | [[README_UseCase]] | 125 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 123 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 112 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 105 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 98 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Stereotype - Hardware Function]] | 97 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 86 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 85 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 82 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 77 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 75 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 71 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 71 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 61 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 60 | 3 | Settled | Map: parent / child |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 54 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 49 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Function]] | 42 | 3 | Settled | Map: parent / child |
| Outgoing | Generalization | [[EA Stereotype - Software Function]] | 40 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 35 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 32 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Usage | [[README_UseCase]] | 32 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - block]] | 30 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 28 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Aggregation | [[EA Stereotype - Software Function]] | 27 | 3 | Settled | Map: parent / child |
| Outgoing | Dependency «verify» | [[EA Stereotype - designConstraint]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «verify» | [[EA Stereotype - functionalRequirement]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Incoming | ControlFlow | [[README_Decision]] | 21 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 20 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 20 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Module Function]] | 20 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | ControlFlow | [[README_Decision]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Synchronization]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 17 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 13 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 12 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | ControlFlow | [[README_StateNode]] | 10 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Nesting | [[EA Stereotype - testCase]] | 10 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 9 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 9 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 9 | 24 | Settled | Map: describes / describedBy |
| Outgoing | ControlFlow | [[README_Synchronization]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 7 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Stereotype - Hardware Function]] | 6 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency «trace» | [[README_Issue]] | 6 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - functionalRequirement]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 5 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Dependency | [[README_Object]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 4 | 13 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[README_UseCase]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | ControlFlow | [[README_Action]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System Function]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 4 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[README_Change]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Software Parameter]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Electrical & Material Interface]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | ControlFlow | [[README_Object]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Software Function]] | 3 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «trace» | [[README_Text]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_UseCase]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Context]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Association | [[README_Actor]] | 2 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | ControlFlow | [[README_Action]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Object]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_UseCase]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - Module Function]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Platform]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Partner]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[README_Change]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Physical System Variant]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Functional]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - System Function]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Usage | [[README_UseCase]] | 2 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - designConstraint]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Document]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Association | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_UseCase]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Module Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Software Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Image]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_InformationItem]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - requirement]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Change]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Boundary]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - Hardware Function]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - extendedRequirement]] | 1 | 63 | Settled | Map: verifies / verifiedBy |
| Incoming | Dependency «verify» | [[EA Stereotype - requirement]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - testCase]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System State]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - Electrical & Material Interface]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[README_Object]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Hardware Function]] | 1 | 48 | Review | Review: Activity→Activity Realisation |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Usage | [[EA Stereotype - System Function]] | 1 | 59 | Review | Review: Usage endpoint pattern |

## Canvas

[[CANVAS_Activity]]
