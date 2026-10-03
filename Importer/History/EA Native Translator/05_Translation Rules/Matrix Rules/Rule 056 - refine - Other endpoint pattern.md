---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 56
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 56 — refine — Other endpoint pattern

## Source pattern

- **EA Connector:** refine
- **EA Stereotype / Pattern:** Other endpoint pattern
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Requirement→Requirement uses `refines/refinedBy`; approved non-Requirement precision/detail uses `describes/describedBy`. Any other pattern requires review.

## Body detail rule

Preserve connector notes and endpoint identities.

## Status

Review

## Review trigger

No approved refine pattern matches

## Source basis / notes

Catch-all after relationship vocabulary simplification.
