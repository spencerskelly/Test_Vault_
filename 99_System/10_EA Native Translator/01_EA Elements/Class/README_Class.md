---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Class"
observedEndpointOccurrences: 11724
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Class

## Source identity

- **EA Object_Type:** `Class`
- **Observed relationship-endpoint occurrences:** 11724

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Element - No Stereotype\|No stereotype]] | 29 |
| [[EA Stereotype - block\|block]] | 702 |
| [[EA Stereotype - Business Line\|Business Line]] | 349 |
| [[EA Stereotype - Data Interface\|Data Interface]] | 156 |
| [[EA Stereotype - Electrical & Material Interface\|Electrical & Material Interface]] | 285 |
| [[EA Stereotype - Generic Physical Interface\|Generic Physical Interface]] | 37 |
| [[EA Stereotype - Hardware Component\|Hardware Component]] | 4335 |
| [[EA Stereotype - Mechanical Interface\|Mechanical Interface]] | 44 |
| [[EA Stereotype - Module\|Module]] | 1730 |
| [[EA Stereotype - Physical Component\|Physical Component]] | 962 |
| [[EA Stereotype - Physical Component + block\|Physical Component \| block]] | 36 |
| [[EA Stereotype - Physical Context\|Physical Context]] | 299 |
| [[EA Stereotype - Physical System Variant\|Physical System Variant]] | 845 |
| [[EA Stereotype - Platform\|Platform]] | 122 |
| [[EA Stereotype - Software Component\|Software Component]] | 992 |
| [[EA Stereotype - Software Unit\|Software Unit]] | 3 |
| [[EA Stereotype - System Partner\|System Partner]] | 798 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 843 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 787 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 519 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 516 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 468 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 453 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 428 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 369 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - System Partner]] | 330 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 293 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 195 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 190 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 183 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 174 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Association | [[README_UseCase]] | 169 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 155 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 153 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 116 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Dependency «trace» | [[EA Stereotype - Image]] | 103 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Generalization | [[EA Stereotype - System Partner]] | 96 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical System Variant]] | 75 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 66 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 65 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 55 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Association | [[README_UseCase]] | 49 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Software Component]] | 45 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 45 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[README_Object]] | 45 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - block]] | 41 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 35 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Generalization | [[EA Stereotype - Mechanical Interface]] | 35 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 35 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Generalization | [[EA Stereotype - Business Line]] | 32 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 29 | 8 | Review | Review: vague Association |
| Incoming | Generalization | [[EA Stereotype - Software Function]] | 28 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[README_Object]] | 27 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 27 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 27 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Generalization | [[EA Stereotype - Generic Physical Interface]] | 26 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 24 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | NoteLink | [[README_Note]] | 23 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 22 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[README_Object]] | 22 | 4 | Settled | Map: participants on the Context endpoint |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 22 | 8 | Review | Review: vague Association |
| Outgoing | Dependency «trace» | [[README_Text]] | 20 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Platform]] | 19 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - FlowProperty]] | 19 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Physical System Variant]] | 18 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 15 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - block]] | 15 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Physical Component + block]] | 14 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Association | [[EA Stereotype - System State]] | 12 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Software Component]] | 12 | 8 | Review | Review: vague Association |
| Outgoing | Dependency | [[EA Stereotype - Software Component]] | 12 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 11 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 11 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[README_Actor]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| Outgoing | Generalization | [[EA Stereotype - Data Interface]] | 10 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - Business Line]] | 10 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 9 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 9 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Sequence | [[EA Stereotype - block]] | 9 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Sequence | [[README_Object]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_Change]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 7 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 7 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 7 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Sequence | [[EA Stereotype - System Partner]] | 7 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[EA Stereotype - block]] | 6 | 8 | Review | Review: vague Association |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 6 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 6 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - System State]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - designConstraint]] | 6 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - extendedRequirement]] | 6 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Partner]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - designConstraint]] | 5 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Aggregation | [[README_Object]] | 4 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Module]] | 4 | 8 | Review | Review: vague Association |
| Outgoing | Sequence | [[README_Object]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Hardware Component]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[README_Sequence]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Platform]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Aggregation | [[README_Actor]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Aggregation | [[README_InformationItem]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Electrical & Material Interface]] | 3 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[README_Action]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[EA Stereotype - Physical System Variant]] | 3 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - System State]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Realisation | [[EA Stereotype - requirement]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Sequence | [[README_Sequence]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Usage «Responsibility» | [[EA Stereotype - Business Line]] | 3 | 70 | Review | Review: StandardProfile Responsibility |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Physical System Variant]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Association | [[README_Issue]] | 2 | 6 | Settled | Map: affects / affectedBy |
| Incoming | Connector | [[EA Element - No Stereotype]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - block]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - functionalRequirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Module]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Text]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - performanceRequirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Sequence | [[README_Actor]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «trace» | [[EA Element - No Stereotype]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Electrical & Material Interface]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Association | [[EA Stereotype - Document]] | 1 | 7 | Settled | Map: describes / describedBy |
| Outgoing | Association | [[EA Stereotype - Physical Component]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[README_Text]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Mechanical Interface]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[README_Object]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Association | [[README_InformationItem]] | 1 | 7 | Settled | Map: describes / describedBy |
| Incoming | Association | [[README_Note]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System Partner]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[README_Boundary]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[README_Actor]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - Software Component]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - extendedRequirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Realisation | [[EA Element - No Stereotype]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - Hardware Function]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation «deriveReqt» | [[EA Stereotype - designConstraint]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Outgoing | Realisation «refine» | [[EA Stereotype - designConstraint]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Sequence | [[README_Issue]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Software Component]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Usage «Responsibility» | [[EA Stereotype - Physical Context]] | 1 | 70 | Review | Review: StandardProfile Responsibility |
| Incoming | UseCase «include» | [[README_UseCase]] | 1 | 61 | Review | Review: include endpoint pattern |

## Canvas

[[CANVAS_Class]]
