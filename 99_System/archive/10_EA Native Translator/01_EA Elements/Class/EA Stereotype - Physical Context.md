---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Physical Context"
observedEndpointOccurrences: 299
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Physical Context

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Physical Context`
- **Observed relationship-endpoint occurrences:** 299

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Aggregation | [[EA Stereotype - System Partner]] | 69 | 4 | Settled | Map: participants on the Context endpoint |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 39 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 30 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Physical System Variant]] | 25 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[README_Object]] | 22 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 20 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 11 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[README_Actor]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Business Line]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 6 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Association | [[README_UseCase]] | 5 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Aggregation | [[EA Stereotype - Platform]] | 3 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Partner]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Association | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Generalization | [[EA Stereotype - Physical System Variant]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Usage «Responsibility» | [[EA Stereotype - Physical System Variant]] | 1 | 70 | Review | Review: StandardProfile Responsibility |

## Canvas

[[CANVAS_Class - Physical Context]]
