# APPROVED — Native SysML v2 Flows
Date: 2026-10-17
Status: APPROVED — Relationship #14

## Plain language
A Connection declares connectivity; a Flow declares a transfer, including the thing transferred and its directed endpoints where defined. A connection does not entail any particular transferred payload.

## Scope of approval
Support native SysML v2 Flow Definitions and Flow Usages including:
- message flows
- streaming flows
- succession flows
Keep their native distinctions and exact semantics; follow the official language specification and validate serialization with a conforming parser. No special invented SysML v2 relationship keywords.

## Import policy
Only create a target Flow from explicit EA evidence of transferred item/message/signal/material/energy or flow semantics. Never infer Flow merely because a port-to-port Connector or Association exists. Where EA evidence is insufficient, retain only the native Connection if appropriate and flag potential flow enrichment as optional review, not fabricated semantics.

## Workbench
- Structural view: flow definition/type, usage, source, destination, payload/item type, direction and owning context. Distinguish message, streaming and succession cases.
- Visual view: directed, distinctly styled flow arrow; allow optional overlay on structural connection, but do not conflate the two. Multiple distinct flows may traverse same connection.
- Editor: adding/modifying flow in any view updates authoritative SysML v2 syntax in owning note; refresh structural and visual projections after validating.
- Validate endpoint resolution, direction, transfer item compatibility, semantics of message/streaming/succession, namespace references, and ordering where required.
- Support nested feature chains to address endpoints without duplicate parts.
- Canonical shared definitions remain single; individual usages do not need separate Markdown notes.

## Teaching examples
- Message: controller sends a CANMessage to gateway, distinct from fact that CAN ports connect.
- Streaming: a producer output is streamed into a receiver input, with directional feature constraints.
- Succession flow: transferred item plus an ordering relation between occurrences/actions.
- Counterexample: two wired CAN ports, no identified messages or transfers — Connection only.

## Further verification
Native example syntax and precise endpoint constraints should be checked against the current OMG SysML v2 Language Specification and the reference parser before the implementation is claimed production-ready.
## Next review
Native succession (temporal ordering) and its distinction from succession flows and transitions.
