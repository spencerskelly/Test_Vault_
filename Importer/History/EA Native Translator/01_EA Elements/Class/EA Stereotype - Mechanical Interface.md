---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Mechanical Interface"
observedEndpointOccurrences: 44
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Mechanical Interface

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Mechanical Interface`
- **Observed relationship-endpoint occurrences:** 44

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 35 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Generic Physical Interface]] | 7 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Association | [[EA Stereotype - Physical Component]] | 1 | 8 | Review | Review: vague Association |

## Canvas

[[CANVAS_Class - Mechanical Interface]]
