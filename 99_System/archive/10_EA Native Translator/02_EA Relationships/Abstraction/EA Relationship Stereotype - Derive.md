---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Abstraction"
eaConnectorStereotype: "Derive"
eaProfile: "StandardProfileL2::Derive"
connectorCount: 8
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Abstraction — Derive

## Source identity

- **Connector_Type:** `Abstraction`
- **Effective stereotype:** `Derive`
- **Profile / FQName:** `StandardProfileL2::Derive`
- **Observed connectors:** 8

## Inventory coverage

- **Unique endpoint combinations:** 3
- **Matrix Rule IDs:** `66, 67`
- **Disposition distribution:** Review 1; Settled 7
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - requirement]] | 6 | 66 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 1 | 66 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - functionalRequirement]] | [[README_Issue]] | 1 | 67 | Review | Review: StandardProfile Derive endpoint pattern |

## Canvas

[[CANVAS_Abstraction - Derive]]
