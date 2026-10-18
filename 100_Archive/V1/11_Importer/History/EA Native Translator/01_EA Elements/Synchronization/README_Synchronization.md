---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Synchronization"
observedEndpointOccurrences: 49
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Synchronization

## Source identity

- **EA Object_Type:** `Synchronization`
- **Observed relationship-endpoint occurrences:** 49

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Synchronization\|No stereotype]] | 49 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Incoming | StateFlow | [[EA Element - No Stereotype]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | StateFlow | [[EA Element - No Stereotype]] | 5 | 47 | Deferred | Deferred: transition evidence |
| Incoming | ControlFlow | [[README_Decision]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Decision]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Object]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_StateNode]] | 2 | 44 | Deferred | Deferred: local flow detail |

## Canvas

[[CANVAS_Synchronization]]
