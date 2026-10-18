---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Dependency"
eaConnectorStereotype: "RecoveryRequirement"
eaProfile: "RAAML::RecoveryRequirement"
connectorCount: 14
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Dependency — RecoveryRequirement

## Source identity

- **Connector_Type:** `Dependency`
- **Effective stereotype:** `RecoveryRequirement`
- **Profile / FQName:** `RAAML::RecoveryRequirement`
- **Observed connectors:** 14

## Inventory coverage

- **Unique endpoint combinations:** 5
- **Matrix Rule IDs:** `68`
- **Disposition distribution:** Review 14
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 4 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |

## Canvas

[[CANVAS_Dependency - RecoveryRequirement]]
