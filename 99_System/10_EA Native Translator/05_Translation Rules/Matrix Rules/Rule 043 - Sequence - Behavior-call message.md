---
uid:
type: Translation Rule
status: "Deferred"
matrixRuleId: 43
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 43 — Sequence — Behavior/call message

## Source pattern

- **EA Connector:** Sequence
- **EA Stereotype / Pattern:** Behavior/call message
- **Source Endpoint Semantics:** Participant / behavior context
- **Target Endpoint Semantics:** Participant / behavior context

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not create a standalone global Sequence relationship; defer to local behavior representation.

## Body detail rule

Preserve sequence/message detail in source evidence/body where needed.

## Status

Deferred

## Review trigger

Always

## Source basis / notes

Earlier rule treats ordering as local Functional Flow content.
