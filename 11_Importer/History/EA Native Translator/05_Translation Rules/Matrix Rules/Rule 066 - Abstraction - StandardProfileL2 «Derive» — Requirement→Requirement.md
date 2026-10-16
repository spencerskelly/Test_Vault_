---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 66
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 66 — Abstraction — StandardProfileL2 «Derive» — Requirement→Requirement

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** StandardProfileL2 «Derive» — Requirement→Requirement
- **Source Endpoint Semantics:** Requirement
- **Target Endpoint Semantics:** Requirement

## MDSE relationship

- **Source YAML Relationship:** derivedFrom
- **Target YAML Inverse:** derivedBy

## Transformation rule

Treat explicit Standard Profile Derive between Requirements as derivation.

## Body detail rule

Preserve connector notes if useful.

## Status

Settled

## Review trigger

Either endpoint is not a Requirement

## Source basis / notes

7 of 8 observed StandardProfileL2::Derive connectors are Requirement→Requirement.
