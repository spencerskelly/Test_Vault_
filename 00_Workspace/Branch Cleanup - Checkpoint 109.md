# Branch Cleanup — Checkpoint 109 (2026-10-14)

## Direct source audit
Inspected `Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html` on PR43 validation branch, especially `renderLocalModel` and `equalsDirectionReviewCsv`.

Source confirms:
- Local Model renderer uses `### Interfaces` / `### Connections`, `####` for Interface and Connection entries, then **`#####` for Flow records nested under a Connection**.
- Connection `endpointA`/`endpointB` fields are Interface block links; nested Flow `endpointA`/`endpointB` fields are textual roles (`transmit`, `receive`, etc.).
- `equals` and `exposes` are written as comma-separated inline wiki-block links.
- Review CSV `owner_note` is chosen from `owner.pathTarget || owner.linkTarget || owner.fileName`, whereas topology index uses relative Markdown note path. Therefore direct string equality can create false failures and needs path normalization grounded in exporter naming.
- Review CSV local IDs are `d.s.localId`, `d.e.localId`, `d.connection.localId`, `d.exposes.localId`; output IDs appear `ep-...` and `conn-...`.

## Defect discovered
The `localmodel_topology_index_v2.py` parser does not stop appending lines when it encounters the nested `#####` Flow heading. It therefore incorporates Flow fields into the preceding Connection and flags duplicated endpointA/endpointB instead of isolating the flow. This would produce a **false validation failure** on valid connections containing flows.

## Regression evidence
Added `66_Testing/consolidation/test_importer_renderer_shape_step109.py`, commit `65bd0d079e46cfe58e75a065d92f8ebd8f3d2dde`. It models the observed renderer shape and is explicitly `@unittest.expectedFailure` until the parser is fixed. This is a source-derived fixture, **not a real QEAX output sample**. It is not a successful acceptance test. No CI or local run verified for this new fixture in this pass.

## Next Step 110
Make v3 topology parser isolate `##### Flow` records, guard owner-path normalization (prefer explicit note resolution over fuzzy suffix matches), change the expectedFailure regression to a passing test once corrected. Then run local tests and CI before real QEAX acceptance.

No main changes, PR merge, branch deletion, or release promotion.
