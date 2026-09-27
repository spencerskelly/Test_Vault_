---
uid:
type: EA Relationship
status: Working
eaConnectorType: "UseCase"
eaConnectorStereotype: "extend"
eaProfile: ""
connectorCount: 736
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA UseCase — extend

## Source identity

- **Connector_Type:** `UseCase`
- **Effective stereotype:** `extend`
- **Profile / FQName:** not specified
- **Observed connectors:** 736

## Inventory coverage

- **Unique endpoint combinations:** 3
- **Matrix Rule IDs:** `30, 60, 71`
- **Disposition distribution:** Settled 733; Exception 1; Review 2
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[README_UseCase]] | [[README_UseCase]] | 733 | 30 | Settled | Map: optionOf / hasOption |
| [[README_Issue]] | [[README_UseCase]] | 2 | 60 | Review | Review: extend endpoint pattern |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |

## Canvas

[[CANVAS_UseCase - extend]]
