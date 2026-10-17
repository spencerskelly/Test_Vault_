# Golden Import — Nested port ownership

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser validation pending.

- Direct nesting of an EA `Port` within an EA Part is sufficient source evidence of port ownership; no Aggregation or Composition connector is required.
- Emit a native SysML v2 `PortUsage` owned by the containing `PartDefinition` or applicable part context.
- Reference a reusable `PortDefinition` when available. If typing is absent, permit untyped `PortUsage` and flag `UNRESOLVED_PORT_TYPE` under the approved element policy.
- Preserve EA source identities, type/stereotype and original nesting provenance in the owning model metadata; do not create an extra MDSE note for port usage.
- EA package folders do not establish port ownership. Missing/invalid owner and conflicting ownership must be flagged rather than inferred from organizational hierarchy.
- Validate native syntax, stable ownership and reimport consistency.
