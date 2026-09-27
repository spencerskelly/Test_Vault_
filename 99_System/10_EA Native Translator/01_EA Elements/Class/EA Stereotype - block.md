---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "block"
observedEndpointOccurrences: 702
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — block

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `block`
- **Observed relationship-endpoint occurrences:** 702

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Aggregation | [[EA Stereotype - System Partner]] | 279 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 54 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - block]] | 36 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Software Function]] | 28 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 27 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 21 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 16 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 14 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 13 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Association | [[EA Stereotype - System State]] | 12 | 52 | Review | Review: Association endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 9 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - block]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Software Component]] | 8 | 8 | Review | Review: vague Association |
| Outgoing | NoteLink | [[README_Note]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Dependency «trace» | [[README_Text]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Physical System Variant]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Nesting | [[EA Stereotype - designConstraint]] | 6 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Association | [[EA Stereotype - block]] | 5 | 8 | Review | Review: vague Association |
| Incoming | Generalization | [[EA Stereotype - System State]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Software Component]] | 4 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical System Variant]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 4 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Sequence | [[EA Stereotype - Module]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - block]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[README_UseCase]] | 3 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Dependency | [[EA Stereotype - Software Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - block]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - System Function]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[README_Object]] | 2 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Usage «Responsibility» | [[EA Stereotype - Business Line]] | 2 | 70 | Review | Review: StandardProfile Responsibility |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[README_Object]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - Software Component]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Association | [[README_Note]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Business Line]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical Context]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - System Partner]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - Software Component]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Nesting | [[EA Stereotype - extendedRequirement]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Sequence | [[EA Stereotype - Physical System Variant]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Module]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[EA Stereotype - Software Component]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Class - block]]
