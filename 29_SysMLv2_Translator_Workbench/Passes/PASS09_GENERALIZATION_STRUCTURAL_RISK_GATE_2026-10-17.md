# Phase 9 — Structural risk gate for provisional same-stereotype generalizations

Added independent read-only structural screening for the previously identified 1,677 same-stereotype generalization candidates. It checks source direction, self-generalization, explicit connector stereotype and presence of cycles in the candidate graph. Aggregate counts only; no source rows, names, GUIDs or IDs reported.

This pass **does not** establish definition-vs-usage intent. Even structurally clean candidates remain `remaining_semantic_evidence_required`. This is a screening gate, not native approval; `native_certified=0` always. The cycle detector provides a conservative graph-level flag, not per-edge conformance proof. Directed graph cycles or anomalous links require review, not automatic deletion.

Nine synthetic tests added; neither local Mac execution nor CI result has yet been observed. Run:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_generalization_structural_risk_screen.py
python3 15_Testing/phase9_generalization_structural_risk_screen.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Workbench: preserve candidate specialization separate from containment, typed usage and redefinition in structural and visual views; show flagged cycles/direction anomalies, navigate to both endpoints and source evidence locally, preserve EA provenance for round-trip. Real definition identification requires approved EA stereotype mapping and independent semantic evidence. Native emission disabled.