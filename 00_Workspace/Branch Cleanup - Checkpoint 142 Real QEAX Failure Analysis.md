# Real QEAX IMP-011 Acceptance — First Actual Results (2026-10-14)

## Operator evidence
User executed `66_Testing/consolidation/step120_real_qeax_operator_gate.py` against source `EA_2026_09_06_endgame.qeax` and candidate vault `261002083`. The report at `~/Documents/MDSE_QEAX_Acceptance_Results/qeax_imp011_acceptance.json` returned FAIL. Operator shared stdout excerpts, not the complete machine-readable report.

- SQLite integrity: `ok`.
- Source `BindingConnector` count: **249**, the current expected count.
- `imp011_binding_review_acceptance.py`: exit 2, 500 reported findings; examples include category `unresolved contextual owner/endpoints` and missing `root_cause`. This does not conform to the current controlled classification contract.
- `imp011_canonical_equals_acceptance.py`: exit 2, 483 reported findings; examples include `<!-- MDSE:LOCAL-MODEL START schema=0.2 -->` in the candidate vault, whereas current acceptance expects schema 0.5.
- `imp011_topology_acceptance_v2.py`: exit 1 due to `ModuleNotFoundError: localmodel_topology_index_v3`. This is a local checker dependency and not yet a topology result. The module exists on integration branch at `66_Testing/consolidation/localmodel_topology_index_v3.py`.

## Assessment
The real source QEAX is intact at SQLite level and connector cardinality matches. The generated vault appears to be an older schema, **but exact source-to-output pairing and importer build provenance remain unverified**. Do not rewrite this vault to satisfy latest validators; retain as a historical output snapshot. The missing checker module is fixed by fetching the one file from the validation branch, not by modifying importer semantics.

## Next operator-controlled gate
1. Retrieve the topology index from the integration branch if testing the old vault further.
2. Determine import version/provenance of `261002083`. If old, generate a **new, separate output** with v0.8.19 candidate from the actual source QEAX, without overwriting `261002083` or editing the QEAX. Confirm the controlled generation method and runtime dependencies before executing; do not blindly run synthetic-only harnesses against the 186 MB model.
3. Run Step120 gate on the newly generated output, retain complete JSON report and hashes, then triage actual remaining failures.
4. Keep static CI green, no release/merge/branch deletion until real-model and GUI acceptance is evidenced.

Evidence only; no real-QEAX acceptance, importer correction or GUI signoff is asserted.
