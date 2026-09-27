---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 36
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 36 — StateMachine composition — State Machine contains State

## Source pattern

- **EA Connector:** StateMachine composition
- **EA Stereotype / Pattern:** State Machine contains State
- **Source Endpoint Semantics:** State Machine
- **Target Endpoint Semantics:** State

## MDSE relationship

- **Source YAML Relationship:** hasState
- **Target YAML Inverse:** stateOf

## Transformation rule

Use for true first-class State Machines.

## Body detail rule

Preserve local state details in state notes.

## Status

Settled

## Review trigger

StateMachine is collapsed/design taxonomy instead

## Source basis / notes

Established state vocabulary.
