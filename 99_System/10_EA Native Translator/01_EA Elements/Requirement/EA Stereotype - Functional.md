---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "Functional"
observedEndpointOccurrences: 6
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — Functional

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `Functional`
- **Observed relationship-endpoint occurrences:** 6

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 4 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |

## Canvas

[[CANVAS_Requirement - Functional]]
