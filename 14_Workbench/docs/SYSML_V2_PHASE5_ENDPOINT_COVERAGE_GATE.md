# Phase 5 endpoint family coverage gate
Date: 2026-10-17
Status: Aggregate comparison against local Phase 2 endpoint_shape_matrix.csv; NOT an engine execution on source records.

| Bucket | Distinct endpoint shapes | Source connectors |
|---|---:|---:|
| Family recognized by Phase 3 registry | 606 | 12,267 |
| Family absent from Phase 3 registry | 232 | 2,421 |
| Total | 838 | 14,688 |

A recognized family only means at least one candidate rule is present. It does not imply endpoint type, source-direction, role, ownership, evidence, parser, provenance, or native conformance acceptance. The remaining 232 patterns are explicitly `UNKNOWN_FAMILY` until registry expansion. Actual connector-level results require canonical element classification and trusted EA role evidence; no heuristic conversion into legal native types was used here.

## Test execution caveat
Phase 5 synthetic test source was committed, but automated execution of the repository version could not be confirmed from this environment because the raw GitHub content host was unreachable. Therefore tests are **not marked passed**. Run `node --test 14_Workbench/registry/runtime/*.test.mjs` on a checked-out branch or CI and commit machine-generated logs before acceptance.

## Next controls
Full native SysML v2.0 parser/type conformance; verified EA orientation extractor; strict machine-readable evidence JSON Schema; insertion-cycle simulation; 838-pattern local rule diagnostic report; GitHub CI tests; BOM/EA reconciliation; Workbench live read-only menu adapter.
