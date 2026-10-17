# Golden Import Step 2 — System Partner

Decision date: 2026-10-17. Status: APPROVED; implementation and parser verification pending.

- EA `Class:System Partner` maps to reusable native SysML v2 `PartDefinition`, classified as **external** in MDSE YAML.
- Preserve `type`, `subtype`, `eaType`, `eaStereotype`, and source provenance in YAML.
- Do not infer internal ownership or physical containment from organizational package nesting or external-part classification.
- One MDSE note per defined System Partner; contextual usages reference its definition without separate notes.
- Preserve explicitly modeled source relationships according to their approved rules; unresolved relationships stay flagged for review.
