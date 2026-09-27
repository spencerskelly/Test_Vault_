---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Boundary"
observedEndpointOccurrences: 2
inventoryBasis: "EA Native Import Relationship Matrix 2026-09-27 r12"
---
# EA Type — Boundary

## Source identity

- **EA Object_Type:** `Boundary`
- **Observed relationship-endpoint occurrences:** 2

## Coverage boundary

This note is grounded in the r12 full-model **relationship endpoint** reconciliation. It proves connector-facing coverage for this source construct; it does not by itself prove that isolated/unconnected t_object rows of other types do not exist.

## Observed connectors and opposite elements

| Direction | EA Connector | Other endpoint | Count | Rule | Status / disposition |
|---|---|---:|---:|---|---|
| Outgoing | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review: Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Module]] | 1 | 50 | Review: Review: trace endpoint pattern |

## Canvas

[[CANVAS_Boundary]]
