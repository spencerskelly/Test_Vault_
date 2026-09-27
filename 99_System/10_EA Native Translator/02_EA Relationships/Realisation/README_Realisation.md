---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Realisation"
connectorCount: 950
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Realisation

## Source identity

- **Connector_Type:** `Realisation`
- **Observed connectors:** 950

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[EA Relationship - No Stereotype\|No stereotype]] | 948 | 49 | 18, 48, 55 | Settled 920; Review 28 |
| [[EA Relationship Stereotype - deriveReqt\|deriveReqt]] | 1 | 1 | 57 | Review 1 |
| [[EA Relationship Stereotype - refine\|refine]] | 1 | 1 | 65 | Settled 1 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - Software Component]] | [[EA Stereotype - functionalRequirement]] | 277 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - designConstraint]] | 129 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - functionalRequirement]] | 93 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[EA Stereotype - designConstraint]] | 91 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - designConstraint]] | 77 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - designConstraint]] | 51 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[EA Stereotype - functionalRequirement]] | 36 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - requirement]] | 33 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - functionalRequirement]] | 24 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - designConstraint]] | 18 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - block]] | [[EA Stereotype - functionalRequirement]] | 13 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - requirement]] | 10 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[EA Stereotype - requirement]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| [[README_Object]] | [[EA Stereotype - functionalRequirement]] | 8 | 18 | Settled | Map: Requirement appliesTo source element |
| [[README_Package]] | [[EA Stereotype - requirement]] | 6 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Data Interface]] | [[EA Stereotype - requirement]] | 5 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Element - No Stereotype]] | [[README_Change]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Software Parameter]] | 4 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - requirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - requirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - extendedRequirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - functionalRequirement]] | 4 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Hardware Component]] | [[EA Element - No Stereotype]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - functionalRequirement]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - System State]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - Software Component]] | [[EA Element - No Stereotype]] | 3 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Physical System Variant]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Hardware Component]] | 3 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - extendedRequirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component + block]] | [[EA Stereotype - designConstraint]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Platform]] | [[EA Stereotype - functionalRequirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| [[README_Object]] | [[EA Stereotype - requirement]] | 2 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Issue]] | 2 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Electrical & Material Interface]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Object]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Hardware Function]] | 1 | 48 | Review | Review: Activity→Activity Realisation |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - designConstraint]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - functionalRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - requirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Hardware Function]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - performanceRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[EA Stereotype - performanceRequirement]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical Component]] | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical System Variant]] | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[README_Package]] | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Physical Component]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Physical Component + block]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - functionalRequirement]] | 1 | 55 | Review | Review: Realisation endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - designConstraint]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| [[EA Stereotype - Module]] | [[EA Stereotype - designConstraint]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |

## Canvas

[[CANVAS_Realisation]]
