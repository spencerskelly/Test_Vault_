---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Platform"
observedEndpointOccurrences: 122
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Platform

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Platform`
- **Observed relationship-endpoint occurrences:** 122

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 27 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Generalization | [[EA Stereotype - Physical System Variant]] | 10 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 9 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Sequence | [[EA Stereotype - Physical System Variant]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 7 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Stereotype - Platform]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 5 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 4 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 3 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Sequence | [[EA Stereotype - Physical System Variant]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - System Partner]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[README_Object]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Module]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Business Line]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[README_InformationItem]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Association | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Incoming | Generalization | [[EA Stereotype - Business Line]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Software Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - Platform]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Class - Platform]]
