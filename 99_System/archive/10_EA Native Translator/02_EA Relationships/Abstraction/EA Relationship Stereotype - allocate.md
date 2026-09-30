---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Abstraction"
eaConnectorStereotype: "allocate"
eaProfile: "SysML1.4::allocate"
connectorCount: 2795
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Abstraction — allocate

## Source identity

- **Connector_Type:** `Abstraction`
- **Effective stereotype:** `allocate`
- **Profile / FQName:** `SysML1.4::allocate`
- **Observed connectors:** 2795

## Inventory coverage

- **Unique endpoint combinations:** 156
- **Matrix Rule IDs:** `10, 12, 13, 14, 53, 71`
- **Disposition distribution:** Review 1816; Settled 977; Exception 2
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - System State]] | [[EA Stereotype - Hardware Component]] | 277 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Hardware Component]] | 231 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System State]] | [[EA Stereotype - Module]] | 199 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Hardware Component]] | 158 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Software Component]] | 139 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Component]] | 123 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Software Component]] | 108 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical System Variant]] | 102 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Business Line]] | 80 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System State]] | [[EA Stereotype - Business Line]] | 76 | 14 | Review | Review: State allocation/context evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Module]] | 75 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical Component]] | 71 | 14 | Review | Review: State allocation/context evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Module]] | 68 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Physical System Variant]] | 62 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Physical System Variant]] | 61 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Module]] | 57 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Element - No Stereotype]] | [[EA Stereotype - block]] | 54 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Business Line]] | 49 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[README_Issue]] | 42 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Element - No Stereotype]] | 41 | 12 | Settled | Map: affects / affectedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Component]] | 35 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Software Component]] | 27 | 10 | Settled | Map: target Thing performs source Function |
| [[README_Issue]] | [[README_Object]] | 27 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Platform]] | 27 | 14 | Review | Review: State allocation/context evidence |
| [[README_Issue]] | [[EA Stereotype - System Function]] | 26 | 12 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[README_UseCase]] | 26 | 12 | Settled | Map: affects / affectedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Business Line]] | 22 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System Function]] | [[EA Stereotype - block]] | 21 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Physical System Variant]] | 21 | 14 | Review | Review: State allocation/context evidence |
| [[README_Issue]] | [[README_Action]] | 20 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Physical Component]] | 20 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System State]] | [[README_Object]] | 18 | 14 | Review | Review: State allocation/context evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - block]] | 16 | 14 | Review | Review: State allocation/context evidence |
| [[README_InformationItem]] | [[README_Object]] | 14 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - block]] | 14 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Hardware Component]] | 12 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Module]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Software Component]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Physical Component]] | 11 | 10 | Settled | Map: target Thing performs source Function |
| [[README_Issue]] | [[EA Element - No Stereotype]] | 11 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 11 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - System State]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - System Partner]] | 10 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Platform]] | 9 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - requirement]] | [[EA Stereotype - block]] | 9 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - functionalRequirement]] | 8 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - System Partner]] | 8 | 14 | Review | Review: State allocation/context evidence |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Platform]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - requirement]] | 7 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Platform]] | 7 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Physical Component]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Data Interface]] | 6 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Component]] | [[README_Object]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - Hardware Function]] | 6 | 12 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - Hardware Component]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Element - No Stereotype]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Element - No Stereotype]] | 6 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Software Component]] | 6 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System State]] | [[EA Stereotype - Electrical & Material Interface]] | 6 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Data Interface]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Physical System Variant]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - block]] | 5 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Generic Physical Interface]] | [[EA Stereotype - System Partner]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - System State]] | 5 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - testCase]] | 5 | 12 | Settled | Map: affects / affectedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Physical Component]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Software Component]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Partner]] | 4 | 10 | Settled | Map: target Thing performs source Function |
| [[README_Change]] | [[EA Stereotype - Module]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[README_Object]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical Component + block]] | 4 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Text]] | [[EA Element - No Stereotype]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - functionalRequirement]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Business Line]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - block]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Physical System Variant]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - block]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Hardware Component]] | 3 | 10 | Settled | Map: target Thing performs source Function |
| [[README_InformationItem]] | [[EA Element - No Stereotype]] | 3 | 13 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - Module]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Physical System Variant]] | 3 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - Module Function]] | 3 | 12 | Settled | Map: affects / affectedBy |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 2 | 71 | Exception | Review — endpoint missing from t_object |
| [[README_Action]] | [[README_ProxyConnector]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Data Interface]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Partner]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Electrical & Material Interface]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Business Line]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Data Interface]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - Module]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Physical Context]] | 2 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - functionalRequirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[EA Stereotype - Physical Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[README_Action]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Platform]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[README_Actor]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - Module]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - Physical Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[README_ProxyConnector]] | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Document]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Hardware Component]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Software Component]] | 2 | 14 | Review | Review: State allocation/context evidence |
| [[README_Action]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[README_Object]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Module]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Physical System Variant]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - System Partner]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Document]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Electrical & Material Interface]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[EA Stereotype - System Function]] | [[README_Object]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| [[README_Change]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[README_Actor]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Change]] | [[EA Stereotype - functionalRequirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Partner]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - block]] | [[EA Stereotype - Physical Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - block]] | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Module Function]] | 1 | 13 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[README_Actor]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - Software Function]] | 1 | 12 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Issue]] | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Object]] | [[EA Stereotype - Module]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Object]] | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - Webasto Requirement]] | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Physical System Variant]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - System State]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - requirement]] | [[README_UseCase]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Object]] | 1 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System State]] | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Mechanical Interface]] | 1 | 14 | Review | Review: State allocation/context evidence |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Text]] | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Text]] | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_Trigger]] | [[EA Stereotype - requirement]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - System Function]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - Physical Component]] | 1 | 53 | Review | Review: allocate endpoint pattern |

## Canvas

[[CANVAS_Abstraction - allocate]]
