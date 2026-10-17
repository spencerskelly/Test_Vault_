# EA Generalization to SysML v2 Specialization — Approved Rule
Date: 2026-10-17
Status: Approved default mapping; parser/semantic conformance and migration implementation pending.

## Decision
- Translate every EA Generalization connector to a SysML v2 Specialization relationship as a **1:1 source-to-target migration rule**, preserving the specialized (child/specific) element and general (parent/general) element roles.
- Do not recategorize existing Generalizations as redefinition, subsetting, conjugation, feature typing, or other more specific SysML v2 relationships during initial migration. Refinements are an explicitly deferred subsequent modeling task.
- Preserve each original EA GUID, endpoint IDs, direction, stereotypes, tags, and notes, even if validation identifies an incompatibility.
- 1:1 applies to traceability between source connector and intended target specialization; valid native model output is conditional on compatible element typing and specialization context. If invalid, keep the exact source record and a clearly flagged exception—never manufacture a valid specialization.
- Distinguish the intended specialization mapping from SysML v2 FeatureTyping, owned usage, Allocation, and component implementation.

## EA translator
- Read Generalization client/child and supplier/parent identities and validate mapped native metaclasses and inheritance/feature restrictions.
- Emit standard native specialization syntax and model constructs without automatically converting to more specific kinds; no inferred subtype changes.
- Record deterministic source/target ID mapping and full original EA evidence, rule/version, eligibility result and disposition.
- Validate and flag cycles, illegal metaclass combinations, unavailable parents, duplicate edges and unresolved namespace/typing.

## BOM translator
- Preserve canonical part identity and approved EA generalizations across BOM import or reimport.
- BOM variantOf is not automatically Generalization/Specialization; evaluate variant similarities explicitly outside this rule.
- Do not infer specialization merely from part-number similarity, optional variants, BOM ancestry or manufacturer revisions.
- Surface any conflicts between BOM hierarchy and specialization assumptions as evidence-backed flags.

## Workbench
- Drawing from a candidate specific element to general element presents Specialization if native typing rules allow; directional preview explicitly labels specific/general roles.
- Standard definitions pane explains Specialization vs FeatureTyping vs Subsetting vs Redefinition vs Allocation and lets engineer inspect source EA provenance without leaving current view.
- Graph/structural/text/tabular projections use same canonical IDs and native syntax. User can intentionally refine relationship later with distinct, audited edit operation.
- Saved type filters can hide specializations from the custom view without affecting model.

## Vault
- Versioned native Specialization definition/help entry with eligible metaclasses, inheritance semantics, qualified identities, graphical and textual forms, provenance, validation status, and follow-up refinements.
- Parent/child navigation and inherited feature inspection; no duplicated inherited declarations solely for drawing arrows.

## Acceptance tests
1. EA Generalization child-to-parent -> one corresponding intended native specialization with correct direction and provenance.
2. Multiple inheritance as allowed by standard validated faithfully.
3. Incompatible endpoints flagged with original preserved; no semantic guess.
4. BOM part variantOf does not silently cause Specialization.
5. Workbench create/edit/inspect/undo and graphical/textual round trip.
6. Type filters show/hide only, without semantic change.
7. Full source-connector coverage ledger accounts for each EA Generalization.

## Follow-up
GEN-01 inventory source EA Generalizations by mapped endpoint kinds and count.
GEN-02 implement strict 1:1 translator rule, stable identity and ledger.
GEN-03 implement native parser/metamodel eligibility and cycles checks.
GEN-04 Workbench create and provenance-backed edit/definition compare.
GEN-05 BOM cross-import identity and variant non-inference tests.
GEN-06 later systematic refinement of specializations where a more precise native relationship is justified.
GEN-07 update central machine-readable relationship registry and Help panel.
