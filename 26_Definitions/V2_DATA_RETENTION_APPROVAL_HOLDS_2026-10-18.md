# V2 Data Retention — Explicit Approval Holds

[Master MOC](../MOC_MDSE_V2.md) · [Source controls](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)

**Status:** Review requested; do not implement destructive cleanup or change approved native SysML semantics. Keep proprietary source evidence private.

## HOLD-01 — EA Copy source records
[Approved Copy and alias consolidation](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-16-ea-copy-alias-consolidation-approved.md) explicitly permits removing redundant notes and discarding source records after clean migration. Native alias semantics are approved and unaffected. Review whether source GUIDs, all original note text/tags, every original connector, redirects, and the complete migration ledger must remain recoverable even after generating one canonical note. **Recommendation: retain in a versioned private evidence archive.**

## HOLD-02 — EA Boundary exclusion
[60-family approved matrix](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) specifies Boundary removed from generated model, though source-ledgered. [Source family execution](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md) recorded 3 excluded-by-policy elements. Review whether source notes, tags, diagram position and identity require a searchable preserved evidence record. Do not conflate "no native SysML node" with permission to discard original observations.

**Pending user approval:** Preserve Copy and excluded Boundary source evidence indefinitely in a private, versioned, recoverable form? No source data should be placed in this public methods repository.
