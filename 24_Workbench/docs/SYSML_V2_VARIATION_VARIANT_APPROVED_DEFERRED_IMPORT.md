# SysML v2 Variation and Variant — Approved Native Support
Date: 2026-10-17
Status: APPROVED native modeling; automatic EA/BOM conversion DEFERRED.

## Decision
- Use native SysML v2 Variation and Variant constructs for explicit configurable alternatives and product configuration choices.
- Workbench should allow defining variation points, permitted variants and their relevant constraints using vault-defined options, distinct from arbitrary relationships.
- Do not automatically convert EA Generalizations, EA copy/aliases, BOM variantOf metadata, assembly alternatives, revisions or part-number similarity into Variation/Variant. Existing mapping remains unchanged.
- DVS and related charger product-family models are candidate examples for evidence-based follow-up, not automatic inference.
- In-editor Definitions reference must distinguish Variant/Variation from Specialization, Redefinition, Feature Typing, Subsetting and BOM revisions.
- Local native model definitions reside in vault, using stable IDs, qualified names, type-safe constraints and valid native syntax.

## EA Translator
- Preserve existing source generalization to specialization, part usages and copy alias consolidation rules.
- Record variation candidates separately from approved translations with original EA GUID, stereotype, relation roles, package and source evidence.
- No synthetic variants; preserve manually authored native choices across reimports and flag conflicts.
- Reconcile all EA source records to native outputs or explicit exceptions.

## BOM Translator
- variantOf remains optional metadata / investigation signal, not automatic SysML v2 variant creation.
- BOM parent usages, quantities, units, revisions and where-used remain independent from variation semantics.
- Different revision or alternative supplier does not alone establish a native variation point.
- Canonical identities and explicit Workbench-authored Variation/Variant usages survive BOM refresh.

## Workbench
- Engineer creates Variation/Variant in valid definition/usage context with filtered vault-sourced choices; offers native constraints and eligible alternatives and displays proposed model edit before commit.
- Product configuration view lists variation points and allowable selections; structural, textual, graph and table views share canonical identities.
- Show/hide Variations/Variants as independent visual filters; custom workflow views remain separate presentation projections.
- Definitions drawer/popover provides short native meaning, valid scope, syntax, compared constructs, examples and normative links without leaving current view.

## Validation
- Check variation-owner and variant-membership structure and cardinality/constraints per SysML v2.0 metamodel.
- Confirm no automatic variant from EA generalization, BOM variantOf, copied object or BOM revision.
- Shared definition appears in multiple valid variation contexts without duplicating canonical definitions.
- EA/BOM import idempotency, provenance, rendering/view filters, native syntax round-trip, and explicit ambiguity flags.

## Follow-ups
VAR-01 Inventory DVS and related family candidate alternatives and source patterns.
VAR-02 Build normative registry entries for Variation, Variant and compatible constraints, backed by parser fixtures.
VAR-03 Define vault model + configuration view and value selection.
VAR-04 Workbench create/edit/compare/visualize variations and resolve options with dropdown filters.
VAR-05 EA translator candidate identification, no-inference and reconciliation tests.
VAR-06 BOM variantOf/revision separation and reimport stability tests.
VAR-07 Conformance and product configuration tests including conflicting choices.
VAR-08 Review whether any mechanical source mapping can be approved after corpus inspection.

## Next review
Causation and occurrence-related native constructs. Distinguish causal claims from ordinary dependencies and temporal successions; avoid inferring causation from flow or ordering.
