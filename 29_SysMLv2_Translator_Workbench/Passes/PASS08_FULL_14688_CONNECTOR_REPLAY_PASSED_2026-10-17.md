# Phase 8 — Full reduced-QEAX normalization replay accepted

Date: 2026-10-17. Evidence: operator Mac terminal output; no raw QEAX, ledger or GUIDs committed.

Source: reduced October 15 QEAX. Operator generated a fresh local Phase 8 ledger with the checked-in v0.2 family registry and replayed every connector using `replay_phase8_local_normalization.py`.

| Acceptance check | Observed |
|---|---:|
| Source connectors | 14688 |
| Ledger connectors | 14688 |
| Replay valid | true |
| Replay error counts | 0 |
| Native certified | 0 |

Disposition totals: deferred_review=6378; orientation_normalized=3601; owner_endpoint_identified=1408; family_candidate=429; role_normalized=2872. These sum to 14688.

Diagnostic occurrences (not unique connectors): DIRECTION_NOT_EXPLICIT=433; UNKNOWN_FAMILY=1524; UNRESOLVED_ENDPOINT_KIND=1418; SPECIALIZATION_REQUIRES_REVIEW=134; NATIVE_PARSER_AND_EVIDENCE_PENDING=8310; REGISTRY_REVIEW_OR_EVIDENCE_ONLY=1915; NON_PART_AGGREGATION=330; SHARED_NOT_COMPOSITE=597; ALLOCATION_ROLE_REVIEW=587; SATISFY_DIRECTION_REVIEW=1330; REALISATION_ROLE_REVIEW=29.

This passes **normalizer-to-ledger consistency**. It is not independent validation of trusted EA/Sparx connector direction, generalization roles, aggregation ownership, or SysML v2 syntax/semantic translation. Follow-up priority: an independent semantic oracle with synthetic and local-only real evidence checks; preserve part/port/binding distinctions, Workbench visual/structural/nav/provenance rules. No native emitter authorization.

Local evidence remains under Documents/MDSE_Local_Phase8, not inside Test_Vault_. No source records published.