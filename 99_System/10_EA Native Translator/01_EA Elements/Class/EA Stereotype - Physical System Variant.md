---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Physical System Variant"
observedEndpointOccurrences: 845
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Physical System Variant

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Physical System Variant`
- **Observed relationship-endpoint occurrences:** 845

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 102 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Generalization | [[EA Stereotype - Physical System Variant]] | 70 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 62 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 61 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 54 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 51 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 48 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 25 | 4 | Settled | Map: participants on the Context endpoint |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 24 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Physical Component]] | 23 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Business Line]] | 23 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 21 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Association | [[README_UseCase]] | 20 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 14 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[README_UseCase]] | 11 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Generalization | [[EA Stereotype - Platform]] | 10 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 10 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[README_Object]] | 8 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Sequence | [[EA Stereotype - Platform]] | 8 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 7 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Aggregation | [[EA Stereotype - block]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 6 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Dependency «trace» | [[README_Issue]] | 4 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Sequence | [[EA Stereotype - Business Line]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - System Partner]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Realisation | [[EA Stereotype - designConstraint]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | Sequence | [[EA Stereotype - Business Line]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Physical System Variant]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Platform]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[EA Stereotype - System Partner]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - Electrical & Material Interface]] | 2 | 8 | Review | Review: vague Association |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Sequence | [[EA Stereotype - System Partner]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Business Line]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Physical Component + block]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[README_Object]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Association | [[README_InformationItem]] | 1 | 7 | Settled | Map: describes / describedBy |
| Incoming | Association | [[README_Issue]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Hardware Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Module]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - Hardware Component]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - Module]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - Physical Component]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Sequence | [[EA Stereotype - block]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Usage «Responsibility» | [[EA Stereotype - Physical Context]] | 1 | 70 | Review | Review: StandardProfile Responsibility |

## Canvas

[[CANVAS_Class - Physical System Variant]]
