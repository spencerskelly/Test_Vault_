---
uid:
type: EA Element
status: Working
eaMetaclass: "Activity"
eaStereotype: "Software Function"
observedEndpointOccurrences: 237
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Activity — Software Function

## Source identity

- **EA Object_Type:** `Activity`
- **EA stereotype:** `Software Function`
- **Observed relationship-endpoint occurrences:** 237

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Software Function]] | 32 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - block]] | 28 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Software Function]] | 25 | 3 | Settled | Map: parent / child |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 22 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - functionalRequirement]] | 12 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Generalization | [[EA Stereotype - System Function]] | 12 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Usage | [[README_UseCase]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Incoming | Aggregation | [[EA Stereotype - System Function]] | 2 | 3 | Settled | Map: parent / child |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «trace» | [[README_Issue]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Generalization | [[EA Element - No Stereotype]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - System State]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Module]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 1 | 12 | Settled | Map: affects / affectedBy |
| Incoming | Association | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |

## Canvas

[[CANVAS_Activity - Software Function]]
