---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 8
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 8 — Association — Thing ↔ Thing vague

## Source pattern

- **EA Connector:** Association
- **EA Stereotype / Pattern:** Thing ↔ Thing vague
- **Source Endpoint Semantics:** Thing
- **Target Endpoint Semantics:** Thing

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not create generic Association relationship.

## Body detail rule

If connector has meaningful name/notes, preserve body detail and flag review; otherwise explicit ignore.

## Status

Review

## Review trigger

Any non-empty label/notes/roles/constraints or meaningful endpoint pattern

## Source basis / notes

No generic associatedWith relationship.
