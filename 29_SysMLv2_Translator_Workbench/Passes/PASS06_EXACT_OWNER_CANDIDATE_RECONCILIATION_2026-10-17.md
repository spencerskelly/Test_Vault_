# Pass 6 — Exact Phase 8 vs expanded typed ownership reconciliation

Date: 2026-10-17. Local-only reduced QEAX `EA_2026_10_15_endgame_mini.qeax`; **14,688 connectors, 2,267 Aggregations**.

## Audited counts

- Broad Phase 8 provisional part-owner endpoint candidates: **1,408**.
- Expanded taxonomy typed owner candidates: **1,195**.
- Exact difference: **213** (all broad-only; none typed-only).
- The 213 difference records are explained by endpoint stereotype scope. No directional or self-link exclusions appeared in this difference for the reduced source.
- **0 native SysML v2 certified**.

An initial independent local reconstruction of Phase 8 showed 1,428 because it mistakenly treated Class `Business Line` and stereotype strings containing `Interface` as part-like. The actual committed Phase 8 `kind()` explicitly excludes both. Reapplying these two conditions reproduced **1,408** and exactly reconciled the **213** difference. This correction supersedes the temporary 1,428 calculation.

Examples of deferred concepts include `Software Component`, `System Partner`, `Physical Context` and unclassified Classes. They must not be swept into part usage. Activities and states remain separate nesting semantic families; proxy/full ports must stay distinguishable. This is a taxonomy coverage discrepancy, not proof that broad-only connectors are invalid.

## Artifacts

- `15_Testing/reconcile_ea_owner_candidates.py`: reproducible aggregate-only comparison; complete record-level identification remains local.
- `15_Testing/test_reconcile_ea_owner_candidates.py`: six synthetic regression tests. The exact committed suite has **not been executed from a full checkout**.
- No source IDs, GUIDs, model rows or detailed ledger are committed.

## Required next gates

Execute the exact committed suites and re-run the committed comparison tool from checkout. Review semantics for the 213 deferred candidate cases by stereotype with explicit Workbench structural, visual, navigation, validation and round-trip obligations. Keep native emission disabled pending approved registry and parser validation.
