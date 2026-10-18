# Golden Import Step 2 — EA Decision mapping

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- EA `Decision` becomes one MDSE descriptive note, not an executable SysML v2 branching construct by default.
- Preserve source-connected incoming and outgoing elements and any explicitly modeled guards as descriptive information in the note, with YAML links to the related elements.
- Retain MDSE type/subtype, original EA type/stereotype, source identity and provenance in YAML.
- Do not infer executable branching, scheduling, control flow, or new SysML v2 relationships from this record.
- If a native control-flow relationship is independently present and eligible, process that source connector under its own approved translation rule; do not duplicate it from the Decision note.
- Confirm links, guards, source evidence, and idempotence during fixture acceptance.
