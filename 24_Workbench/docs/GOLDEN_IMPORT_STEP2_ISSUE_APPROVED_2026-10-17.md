# Golden Import Step 2 — Issue mapping

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- EA `Issue` elements become MDSE `Issue` notes, not native SysML v2 model definitions or relationships.
- Each Issue note preserves MDSE type/subtype and original `eaType` and `eaStereotype` in YAML.
- YAML links reference the affected model elements where supported by source evidence. No affected-element relationship is inferred solely from placement or names.
- Preserve source identity and provenance under the standard import contract.
- Maintain one note per Issue source element; no extra usage notes.
- The source ledger records each Issue as a retained MDSE note disposition, not a silently discarded source record.
- Confirm note link integrity and idempotent reimport during acceptance.
