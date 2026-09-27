---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Association"
connectorCount: 603
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Association

## Source identity

- **Connector_Type:** `Association`
- **Observed connectors:** 603

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[README_Association\|No stereotype]] | 603 | 55 | 5, 6, 7, 8, 34, 52 | Review 98; Settled 505 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[README_Actor]] | [[README_UseCase]] | 210 | 34 | Settled | Map: participants on the Use Case endpoint |
| [[README_UseCase]] | [[EA Stereotype - Module]] | 61 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[README_Object]] | 39 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - System Partner]] | [[README_UseCase]] | 29 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Hardware Component]] | 25 | 8 | Review | Review: vague Association |
| [[README_UseCase]] | [[EA Stereotype - System Partner]] | 24 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Physical System Variant]] | 20 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_Object]] | [[README_UseCase]] | 17 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Software Component]] | 15 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Hardware Component]] | 14 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Physical Component]] | 13 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - System State]] | [[EA Stereotype - block]] | 12 | 52 | Review | Review: Association endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - Business Line]] | 12 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Physical System Variant]] | [[README_UseCase]] | 11 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - System Partner]] | 8 | 8 | Review | Review: vague Association |
| [[EA Stereotype - block]] | [[EA Stereotype - Software Component]] | 8 | 8 | Review | Review: vague Association |
| [[README_UseCase]] | [[README_UseCase]] | 6 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - System Partner]] | 5 | 8 | Review | Review: vague Association |
| [[EA Stereotype - block]] | [[EA Stereotype - block]] | 5 | 8 | Review | Review: vague Association |
| [[README_UseCase]] | [[README_Actor]] | 5 | 34 | Settled | Map: participants on the Use Case endpoint |
| [[README_UseCase]] | [[EA Stereotype - Physical Context]] | 5 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - System Function]] | [[README_UseCase]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Module]] | [[EA Stereotype - System Partner]] | 4 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Physical Component]] | [[README_UseCase]] | 4 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Software Component]] | 4 | 8 | Review | Review: vague Association |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Hardware Component]] | 3 | 8 | Review | Review: vague Association |
| [[README_UseCase]] | [[EA Stereotype - block]] | 3 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_Actor]] | [[EA Element - No Stereotype]] | 2 | 52 | Review | Review: Association endpoint pattern |
| [[EA Stereotype - Business Line]] | [[README_UseCase]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Physical System Variant]] | 2 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - System Partner]] | 2 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Module]] | [[EA Stereotype - Module]] | 2 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - System Partner]] | 2 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Platform]] | [[EA Stereotype - Module]] | 2 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Software Component]] | [[README_UseCase]] | 2 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Electrical & Material Interface]] | 2 | 8 | Review | Review: vague Association |
| [[README_Actor]] | [[README_Issue]] | 1 | 6 | Settled | Map: affects / affectedBy |
| [[EA Stereotype - Document]] | [[EA Stereotype - Hardware Component]] | 1 | 7 | Settled | Map: describes / describedBy |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Electrical & Material Interface]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Hardware Component]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Physical Component]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Module]] | [[README_Text]] | 1 | 52 | Review | Review: Association endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Mechanical Interface]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Physical Context]] | [[README_UseCase]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - System Partner]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Physical System Variant]] | [[README_Object]] | 1 | 8 | Review | Review: vague Association |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - block]] | 1 | 8 | Review | Review: vague Association |
| [[README_InformationItem]] | [[EA Stereotype - Physical System Variant]] | 1 | 7 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[EA Stereotype - Module]] | 1 | 6 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - Physical System Variant]] | 1 | 6 | Settled | Map: affects / affectedBy |
| [[README_Note]] | [[EA Stereotype - block]] | 1 | 52 | Review | Review: Association endpoint pattern |
| [[README_Object]] | [[README_Object]] | 1 | 8 | Review | Review: vague Association |
| [[README_UseCase]] | [[EA Stereotype - Software Function]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Data Interface]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |
| [[README_UseCase]] | [[EA Stereotype - Platform]] | 1 | 5 | Settled | Map: participants on the Use Case/Context endpoint |

## Canvas

[[CANVAS_Association]]
