---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: "System Function"
observedEndpointOccurrences: 2192
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — System Function

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** `System Function`
- **Observed relationship-endpoint occurrences:** 2192

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 224 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 187 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 185 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 158 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Usage | [[README_UseCase]] | 114 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 113 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 108 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 88 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 80 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 62 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 57 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 51 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 48 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Hardware Function]] | 45 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Stereotype - Hardware Function]] | 38 | 3 | Settled | Map: parent / child |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 35 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 35 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | NoteLink | [[README_Note]] | 33 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 26 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 25 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 22 | 3 | Settled | Map: parent / child |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 21 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 18 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Generalization | [[EA Stereotype - Software Function]] | 12 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Function]] | 12 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Platform]] | 9 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 8 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Function]] | 4 | 3 | Settled | Map: parent / child |
| Outgoing | Association | [[README_UseCase]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Generalization | [[EA Stereotype - Module Function]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Software Function]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Hardware Function]] | 3 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Stereotype - Module Function]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Context]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - functionalRequirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Software Function]] | 2 | 3 | Settled | Map: parent / child |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - Hardware Function]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - Module Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency | [[EA Stereotype - Software Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Generalization | [[EA Stereotype - block]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Usage | [[README_UseCase]] | 2 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Document]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Electrical & Material Interface]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Element - No Stereotype]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | ControlFlow | [[EA Stereotype - Hardware Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - Module Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Module Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Software Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «RecoveryRequirement» | [[EA Stereotype - requirement]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Module Function]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - System Function]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - System State]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - Hardware Function]] | 1 | 48 | Review | Review: Activity→Activity Realisation |
| Incoming | Usage | [[EA Element - No Stereotype]] | 1 | 59 | Review | Review: Usage endpoint pattern |

## Canvas

[[CANVAS_Activity - System Function]]
