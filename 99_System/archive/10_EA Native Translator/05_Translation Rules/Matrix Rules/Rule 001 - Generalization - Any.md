---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 1
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 1 — Generalization — Any

## Source pattern

- **EA Connector:** Generalization
- **EA Stereotype / Pattern:** Any
- **Source Endpoint Semantics:** Specific element
- **Target Endpoint Semantics:** General element

## MDSE relationship

- **Source YAML Relationship:** subtypeOf
- **Target YAML Inverse:** supertypeOf

## Transformation rule

Direct semantic mapping; multiple inheritance allowed.

## Body detail rule

Preserve connector body detail only if separately populated.

## Status

Settled

## Review trigger

None

## Source basis / notes

EA source is specific; destination is general.
