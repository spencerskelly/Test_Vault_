# Phase 9 — Nested Hardware Component extended-stereotype evidence

Read-only local review of reduced October 15 QEAX: 8 unique nested endpoints (16 connector endpoint appearances) among 1,677 same-stereotype generalization candidates. All eight distinct nested endpoints contain exactly one extended stereotype record with Name `Hardware Component` and FQName `Webasto MBDV Profile::Hardware Component`. All eight parent elements are `Class` / `Hardware Component`. No profile mismatches observed.

This validates EA metadata **consistency**, not SysML v2 declaration intent. A consistent source profile is not evidence that the nested element is a reusable definition rather than usage. Do not emit native specialization, manufacture part containment, or remove lexical nesting on this evidence alone.

Added `15_Testing/phase9_nested_profile_consistency.py` and four synthetic tests. Run locally:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_nested_profile_consistency.py
python3 15_Testing/phase9_nested_profile_consistency.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Follow-up: review the eight distinct nested declarations in local-only evidence for EA structural relationship patterns, provenance and definition-versus-usage intent. Workbench must preserve lexical nesting, subtype links, per-endpoint navigation, validation and round-trip source evidence independently. Native emission disabled; no private model rows committed.