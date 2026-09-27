---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 9
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 9 — Instance / classifier — Real-world occurrence

## Source pattern

- **EA Connector:** Instance / classifier
- **EA Stereotype / Pattern:** Real-world occurrence
- **Source Endpoint Semantics:** Occurrence
- **Target Endpoint Semantics:** Reusable type

## MDSE relationship

- **Source YAML Relationship:** instanceOf
- **Target YAML Inverse:** hasInstance

## Transformation rule

Use only for genuine installed/serialized occurrences.

## Body detail rule

Preserve classifier detail only if useful.

## Status

Settled

## Review trigger

Product-design occurrence, firmware version, reusable variant

## Source basis / notes

instanceOf reserved for real occurrences.
