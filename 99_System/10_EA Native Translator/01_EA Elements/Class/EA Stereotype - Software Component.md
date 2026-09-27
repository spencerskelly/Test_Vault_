---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Software Component"
observedEndpointOccurrences: 992
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Software Component

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Software Component`
- **Observed relationship-endpoint occurrences:** 992

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 277 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 139 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 108 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 58 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Software Component]] | 41 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 33 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 27 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Generalization | [[README_Object]] | 27 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 18 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Association | [[README_UseCase]] | 15 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 14 | 24 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Module Function]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Dependency | [[EA Stereotype - Software Component]] | 10 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 9 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - block]] | 8 | 8 | Review | Review: vague Association |
| Outgoing | NoteLink | [[README_Note]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 6 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 6 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Software Function]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[EA Stereotype - block]] | 4 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - Software Component]] | 4 | 8 | Review | Review: vague Association |
| Incoming | Generalization | [[EA Stereotype - block]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - extendedRequirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Generalization | [[EA Stereotype - Software Unit]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 2 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Association | [[README_UseCase]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency | [[EA Stereotype - block]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | NoteLink | [[README_Note]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - System Partner]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - block]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Physical Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Physical Component + block]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Platform]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Nesting | [[EA Stereotype - block]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Sequence | [[EA Stereotype - block]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Class - Software Component]]
