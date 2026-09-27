---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Usage"
eaConnectorStereotype: "Responsibility"
eaProfile: "StandardProfileL2::Responsibility"
connectorCount: 4
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Usage — Responsibility

## Source identity

- **Connector_Type:** `Usage`
- **Effective stereotype:** `Responsibility`
- **Profile / FQName:** `StandardProfileL2::Responsibility`
- **Observed connectors:** 4

## Inventory coverage

- **Unique endpoint combinations:** 3
- **Matrix Rule IDs:** `70`
- **Disposition distribution:** Review 4
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - block]] | [[EA Stereotype - Business Line]] | 2 | 70 | Review | Review: StandardProfile Responsibility |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - Business Line]] | 1 | 70 | Review | Review: StandardProfile Responsibility |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical Context]] | 1 | 70 | Review | Review: StandardProfile Responsibility |

## Canvas

[[CANVAS_Usage - Responsibility]]
