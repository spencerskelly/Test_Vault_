---
uid:
type: Info
status: Working
workspace: EA Native Translator
inventoryDate: 2026-09-27
relationshipConnectorCount: 21822
rawRelationshipTypeStereotypePairs: 30
observedEndpointCombinations: 1000
observedElementTypeStereotypeEndpointCombinations: 65
---
# EA Source Inventory Completeness

## Relationship-source coverage

The r12 workbook certifies the native relationship source inventory against `t_connector/t_object/t_xref`:

- 21,822 connectors;
- 30 raw Connector_Type / effective-stereotype pairs;
- 1,000 observed endpoint combinations;
- every observed combination resolves to a matrix rule or explicit Review/Deferred/Exception disposition;
- 0 unrecognized raw relationship type/stereotype pairs.

## Element coverage

The same reconciliation exposes 65 distinct EA Object_Type / stereotype combinations **that participate in at least one connector**. All of those combinations now have navigable notes and canvases under [[README_EA Elements]].

This is not a separate full `t_object` inventory of isolated/unconnected elements. Therefore the vault now has complete **connector-facing element-type coverage**, but we should not claim complete isolated-element type coverage until a full source-element inventory is supplied or generated.

## Navigation rule

- one folder per EA Object_Type;
- stereotype notes and canvases live under that type;
- one folder per raw Connector_Type;
- effective connector stereotype notes and canvases live under that connector type;
- canvases are generated from the 1,000 observed endpoint combinations and show connector direction, opposite endpoint type/stereotype, observed count, Matrix Rule ID, coverage state, and import disposition.
