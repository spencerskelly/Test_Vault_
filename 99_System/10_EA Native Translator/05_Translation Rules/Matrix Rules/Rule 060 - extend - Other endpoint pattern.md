---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 60
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 60 — extend — Other endpoint pattern

## Source pattern

- **EA Connector:** extend
- **EA Stereotype / Pattern:** Other endpoint pattern
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Only a true optional Use Case→base Use Case pattern maps to `optionOf/hasOption`. Other endpoint patterns require review.

## Body detail rule

Preserve extension condition/name/notes and endpoint identities.

## Status

Review

## Review trigger

Endpoints are not true Use Cases / optional behavior

## Source basis / notes

Catch-all semantic review.
