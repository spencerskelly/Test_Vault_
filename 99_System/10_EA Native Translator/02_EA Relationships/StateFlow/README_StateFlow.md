---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "StateFlow"
connectorCount: 200
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — StateFlow

## Source identity

- **Connector_Type:** `StateFlow`
- **Observed connectors:** 200

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[README_StateFlow\|No stereotype]] | 200 | 12 | 47 | Deferred 200 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 110 | 47 | Deferred | Deferred: transition evidence |
| [[README_StateNode]] | [[EA Element - No Stereotype]] | 41 | 47 | Deferred | Deferred: transition evidence |
| [[EA Element - No Stereotype]] | [[README_StateNode]] | 24 | 47 | Deferred | Deferred: transition evidence |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 7 | 47 | Deferred | Deferred: transition evidence |
| [[EA Element - No Stereotype]] | [[README_Synchronization]] | 5 | 47 | Deferred | Deferred: transition evidence |
| [[README_Synchronization]] | [[EA Element - No Stereotype]] | 5 | 47 | Deferred | Deferred: transition evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Fault State]] | 2 | 47 | Deferred | Deferred: transition evidence |
| [[README_StateNode]] | [[EA Stereotype - System State]] | 2 | 47 | Deferred | Deferred: transition evidence |
| [[README_Event]] | [[EA Stereotype - System State]] | 1 | 47 | Deferred | Deferred: transition evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 1 | 47 | Deferred | Deferred: transition evidence |
| [[EA Stereotype - System State]] | [[README_Event]] | 1 | 47 | Deferred | Deferred: transition evidence |
| [[EA Stereotype - System State]] | [[README_StateNode]] | 1 | 47 | Deferred | Deferred: transition evidence |

## Canvas

[[CANVAS_StateFlow]]
