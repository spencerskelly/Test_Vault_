---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "performanceRequirement"
observedEndpointOccurrences: 6
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — performanceRequirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `performanceRequirement`
- **Observed relationship-endpoint occurrences:** 6

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Module]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |

## Canvas

[[CANVAS_Requirement - performanceRequirement]]
