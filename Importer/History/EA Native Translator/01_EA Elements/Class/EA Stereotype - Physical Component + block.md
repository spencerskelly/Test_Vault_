---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Physical Component | block"
observedEndpointOccurrences: 36
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Physical Component | block

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Physical Component | block`
- **Observed relationship-endpoint occurrences:** 36

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Physical Component + block]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 4 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 2 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Generalization | [[EA Stereotype - Software Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Realisation | [[EA Stereotype - designConstraint]] | 1 | 55 | Review | Review: Realisation endpoint pattern |

## Canvas

[[CANVAS_Class - Physical Component + block]]
