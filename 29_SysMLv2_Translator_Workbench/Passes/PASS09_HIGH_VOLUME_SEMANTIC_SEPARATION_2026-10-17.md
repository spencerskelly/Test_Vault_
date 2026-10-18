# Phase 9 — Four-family generalization semantic separation

Read-only aggregate inspection of the October 15 reduced QEAX for generalization connectors involving Hardware Component, Physical Component, Module, Logical Signal. Only reusable tools, synthetic tests and aggregate results are committed.

| Class | Count |
|---|---:|
| Same-stereotype definition candidates | 1677 |
| Cross-stereotype or cross-kind review | 166 |
| Usage or occurrence review | 45 |
| Total in this review slice | 1888 |

Same-stereotype counts: Hardware Component 767, Physical Component 181, Module 150, Logical Signal 579. The grouping provides a *necessary screening category*, not sufficient evidence that any relationship is a legal native specialization. User-owned EA type conventions and definition-versus-occurrence behavior must be checked separately.

**Semantic safeguard:** Object/Part/Action source or target is never silently promoted to a reusable definition by this classifier. Cross-stereotype cases remain review even when both endpoints could eventually map to PartDefinition; explicit subtype semantics must be demonstrated. Generalization does not replace substate or subactivity containment, part ownership, typed usage, binding, or redefinition.

Workbench implementation: structural view stores candidate specialization separate from usage and containment; visual view displays directional specialization in a review state; navigation opens both definitions and original source provenance; validation checks endpoints, direction, cycles, versioned source evidence and declaration/usage semantics; round-trip retains the original EA connector locally. No public source rows or GUIDs.

Added `15_Testing/phase9_high_volume_semantic_separation.py` and six synthetic classification tests. Local aggregate source was inspected, but the newly committed tests have not yet been observed in GitHub CI or on the user's Mac. Next check:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_high_volume_semantic_separation.py
python3 15_Testing/phase9_high_volume_semantic_separation.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

All outcomes stay review-only. `native_certified=0`; native emission disabled.