---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 63
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 63 — Dependency — verify — testCase → Requirement

## Source pattern

- **EA Connector:** Dependency
- **EA Stereotype / Pattern:** verify — testCase → Requirement
- **Source Endpoint Semantics:** Activity «testCase»
- **Target Endpoint Semantics:** Requirement

## MDSE relationship

- **Source YAML Relationship:** verifies
- **Target YAML Inverse:** verifiedBy

## Transformation rule

Direct verification relationship.

## Body detail rule

Preserve connector notes/constraints in Test/Requirement bodies when meaningful.

## Status

Settled

## Review trigger

Either endpoint is not testCase→Requirement

## Source basis / notes

325 of 333 observed «verify» connectors match this pattern.
