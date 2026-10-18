# Pass 05 — SysML v2 semantic rules, first bounded increment

Created `14_Workbench/registry/sysml_v2_semantic_rules.v0.1.json` commit `52534c9` with 17 provisional EA element selectors and 13 relationship families. Every mapping is a **candidate**, not approved parser-backed emission. The registry defaults to `deferred_review`, disables native emission, preserves provenance and requires evidence and parser validation. Explicitly distinguishes proxy-port PortUsage and full-port PartUsage. No custom SysML v2 relationships are invented.

Added `15_Testing/test_sysml_v2_semantic_rules.py` commit `29161db` with five synthetic invariant tests (fail-closed default, unique selectors, port distinction, evidence gates, Workbench/provenance obligations). The exact committed tests still need running from a full checkout. This is not yet a full matrix of all EA endpoint families, nor is the registry wired into the production translator.

Workbench obligations recorded: structural and visual views must distinguish kinds, preserve navigable containment and connections, validate before edits, and retain source provenance and round-trip history. Both note and element identity must remain distinct. There is no automatic rewriting of source text or unsupported transformations.

Open decisions: redefinition semantics, proxy/full/binding port details, nested action/state usages, causal versus temporal constructs, analysis/trade-study representation, and full normative syntax tests. Before activation, reconcile against all 26 existing Phase 8 registry families, resolve mappings against v2 specification and independent parser, and test synthetic examples; missing cases remain explicitly deferred.

Release status: **NO-GO**. Next small pass: complete family coverage by merging the 26 registry families into the candidate ruleset without overwriting approved distinctions, then add consistency tests and actionable semantic-decision ledger. Reply `y` to proceed.
