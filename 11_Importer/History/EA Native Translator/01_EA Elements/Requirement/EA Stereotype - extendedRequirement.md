---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "extendedRequirement"
observedEndpointOccurrences: 188
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — extendedRequirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `extendedRequirement`
- **Observed relationship-endpoint occurrences:** 188

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 62 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 53 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | NoteLink | [[README_Note]] | 10 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Dependency «trace» | [[EA Stereotype - Document]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 5 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - extendedRequirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency | [[EA Stereotype - extendedRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «refine» | [[README_UseCase]] | 1 | 20 | Settled | Map: describes / describedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Document]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Component]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Webasto Requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 1 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Nesting | [[EA Stereotype - block]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |

## Canvas

[[CANVAS_Requirement - extendedRequirement]]
