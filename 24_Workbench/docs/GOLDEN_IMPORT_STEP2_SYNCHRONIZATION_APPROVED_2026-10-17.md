# Golden Import Step 2 — Synchronization

Decision date: 2026-10-17. Status: APPROVED; native serialization and fixture validation pending.

- EA `Synchronization` elements represent local workflow fork/join control constructs, not reusable definitions and not standalone MDSE notes.
- Preserve each occurrence within its owning action/workflow, maintaining source identity and original EA type/stereotype as provenance.
- Determine fork/join behavior from the source's incoming and outgoing control-flow connections, not from the name or presumed glyph semantics alone.
- Where source connections do not unambiguously establish behavior or ownership, retain an explicit review disposition rather than invent behavior.
- Emit only native SysML v2-compatible control-flow semantics, validated against the pinned parser. No custom SysML relationship.
- Confirm independent occurrence identity, connection fidelity and repeat-import stability.
