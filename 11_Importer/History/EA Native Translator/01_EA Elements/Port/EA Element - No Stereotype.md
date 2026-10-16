---
uid:
type: EA Element
status: Working
eaMetaclass: "Port"
eaStereotype: ""
observedEndpointOccurrences: 1513
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Port — No Stereotype

## Source identity

- **EA Object_Type:** `Port`
- **EA stereotype:** none
- **Observed relationship-endpoint occurrences:** 1513

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Connector | [[EA Element - No Stereotype]] | 406 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector «BindingConnector» | [[EA Element - No Stereotype]] | 197 | 40 | Settled | Map: equals / equals |
| Outgoing | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 110 | 42 | Deferred | Deferred: Item Flow import postponed |
| Outgoing | Connector | [[EA Stereotype - ProxyPort]] | 27 | 41 | Settled | Map: interfaces / interfaces |
| Incoming | Connector | [[EA Stereotype - ProxyPort]] | 23 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Dependency | [[EA Stereotype - designConstraint]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 5 | 42 | Deferred | Deferred: Item Flow import postponed |
| Incoming | Abstraction «allocate» | [[README_Text]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | InformationFlow «itemFlow» | [[EA Element - No Stereotype]] | 4 | 42 | Deferred | Deferred: Item Flow import postponed |
| Outgoing | Connector | [[EA Stereotype - Module]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[README_InformationItem]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[EA Stereotype - FullPort]] | 2 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector «BindingConnector» | [[EA Stereotype - FullPort]] | 2 | 40 | Settled | Map: equals / equals |
| Outgoing | InformationFlow «itemFlow» | [[EA Stereotype - ProxyPort]] | 2 | 42 | Deferred | Deferred: Item Flow import postponed |
| Incoming | InformationFlow «itemFlow» | [[EA Stereotype - ProxyPort]] | 2 | 42 | Deferred | Deferred: Item Flow import postponed |
| Incoming | Abstraction «allocate» | [[README_Action]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Connector | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector | [[EA Element - No Stereotype]] | 1 | 41 | Settled | Map: interfaces / interfaces |
| Outgoing | Connector «BindingConnector» | [[EA Stereotype - ProxyPort]] | 1 | 40 | Settled | Map: equals / equals |
| Incoming | Connector «BindingConnector» | [[EA Stereotype - ProxyPort]] | 1 | 40 | Settled | Map: equals / equals |
| Outgoing | Dependency | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |

## Canvas

[[CANVAS_Port - No Stereotype]]
