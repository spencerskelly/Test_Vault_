# Pass 6 — Expanded EA stereotype ownership audit

Date: 2026-10-17. Status: **candidate classification only, not native translation approval**.

The new versioned source taxonomy `14_Workbench/registry/ea_source_stereotypes.v0.1.json` (commit `82c376b`) includes explicit candidate kinds for Class stereotypes `block`, `Hardware Component`, `Module`, `Physical Component` and `Physical System Variant`. Unknown classes remain deferred. Activity, State, Port and Interface are deliberately distinct and cannot be swept into part ownership. Workbench obligations are recorded for structural and visual display, navigation, validation and provenance.

`15_Testing/audit_ea_stereotype_ownership.py` (commit `55fabaa`) reads the taxonomy and classifies each EA Aggregation without accepting native SysML v2. Four synthetic tests `15_Testing/test_audit_ea_stereotype_ownership.py` (commit `2cb39f1`) were added; they have not been executed from the exact full checkout.

## Local real-QEAX aggregate reconciliation

Ran locally against `EA_2026_10_15_endgame_mini.qeax` using matching independent classification rules with SQLite read-only:

- Total EA Aggregations: **2,267**
- Expanded part ownership candidates: **1,195**
- Unclassified endpoints: **707**
- Behavior nesting review: **230**
- Shared/ambiguous ownership: **135**
- Native certified: **0**

This is **1,041 more candidates** than the former strict classifier (154) and **213 fewer** than the original Phase 8 provisional `owner_endpoint_identified` count (1,408). Both semantic taxonomy differences and direction/role handling may contribute; no per-row equivalence has been established. These numbers are aggregate observations, not approvals.

## Required follow-up

Reconcile the remaining 213 candidate difference by direction, typed endpoint combinations and source aggregation flags in a **local-only** comparison; decide which classifications are normatively legitimate before broadening eligibility. Ensure port/interface and state/action structures are translated to their own proper usage semantics. Run exact committed Python tests and the audit from a complete checkout. Do not import private row-level data into Test_Vault_.
