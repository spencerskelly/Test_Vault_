---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: "Hardware Function"
observedEndpointOccurrences: 815
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — Hardware Function

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** `Hardware Function`
- **Observed relationship-endpoint occurrences:** 815

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 231 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Generalization | [[EA Stereotype - Hardware Function]] | 68 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 49 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 45 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Function]] | 38 | 3 | Settled | Map: parent / child |
| Outgoing | Aggregation | [[EA Stereotype - System Function]] | 38 | 3 | Settled | Map: parent / child |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 31 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 27 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 18 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 17 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 14 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 12 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 9 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Module Function]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 6 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 5 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Aggregation | [[EA Stereotype - System Function]] | 4 | 3 | Settled | Map: parent / child |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 4 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | ControlFlow | [[EA Stereotype - Hardware Function]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 3 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 3 | 24 | Settled | Map: describes / describedBy |
| Incoming | Usage | [[README_UseCase]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Electrical & Material Interface]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | ControlFlow | [[EA Stereotype - System Function]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - Functional]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Element - No Stereotype]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - Module Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - System Function]] | 1 | 48 | Review | Review: Activity→Activity Realisation |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 1 | 55 | Review | Review: Realisation endpoint pattern |

## Canvas

[[CANVAS_Activity - Hardware Function]]
