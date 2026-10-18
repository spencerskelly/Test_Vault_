---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "Regulatory Requirement"
observedEndpointOccurrences: 221
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — Regulatory Requirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `Regulatory Requirement`
- **Observed relationship-endpoint occurrences:** 221

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Dependency | [[EA Stereotype - Document]] | 173 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 29 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Nesting | [[EA Stereotype - Webasto Requirement]] | 11 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 2 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |

## Canvas

[[CANVAS_Requirement - Regulatory Requirement]]
