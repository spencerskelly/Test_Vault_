---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Data Interface"
observedEndpointOccurrences: 156
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Data Interface

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Data Interface`
- **Observed relationship-endpoint occurrences:** 156

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 108 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Generic Physical Interface]] | 13 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 9 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 5 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Data Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |

## Canvas

[[CANVAS_Class - Data Interface]]
