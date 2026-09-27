---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "Webasto Requirement"
observedEndpointOccurrences: 16
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — Webasto Requirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `Webasto Requirement`
- **Observed relationship-endpoint occurrences:** 16

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Nesting | [[EA Stereotype - Regulatory Requirement]] | 11 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «trace» | [[EA Stereotype - extendedRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[README_InformationItem]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |

## Canvas

[[CANVAS_Requirement - Webasto Requirement]]
