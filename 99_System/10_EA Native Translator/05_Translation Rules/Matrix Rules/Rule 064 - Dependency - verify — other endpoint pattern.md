---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 64
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 64 — Dependency — verify — other endpoint pattern

## Source pattern

- **EA Connector:** Dependency
- **EA Stereotype / Pattern:** verify — other endpoint pattern
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not coerce malformed/non-test verification connectors. Preserve evidence and review.

## Body detail rule

Preserve connector metadata and endpoint identities.

## Status

Review

## Review trigger

Always when rule 63 does not match

## Source basis / notes

8 observed connectors fall outside testCase→Requirement.
