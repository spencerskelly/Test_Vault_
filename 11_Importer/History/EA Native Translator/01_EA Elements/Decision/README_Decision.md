---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Decision"
observedEndpointOccurrences: 78
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Decision

## Source identity

- **EA Object_Type:** `Decision`
- **Observed relationship-endpoint occurrences:** 78

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Decision\|No stereotype]] | 78 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 21 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 18 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Issue]] | 10 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Action]] | 9 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Synchronization]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Action]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Synchronization]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Object]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_StateNode]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Object]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Decision]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System State]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_StateNode]] | 1 | 44 | Deferred | Deferred: local flow detail |

## Canvas

[[CANVAS_Decision]]
