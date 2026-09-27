---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Action"
observedEndpointOccurrences: 286
inventoryBasis: "EA Native Import Relationship Matrix 2026-09-27 r12"
---
# EA Type — Action

## Source identity

- **EA Object_Type:** `Action`
- **Observed relationship-endpoint occurrences:** 286

## Coverage boundary

This note is grounded in the r12 full-model **relationship endpoint** reconciliation. It proves connector-facing coverage for this source construct; it does not by itself prove that isolated/unconnected t_object rows of other types do not exist.

## Observed connectors and opposite elements

| Direction | EA Connector | Other endpoint | Count | Rule | Status / disposition |
|---|---|---:|---:|---|---|
| Outgoing | ControlFlow | [[README_Action]] | 104 | 44 | Deferred: Deferred: local flow detail |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 20 | 53 | Review: Review: allocate endpoint pattern |
| Incoming | ControlFlow | [[README_Decision]] | 9 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Object]] | 6 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - requirement]] | 5 | 54 | Review: Review: satisfy endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 4 | 44 | Deferred: Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Object]] | 4 | 44 | Deferred: Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 4 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Decision]] | 3 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_StateNode]] | 3 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | Abstraction «allocate» | [[README_ProxyConnector]] | 2 | 53 | Review: Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 2 | 53 | Review: Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Stereotype - System State]] | 2 | 44 | Deferred: Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 2 | 44 | Deferred: Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Stereotype - System State]] | 2 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review: Review: Dependency endpoint pattern |
| Incoming | Dependency «refine» | [[README_InformationItem]] | 2 | 65 | Settled: Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 1 | 53 | Review: Review: allocate endpoint pattern |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 1 | 44 | Deferred: Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Issue]] | 1 | 44 | Deferred: Deferred: local flow detail |
| Outgoing | Dependency | [[EA Stereotype - Physical Component]] | 1 | 58 | Review: Review: Dependency endpoint pattern |
| Outgoing | Dependency «satisfy» | [[EA Element - No Stereotype]] | 1 | 54 | Review: Review: satisfy endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Image]] | 1 | 50 | Review: Review: trace endpoint pattern |

## Canvas

[[CANVAS_Action]]
