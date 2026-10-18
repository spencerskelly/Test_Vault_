---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Business Line"
observedEndpointOccurrences: 349
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Business Line

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Business Line`
- **Observed relationship-endpoint occurrences:** 349

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 80 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 76 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 49 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Physical System Variant]] | 23 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 22 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Association | [[README_UseCase]] | 12 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Business Line]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Sequence | [[EA Stereotype - Module]] | 5 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Physical System Variant]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Sequence | [[EA Stereotype - Physical System Variant]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[EA Stereotype - Physical System Variant]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - block]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[README_UseCase]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Generalization | [[EA Stereotype - Platform]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - Business Line]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Usage «Responsibility» | [[EA Stereotype - block]] | 2 | 70 | Review | Review: StandardProfile Responsibility |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Physical Component + block]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Generalization | [[EA Stereotype - Platform]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | NoteLink | [[README_Note]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Usage «Responsibility» | [[EA Stereotype - Business Line]] | 1 | 70 | Review | Review: StandardProfile Responsibility |

## Canvas

[[CANVAS_Class - Business Line]]
