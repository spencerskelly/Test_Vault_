# MDSE v2 — Testing

**Status:** Test plan scaffold.

## Acceptance progression
1. Synthetic SysML structure with reusable part definitions and contextual usages.
2. Ports, interfaces, connections, binding, flow and inverse navigation.
3. One representative charger assembly with real-world shaped but synthetic BOM rows.
4. Cross-note ownership and export to standards-valid `.sysml` source.
5. Independent SysML parser validation plus round-trip semantic diff.
6. Workbench create/edit/undo and visual read-only structure exploration.
7. Repeatable scoped EA imports using sanitized fixtures.
8. Controlled real-source tests outside this repo, with hashes and summary evidence checked in.

Test each semantic rule for source preservation, no double-counting, identity stability and deterministic output. Keep an explicit **unresolved/review** category; it must not become valid semantic graph content.
