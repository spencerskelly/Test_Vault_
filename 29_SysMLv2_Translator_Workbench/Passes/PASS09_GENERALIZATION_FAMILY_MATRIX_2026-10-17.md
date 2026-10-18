# Phase 9 — Expanded generalization definition family audit

The first strict Phase 9 audit found 8 block-to-block candidates and 3,593 Phase 8 orientation candidates outside that strict policy. These are a coverage difference, not proven errors.

Added `15_Testing/phase9_generalization_family_matrix.py` with independent, conservative classification for Part, Action, State, Requirement, and Item definition families. Mixed definition types, unstereotyped EA classes, usages, ports and ambiguous directions are deferred. This module does not import the Phase 8 normalizer. Eleven synthetic classification tests added; tests have not yet been confirmed running in CI.

Important: classification of EA Activity/State/Requirement/Signal types as potential SysML v2 definitions is **provisional**, not certified EA semantic mapping; the family candidate category must never enable emission. Port usage is expressly excluded until port definition versus usage semantics are established. Redefinition, typing and containment are not generalization. Cross-kind specialization requires separate source evidence and review.

Local aggregate-only command from Test_Vault_:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_generalization_family_matrix.py
python3 15_Testing/phase9_generalization_family_matrix.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Workbench contract: structural hierarchy shows subtype-of separate from usage containment; visual arrow is subtype to supertype; navigate both definitions; errors remain visibly review-only; retain EA source direction and connector provenance for roundtrip. No Workbench renderer implementation yet.

Never publish source rows or GUIDs. Native emission disabled.