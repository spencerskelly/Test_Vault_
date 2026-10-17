# Golden Import Step 2 — EA Object mapping

Decision date: 2026-10-17. Status: APPROVED; implementation and parser validation pending.

- EA `Object` becomes a reusable native SysML v2 `PartDefinition`, not an instance usage.
- Do **not** translate the EA instance-classifier association into a native SysML relationship or typing reference.
- Preserve the original EA classifier ID in MDSE YAML strictly as source provenance (not a live semantic classifier link).
- Preserve `type`, `subtype`, `eaType`, `eaStereotype`, original source identity and import provenance in YAML.
- Create one MDSE note per defined Object. Usages of that definition in other owning models do not create additional notes.
- Independently modeled EA connectors are processed according to their own approved relationship mappings; removal of instance-classifier typing does not authorize deletion of unrelated source relationships.
- Acceptance: classifier ID present as provenance only; native output has no inferred classifier edge; stable IDs and repeat-import behavior validated.
