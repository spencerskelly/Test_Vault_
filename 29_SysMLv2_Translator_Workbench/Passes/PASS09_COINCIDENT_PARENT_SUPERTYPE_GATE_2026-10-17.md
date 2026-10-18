# Phase 9 — Coincident lexical parent and supertype gate

Read-only local run against the reduced QEAX found 8 distinct nested Hardware Component elements and 8 with an explicitly directed Generalization from the nested element to its lexical parent. Zero reversed/ambiguous direction within these eight. All eight remain review-only; no native certification.

Added an aggregate-only source audit and eight synthetic tests, locally passing before check-in. Native emission remains disabled.

**Semantic rule:** Preserve lexical nesting separately from definition specialization. Coincident parent and supertype is neither automatically valid specialization nor proof of composition/part usage. No QEAX rewrite.

**Workbench:** Structural view must retain independent owner and specialization edges; visual view shows directed specialization and containment independently; navigation opens parent and child plus local source evidence. Validate cycles, direction, kind, use-vs-definition intent and source provenance. Round-trip retains original EA source metadata privately. No custom SysML v2 relationship or Binding Port collapse.

Run locally from repo:
```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_coincident_parent_specialization.py
python3 15_Testing/phase9_coincident_parent_specialization.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```
No model data or source identifiers are committed.
