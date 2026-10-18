---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Hardware Component"
observedEndpointOccurrences: 4335
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Hardware Component

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Hardware Component`
- **Observed relationship-endpoint occurrences:** 4335

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 763 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 371 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 350 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 277 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 231 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 158 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 129 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 123 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Image]] | 103 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 93 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 48 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 43 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 41 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 35 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 27 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 25 | 8 | Review | Review: vague Association |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 25 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 22 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 20 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 20 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Element - No Stereotype]] | 16 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 16 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Module]] | 15 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Association | [[README_UseCase]] | 14 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Generalization | [[README_Object]] | 13 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 12 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 11 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Data Interface]] | 9 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Aggregation | [[EA Stereotype - Electrical & Material Interface]] | 8 | 2 | Settled | Map: partOf / hasPart |
| Incoming | NoteLink | [[README_Note]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[README_Object]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - System Partner]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 5 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 5 | 8 | Review | Review: vague Association |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 5 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - System Partner]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Physical System Variant]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Sequence | [[README_Object]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[EA Stereotype - Module]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[README_Actor]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - System Partner]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - System Partner]] | 3 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | NoteLink | [[README_Note]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - requirement]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[README_InformationItem]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Aggregation | [[README_Object]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Dependency | [[README_Action]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - functionalRequirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Module]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - block]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 2 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - extendedRequirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «trace» | [[EA Element - No Stereotype]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Data Interface]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[README_Object]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Platform]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - System State]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Association | [[EA Stereotype - Document]] | 1 | 7 | Settled | Map: describes / describedBy |
| Incoming | Association | [[EA Stereotype - Electrical & Material Interface]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Data Interface]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Data Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System Partner]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - System State]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - Physical System Variant]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - Hardware Function]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Realisation | [[EA Stereotype - performanceRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation «deriveReqt» | [[EA Stereotype - designConstraint]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |

## Canvas

[[CANVAS_Class - Hardware Component]]
