# Phase 9 — Nested element relationships: parent generalization versus nesting

Read-only audit of reduced October 15 QEAX, 11,447 elements / 14,688 connectors. Among 1,677 same-stereotype generalization candidates: eight unique nested Hardware Component elements. All eight are nested within Hardware Component parents.

New independent incident-connector audit found 17 total connector appearances touching those eight nested endpoints: **8 Generalization connectors from a nested element directly to its lexical parent; 8 other Generalization connectors; 1 Abstraction connector**. These categories count connectors once if either endpoint is nested. No individual source model rows or GUIDs are published.

This is a material ambiguity: lexical nesting and generalization from child to lexical parent coexist and must remain two distinct source semantics. A parent-child Generalization is not automatically a SysML v2 part usage or definition containment. The extra eight generalizations are not presumed invalid. Source intent requires qualified local review. Preserve native emission disabled.

Added `15_Testing/phase9_nested_relationship_context.py`, including source-only aggregate metadata, and `15_Testing/test_phase9_nested_relationship_context.py` synthetic tests for both nested and unnested cases. Two local synthetic tests passed in an isolated container; GitHub CI and Mac tests not yet observed.

Workbench requirements: Structural view must retain separate lexical ownership and specialization edges; visual view shows an explicitly directed subtype-to-supertype link plus nesting independent of composition; navigation must open parent, nested element and all reviewed relationships. Validation must detect coincident owner and supertype, flag for review and preserve cycles/type checks. Round-trip retains original EA connector identities and direction only in local provenance. Binding Port and part-as-port remain separate.

Mac check:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_nested_relationship_context.py
python3 15_Testing/phase9_nested_relationship_context.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Next: review EA source intent for coincident lexical parent and supertype, with private per-element evidence and optional source cleanup recommendation, never automatically rewrite the model.