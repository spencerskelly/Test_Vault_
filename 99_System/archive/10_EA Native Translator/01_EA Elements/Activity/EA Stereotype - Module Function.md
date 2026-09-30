---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: "Module Function"
observedEndpointOccurrences: 119
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — Module Function

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** `Module Function`
- **Observed relationship-endpoint occurrences:** 119

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 13 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 12 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 7 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Hardware Function]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 5 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Usage | [[README_UseCase]] | 5 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 3 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Generalization | [[EA Stereotype - Module Function]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Business Line]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Data Interface]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency «trace» | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 1 | 13 | Settled | Map: describes / describedBy |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - Hardware Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - System Function]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - System Function]] | 1 | 54 | Review | Review: satisfy endpoint pattern |

## Canvas

[[CANVAS_Activity - Module Function]]
