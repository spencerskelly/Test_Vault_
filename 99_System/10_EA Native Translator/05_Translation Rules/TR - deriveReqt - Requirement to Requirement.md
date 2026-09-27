---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "deriveReqt"
sourcePattern: "Requirement → Requirement"
targetMapping: "derivedFrom"
disposition: "Direct"
---
# deriveReqt - Requirement to Requirement

## Rule

Source Requirement is derivedFrom destination Requirement.

## Source

- EA relationship: [[EA Relationship - deriveReqt]]
- Endpoint pattern: `Requirement → Requirement`

## Target

`derivedFrom`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
