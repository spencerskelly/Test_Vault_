# Branch Cleanup — Checkpoint 96: BindingConnector negative-test gap (2026-10-14)

## Reviewed existing validation source
At PR43 validation branch `integration/p03-legacy-compat-tests-20261013`:
- `Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py` (blob `e835c01ba10e0010a118e5d231836f95348733a6`)
- `Importer/Testing/v0.8.19/imp011_canonical_equals_acceptance.py` (blob `d9a92d1469c2456d75fb2673b8f31552f3b53dc5`)

These scripts validate source/review GUID identity, expected 249 BindingConnector classifications, 23 exposures, 209 equality bindings, 17 unresolved cross-owner cases; canonical-equals validator checks 418 directed links, 209 undirected links, no self-edges and symmetry. **None of that is a freshly executed real-QEAX acceptance result.**

## Specific fail-closed gaps confirmed by source inspection
1. `imp011_binding_review_acceptance.py`: exposure case requires candidate_connection_count==1, but does **not independently validate** the actual connection's two endpoints, owner-note equality, or boundary-interface role. A fabricated CSV can pass shape-only assertions if counts otherwise match.
2. Canonical-equals acceptance checks symmetric pairs and matches classified CSV rows, but does **not independently assert every pair's endpoints share the same owner**. The parser builds endpoint_owner, yet no ownership requirement appears in the assertions.
3. No dedicated mutation/negative fixture was identified among these inspected scripts that intentionally injects an ambiguous multi-connection BindingConnector and proves no `Connection.exposes` is written.
4. Current expected-category totals alone cannot detect a swapped disposition if compensating swaps preserve aggregate counts.

## Small implementation sequence on non-release validation branch
A. Extract or add one pure `validate_binding_disposition(row, endpoint_owner, connection_endpoints)` routine used by the acceptance validator. Require: for `Connection.exposes`, exactly one candidate Connection, same Local Model owner, valid internal endpoint and assembly-boundary endpoint; for `Interface.equals`, explicit source binding, two same-owner endpoints, symmetric persisted edge, and no duplicate exposure; for unresolved cross-owner, no persisted equality/exposure.
B. Add table-driven negative fixtures: 0/2 candidate Connections wrongly marked exposure; boundary endpoint on wrong owner; equals across owners; missing endpoint; exposure simultaneously stored as equals; duplicate GUIDs; two rows with deliberately swapped relation/category to defeat count-only checking.
C. Run new synthetic unittest in source-only CI, then real QEAX IMP-011/011B on authorized generated vault and record exact run SHA and result.
D. Preserve original source/review artifacts and release hold.

## State
This checkpoint identifies concrete missing invariants; **no importer code was modified or test executed here**. Continue with minimal synthetic harness and checker update in Step97. No main updates, merges, deletion, or release promotion.
