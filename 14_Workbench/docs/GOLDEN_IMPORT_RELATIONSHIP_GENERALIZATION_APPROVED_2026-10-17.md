# Golden Import — EA Generalization to native specialization

Decision date: 2026-10-17. Status: APPROVED; fixture-level orientation checking, implementation and official native parser verification pending.

- Translate explicit EA Generalization between compatible reusable definitions into native SysML v2 specialization.
- Preserve original **specific (child) → general (parent)** direction, validated against trusted EA source metadata; do not infer direction from diagram glyph or layout.
- Do not infer native redefinition, variation or any more specific semantic construct solely from Generalization.
- Preserve EA connector identity, endpoints, stereotype, source orientation and provenance in the local ledger and linked MDSE model metadata.
- If either endpoint is not a compatible definition, is unresolved, or creates an invalid specialization/cycle, preserve evidence and flag review instead of emitting invalid native syntax.
- Existing separately approved EA Object classifier -> specialization transformation remains distinct source evidence and must follow the same target compatibility checks.
- Maintain one MDSE note per reusable definition; specialization does not create additional notes.
