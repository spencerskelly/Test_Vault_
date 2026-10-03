---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Connector"
connectorCount: 823
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Connector

## Source identity

- **Connector_Type:** `Connector`
- **Observed connectors:** 823

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[EA Relationship - No Stereotype\|No stereotype]] | 574 | 15 | 41, 71 | Settled 573; Exception 1 |
| [[EA Relationship Stereotype - BindingConnector\|BindingConnector]] | 249 | 5 | 40 | Settled 249 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 406 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 197 | 40 | Settled | Map: equals / equals |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 87 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Stereotype - ProxyPort]] | [[EA Stereotype - ProxyPort]] | 48 | 40 | Settled | Map: equals / equals |
| [[EA Element - No Stereotype]] | [[EA Stereotype - ProxyPort]] | 27 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Stereotype - ProxyPort]] | [[EA Element - No Stereotype]] | 23 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Stereotype - ProxyPort]] | [[EA Stereotype - ProxyPort]] | 7 | 41 | Settled | Map: interfaces / interfaces |
| [[README_Object]] | [[README_Object]] | 6 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Stereotype - FullPort]] | 6 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Module]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[README_InformationItem]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Stereotype - FullPort]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Stereotype - FullPort]] | [[EA Element - No Stereotype]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Stereotype - FullPort]] | 2 | 40 | Settled | Map: equals / equals |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Stereotype - ProxyPort]] | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| [[EA Element - No Stereotype]] | [[EA Stereotype - ProxyPort]] | 1 | 40 | Settled | Map: equals / equals |
| [[EA Stereotype - ProxyPort]] | [[EA Element - No Stereotype]] | 1 | 40 | Settled | Map: equals / equals |

## Canvas

[[CANVAS_Connector]]
