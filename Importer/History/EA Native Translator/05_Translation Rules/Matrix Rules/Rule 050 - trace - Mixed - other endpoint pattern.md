---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 50
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 50 — trace — Mixed / other endpoint pattern

## Source pattern

- **EA Connector:** trace
- **EA Stereotype / Pattern:** Mixed / other endpoint pattern
- **Source Endpoint Semantics:** Any semantic element
- **Target Endpoint Semantics:** Any semantic element

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not preserve generic trace mechanically. If none of the approved endpoint-specific trace rules applies, preserve evidence and require semantic review.

## Body detail rule

Preserve connector name/notes/roles and endpoint identities.

## Status

Review

## Review trigger

No approved endpoint-specific trace rule matches

## Source basis / notes

Monitor System documented mixed Activity/State/Requirement trace patterns.
