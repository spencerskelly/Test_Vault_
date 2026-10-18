# Phase 9 — Four high-volume EA stereotype mappings, review-only

Extended the independently implemented generalization family matrix to recognize `(Class, Hardware Component)`, `(Class, Physical Component)`, `(Class, Module)` as provisional PartDefinition patterns, and `(Signal, Logical Signal)` as provisional ItemDefinition patterns. **Each returns `STEREOTYPE_MAPPING_REVIEW` rather than `SAME_DEFINITION_FAMILY_CANDIDATE`**. No native translation authorized.

Eight synthetic tests include the four positive review categories plus mixed-family, ambiguous direction, usage type and unmapped stereotype negatives. Tests committed, but execution not yet observed.

Workbench: structural graph displays proposed subtype-to-supertype separately from part containment and typing; visual graph uses review-only specialization edge styling; both endpoints navigate to definitions; validation must verify source stereotype semantics, connector direction, cycles, provenance; round-trip must preserve local EA connector source/target and decision version without source rows in GitHub. Binding Port and port-as-part distinctions remain intact.

Local commands:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_generalization_family_matrix.py 15_Testing/test_phase9_high_volume_stereotype_reviews.py
python3 15_Testing/phase9_generalization_family_matrix.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

The expected larger review classification changes the previously observed 3,531 ENDPOINT_KIND_REVIEW count; preserve both prior and new baselines. Next approve genuine definitions vs usages only after examining independent source conventions. No local private ledger or QEAX committed. Native emission disabled.