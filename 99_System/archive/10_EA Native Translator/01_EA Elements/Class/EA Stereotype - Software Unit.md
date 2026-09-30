---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Software Unit"
observedEndpointOccurrences: 3
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Software Unit

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Software Unit`
- **Observed relationship-endpoint occurrences:** 3

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |

## Canvas

[[CANVAS_Class - Software Unit]]
