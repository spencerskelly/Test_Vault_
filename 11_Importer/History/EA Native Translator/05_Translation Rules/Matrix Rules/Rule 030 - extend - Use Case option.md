---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 30
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 30 — extend — Use Case option

## Source pattern

- **EA Connector:** extend
- **EA Stereotype / Pattern:** Use Case option
- **Source Endpoint Semantics:** Optional Use Case
- **Target Endpoint Semantics:** Base Use Case

## MDSE relationship

- **Source YAML Relationship:** optionOf
- **Target YAML Inverse:** hasOption

## Transformation rule

Direct optional/conditional behavior relation.

## Body detail rule

Preserve extension condition in optional Use Case body.

## Status

Settled

## Review trigger

Endpoints are not true Use Cases after semantic classification

## Source basis / notes

Approved high-volume rule.
