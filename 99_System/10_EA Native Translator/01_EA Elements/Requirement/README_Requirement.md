---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Requirement"
observedEndpointOccurrences: 11023
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Requirement

## Source identity

- **EA Object_Type:** `Requirement`
- **Observed relationship-endpoint occurrences:** 11023

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Element - No Stereotype\|No stereotype]] | 465 |
| [[EA Stereotype - designConstraint\|designConstraint]] | 2248 |
| [[EA Stereotype - extendedRequirement\|extendedRequirement]] | 188 |
| [[EA Stereotype - Functional\|Functional]] | 6 |
| [[EA Stereotype - functionalRequirement\|functionalRequirement]] | 1979 |
| [[EA Stereotype - performanceRequirement\|performanceRequirement]] | 6 |
| [[EA Stereotype - physicalRequirement\|physicalRequirement]] | 2 |
| [[EA Stereotype - Regulatory Requirement\|Regulatory Requirement]] | 221 |
| [[EA Stereotype - requirement\|requirement]] | 5892 |
| [[EA Stereotype - Webasto Requirement\|Webasto Requirement]] | 16 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - requirement]] | 1196 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 800 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 713 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 675 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System Function]] | 508 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Dependency «refine» | [[README_UseCase]] | 412 | 20 | Settled | Map: describes / describedBy |
| Incoming | Realisation | [[EA Stereotype - Software Component]] | 335 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «verify» | [[EA Stereotype - testCase]] | 325 | 63 | Settled | Map: verifies / verifiedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 316 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 278 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «satisfy» | [[EA Element - No Stereotype]] | 248 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 236 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Realisation | [[EA Stereotype - Hardware Component]] | 232 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency | [[EA Stereotype - Document]] | 173 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Module]] | 136 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 130 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «deriveReqt» | [[EA Element - No Stereotype]] | 95 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Function]] | 87 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Realisation | [[EA Stereotype - Physical System Variant]] | 86 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Physical Component]] | 85 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | NoteLink | [[README_Note]] | 77 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 39 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Software Function]] | 36 | 15 | Settled | Map: satisfies / satisfiedBy |
| Outgoing | Nesting | [[EA Stereotype - block]] | 34 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Regulatory Requirement]] | 32 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 30 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Module Function]] | 28 | 15 | Settled | Map: satisfies / satisfiedBy |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 26 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - requirement]] | 26 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - designConstraint]] | 26 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency | [[README_InformationItem]] | 25 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - extendedRequirement]] | 25 | 23 | Settled | Map: derivedFrom / derivedBy |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 25 | 22 | Settled | Map: refines / refinedBy |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - functionalRequirement]] | 23 | 23 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «trace» | [[README_Issue]] | 22 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Document]] | 18 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - Document]] | 16 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Usage | [[EA Stereotype - requirement]] | 15 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | Dependency «refine» | [[EA Stereotype - Document]] | 14 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Realisation | [[EA Stereotype - block]] | 13 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - System State]] | 12 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Webasto Requirement]] | 11 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Realisation | [[README_Object]] | 10 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - block]] | 9 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 8 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 8 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «Derive» | [[EA Stereotype - requirement]] | 7 | 66 | Settled | Map: derivedFrom / derivedBy |
| Incoming | Dependency «RecoveryRequirement» | [[EA Stereotype - System State]] | 7 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «trace» | [[EA Stereotype - Document]] | 7 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Function]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Realisation | [[README_Package]] | 7 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[README_Issue]] | 6 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «RecoveryRequirement» | [[EA Element - No Stereotype]] | 6 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «satisfy» | [[README_Action]] | 6 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[README_Object]] | 6 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 5 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Module Function]] | 5 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Data Interface]] | 5 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «ASILDecompose» | [[EA Stereotype - requirement]] | 4 | 69 | Review | Review: RAAML ASILDecompose |
| Outgoing | Dependency «trace» | [[README_Text]] | 4 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - designConstraint]] | 4 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - functionalRequirement]] | 4 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - System Partner]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «Refine» | [[README_UseCase]] | 3 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Abstraction «trace» | [[EA Stereotype - requirement]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency | [[README_Change]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «deriveReqt» | [[EA Stereotype - Document]] | 3 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 3 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 3 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical System Variant]] | 3 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Partner]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Element - No Stereotype]] | 3 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - Physical System Variant]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Hardware Component]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - Business Line]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Document]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_UseCase]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Partner]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Document]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - physicalRequirement]] | 2 | 22 | Settled | Map: refines / refinedBy |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Hardware Component]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical Component]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - extendedRequirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Stereotype - functionalRequirement]] | 2 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Document]] | 2 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[README_InformationItem]] | 2 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Stereotype - Physical Component + block]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - Platform]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Abstraction «Derive» | [[README_Issue]] | 1 | 67 | Review | Review: StandardProfile Derive endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Trigger]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «trace» | [[EA Stereotype - Hardware Component]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | ControlFlow | [[README_Action]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - extendedRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - functionalRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - block]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «RecoveryRequirement» | [[EA Stereotype - System Function]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - System Function]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «deriveReqt» | [[README_InformationItem]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - System State]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Dependency «refine» | [[EA Stereotype - System State]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Document]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - Physical Component]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Business Line]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Software Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Webasto Requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_UseCase]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «verify» | [[EA Element - No Stereotype]] | 1 | 64 | Review | Review: verify endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Hardware Function]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - System Function]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | NoteLink | [[README_Note]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Realisation | [[EA Stereotype - Physical Component]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Physical Component + block]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Realisation | [[README_UseCase]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Realisation «deriveReqt» | [[EA Stereotype - Hardware Component]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Realisation «refine» | [[EA Stereotype - Module]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |

## Canvas

[[CANVAS_Requirement]]
