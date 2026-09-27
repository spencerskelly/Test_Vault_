---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "extend"
sourcePattern: "Use Case → Use Case"
targetMapping: "optionOf / hasOption"
disposition: "Direct"
---
# extend - Use Case to Use Case

## Rule

Source is optional/conditional behavior relative to the base Use Case.

## Source

- EA relationship: [[EA Relationship - extend]]
- Endpoint pattern: `Use Case → Use Case`

## Target

`optionOf / hasOption`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
