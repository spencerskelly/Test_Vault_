---
uid:
type: Info
status: Working
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# r12 — Body Detail Rules

| Detail Type | Where Written | Source Endpoint | Target Endpoint | Create Connector Note? | Importer Rule | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Connector Name | Body of source note | Write with target identified | No unless separately defined | No | Preserve meaningful non-redundant label as generated relationship detail. | Settled |
| Connector Notes | Body of source note | Write with target identified | No unless separately defined | No | Preserve meaningful notes; do not promote to connector properties. | Settled |
| Source Role | Body of source note | Write with target identified |  | No | Preserve endpoint role without adding connector YAML properties. | Settled |
| Target Role | Body of target note |  | Write with source identified | No | Preserve endpoint role without adding connector YAML properties. | Settled |
| Source Multiplicity | Body of source note | Write with target identified |  | No | Preserve when populated/meaningful. | Settled |
| Target Multiplicity | Body of target note |  | Write with source identified | No | Preserve when populated/meaningful. | Settled |
| Source/Target Constraints | Both endpoint bodies | Write target identified | Write source identified | No | Preserve constraints on both relevant endpoints. | Settled |
| Guard | Body of source note | Write with target identified |  | No | Preserve local transition/control condition. | Settled |
| Trigger / Event | Body of source note | Write with target identified |  | No | Preserve local transition trigger/event detail. | Settled |
| Effect / Action | Body of target note |  | Write with source identified | No | Preserve local transition effect/action detail. | Settled |
| Flow-control construct | Endpoint body detail | Describe control between source and target | Describe when useful | No | Initial/Final/Decision/Merge/Fork/Join/Timer/etc. are inline relationship/behavior detail by default. | Settled |
| Conveyed Item / Item Flow | Source evidence only |  |  | No | Postponed until Item Flow import is defined. | Deferred |
| Participant relationship detail | Owning Use Case/Context body | Use Case/Context owns any generated detail | No duplicate data on participant note | No | `participants` YAML captures membership. Preserve role, multiplicity, constraints, connector name, or notes only on the owning Use Case/Context when meaningful. | Settled |
