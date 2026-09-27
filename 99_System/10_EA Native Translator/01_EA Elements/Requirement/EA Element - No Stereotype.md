---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: ""
observedEndpointOccurrences: 465
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — No Stereotype

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** none
- **Observed relationship-endpoint occurrences:** 465

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 160 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 88 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 55 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 40 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 30 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 11 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 8 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «refine» | [[README_UseCase]] | 7 | 20 | Settled | Map: describes / describedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Module Function]] | 7 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | NoteLink | [[README_Note]] | 7 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Element - No Stereotype]] | 3 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[README_Object]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «trace» | [[EA Stereotype - Hardware Component]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | ControlFlow | [[README_Action]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - System Function]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - System State]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «satisfy» | [[README_Action]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Component]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Physical System Variant]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[README_Package]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |

## Canvas

[[CANVAS_Requirement - No Stereotype]]
