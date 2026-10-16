---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Generic Physical Interface"
observedEndpointOccurrences: 37
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Generic Physical Interface

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Generic Physical Interface`
- **Observed relationship-endpoint occurrences:** 37

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Generalization | [[EA Stereotype - Data Interface]] | 13 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Mechanical Interface]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Generic Physical Interface]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 5 | 53 | Review | Review: allocate endpoint pattern |

## Canvas

[[CANVAS_Class - Generic Physical Interface]]
