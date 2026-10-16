---
uid:
type: Info
status: Active
workspace: EA Native Translator
---
# Translator Open Decisions

This is a program-level queue. Detailed decisions belong in the applicable source/target/rule notes.

## Highest-priority work

1. **Requirement end-to-end definition** — current pilot: subtype mapping, property/tag mapping, relationship review, verification.
2. **Source-only EA constructs from full t_object evidence** — ActionPin, ActivityParameter, ActivityPartition, StateMachine and newly observed raw stereotypes.
3. **ControlFlow** — finalize local Functional Flow representation.
4. **ObjectFlow** — determine reusable Item Flow versus local behavioral transfer behavior.
5. **StateFlow / transition reconstruction** — define creation, trigger, guard, effect preservation.
6. **Ports and port-related behavior** — settle source Port/Part/ProxyConnector semantics.
7. **InformationFlow / Item Flow** — complete the native rule.
8. **Explicit EA Nesting** — distinguish semantic nesting from ownership/placement evidence.
9. **State/StateMachine satisfaction patterns** — finish deterministic treatment.
10. **Remaining Review/Deferred endpoint combinations** — process by frequency and engineering importance.
11. **MDSE relationship contracts** — ensure every property emitted by a rule has a complete definition.
12. **MDSE element contracts** — required/optional properties, body schema, placement, validation.

## Already settled; do not keep open

- BindingConnector → symmetric `equals` for approved rule.
- plain Connector → symmetric `interfaces` for approved rule.
- Dependency «verify» testCase → Requirement → `verifies / verifiedBy`.
- MDSE `Thing` → `Object`.
- `kind` → `subtype`.

## Review rule

A repeated pattern becomes a direct translator rule only when the semantic meaning is consistent enough to apply without human interpretation.
