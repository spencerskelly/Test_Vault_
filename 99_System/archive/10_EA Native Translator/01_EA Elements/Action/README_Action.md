---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Action"
observedEndpointOccurrences: 286
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Action

## Source identity

- **EA Object_Type:** `Action`
- **Observed relationship-endpoint occurrences:** 286

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Action\|No stereotype]] | 286 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | ControlFlow | [[README_Action]] | 104 | 44 | Deferred | Deferred: local flow detail |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 20 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | ControlFlow | [[README_Decision]] | 9 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Object]] | 6 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 5 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Object]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Decision]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_StateNode]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[README_ProxyConnector]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Stereotype - System State]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - System State]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Issue]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |

## Canvas

[[CANVAS_Action]]
