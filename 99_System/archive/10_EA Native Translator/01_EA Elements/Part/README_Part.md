---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Part"
observedEndpointOccurrences: 213
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Part

## Source identity

- **EA Object_Type:** `Part`
- **Observed relationship-endpoint occurrences:** 213

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Element - No Stereotype\|No stereotype]] | 194 |
| [[EA Stereotype - FlowProperty\|FlowProperty]] | 19 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Connector | [[EA Element - No Stereotype]] | 87 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Sequence | [[EA Stereotype - Module]] | 19 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Connector | [[EA Stereotype - FullPort]] | 6 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 5 | 42 | Deferred | Deferred: Item Flow import postponed |
| Incoming | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 4 | 42 | Deferred | Deferred: Item Flow import postponed |
| Incoming | Connector | [[EA Stereotype - FullPort]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Connector | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Connector | [[EA Stereotype - ProxyPort]] | 1 | 41 | Settled | Map: interfaces / interfaces |

## Canvas

[[CANVAS_Part]]
