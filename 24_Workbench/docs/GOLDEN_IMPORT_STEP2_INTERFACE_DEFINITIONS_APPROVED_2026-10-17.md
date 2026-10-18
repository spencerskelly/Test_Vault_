# Golden Import Step 2 — EA Interface families

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser verification pending.

- EA `Class:Electrical & Material Interface`, `Class:Data Interface`, and `Class:Mechanical Interface` all map to reusable native SysML v2 `InterfaceDefinition` elements for the first import.
- Apply the same translation rule to all three families, while preserving each original EA type and stereotype, MDSE type/subtype and source provenance in YAML.
- One MDSE note per InterfaceDefinition; local usages do not create additional notes.
- Preserve explicitly modeled relationship endpoints and other source details subject to their independently approved native translation rules; do not infer interface flows or ports merely from the stereotype.
- Validate native serialization, reference integrity and repeat-import stability.
