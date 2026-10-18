# STEP-02E — Real-Source Phase 8 Ledger Verification and Outlier Priorities

**Date:** 2026-10-18  
**Status:** independent real-source **14,688-row** private ledger parity verified. **The exact GitHub-committed `run_gated_v2_approved_phase8.py` has not been executed against the real QEAX in a checked-out copy**; its synthetic CI passed with enhanced source-ID, GUID and endpoint-type tests. Native SysML parser/Workbench/golden-import acceptance are still pending.

[Master MOC](../MOC_MDSE_V2.md) · [STEP-02D](STEP_02D_APPROVED_PHASE8_GATE_AND_SOURCE_REVIEW_2026-10-18.md) · [Exact group decisions](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md) · [Diagram scope lock](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md)

## STEP-02E.1 — Full private row-level independent audit

Read-only local SQLite input `EA_2026_10_15_endgame_mini.qeax`. The independent local verifier wrote a **temporary private 24-column connector ledger** and reread all original connector rows to check primary keys, GUIDs, endpoints, direction, roles, cardinalities, aggregation flags and connector family. Source fingerprint matched before and after. It did not query EA diagram tables, publish source rows, emit SysML, overwrite the QEAX or create a permanent source archive. This is **independent reproducibility evidence**, not verification that an exact source checkout ran the official gated executable.

| Source/evidence gate | Result |
|---|---:|
| Element rows | 11,447 |
| Connector rows written / reread / matched | **14,688 / 14,688 / 14,688** |
| Unique connector IDs and nonempty unique GUIDs | **14,688 each** |
| Missing source endpoint elements | 0 |
| Connector-family or endpoint-family names unmatched | 0 |
| Packages used for folder organization | 1,389 |
| EA diagram tables processed | 0 |
| Native declarations / native certification | 0 / 0 |
| Read-only source integrity/fingerprint | unchanged |
| Temporarily classified evidence-only (NoteLink/Sequence) | 413 |
| Conditionally reviewable native-family connector candidates | 14,275 |

**Important:** `deferred_review` in the current group-stage ledger is a conservative guard meaning row semantics and official syntax have **not** yet been proved. It does **not** mean 14,275 human review actions or 14,275 `flagLink` records are required.

## STEP-02E.2 — Approved group evidence and actionable outliers

The following counts are overlapping **source-evidence categories**, not an additive total.

| Group | Real-source count | Approved rule / next classification |
|---|---:|---|
| Shared aggregation (source flag 1) | **597** | Approved candidate for owned typed usage, independent owner verification required |
| Composite aggregation (source flag 2) | **1,670** | Same ownership and endpoint-type verification; no assumption of native legality from flag alone |
| Source direction not `Source -> Destination` | **433** | 395 Association, 27 NoteLink, 9 Connector, **2 other** |
| Relationship rows touching non-native source elements | **946** | Retain MDSE data/links or `flagLink`; **not automatically 946 unresolved `flagLink`** |
| NoteLink + Sequence reference-only connector rows | **413** | Evidence-only by approved group policy, no EA diagram interpretation |
| Rows touching conditional-use kinds | **49** | Source semantic role or context review |
| Unknown mapped families | **0** | Exact 60+26 family approvals already sufficient |

### OUTLIER-DIR-01 — Reversed allocation involving Trigger and Requirement
One `Abstraction:allocate` has source direction `Destination -> Source`, connecting `Trigger` and `Requirement:requirement`. Under approved native eligibility this is **not** evidence for a legal Part/Action/State allocation. Retain as source-specific review / MDSE `flagLink` candidate with original direction and one explanatory body line; do not invent native allocation. Original connector GUID remains in the *private* row ledger.

### OUTLIER-DIR-02 — Reversed trace from Boundary to Module
One `Dependency:trace` has reversed direction between `Boundary` and `Class:Module`. Boundary is explicitly grouped into one MDSE Boundary note by [STEP-00](STEP_00_APPROVED_MODEL_HANDLING_CLARIFICATIONS_2026-10-18.md). This is **not** a valid native dependency endpoint without additional evidence; maintain the Boundary-to-Module reference in the grouped note or `flagLink`, with source direction and a short reason. No new SysML relationship definition required.

### OUTLIER-AGG-01 — Fifteen aggregation links with non-native endpoints
Among 2,267 aggregations, **12** are `Change → Change` and **3** are `InformationItem → PartDefinition` (two to a hardware component, one to a platform). The existing [aggregation reconciliation](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md) already distinguishes MDSE-only Change hierarchy and the three InformationItem flags. Retain these as descriptive MDSE hierarchy/review, not unjustified native `PartUsage`. Do not reopen the full 2,267-group approval.

### OUTLIER-ENDPOINT-01 — Non-native relationship concentration
The 946 source connectors touching non-native endpoints concentrate in:
- **303 `Dependency:trace`** — many artifacts, InformationItems, Issues and text references. Source links belong in the relevant descriptive MDSE note or attachment-owning engineering note.
- **255 `Abstraction:allocate`** — many Issue, Change, InformationItem-to-Object/Action/Requirement relations. Do not fabricate native allocation to a non-native kind; use a descriptive MDSE link or focused review.
- **220 `NoteLink`** — already evidence-only; not a `flagLink` candidate merely for being NoteLink.
- **69 `ControlFlow`** — often Decision↔Activity; preserve behavior intent and flag missing native context, not every row individually by default.
- **99 across smaller connector families**, including 26 `Dependency:refine`, 21 `Dependency`, 15 `Aggregation`, and others.

Original [flagLink policy](../24_Workbench/docs/GOLDEN_IMPORT_UNRESOLVED_RELATIONSHIP_FLAGLINK_APPROVED_2026-10-17.md) applies **only where the actual semantic link remains unresolved**, with a compact body explanation and private source lineage. A threshold should be set from counted unresolved outcomes **after** group disposition, not from the 946 candidate total.

## STEP-02E.3 — Strengthened committed gating implementation

[Current approved runner](../25_Testing/run_gated_v2_approved_phase8.py) now independently verifies endpoint element types/stereotypes, unique nonempty connector GUIDs, source PK order, all original connector evidence, selected source hash, exactly one row per connector, summary agreement, and private atomic publication. [Expanded synthetic regression](../25_Testing/test_run_gated_v2_approved_phase8.py) covers duplicate GUIDs, orphan endpoints and tampered endpoint typing, plus existing profile drift/tamper/rollback/diagram cases.

**Latest passing CI:** [run 39168257357](https://github.com/spencerskelly/Test_Vault_/actions/runs/39168257357). No real source bytes, GUIDs, or private ledger rows were committed.

## STEP-02E.4 — Acceptance status and handoff

**Done:** exact family coverage, local independent row-level audit, source integrity, group-focused anomaly count, no-diagram guarantee, committed fail-closed gate plus synthetic CI. **Not done:** real QEAX through *exact* committed gated runner, actual Phase 9 trusted role normalization for all conditional candidates, native emitter/parser/Workbench acceptance and golden import.

**Next titled step — STEP-02F: Approved Semantic Outlier Disposition and Verified Real-Source Gate.** In a local checkout with exact GitHub code, run the pinned-source CLI to generate the private ledger; compare its aggregate to these measurements. Then implement group-backed native vs MDSE-link vs `flagLink` evidence decisions, concentrating on OUTLIER-DIR-01/02, OUTLIER-AGG-01, and the 946 non-native endpoint candidates. Do not assign every candidate to human review merely because parser or use-site eligibility is deferred. Native emission remains disabled until explicit acceptance.
