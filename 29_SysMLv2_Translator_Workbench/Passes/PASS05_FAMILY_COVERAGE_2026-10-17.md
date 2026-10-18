# Pass 5 continuation — full relationship family coverage

Date: 2026-10-17. Status: **coverage implemented; semantics not certified**.

The previous candidate semantic ruleset contained 13 relationship family keys. The existing Phase 8 registry contained 26. New immutable candidate file `14_Workbench/registry/sysml_v2_semantic_rules.v0.2.json` covers exactly **26/26** existing Phase 8 families. The 13 previously absent families were carried forward as explicitly deferred, with existing registry disposition and rule IDs retained. Existing candidate targets were preserved, not overwritten.

The new registry records **11 source candidate differences** between v2 names and the older registry candidate field. Several simply reflect an older `null` native candidate or different labels, so **11 is not an assertion of 11 semantic contradictions**. All 26 require evidence and independent parser validation before native emission. In particular, `NoteLink:` and `Connector:` remain evidence-only and no new custom v2 relationship is introduced.

Commit `2cbfbc67172a492a5f526d18e8f14db0e7d59ece`: complete v0.2 JSON. Commit `23a7c788f3cb8ddc378239b6f733f2bfea4a2812`: four synthetic cross-registry tests, covering exact families and unique keys, retention of source dispositions and rule IDs, global fail-closed emission, and distinct proxy/full port mapping. Tests are **committed, but not executed against a full checkout**.

Important limitation: `v0.2` is a **candidate vocabulary and coverage manifest**, not a checked native SysML v2 compiler mapping. The existing Phase 8 Python engine remains on its previous registry until explicitly integrated and tested. Native certified count remains **zero**. No source model records were committed.

## Next short pass

Reconcile 11 candidate-label differences against documented approvals, preserve exceptions in a machine-readable decision register, add source-rule hashes/pins and deterministic registry validation. Only then prepare an emitter consuming this registry; never switch on native emission before independent parse validation. Retain unresolved first-run checkout/CI/base-vault blockers. Require user `y` to proceed.
