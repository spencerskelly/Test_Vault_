# Phase 9 — Fail-closed source generalization handoff (aggregate only)

Added `15_Testing/phase9_source_generalization_handoff.py`. Before producing source-derived generalization review categories it reruns the existing Phase 8 full local ledger replay and requires a valid complete coverage result. A failed replay returns review ineligible; successful replay allows only aggregated **review candidates**. Its output never includes source identities or rows, and `native_certified=0`, `semantic_authorization=false` remain fixed.

Three synthetic tests cover replay failure, record-count mismatch, and passing replay that still cannot certify native semantics. The tests are committed, but have not yet been executed in the operator Mac or observed GitHub Actions.

**Trust limitations:** This is not a cryptographically independent proof of source provenance. It reuses the Phase 8 replay implementation and does not independently validate approved SysML v2 semantics. It also does not yet project per-connector data into the JS canonical graph; this deliberately stops short of that unsafe leap. A trusted local issuer, immutable source/registry/ledger hashes, native semantics, and a narrow per-connector adapter must be developed and verified before permitting actual canonical mutations.

Workbench requirements: retain lexical owner vs specialization distinction in both structural and visual views, no invented part usages, navigate source and target definitions, show review reason and preserve private round-trip connector provenance; keep Binding Port separate. No native emitter enabled.

Operator commands (source ledger stays outside GitHub):

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_generalization_handoff.py
python3 15_Testing/phase9_source_generalization_handoff.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv" --registry 14_Workbench/registry/family_disposition_registry.v0.2.json
```

Do not equate eligibility for aggregate review with native translation authorization.