---
uid:
type: Info
status: Active
workspace: EA Native Translator
inventoryDate: 2026-09-27
sourceElementCount: 35969
rawObjectTypes: 31
rawElementTypeStereotypeCombinations: 72
relationshipConnectorCount: 21822
rawRelationshipTypeStereotypePairs: 30
observedEndpointCombinations: 1000
connectorFacingEffectiveElementCombinations: 65
---
# EA Source Inventory Completeness

## Current conclusion

The 2026-09-27 CSV evidence bundle closes the prior isolated-element inventory gap.

We now have:

- **35,969** complete source `t_object` rows;
- **31** raw EA `Object_Type` values;
- **72** raw `Object_Type / Stereotype` combinations;
- **21,822** source connectors;
- **30** raw connector type/effective-stereotype pairs from r12;
- **1,000** observed connector endpoint combinations;
- **65** effective element type/stereotype combinations represented as connector endpoints in r12.

## Important distinction

The **72 raw element combinations** and **65 connector-facing effective combinations** measure different things.

The raw source inventory comes directly from `t_object.Object_Type` and `t_object.Stereotype`.

The r12 endpoint inventory includes only elements participating in connectors and may use effective stereotype/profile interpretation. Therefore these counts must not be compared as though seven combinations are simply missing.

## What is complete

### Source evidence coverage

Complete for the supplied QEA/QEAX extract:

- full element rows;
- full connector rows;
- full object-property rows;
- package structure;
- diagrams and diagram placements;
- xref/profile evidence;
- connector tags;
- element connectivity audit;
- requirement connectivity audit.

### Relationship-source coverage

r12 certifies:

- all 21,822 connectors reconciled;
- 30 raw relationship type/stereotype pairs;
- 1,000 observed endpoint combinations;
- every combination assigned to a Matrix Rule or explicit Review/Deferred/Exception disposition.

## What is not yet complete

Translation is not import-ready merely because source evidence is complete.

Remaining work includes:

- explicit import disposition for every raw EA element construct;
- property/tagged-value disposition;
- complete MDSE element contracts;
- complete MDSE relationship contracts;
- resolution or explicit exclusion/error treatment for Review/Deferred relationship patterns;
- verification fixtures for settled rules.

See [[Translator Definition Tracker]].
