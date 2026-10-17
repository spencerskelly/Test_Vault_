# Feature Typing, Composite and Shared Usage — Scope Confirmation
Date: 2026-10-17
Status: CONFIRMED — no new semantic decision, no reopening of approved rules.

## Baseline retained
- One reusable definition, with multiple typed usages, remains the approved native SysML v2 Feature Typing model.
- Composite and shared/referential usage behavior remains governed by the previously agreed definitions. No replacement default, reinterpretation, or new classification requirement is introduced by the current review.
- Generalization -> Specialization retains the approved 1:1 EA mapping.
- A BOM part number's reusable identity is not duplicated for each where-used occurrence. Parent assemblies hold usage, multiplicity, quantity and unit information under the previously approved BOM modeling rules.
- Workbench uses the common native semantic registry and in-editor definitions panel; no separate conflicting composite/shared convention.
- Preserve EA and BOM source evidence and deterministic source-to-target dispositions; deviations are flagged rather than silently changed.

## Downstream review and follow-ups
- EA translator: verify inherited approved mapping for classifier/type, usage identity, owner and source associations; no newly inferred composite/ref classification.
- BOM translator: preserve one canonical definition with distinct typed usages in parent BOMs, prior quantity/unit rules and shared-part semantics.
- Workbench: show definition, usages and where-used navigation without cloning definitions; native creation operations remain eligible by context.
- Vault: retain previous definition/usage notes and their semantics, avoid parallel registries.
- Validation: repeat import, cross-source merge, where-used queries, multiplicities and view/edit synchronization.
- No implementation claimed. Next topic should be an unresolved relationship rather than revisiting Feature Typing or composite/shared.

Related documents: SYSML_V2_GENERALIZATION_SPECIALIZATION_APPROVED_MAPPING.md, SYSML_V2_DRAW_TO_RELATE_AND_VAULT_DEFINITIONS_CONTRACT.md, SYSML_V2_RELATIONSHIP_REFERENCE_AND_HELP_PANEL.md.
