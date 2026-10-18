# Pass 8 — Reduced QEAX read-only integrity audit (2026-10-17 Pacific)

Audited the locally provided reduced `EA_2026_10_15_endgame_mini.qeax` SQLite model; did not copy or commit source rows, GUIDs or ledgers.

| Metric | Count |
|---|---:|
| t_object elements | 11447 |
| t_connector rows | 14688 |
| t_package rows | 1389 |
| missing connector GUIDs | 0 |
| duplicate connector integer IDs | 0 |
| duplicate connector GUIDs | 0 |
| unresolved source endpoints | 0 |
| unresolved destination endpoints | 0 |

Connector-family aggregate relevant to native connection review: `Connector` 9; `Association` 395; `Aggregation` 2267; `Generalization` 3735. EA direction values: `Source -> Destination` 14255; `Unspecified` 404; NULL 25; `Destination -> Source` 2; empty string 2. These direction values are raw source metadata, not semantic authorization.

**Key blocker:** `phase8-ledger-connection-gate.mjs` presently requires source family `Connector` or `Association`, reviewed owner role and permitted normalization status; the existing Phase 8 `decide()` function does not infer `explicit-connection-owner` from source and does not establish a trusted `connection_owner_id`. Hence there is no supported path to real eligible native connections based merely on the aggregate counts. Do not manufacture the missing owner role or set a caller-supplied verified flag.

This audit verifies source database schema-level identities/endpoints only. The local ledger itself was not available in this runtime and full 14688-row ledger-to-QEAX comparison was **not** executed here. Next pass must run the local verifier against an actual fresh ledger, independently verify `normalized_from`, `normalized_to`, `role`, `status`, and model-reconciled source direction, and explicitly document unresolved source semantics.

Keep all model data private/local. Native emission stays disabled.