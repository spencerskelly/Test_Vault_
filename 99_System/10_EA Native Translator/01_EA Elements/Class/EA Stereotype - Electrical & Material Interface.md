---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Electrical & Material Interface"
observedEndpointOccurrences: 285
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Electrical & Material Interface

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Electrical & Material Interface`
- **Observed relationship-endpoint occurrences:** 285

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Generalization | [[EA Stereotype - Data Interface]] | 108 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 39 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Mechanical Interface]] | 35 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 20 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 8 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 6 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[README_Object]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Physical System Variant]] | 2 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Association | [[EA Stereotype - System Partner]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Electrical & Material Interface]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Electrical & Material Interface]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[EA Stereotype - Physical Component]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Module]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Realisation | [[EA Element - No Stereotype]] | 1 | 55 | Review | Review: Realisation endpoint pattern |

## Canvas

[[CANVAS_Class - Electrical & Material Interface]]
