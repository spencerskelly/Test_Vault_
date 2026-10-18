# V2 Data Retention — Historical Review, Superseded

[Master MOC](../MOC_MDSE_V2.md) · [Source controls](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)

**CURRENT STATUS: SUPERSEDED.** The user resolved these holds on October 18 in [STEP-00 approved model-handling clarifications](STEP_00_APPROVED_MODEL_HANDLING_CLARIFICATIONS_2026-10-18.md). The sections below are historical proposals, **not active requests to maintain duplicate source archives**. Aliased content/relationships merge into one canonical note; Boundary elements become one indexed MDSE Boundary note; packages map to folders; original source remains available externally. New generated artifacts preserve meaningful data and explanatory review links.

## HOLD-01 — EA Copy source records
[Approved Copy and alias consolidation](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-16-ea-copy-alias-consolidation-approved.md) explicitly permits removing redundant notes and discarding source records after clean migration. Native alias semantics are approved and unaffected. Review whether source GUIDs, all original note text/tags, every original connector, redirects, and the complete migration ledger must remain recoverable even after generating one canonical note. **Recommendation: retain in a versioned private evidence archive.**

## HOLD-02 — EA Boundary exclusion
[60-family approved matrix](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) specifies Boundary removed from generated model, though source-ledgered. [Source family execution](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md) recorded 3 excluded-by-policy elements. Review whether source notes, tags, diagram position and identity require a searchable preserved evidence record. Do not conflate "no native SysML node" with permission to discard original observations.

**Resolved:** No second archival source copy is required. Current handling is defined in STEP-00. Source records are available from the user's underlying source systems for future updates.

## Additional preservation gates (existing definitions, implementation unverified)

**RISK-03 — Package data:** [Package mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_PACKAGE_APPROVED_2026-10-17.md) uses folder-only output. Preserve GUID, notes/tags, folder history, links and original diagram context in governed metadata; folder placement cannot imply native ownership.

**RISK-04 — Interaction/connection reference:** [Sequence mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_SEQUENCE_REFERENCE_APPROVED_2026-10-17.md) is view-only; [ProxyConnector mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_PROXY_CONNECTOR_APPROVED_2026-10-17.md) is reference-only. Preserve sequence participants/messages/order and connection endpoints/direction/identity even when no extra note or native semantic relationship is created.

**RISK-05 — Source attachment fidelity:** [Step 2 execution](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md) lists 144 attachment-family elements in the reduced source. Reuse [historical full-import attachment checks](../100_Archive/V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md). Track payloads, hashes, source IDs, links and retained references separately.

**RISK-06 — Flagged exceptions:** [flagLink approval](../24_Workbench/docs/GOLDEN_IMPORT_UNRESOLVED_RELATIONSHIP_FLAGLINK_APPROVED_2026-10-17.md) requires per-connector identity, YAML link, and a human-readable reason in the note; local-only disposition ledger alone does not satisfy generated-vault visibility. Permitted untyped usages must also retain review flags.


**RISK-07 — BOM raw values:** [Historical BOM reader](../29_SysMLv2_Translator_Workbench/Passes/PASS06_BOM_XLSX_ADAPTER_2026-10-17.md) rejects formulas and skips wholly empty rows. Preserve rejected-row source position/value and never round decimals, infer units, or silently omit meaningful formulas, revisions or effectivity.

**RISK-08 — Competing formal edit authority:** [Earlier build-readiness narrative](../24_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md) includes graph-as-authority wording. [Later approved release decisions](V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md) supersede it: SysML v2 text in the note owns formal semantics, and graphical edits must transactionally reparse and update the text. Derived graph overwrite must be forbidden.

## Zero-silent-loss acceptance

The private importer must reconcile each source record exactly once into `native`, `alias_merged`, `evidence_only`, `deferred_review`, `excluded_by_policy`, or `error`, each with stable source ID and explicit rationale. Valid source metadata must not disappear merely because there is no native SysML counterpart. Treat unrecoverable omission, non-authorized deletion, silent deduplication, failed note link resolution and conflicting edit overwrite as export blockers.

Further engineering review is required for the source-to-generated-vault preservation of each risk. No direct model data is committed to the public methods repository.
