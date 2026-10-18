# Golden Import Step 2 — InformationItem mapping

Decision date: 2026-10-17. Status: APPROVED; runtime implementation pending.

- EA `InformationItem` means **description only**, not an exchanged payload or native SysML v2 `ItemDefinition`.
- Translate each source element into one MDSE descriptive Information Item note, outside canonical SysML v2 declarations.
- Preserve `type`, `subtype`, `eaType`, and `eaStereotype` in YAML, and link from its YAML to described/associated MDSE elements only when backed by source evidence.
- Do not infer flow, item typing, or relationships from the name or description.
- Preserve EA source identity/provenance and ensure source ledger disposition, link validation, and idempotence.
- This is distinct from the separately approved EA Signal -> ItemDefinition rule.
