# Golden Import Step 2 — Signal and Software Parameter Decision

Decision date: 2026-10-17
Status: APPROVED by model owner; implementation and native parser verification pending.

## Translation
- All EA Signal elements, including `Signal:Logical Signal` and `Signal:Physical Signal`, map to one reusable SysML v2 `ItemDefinition` per source-defined element.
- `Signal:Software Parameter` maps to a reusable SysML v2 `AttributeDefinition`, **not** an `ItemDefinition`.
- Element definition appears in exactly one MDSE note; native usages occur in their owning models without creating additional MDSE notes.
- Preserve `type`, `subtype`, `eaType`, and `eaStereotype` in note YAML (with original EA type also retained when a stereotype is present). Maintain source GUID provenance under the established private identity policy.
- Usage references the reusable definition; preserve native feature typing, ownership and optional units where explicitly modeled. No inferred additional meaning.

## Test gates
- All Signal families are accounted for in the per-element ledger.
- Software Parameter cannot silently fall back to ItemDefinition.
- Native serialization and parser/type checking required before declaring accepted.
- Repeated usages must not generate additional MDSE notes.

## Next discussion
Physical Context (unresolved semantics). Discuss one concrete example before finalizing rule.
