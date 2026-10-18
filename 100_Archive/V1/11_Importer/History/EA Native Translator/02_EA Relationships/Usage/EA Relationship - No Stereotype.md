---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Usage"
eaConnectorStereotype: ""
eaProfile: ""
connectorCount: 235
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Usage — No Stereotype

## Source identity

- **Connector_Type:** `Usage`
- **Effective stereotype:** none
- **Profile / FQName:** not specified
- **Observed connectors:** 235

## Inventory coverage

- **Unique endpoint combinations:** 11
- **Matrix Rule IDs:** `49, 59, 28/29`
- **Disposition distribution:** Review 235
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[README_UseCase]] | [[EA Stereotype - System Function]] | 114 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| [[README_UseCase]] | [[EA Stereotype - System State]] | 54 | 59 | Review | Review: Usage endpoint pattern |
| [[README_UseCase]] | [[EA Element - No Stereotype]] | 32 | 59 | Review | Review: Usage endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 15 | 59 | Review | Review: Usage endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - Module Function]] | 5 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| [[README_UseCase]] | [[EA Element - No Stereotype]] | 4 | 59 | Review | Review: Usage endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - Hardware Function]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| [[README_UseCase]] | [[EA Stereotype - Software Function]] | 3 | 28/29 | Review | Review: choose realizedBy vs dependsOn from relationship meaning |
| [[EA Stereotype - System Function]] | [[README_UseCase]] | 2 | 59 | Review | Review: Usage endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - System State]] | 2 | 49 | Review | Review: Issue→State Usage |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 1 | 59 | Review | Review: Usage endpoint pattern |

## Canvas

[[CANVAS_Usage - No Stereotype]]
