# Golden Import — Generated usage naming

Decision date: 2026-10-17. Status: APPROVED policy; implementation pending.

- Prefer an explicitly modeled EA relationship-end role/name for each owned usage when present.
- If absent, derive a readable native SysML v2 usage name from the referenced child definition's name (e.g. `PowerModule` -> `powerModule`).
- When multiple usages in the **same owning context** would have the same generated name, apply deterministic numeric suffixes: `powerModule`, `powerModule_2`, etc.
- Preserve each independently modeled EA aggregation connector as a distinct usage and a distinct line in the parent model, even if endpoints match. Do not merge by name or endpoints.
- Persist a stable usage identity associated with the source connector. On reimport, retain established names where possible; resolve newly introduced collisions deterministically without gratuitously renaming existing usages.
- Follow native SysML v2 identifier escaping/validation where names contain spaces, symbols, reserved words or collisions. Keep source names and connector identities in provenance.
- One MDSE note per reusable definition; generated usage names do not create additional definition notes.
