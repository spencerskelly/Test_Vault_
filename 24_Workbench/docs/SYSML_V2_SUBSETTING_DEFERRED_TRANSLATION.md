# SysML v2 Feature Subsetting — Approved Native Support, Deferred Translation
Date: 2026-10-17
Status: APPROVED modeling capability; automatic EA/BOM mapping not approved.

## Decision
- Support native SysML v2 Subsetting as a distinct feature relationship in Workbench.
- Subsetting states that values of a subsetted feature are within the values of its superset feature, under native feature typing and contextual restrictions.
- Preserve its distinction from Specialization (type-level), Redefinition (refinement of inherited features), Feature Typing (feature to type), Composite/Reference usages and Allocation.
- Do NOT automatically convert any EA Generalization, Aggregation, Dependency, Realization, or BOM part/variant/quantity relationship into Subsetting under current rules.
- EA Generalization -> Specialization remains 1:1. Previously approved shared/composite, typing, redefinition deferral and other mappings remain unchanged.

## EA translator
- No mechanical Subsetting generation unless explicit valid source semantics are later found and individually approved.
- Preserve all original EA connector/element data in the migration ledger. Flag candidate cases for review but do not recategorize source relationships.
- Preserve manually created native subsets across subsequent imports with conflict detection.

## BOM translator
- Keep canonical definition per part identity and separate parent-owned usages/multiplicity/quantity/unit rules.
- A subset of BOM components, optional parts, product variants or compatible part-number groups does not automatically imply native feature subsetting.
- Preserve authored subset relationships; avoid inferred ones.

## Workbench and vault
- Engineer draws/chooses eligible features in a valid model context and can select Subsetting when metamodel typing, owner, scope and multiplicity rules permit.
- Preview subset feature, superset feature, ownership, typing constraints, native syntax and structural/graphical depiction before confirming; never store merely as arbitrary arrow.
- In-editor reference panel compares Subsetting to Redefinition, Specialization, Feature Typing and Reference Usage, with examples and validation guidance.
- Maintain vault-backed feature definitions/usages with stable IDs, reverse navigation, type-filtered show/hide and synchronized textual, structural, graphical and tabular editing.
- Keep any authored native subsets distinct from EA/BOM imported data in provenance.

## Validation
SUB-01 Valid native feature subsetting parses and satisfies semantic rules.
SUB-02 Invalid super/subset element kinds and incompatible typing are rejected with reason.
SUB-03 Existing EA generalizations remain 1:1 specializations.
SUB-04 BOM quantity, optional feature or variant does not spuriously create subset relationship.
SUB-05 UI help defines contrasts with redefinition and type specialization.
SUB-06 Round trip Workbench creation/edit/removal, source ledger, saved view filters, EA/BOM reimport stability.

## Follow-up tracker
SUB-F01 [Registry] Specify metamodel and exact normative subsetting syntax/constraints for selected SysML v2 version.
SUB-F02 [Workbench] Eligibility filtering, line gesture, directional preview and editing.
SUB-F03 [Vault] Author reference entry, examples, compare-to links, index.
SUB-F04 [EA] Identify any explicitly modeled compatible feature-subsetting relationships for later individual approval.
SUB-F05 [BOM] Non-inference, identity consistency and authored-relationship persistence tests.
SUB-F06 [QA] Parser validation, feature typing, inheritance, multiplicity, UI and round-trip tests.
SUB-F07 [Documentation] Add to central mappings and deferred-auto-translation register.

## Next review
Conjugation (especially Port conjugation): inspect native direction inversion and inherited features separately from generalization and typing. Previously agreed port distinctions remain in force; prioritize only unresolved interpretation, not reopen approvals.
