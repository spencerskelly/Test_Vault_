# SysML v2 Redefinition — Deferred Translation Decision
Date: 2026-10-17
Status: Native Workbench support approved in principle; automatic EA/BOM translation DEFERRED.

## Decision
- Native SysML v2 feature redefinition will be used, particularly for product families such as DVS whose inherited features are intentionally overridden in specialized models.
- There is no approved deterministic/mechanical EA or BOM translation for redefinition today.
- Do not infer redefinition from EA Generalization, variantOf, part name similarity, subtype relationships, BOM revision, alternative component, or related product family.
- Keep EA Generalization -> native Specialization 1:1; preserve all other previously approved translation rules unchanged.
- Retain original source relationship/part identity and provenance. Potential redefinition cases may be flagged as nonblocking *refinement candidates*, not silently transformed.
- Revisit only after real source examples, family inheritance structures and native v2 constraints are reviewed.

## EA translator impact
- Do not automatically emit redefining features from Generalizations or other relations.
- Inventory candidate inherited overrides for later review, including DVS family; retain actual EA data, roles, owner and stable IDs.
- Distinguish later explicit native redefinitions authored in Workbench from unchanged EA source mappings. Re-import must not overwrite these authored edits without review.

## BOM translator impact
- Keep one reusable part definition with approved composite/shared usages and quantity/unit rules.
- Alternative BOM members and product variants do not by themselves imply redefinition.
- Preserve explicit native redefinitions authored by engineers and flag import conflicts rather than rewriting.

## Workbench / vault
- Support eligible native Redefinition creation/editing once implemented: select inherited feature, choose redefining feature, preview inherited context/ownership/type restrictions, validate actual v2 semantics and show inheritance/override in structural, visual, textual and tabular views.
- Definitions info panel must distinguish Redefinition vs Specialization, Feature Typing, Subsetting and Allocation, with DVS-family examples only after evidence verified.
- Preserve a definition/usage registry and trace from redefining feature to redefined feature; create no new ad hoc relationship type.
- Add optional per-view visibility filter for redefinitions; view behavior is presentation-only.

## Validation and follow-up
RED-01 Collect representative DVS product-family inheritance, variant and feature-override cases from EA and BOM exports.
RED-02 Validate native SysML v2 redefinition syntax/metamodel, permissible redefining features, ownership and multiplicities.
RED-03 Establish source-evidence criteria for any future automatic EA/BOM translation and approve separately.
RED-04 Implement Workbench guided Redefinition creation, help and edit preview.
RED-05 Show inherited vs overridden features and original definitions across Workbench perspectives.
RED-06 Regression: initial imports produce no guessed redefinitions; preserve specialization 1:1.
RED-07 Regression: EA/BOM reimport retains authored redefinitions and flags conflicts.
RED-08 Update central relationship registry, exceptions, and implementation status.

## Next review
Feature Subsetting: distinguish selecting a subset of an inherited/referenced feature from Redefinition and Specialization; no new automatic mapping without explicit approval.
