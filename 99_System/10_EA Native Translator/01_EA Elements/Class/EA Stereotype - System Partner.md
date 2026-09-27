---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "System Partner"
observedEndpointOccurrences: 798
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — System Partner

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `System Partner`
- **Observed relationship-endpoint occurrences:** 798

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Aggregation | [[EA Stereotype - block]] | 279 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - System Partner]] | 90 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 69 | 4 | Settled | Map: participants on the Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - System Partner]] | 44 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[README_UseCase]] | 29 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Association | [[README_UseCase]] | 24 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 8 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 8 | 8 | Review | Review: vague Association |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Generic Physical Interface]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Association | [[EA Stereotype - Hardware Component]] | 5 | 8 | Review | Review: vague Association |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Association | [[EA Stereotype - Module]] | 4 | 8 | Review | Review: vague Association |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 3 | 8 | Review | Review: vague Association |
| Incoming | Sequence | [[EA Stereotype - Platform]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Physical System Variant]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Association | [[EA Stereotype - Electrical & Material Interface]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Association | [[EA Stereotype - Physical Component]] | 2 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[EA Stereotype - Electrical & Material Interface]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Sequence | [[README_Actor]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[EA Stereotype - Physical System Variant]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - System Partner]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Software Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - Physical System Variant]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Dependency | [[EA Stereotype - System Partner]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[README_Issue]] | 1 | 25 | Settled | Map: affects / affectedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[README_Actor]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Sequence | [[README_Issue]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Class - System Partner]]
