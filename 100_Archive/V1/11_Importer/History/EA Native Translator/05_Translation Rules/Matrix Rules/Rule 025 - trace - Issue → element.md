---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 25
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 25 — trace — Issue → element

## Source pattern

- **EA Connector:** trace
- **EA Stereotype / Pattern:** Issue → element
- **Source Endpoint Semantics:** Issue
- **Target Endpoint Semantics:** Affected element

## MDSE relationship

- **Source YAML Relationship:** affects
- **Target YAML Inverse:** affectedBy

## Transformation rule

Do not preserve trace mechanically; map to impact when clear.

## Body detail rule

Preserve detail in endpoint bodies.

## Status

Settled

## Review trigger

Meaning not impact

## Source basis / notes

Approved trace semantic mapping.
