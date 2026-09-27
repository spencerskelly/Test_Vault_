---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "<MISSING>"
observedEndpointOccurrences: 18
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — <MISSING>

## Source identity

- **EA Object_Type:** `<MISSING>`
- **Observed relationship-endpoint occurrences:** 18

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_MISSING Endpoint\|<MISSING>]] | 18 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «satisfy» | [[README_MISSING Endpoint]] | 4 | 71 | Exception | Review — endpoint missing from t_object |
| Outgoing | Abstraction «allocate» | [[README_MISSING Endpoint]] | 2 | 71 | Exception | Review — endpoint missing from t_object |
| Outgoing | Connector | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |
| Outgoing | Generalization | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |
| Outgoing | UseCase «extend» | [[README_MISSING Endpoint]] | 1 | 71 | Exception | Review — endpoint missing from t_object |

## Canvas

[[CANVAS_MISSING Endpoint]]
