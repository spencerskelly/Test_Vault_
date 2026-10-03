---
uid:
type: Translation Rule
status: "Deferred"
matrixRuleId: 46
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 46 — ObjectFlow — Behavioral transfer

## Source pattern

- **EA Connector:** ObjectFlow
- **EA Stereotype / Pattern:** Behavioral transfer
- **Source Endpoint Semantics:** Behavior usage / action / object node
- **Target Endpoint Semantics:** Behavior usage / action / object node

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Identify and retain as local behavioral transfer evidence. Do not create a global YAML relationship in the native pass; Item Flow / Functional Flow reconstruction remains postponed.

## Body detail rule

Preserve conveyed object/item, direction, guards, and local context in source/body evidence where available.

## Status

Deferred

## Review trigger

Always until Item Flow / Functional Flow native-import rules are finalized

## Source basis / notes

Primary reference §8.12.
