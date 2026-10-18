---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 57
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 57 — deriveReqt — Other endpoint pattern

## Source pattern

- **EA Connector:** deriveReqt
- **EA Stereotype / Pattern:** Other endpoint pattern
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Only Requirement→Requirement maps to `derivedFrom/derivedBy`. Other endpoint patterns require review.

## Body detail rule

Preserve connector notes and endpoint identities.

## Status

Review

## Review trigger

Either endpoint is not a Requirement

## Source basis / notes

Catch-all for malformed/nonstandard deriveReqt.
