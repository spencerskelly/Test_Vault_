# Golden Import Step 2 — FlowProperty

Decision date: 2026-10-17. Status: APPROVED; native serialization/parser verification pending.

- EA `Part:FlowProperty` maps to a native SysML v2 `ItemUsage` owned by its containing port.
- Type the ItemUsage using an existing reusable `ItemDefinition` where source evidence supports that type.
- Preserve explicitly modeled flow direction (`in`, `out`, `inout`), with its source evidence and original EA type/stereotype.
- No separate MDSE note is created for the local FlowProperty usage; retained source provenance and usage identity belong to the owning model representation.
- Where owner, flow direction, or typing is uncertain, retain explicit review disposition; do not infer payload or direction.
- Validate against pinned native grammar/libraries, verify reference integrity and stable reimport behavior.
