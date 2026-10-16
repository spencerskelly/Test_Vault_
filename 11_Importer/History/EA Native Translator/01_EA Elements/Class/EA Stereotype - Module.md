---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Module"
observedEndpointOccurrences: 1730
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Module

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Module`
- **Observed relationship-endpoint occurrences:** 1730

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 371 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 199 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 150 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 91 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 75 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 68 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Association | [[README_UseCase]] | 61 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 57 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 54 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 47 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 36 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 32 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 30 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 25 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - FlowProperty]] | 19 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Aggregation | [[README_Object]] | 15 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 15 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 12 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency «trace» | [[README_Text]] | 11 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 11 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Sequence | [[EA Stereotype - Hardware Component]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - block]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 6 | 24 | Settled | Map: describes / describedBy |
| Incoming | Generalization | [[EA Stereotype - Physical System Variant]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[EA Stereotype - Business Line]] | 5 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_Change]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 4 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 4 | 8 | Review | Review: vague Association |
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Sequence | [[EA Stereotype - Business Line]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Hardware Component]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - block]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[README_Sequence]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[README_Sequence]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[EA Stereotype - System Partner]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Physical Component + block]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Module]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Association | [[EA Stereotype - Platform]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Connector | [[EA Element - No Stereotype]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Physical Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[README_Object]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[README_Text]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Incoming | Association | [[README_Issue]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Incoming | Dependency | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «trace» | [[README_Boundary]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical System Variant]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - Physical System Variant]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Stereotype - performanceRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation «refine» | [[EA Stereotype - designConstraint]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Sequence | [[EA Stereotype - block]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Class - Module]]
