---
uid:
type: EA Element
status: Working
eaMetaclass: "Class"
eaStereotype: "Physical Component"
observedEndpointOccurrences: 962
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Class — Physical Component

## Source identity

- **EA Object_Type:** `Class`
- **EA stereotype:** `Physical Component`
- **Observed relationship-endpoint occurrences:** 962

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Generalization | [[EA Stereotype - Physical Component]] | 168 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - designConstraint]] | 77 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System State]] | 71 | 14 | Review | Review: State allocation/context evidence |
| Outgoing | Aggregation | [[EA Stereotype - Physical Component]] | 54 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Module]] | 47 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 43 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Hardware Component]] | 41 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Hardware Component]] | 27 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Aggregation | [[EA Stereotype - Physical System Variant]] | 23 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 20 | 14 | Review | Review: State allocation/context evidence |
| Incoming | Generalization | [[EA Stereotype - Hardware Component]] | 16 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Association | [[README_UseCase]] | 13 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 11 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | NoteLink | [[README_Note]] | 9 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Hardware Function]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Aggregation | [[EA Stereotype - Module]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - System Partner]] | 6 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Generalization | [[EA Stereotype - Physical Component + block]] | 6 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Abstraction «allocate» | [[EA Element - No Stereotype]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[README_UseCase]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Generalization | [[EA Stereotype - Module]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - block]] | 4 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Aggregation | [[EA Stereotype - Electrical & Material Interface]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Aggregation | [[EA Stereotype - Business Line]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - block]] | 3 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Dependency | [[EA Stereotype - System State]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Generalization | [[EA Stereotype - Module]] | 3 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | NoteLink | [[README_Note]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Stereotype - System State]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Change]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Aggregation | [[EA Stereotype - Physical Component + block]] | 2 | 2 | Settled | Map: partOf / hasPart |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 2 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Module]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 2 | 24 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[EA Stereotype - block]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Aggregation | [[EA Stereotype - Platform]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Aggregation | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| Incoming | Association | [[EA Stereotype - Electrical & Material Interface]] | 1 | 8 | Review | Review: vague Association |
| Outgoing | Association | [[EA Stereotype - Mechanical Interface]] | 1 | 8 | Review | Review: vague Association |
| Incoming | Dependency | [[README_Action]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Generalization | [[EA Element - No Stereotype]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Electrical & Material Interface]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Generalization | [[EA Stereotype - Software Component]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Generalization | [[README_Object]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Outgoing | Nesting | [[EA Stereotype - Physical System Variant]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| Incoming | Realisation | [[EA Stereotype - designConstraint]] | 1 | 55 | Review | Review: Realisation endpoint pattern |

## Canvas

[[CANVAS_Class - Physical Component]]
