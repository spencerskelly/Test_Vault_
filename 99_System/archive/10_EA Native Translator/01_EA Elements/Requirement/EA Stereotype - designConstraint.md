---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "designConstraint"
observedEndpointOccurrences: 2248
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — designConstraint

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `designConstraint`
- **Observed relationship-endpoint occurrences:** 2248

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 542 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 340 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 228 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 129 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Module]] | 91 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 77 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «refine» | [[README_UseCase]] | 70 | 20 | Settled | Map: describes / describedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 60 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Realisation | [[EA Stereotype - Physical System Variant]] | 51 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 40 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Regulatory Requirement]] | 29 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 27 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Nesting | [[EA Stereotype - designConstraint]] | 25 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - extendedRequirement]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 20 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 18 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | NoteLink | [[README_Note]] | 17 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 13 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 6 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «trace» | [[README_Issue]] | 6 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Nesting | [[EA Stereotype - block]] | 6 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency | [[README_Issue]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 5 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «RecoveryRequirement» | [[EA Stereotype - System State]] | 4 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 4 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «verify» | [[EA Stereotype - requirement]] | 4 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «RecoveryRequirement» | [[EA Element - No Stereotype]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Document]] | 3 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «refine» | [[EA Stereotype - requirement]] | 3 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Realisation | [[EA Stereotype - Physical System Variant]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Abstraction «Refine» | [[README_UseCase]] | 2 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Dependency | [[EA Stereotype - Document]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - functionalRequirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «refine» | [[EA Stereotype - Document]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - physicalRequirement]] | 2 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Software Function]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Partner]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Physical Component + block]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «Derive» | [[EA Stereotype - requirement]] | 1 | 66 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[README_InformationItem]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 1 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Software Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - functionalRequirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - functionalRequirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | NoteLink | [[README_Note]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Realisation | [[EA Stereotype - Business Line]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - Physical Component]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Physical Component + block]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Realisation «deriveReqt» | [[EA Stereotype - Hardware Component]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Realisation «refine» | [[EA Stereotype - Module]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |

## Canvas

[[CANVAS_Requirement - designConstraint]]
