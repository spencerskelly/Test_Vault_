# Approved: Specialization, Subsetting, Redefinition
Date: 2026-10-16
Status: APPROVED Option A
Repository: Test_Vault_; scope EA → SysML v2 → MDSE → Workbench

## Semantic separation
1. **Specialization**: definition/type-level classification (native SysML v2 specialization). Do not mistake it for part containment or configuration similarity.
2. **Subsetting**: feature/usage-level constraint/subset of an existing feature; retain feature identity and ownership.
3. **Redefinition**: a feature/usage redefines an inherited feature in a specializing context; preserve both original and redefining features and their context.
Use native constructs, not a merged `subtypeOf` or generic edge internally.
EA Generalization between compatible definitions is a candidate specialization. Other EA connectors require semantic checks; never silently infer subsetting/redefinition.
MDSE `partOf` corresponds to containment/part usage, not subsetting. `variantOf` is an evaluation marker; specialization or redefinition must be substantiated.

## Workbench structure
- Distinct typed relationship records, owner, source, target, usage vs definition identity, owning context, EA GUID/provenance.
- Tree overlays for inherited, subsetted and redefined features; distinguish directly owned from inherited.
- Navigate from redefining feature to original; preserve definition references and contextual usage.
- Do not duplicate reusable definitions merely to render usages.

## Workbench visual behavior
- Different visible edge/label conventions and inspector modes for specialization, subsetting and redefinition.
- Contextual overlays identify inherited and redefined features.
- Select and edit an edge without changing its meaning; synchronize structural + diagram projections via same model.
- Support multiple diagrams sharing one semantic model.

## Validation and tests
- Validate endpoint kind/ownership/context and target resolution; detect invalid inheritance/redefinition and cycles where forbidden.
- Verify import from EA, export to native SysML v2, replay and provenance retention.
- Golden cases: Charger/ProCore/Controller/AdvancedController; subsetting case; invalid redefinition case; similar-but-not-subtype variant.
- Where specific textual serialization is uncertain, verify against SysML v2 reference implementation before claiming compliance.

## Next discussion
Part usages/containment vs references to shared definitions; determine representation for BOM counts, assembly hierarchy and reusable shared parts.
