# APPROVED — Native SysML v2 Transition Usages
Date: 2026-10-17
Status: APPROVED — relationship #16

## Meaning in plain language
A Transition represents a switch from one active state to another within its owning state behavior. It may have an event trigger, a Boolean guard condition, and an effect action. It is not just a generic before/after sequence.

## Native modeling
- Record source and target states, owning state context, and event acceptance, guard, and effect where present.
- Support transitions in nested state contexts and precise validation of references.
- Syntax must be checked against an official SysML v2 parser before being declared production compliant.

## EA migration
Translate EA StateFlow connectors into native transition usages when their endpoints and context establish genuine state transitions. Preserve transition direction and all available event, guard, effect, and state-machine context.
- Do not reinterpret ordinary ControlFlow as a state transition.
- If EA StateFlow lacks mandatory native context or its endpoints are incompatible, flag rather than fabricate valid syntax.
- EA source links may be discarded once successfully translated into canonical note syntax.

## Workbench
- Structural view: incoming/outgoing transitions per state, source/target, trigger/guard/effect, nested owning state.
- Visual view: state diagram arrows labelled with trigger, guard and effect; distinction from succession, flow, connection.
- Editors: changing any transition in state diagram, structural view or text updates the owning note's authoritative SysML v2 syntax; other views refresh.
- Validation: state scope, source/target resolution, guard typing, accepted event and effect compatibility, legal transition constructs.
- Single shared definition per type; individual transition usages do not need separate Markdown notes.
- Documentation: formal definition, plain language, examples, counterexamples, comparison with Succession and Flow, editable Workbench presentation.

## Next relationship
Native allocation definitions and usages; distinguish generic mapping from specific performs/implements or requirement satisfaction semantics.
