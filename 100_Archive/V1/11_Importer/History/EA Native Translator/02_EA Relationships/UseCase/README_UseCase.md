---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "UseCase"
connectorCount: 1258
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — UseCase

## Source identity

- **Connector_Type:** `UseCase`
- **Observed connectors:** 1258

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[EA Relationship Stereotype - extend\|extend]] | 736 | 3 | 30, 60, 71 | Settled 733; Exception 1; Review 2 |
| [[EA Relationship Stereotype - include\|include]] | 522 | 2 | 31, 61 | Review 522 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[README_UseCase]] | [[README_UseCase]] | 733 | 30 | Settled | Map: optionOf / hasOption |
| [[README_UseCase]] | [[README_UseCase]] | 521 | 31 | Review | Review: required constituent Use Case decomposition |
| [[README_Issue]] | [[README_UseCase]] | 2 | 60 | Review | Review: extend endpoint pattern |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |
| [[README_UseCase]] | [[EA Element - No Stereotype]] | 1 | 61 | Review | Review: include endpoint pattern |

## Canvas

[[CANVAS_UseCase]]
