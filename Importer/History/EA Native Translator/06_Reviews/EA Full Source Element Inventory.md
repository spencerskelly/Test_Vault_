---
uid:
type: Info
status: Active
workspace: EA Native Translator
artifactRole: Source Evidence Summary
sourceBundle: 99_System/CSV_EA
inventoryDate: 2026-09-27
sourceElementCount: 35969
rawObjectTypes: 31
rawTypeStereotypeCombinations: 72
connectorCount: 21822
---
# EA Full Source Element Inventory

## Purpose

This note summarizes the complete EA element evidence supplied in `99_System/CSV_EA`. It complements the r12 connector-endpoint inventory and closes the earlier gap around isolated/unconnected `t_object` rows.

The raw CSV files remain evidence. This note records what that evidence proves; it does not itself define MDSE semantics.

## Evidence bundle

Source: `EA_2026_09_06_endgame.qeax`

Evidence manifest reports:

- **35,969** `t_object` rows;
- **21,822** `t_connector` rows;
- **1,387** packages;
- **249,892** `t_objectproperties` rows;
- **2,924** diagrams;
- **42,966** diagram-object placements;
- **42,052** `t_xref` rows.

## Full raw EA Object_Type inventory

| EA Object_Type | Source elements |
|---|---:|
| Requirement | 13,988 |
| Port | 4,387 |
| Part | 3,137 |
| InformationItem | 2,825 |
| Class | 2,737 |
| Activity | 1,668 |
| UseCase | 1,667 |
| Package | 1,386 |
| State | 1,112 |
| Signal | 623 |
| Object | 545 |
| Artifact | 459 |
| Note | 431 |
| Action | 323 |
| Issue | 264 |
| StateNode | 73 |
| Change | 65 |
| Text | 61 |
| Actor | 44 |
| Boundary | 44 |
| Decision | 34 |
| ActivityPartition | 28 |
| Trigger | 27 |
| Synchronization | 14 |
| Sequence | 11 |
| ActionPin | 6 |
| ProxyConnector | 5 |
| StateMachine | 2 |
| Constraint | 1 |
| Event | 1 |
| ActivityParameter | 1 |

## Raw Object_Type / Stereotype combinations

The full `t_object` evidence contains **72 raw Object_Type / Stereotype combinations**.

This number must not be directly subtracted from the r12 value of 65 connector-facing combinations. The r12 inventory is based on connector endpoints and effective stereotype/profile interpretation, while this inventory is the raw `t_object.Object_Type + Stereotype` source view.

## Source constructs newly visible outside the connector-facing inventory

The full source inventory reveals source constructs that did not have active source notes from the endpoint-driven pass:

### Additional Object_Types

- `ActionPin` — 6
- `ActivityParameter` — 1
- `ActivityPartition` — 28
- `StateMachine` — 2

### Additional raw stereotypes

- Artifact «CustomDocument» — 1
- Class «Environmental Interface» — 7
- Signal «Environmental Effect» — 8
- Signal «Physical Signal» — 46
- Text «NavigationCell» — 2

These now require explicit import dispositions even though they do not participate in the current connector-facing rule matrix.

## Connectivity observations

The connectivity audit shows **22,059** elements with no direct connector and **18,505** with neither direct connectors nor child-connector evidence. This confirms that connector-endpoint coverage alone was not sufficient for element-source completeness.

Examples:

- 10,110 of 13,988 Requirements have no direct connector.
- 2,868 of 4,387 Ports have no direct connector.
- 3,041 of 3,137 Parts have no direct connector.
- Both StateMachine elements have no direct connector but do own child elements.
- ActivityPartition elements have no direct connector but collectively own 143 child elements.

## Requirement evidence now available

The source contains **13,988 Requirements** and a dedicated requirement connectivity audit.

Observed raw Requirement stereotypes:

| Stereotype | Count |
|---|---:|
| requirement | 7,648 |
| Regulatory Requirement | 3,363 |
| Webasto Requirement | 1,485 |
| designConstraint | 733 |
| functionalRequirement | 514 |
| no stereotype | 170 |
| extendedRequirement | 71 |
| Functional | 2 |
| performanceRequirement | 1 |
| physicalRequirement | 1 |

This is now the appropriate evidence base for Requirement element/property translation decisions.

## Coverage conclusion

We can now claim **full raw EA element inventory coverage for this source extract** at the Object_Type/Stereotype evidence level.

We still cannot claim translation completeness. Every source construct and relevant source property still needs an explicit import disposition and every MDSE output contract must be defined.
