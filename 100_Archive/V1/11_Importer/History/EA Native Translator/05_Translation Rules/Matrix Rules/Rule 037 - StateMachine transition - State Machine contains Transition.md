---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 37
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 37 — StateMachine transition — State Machine contains Transition

## Source pattern

- **EA Connector:** StateMachine transition
- **EA Stereotype / Pattern:** State Machine contains Transition
- **Source Endpoint Semantics:** State Machine
- **Target Endpoint Semantics:** Transition

## MDSE relationship

- **Source YAML Relationship:** hasTransition
- **Target YAML Inverse:** transitionOf

## Transformation rule

Use for true State Machines.

## Body detail rule

Transition guard/trigger/effect in body.

## Status

Settled

## Review trigger

StateMachine is collapsed/suppressed

## Source basis / notes

Established state vocabulary.
