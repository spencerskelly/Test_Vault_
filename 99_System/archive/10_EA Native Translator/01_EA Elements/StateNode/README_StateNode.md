---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "StateNode"
observedEndpointOccurrences: 112
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — StateNode

## Source identity

- **EA Object_Type:** `StateNode`
- **Observed relationship-endpoint occurrences:** 112

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_StateNode\|No stereotype]] | 112 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | StateFlow | [[EA Element - No Stereotype]] | 41 | 47 | Deferred | Deferred: transition evidence |
| Incoming | StateFlow | [[EA Element - No Stereotype]] | 24 | 47 | Deferred | Deferred: transition evidence |
| Incoming | ControlFlow | [[EA Element - No Stereotype]] | 10 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Element - No Stereotype]] | 8 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Issue]] | 5 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Object]] | 5 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Action]] | 4 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Action]] | 3 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Decision]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_Synchronization]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Incoming | ControlFlow | [[README_Synchronization]] | 2 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | StateFlow | [[EA Stereotype - System State]] | 2 | 47 | Deferred | Deferred: transition evidence |
| Outgoing | ControlFlow | [[README_Decision]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[EA Stereotype - System State]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Outgoing | ControlFlow | [[README_UseCase]] | 1 | 44 | Deferred | Deferred: local flow detail |
| Incoming | StateFlow | [[EA Stereotype - System State]] | 1 | 47 | Deferred | Deferred: transition evidence |

## Canvas

[[CANVAS_StateNode]]
