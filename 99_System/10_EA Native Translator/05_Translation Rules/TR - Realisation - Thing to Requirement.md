---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Realisation"
sourcePattern: "Thing / Document / Firmware → Requirement"
targetMapping: "Requirement appliesTo source element"
disposition: "Direct"
---
# Realisation - Thing to Requirement

## Rule

Normalize to MDSE applicability direction; this is scope, not fulfillment.

## Source

- EA relationship: [[EA Relationship - Realisation]]
- Endpoint pattern: `Thing / Document / Firmware → Requirement`

## Target

`Requirement appliesTo source element`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
