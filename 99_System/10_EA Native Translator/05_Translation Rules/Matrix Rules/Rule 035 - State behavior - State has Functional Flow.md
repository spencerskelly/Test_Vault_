---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 35
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 35 — State behavior — State has Functional Flow

## Source pattern

- **EA Connector:** State behavior
- **EA Stereotype / Pattern:** State has Functional Flow
- **Source Endpoint Semantics:** State
- **Target Endpoint Semantics:** Functional Flow

## MDSE relationship

- **Source YAML Relationship:** hasBehavior
- **Target YAML Inverse:** behaviorOf

## Transformation rule

Generated when StateMachine/detail behavior collapses or explicit state behavior is resolved.

## Body detail rule

Preserve entry/do/exit role locally in body/flow data.

## Status

Settled

## Review trigger

Functional Flow is not retained in current native pass

## Source basis / notes

Established pair.
