# Golden Import Step 2 — EA Object mapping

Decision date: 2026-10-17. Status: APPROVED; implementation and parser validation pending.

- EA `Object` becomes a reusable native SysML v2 `PartDefinition`, not an instance usage.
- **Revised decision (2026-10-17):** Translate the EA Object instance classifier to native SysML v2 **specialization** of the corresponding reusable definition, provided the referenced classifier resolves to a compatible definition. Do not retain it as instance-typing. Unresolved or incompatible classifiers are explicitly flagged for review, with original evidence preserved.
- Preserve the original EA classifier ID in MDSE YAML as provenance and retain the resolved specialization target as a genuine native semantic relationship when validated.
- Preserve `type`, `subtype`, `eaType`, `eaStereotype`, original source identity and import provenance in YAML.
- Create one MDSE note per defined Object. Usages of that definition in other owning models do not create additional notes.
- Independently modeled EA connectors are processed according to their own approved relationship mappings; removal of instance-classifier typing does not authorize deletion of unrelated source relationships.
- Acceptance: valid classifier becomes specialization; unresolved/incompatible classifier is flagged, not fabricated; original classifier ID remains in provenance; stable IDs, direction, parser compatibility and repeat-import behavior validated.
