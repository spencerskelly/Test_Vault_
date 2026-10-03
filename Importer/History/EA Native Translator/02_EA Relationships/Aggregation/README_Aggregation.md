---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Aggregation"
connectorCount: 2288
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Aggregation

## Source identity

- **Connector_Type:** `Aggregation`
- **Observed connectors:** 2288

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[README_Aggregation\|No stereotype]] | 2288 | 92 | 2, 3, 4, 51 | Settled 2158; Review 130 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Module]] | 371 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Hardware Component]] | 350 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - System Partner]] | 279 | 2 | Settled | Map: partOf / hasPart |
| [[README_Object]] | [[README_Object]] | 195 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 74 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Physical Context]] | 69 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - Module]] | [[EA Stereotype - Physical System Variant]] | 54 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Physical Component]] | 54 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Physical System Variant]] | 48 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Module]] | 47 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - System Partner]] | 44 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Hardware Component]] | 43 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Physical Component]] | 41 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Software Component]] | 41 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Hardware Function]] | 38 | 3 | Settled | Map: parent / child |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - System Function]] | 38 | 3 | Settled | Map: parent / child |
| [[EA Stereotype - Module]] | [[EA Stereotype - Module]] | 32 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Module]] | [[EA Stereotype - Physical Context]] | 30 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Software Function]] | 25 | 3 | Settled | Map: parent / child |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical Context]] | 25 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Physical System Variant]] | 23 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Function]] | 22 | 3 | Settled | Map: parent / child |
| [[README_Object]] | [[EA Stereotype - Physical Context]] | 22 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Physical Context]] | 20 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Component]] | 16 | 2 | Settled | Map: partOf / hasPart |
| [[README_Object]] | [[EA Stereotype - Module]] | 15 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical System Variant]] | 14 | 2 | Settled | Map: partOf / hasPart |
| [[README_Change]] | [[README_Change]] | 12 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Physical Context]] | 11 | 4 | Settled | Map: participants on the Context endpoint |
| [[README_Actor]] | [[EA Stereotype - Physical Context]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - Physical Context]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| [[README_UseCase]] | [[README_UseCase]] | 10 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Module]] | [[EA Stereotype - Business Line]] | 9 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Module]] | 9 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Physical System Variant]] | 9 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - block]] | 9 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Hardware Component]] | 8 | 2 | Settled | Map: partOf / hasPart |
| [[README_Object]] | [[EA Stereotype - Physical System Variant]] | 8 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 8 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 6 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Business Line]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - System Partner]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Module]] | [[EA Stereotype - Hardware Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Module]] | [[EA Stereotype - Physical Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - block]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Physical Context]] | 6 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Physical Component]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - Module]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Logical Signal]] | [[EA Stereotype - Logical Signal]] | 6 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Platform]] | 5 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Hardware Function]] | 4 | 3 | Settled | Map: parent / child |
| [[EA Stereotype - Module]] | [[EA Stereotype - Platform]] | 4 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - Software Component]] | 4 | 2 | Settled | Map: partOf / hasPart |
| [[README_Actor]] | [[EA Stereotype - Hardware Component]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Physical Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Business Line]] | 3 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Platform]] | [[EA Stereotype - Physical Context]] | 3 | 4 | Settled | Map: participants on the Context endpoint |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Hardware Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - Physical System Variant]] | 3 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - Physical Component]] | 3 | 2 | Settled | Map: partOf / hasPart |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - System Function]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Software Function]] | 2 | 3 | Settled | Map: parent / child |
| [[EA Stereotype - Electrical & Material Interface]] | [[README_Object]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component + block]] | [[EA Stereotype - Module]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component + block]] | [[EA Stereotype - Physical Component]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Business Line]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[EA Stereotype - Business Line]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Component]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| [[README_Object]] | [[EA Stereotype - Hardware Component]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[README_Object]] | [[EA Stereotype - Platform]] | 2 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - System State]] | [[EA Stereotype - Hardware Function]] | 2 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Element - No Stereotype]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Data Interface]] | [[EA Stereotype - Hardware Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Electrical & Material Interface]] | [[EA Stereotype - Electrical & Material Interface]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Hardware Component]] | [[README_Object]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Platform]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component + block]] | [[EA Stereotype - Business Line]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical Component + block]] | [[EA Stereotype - Physical System Variant]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Module]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Platform]] | [[EA Stereotype - Hardware Component]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Business Line]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Platform]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - System Partner]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[EA Stereotype - block]] | [[README_Object]] | 1 | 2 | Settled | Map: partOf / hasPart |
| [[README_InformationItem]] | [[EA Stereotype - Platform]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Hardware Component]] | 1 | 51 | Review | Review: Aggregation endpoint pattern |

## Canvas

[[CANVAS_Aggregation]]
