---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 68
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 68 — Dependency — RAAML «RecoveryRequirement»

## Source pattern

- **EA Connector:** Dependency
- **EA Stereotype / Pattern:** RAAML «RecoveryRequirement»
- **Source Endpoint Semantics:** Any observed endpoint
- **Target Endpoint Semantics:** Any observed endpoint

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Identify explicitly but do not auto-convert until RAAML semantics are approved for MDSE.

## Body detail rule

Preserve raw stereotype, connector metadata, endpoints, and package context.

## Status

Review

## Review trigger

Always

## Source basis / notes

14 observed connectors; mainly State/Function → Requirement.
