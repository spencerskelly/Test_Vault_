---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Dependency"
eaConnectorStereotype: "verify"
eaProfile: "SysML1.4::verify"
connectorCount: 333
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Dependency — verify

## Source identity

- **Connector_Type:** `Dependency`
- **Effective stereotype:** `verify`
- **Profile / FQName:** `SysML1.4::verify`
- **Observed connectors:** 333

## Inventory coverage

- **Unique endpoint combinations:** 8
- **Matrix Rule IDs:** `63, 64`
- **Disposition distribution:** Settled 325; Review 8
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - testCase]] | [[EA Stereotype - requirement]] | 272 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - testCase]] | [[EA Stereotype - designConstraint]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - testCase]] | [[EA Stereotype - functionalRequirement]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - designConstraint]] | 4 | 64 | Review | Review: verify endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - functionalRequirement]] | 2 | 64 | Review | Review: verify endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - Hardware Function]] | 1 | 64 | Review | Review: verify endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - extendedRequirement]] | 1 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - requirement]] | [[EA Element - No Stereotype]] | 1 | 64 | Review | Review: verify endpoint pattern |

## Canvas

[[CANVAS_Dependency - verify]]
