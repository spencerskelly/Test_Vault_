---
uid:
type: EA Element
status: Working
eaMetaclass: "Port"
eaStereotype: "ProxyPort"
observedEndpointOccurrences: 167
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Port — ProxyPort

## Source identity

- **EA Object_Type:** `Port`
- **EA stereotype:** `ProxyPort`
- **Observed relationship-endpoint occurrences:** 167

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Connector «BindingConnector» | [[EA Stereotype - ProxyPort]] | 48 | 40 | Settled | Map: equals / equals |
| Incoming | Connector | [[EA Element - No Stereotype]] | 27 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[EA Element - No Stereotype]] | 23 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[EA Stereotype - ProxyPort]] | 7 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 2 | 42 | Deferred | Deferred: Item Flow import postponed |
| Outgoing | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 2 | 42 | Deferred | Deferred: Item Flow import postponed |
| Outgoing | Connector | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Connector «BindingConnector» | [[EA Element - No Stereotype]] | 1 | 40 | Settled | Map: equals / equals |
| Outgoing | Connector «BindingConnector» | [[EA Element - No Stereotype]] | 1 | 40 | Settled | Map: equals / equals |

## Canvas

[[CANVAS_Port - ProxyPort]]
