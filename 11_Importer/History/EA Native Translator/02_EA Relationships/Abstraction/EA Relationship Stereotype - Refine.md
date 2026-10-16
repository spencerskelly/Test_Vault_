---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Abstraction"
eaConnectorStereotype: "Refine"
eaProfile: "StandardProfileL2::Refine"
connectorCount: 3
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Abstraction — Refine

## Source identity

- **Connector_Type:** `Abstraction`
- **Effective stereotype:** `Refine`
- **Profile / FQName:** `StandardProfileL2::Refine`
- **Observed connectors:** 3

## Inventory coverage

- **Unique endpoint combinations:** 2
- **Matrix Rule IDs:** `20`
- **Disposition distribution:** Settled 3
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[README_UseCase]] | [[EA Stereotype - designConstraint]] | 2 | 20 | Settled | Map: describes / describedBy |
| [[README_UseCase]] | [[EA Stereotype - functionalRequirement]] | 1 | 20 | Settled | Map: describes / describedBy |

## Canvas

[[CANVAS_Abstraction - Refine]]
