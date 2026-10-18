---
uid:
type: EA Element
status: Working
eaMetaclass: "Requirement"
eaStereotype: "requirement"
observedEndpointOccurrences: 5892
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Requirement — requirement

## Source identity

- **EA Object_Type:** `Requirement`
- **EA stereotype:** `requirement`
- **Observed relationship-endpoint occurrences:** 5892

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 605 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 560 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 542 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 364 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 336 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 295 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 272 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 236 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 185 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 176 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «refine» | [[README_UseCase]] | 155 | 20 | Settled | Map: describes / describedBy |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 121 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 78 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Nesting | [[EA Stereotype - extendedRequirement]] | 62 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 49 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | NoteLink | [[README_Note]] | 40 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 33 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «refine» | [[EA Stereotype - designConstraint]] | 27 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Nesting | [[EA Stereotype - block]] | 27 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Generalization | [[EA Stereotype - requirement]] | 26 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Dependency | [[README_InformationItem]] | 25 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Software Function]] | 22 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 21 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 18 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Nesting | [[EA Stereotype - Document]] | 16 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 15 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Usage | [[EA Stereotype - requirement]] | 15 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Module Function]] | 13 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «refine» | [[EA Stereotype - Document]] | 11 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Document]] | 10 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Physical System Variant]] | 10 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 9 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Module]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 7 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Document]] | 7 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Abstraction «Derive» | [[EA Stereotype - functionalRequirement]] | 6 | 66 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 6 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[README_Package]] | 6 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - extendedRequirement]] | 5 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[README_Action]] | 5 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Module Function]] | 5 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Data Interface]] | 5 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «ASILDecompose» | [[EA Stereotype - functionalRequirement]] | 4 | 69 | Review | Review: RAAML ASILDecompose |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - Functional]] | 4 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «trace» | [[README_Object]] | 4 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[README_Text]] | 4 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - designConstraint]] | 4 | 64 | Review | Review: verify endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - designConstraint]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - functionalRequirement]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «trace» | [[EA Stereotype - requirement]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency | [[README_Change]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «RecoveryRequirement» | [[EA Element - No Stereotype]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «RecoveryRequirement» | [[EA Stereotype - System State]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - performanceRequirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 3 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Hardware Component]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Document]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Partner]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Regulatory Requirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - extendedRequirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical Component]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - extendedRequirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - functionalRequirement]] | 2 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Document]] | 2 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[README_Object]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Abstraction «Derive» | [[EA Stereotype - designConstraint]] | 1 | 66 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Trigger]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - block]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «RecoveryRequirement» | [[EA Stereotype - System Function]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - Regulatory Requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - System State]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Physical Component]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - designConstraint]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Business Line]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - Regulatory Requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_UseCase]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Element - No Stereotype]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Incoming | Nesting | [[README_InformationItem]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - Hardware Function]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - System Function]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Business Line]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |

## Canvas

[[CANVAS_Requirement - requirement]]
