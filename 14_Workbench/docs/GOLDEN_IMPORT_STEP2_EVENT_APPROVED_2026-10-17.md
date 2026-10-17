# Golden Import Step 2 — EA Event mapping

Decision date: 2026-10-17. Status: APPROVED; implementation and official SysML v2 parser verification pending.

- EA `Event` representing a reusable event type maps to native SysML v2 `OccurrenceDefinition`.
- Event usages are local to their owning workflows and refer to the reusable definition; no separate MDSE note for usages.
- Maintain one MDSE note for the defined event, including MDSE type/subtype, original EA type/stereotype, and source provenance in YAML.
- If source evidence does not establish a reusable event type or workflow ownership, flag for review instead of inferring context.
- Validate syntax, typing, source links, usage identities and repeated import stability.
