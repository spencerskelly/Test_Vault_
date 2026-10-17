# Approved — Native SysML v2 Connection mapping
Date: 2026-10-17
Status: APPROVED; full-source coverage audit remains open

## Decision
Support native SysML v2 connection definitions and usages. Map EA connector type `Connector` to a native SysML v2 connection usage by default, preserving endpoint identities, directions/roles when semantically meaningful, ownership/context and named characteristics. Translate to native `interface` instead only if explicit interface semantics are established; do not treat every EA Association as a connection. Physical/logical connections, interfaces, and bindings retain distinct semantic types.

## Structural and visual Workbench
- The authoritative SysML v2 source is stored in the owning Obsidian note.
- Structural view: show connection usages, owning context, and endpoint feature paths; optionally a reusable connection definition for typed connections.
- Visual view: connectors between actual part or port usages, including endpoints addressed via nested feature chains, not duplicate nodes or invented ports.
- Editing any view rewrites/validates native syntax and updates all other views. Preserve resolved endpoints when moving or renaming usages.
- Native connections do not imply component containment, feature equivalence/binding, or dependency.
- One canonical reusable definition per type. Usage notes optional.
- Provide plain-language definition, good/bad examples, constraints, and distinct visualization.

## Source audit caveat
The uploaded 2026-10-15 mini QEAX was substantially reduced and contains only 9 EA Connector-type records and few ports; user confirms original full QEAX has hundreds of port-to-port links. Do not use mini model counts to infer complete production-model connectivity. Later audit full source for port-to-port links and EA connector classifications. This audit is NOT a blocker to approving semantic mapping and continuing relationship review.

## Next review
Native SysML v2 Interface definition and usage, its required port ends and distinction from general Connection.
