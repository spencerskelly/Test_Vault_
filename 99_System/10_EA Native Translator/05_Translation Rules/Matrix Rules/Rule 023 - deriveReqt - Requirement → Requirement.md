---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 23
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 23 — deriveReqt — Requirement → Requirement

## Source pattern

- **EA Connector:** deriveReqt
- **EA Stereotype / Pattern:** Requirement → Requirement
- **Source Endpoint Semantics:** Derived Requirement
- **Target Endpoint Semantics:** Source Requirement

## MDSE relationship

- **Source YAML Relationship:** derivedFrom
- **Target YAML Inverse:** derivedBy

## Transformation rule

Map SysML deriveReqt to derivedFrom / derivedBy.

## Body detail rule

Preserve connector notes if useful.

## Status

Settled

## Review trigger

Destination unavailable or endpoint not Requirement

## Source basis / notes

Approved mapping.
