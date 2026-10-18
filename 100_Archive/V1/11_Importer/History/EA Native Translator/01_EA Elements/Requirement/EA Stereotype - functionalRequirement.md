---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "functionalRequirement"
observedEndpointOccurrences: 1979
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — functionalRequirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `functionalRequirement`
- **Observed relationship-endpoint occurrences:** 1979

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 560 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 277 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 224 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 196 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «refine» | [[README_UseCase]] | 179 | 20 | Settled | Map: describes / describedBy |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 93 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 55 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Realisation | [[EA Stereotype - Module]] | 36 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 31 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| Incoming | Realisation | [[EA Stereotype - Physical System Variant]] | 24 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «refine» | [[EA Stereotype - requirement]] | 18 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «trace» | [[README_Issue]] | 16 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 15 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 13 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Realisation | [[EA Stereotype - block]] | 13 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Software Function]] | 12 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 9 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 9 | 24 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 8 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Module Function]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Realisation | [[README_Object]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «Derive» | [[EA Stereotype - requirement]] | 6 | 66 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 6 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 6 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 5 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «ASILDecompose» | [[EA Stereotype - requirement]] | 4 | 69 | Review | Review: RAAML ASILDecompose |
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - System Partner]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - extendedRequirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 3 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Nesting | [[EA Stereotype - functionalRequirement]] | 3 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | NoteLink | [[README_Note]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «verify» | [[EA Stereotype - requirement]] | 2 | 64 | Review | Review: verify endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Platform]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «Derive» | [[README_Issue]] | 1 | 67 | Review | Review: StandardProfile Derive endpoint pattern |
| Incoming | Abstraction «Refine» | [[README_UseCase]] | 1 | 20 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - functionalRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Regulatory Requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «refine» | [[EA Stereotype - Document]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «refine» | [[EA Stereotype - designConstraint]] | 1 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Partner]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - designConstraint]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - designConstraint]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Business Line]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[README_UseCase]] | 1 | 55 | Review | Review: Realisation endpoint pattern |

## Canvas

[[CANVAS_Requirement - functionalRequirement]]
