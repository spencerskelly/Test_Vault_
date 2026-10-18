# V2 Data Retention — Explicit Approval Holds

[Master MOC](../MOC_MDSE_V2.md) · [Source controls](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)

**Status:** Review requested; do not implement destructive cleanup or change approved native SysML semantics. Keep proprietary source evidence private.

## HOLD-01 — EA Copy source records
[Approved Copy and alias consolidation](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-16-ea-copy-alias-consolidation-approved.md) explicitly permits removing redundant notes and discarding source records after clean migration. Native alias semantics are approved and unaffected. Review whether source GUIDs, all original note text/tags, every original connector, redirects, and the complete migration ledger must remain recoverable even after generating one canonical note. **Recommendation: retain in a versioned private evidence archive.**

## HOLD-02 — EA Boundary exclusion
[60-family approved matrix](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) specifies Boundary removed from generated model, though source-ledgered. [Source family execution](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md) recorded 3 excluded-by-policy elements. Review whether source notes, tags, diagram position and identity require a searchable preserved evidence record. Do not conflate "no native SysML node" with permission to discard original observations.

**Pending user approval:** Preserve Copy and excluded Boundary source evidence indefinitely in a private, versioned, recoverable form? No source data should be placed in this public methods repository.

## Additional preservation gates (existing definitions, implementation unverified)

**RISK-03 — Package data:** [Package mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_PACKAGE_APPROVED_2026-10-17.md) uses folder-only output. Preserve GUID, notes/tags, folder history, links and original diagram context in governed metadata; folder placement cannot imply native ownership.

**RISK-04 — Interaction/connection reference:** [Sequence mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_SEQUENCE_REFERENCE_APPROVED_2026-10-17.md) is view-only; [ProxyConnector mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_PROXY_CONNECTOR_APPROVED_2026-10-17.md) is reference-only. Preserve sequence participants/messages/order and connection endpoints/direction/identity even when no extra note or native semantic relationship is created.

**RISK-05 — Source attachment fidelity:** [Step 2 execution](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md) lists 144 attachment-family elements in the reduced source. Reuse [historical full-import attachment checks](../100_Archive/V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md). Track payloads, hashes, source IDs, links and retained references separately.

**RISK-06 — Flagged exceptions:** [flagLink approval](../24_Workbench/docs/GOLDEN_IMPORT_UNRESOLVED_RELATIONSHIP_FLAGLINK_APPROVED_2026-10-17.md) requires per-connector identity, YAML link, and a human-readable reason in the note; local-only disposition ledger alone does not satisfy generated-vault visibility. Permitted untyped usages must also retain review flags.

