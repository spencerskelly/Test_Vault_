---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "UseCase"
observedEndpointOccurrences: 4664
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — UseCase

## Source identity

- **EA Object_Type:** `UseCase`
- **Observed relationship-endpoint occurrences:** 4664

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_UseCase\|No stereotype]] | 4664 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | UseCase «extend» | [[README_UseCase]] | 733 | 30 | Settled | Map: optionOf / hasOption |
| Outgoing | UseCase «include» | [[README_UseCase]] | 521 | 31 | Review | Review: required constituent Use Case decomposition |
| Outgoing | Generalization | [[README_UseCase]] | 384 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | Association | [[README_Actor]] | 210 | 34 | Settled | Map: participants on the Use Case endpoint |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 179 | 20 | Settled | Map: describes / describedBy |
| Incoming | NoteLink | [[README_Note]] | 159 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 155 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Usage | [[EA Stereotype - System Function]] | 114 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 70 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Association | [[EA Stereotype - Module]] | 61 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Usage | [[EA Stereotype - System State]] | 54 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Association | [[README_Object]] | 39 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Usage | [[EA Element - No Stereotype]] | 32 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | Association | [[EA Stereotype - System Partner]] | 29 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 26 | 12 | Settled | Map: affects / affectedBy |
| Outgoing | Association | [[EA Stereotype - System Partner]] | 24 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Physical System Variant]] | 20 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Association | [[README_Object]] | 17 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Software Component]] | 15 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 14 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Physical Component]] | 13 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Business Line]] | 12 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Association | [[EA Stereotype - Physical System Variant]] | 11 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency «trace» | [[README_Issue]] | 11 | 25 | Settled | Map: affects / affectedBy |
| Outgoing | Aggregation | [[README_UseCase]] | 10 | 51 | Review | Review: Aggregation endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Element - No Stereotype]] | 7 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Association | [[README_UseCase]] | 6 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[README_Actor]] | 5 | 34 | Settled | Map: participants on the Use Case endpoint |
| Outgoing | Association | [[EA Stereotype - Physical Context]] | 5 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 5 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Usage | [[EA Stereotype - Module Function]] | 5 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Incoming | Association | [[EA Stereotype - System Function]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Association | [[EA Stereotype - Physical Component]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Usage | [[EA Element - No Stereotype]] | 4 | 59 | Review | Review: Usage endpoint pattern |
| Outgoing | Association | [[EA Stereotype - block]] | 3 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Usage | [[EA Stereotype - Hardware Function]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Usage | [[EA Stereotype - Software Function]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| Outgoing | Abstraction «Refine» | [[EA Stereotype - designConstraint]] | 2 | 20 | Settled | Map: describes / describedBy |
| Incoming | Association | [[EA Stereotype - Business Line]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | Association | [[EA Stereotype - Software Component]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[README_Issue]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Change]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Module Function]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Usage | [[EA Stereotype - System Function]] | 2 | 59 | Review | Review: Usage endpoint pattern |
| Incoming | UseCase «extend» | [[README_Issue]] | 2 | 60 | Review | Review: extend endpoint pattern |
| Outgoing | Abstraction «Refine» | [[EA Stereotype - functionalRequirement]] | 1 | 20 | Settled | Map: describes / describedBy |
| Incoming | Abstraction «allocate» | [[EA Stereotype - Webasto Requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Stereotype - Physical Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Association | [[EA Stereotype - Physical Context]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Software Function]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Data Interface]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Outgoing | Association | [[EA Stereotype - Platform]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_UseCase]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[README_UseCase]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| Outgoing | Dependency «refine» | [[EA Stereotype - extendedRequirement]] | 1 | 20 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | NoteLink | [[README_Constraint]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Realisation | [[EA Stereotype - functionalRequirement]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| Outgoing | UseCase «include» | [[EA Element - No Stereotype]] | 1 | 61 | Review | Review: include endpoint pattern |

## Canvas

[[CANVAS_UseCase]]
