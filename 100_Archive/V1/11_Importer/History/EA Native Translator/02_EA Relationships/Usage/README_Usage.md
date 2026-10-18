---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Usage"
connectorCount: 239
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Usage

## Source identity

- **Connector_Type:** `Usage`
- **Observed connectors:** 239

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[EA Relationship - No Stereotype\|No stereotype]] | 235 | 11 | 49, 59, 28/29 | Review 235 |
| [[EA Relationship Stereotype - Responsibility\|Responsibility]] | 4 | 3 | 70 | Review 4 |

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
| [[EA Stereotype - block]] | [[EA Stereotype - Business Line]] | 2 | 70 | Review | Review: StandardProfile Responsibility |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 1 | 59 | Review | Review: Usage endpoint pattern |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - Business Line]] | 1 | 70 | Review | Review: StandardProfile Responsibility |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical Context]] | 1 | 70 | Review | Review: StandardProfile Responsibility |

## Canvas

[[CANVAS_Usage]]
