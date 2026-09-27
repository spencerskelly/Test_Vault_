---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Abstraction"
eaConnectorStereotype: "trace"
eaProfile: "EAUML::trace"
connectorCount: 5
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Abstraction — trace

## Source identity

- **Connector_Type:** `Abstraction`
- **Effective stereotype:** `trace`
- **Profile / FQName:** `EAUML::trace`
- **Observed connectors:** 5

## Inventory coverage

- **Unique endpoint combinations:** 3
- **Matrix Rule IDs:** `26, 50`
- **Disposition distribution:** Review 4; Settled 1
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 3 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Element - No Stereotype]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |

## Canvas

[[CANVAS_Abstraction - trace]]
