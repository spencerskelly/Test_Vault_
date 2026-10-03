---
uid:
type: Info
status: Active
workspace: EA Native Translator
---
# EA Elements

This area is organized by exact EA `Object_Type`. Raw stereotype variants live beneath their source type.

## Coverage

The comprehensive EA evidence bundle now supplies a complete raw `t_object` inventory:

- 35,969 source elements;
- 31 raw Object_Types;
- 72 raw Object_Type/Stereotype combinations.

The r12 relationship workbook separately supplies connector-facing effective element combinations and relationship rules.

See [[EA Full Source Element Inventory]].

## Full source types

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

## Special source-integrity view

`MISSING Endpoint` is not an EA Object_Type. It remains a translator/source-integrity construct for connector endpoints that do not resolve to a source object.

## Rule

A source construct appearing in this inventory does not automatically define its MDSE target. Each construct requires an explicit import disposition.
