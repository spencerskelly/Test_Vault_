---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Event"
observedEndpointOccurrences: 2
inventoryBasis: "EA Native Import Relationship Matrix 2026-09-27 r12"
---
# EA Type — Event

## Source identity

- **EA Object_Type:** `Event`
- **Observed relationship-endpoint occurrences:** 2

## Coverage boundary

This note is grounded in the r12 full-model **relationship endpoint** reconciliation. It proves connector-facing coverage for this source construct; it does not by itself prove that isolated/unconnected t_object rows of other types do not exist.

## Observed connectors and opposite elements

| Direction | EA Connector | Other endpoint | Count | Rule | Status / disposition |
|---|---|---:|---:|---|---|
| Outgoing | StateFlow | [[EA Stereotype - System State]] | 1 | 47 | Deferred: Deferred: transition evidence |
| Incoming | StateFlow | [[EA Stereotype - System State]] | 1 | 47 | Deferred: Deferred: transition evidence |

## Canvas

[[CANVAS_Event]]
