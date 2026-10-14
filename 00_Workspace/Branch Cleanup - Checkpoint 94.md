# Branch Cleanup — Checkpoint 94 (2026-10-14)

## Scope
Static inspection of importer v0.8.19 acceptance tools on `integration/p03-legacy-compat-tests-20261013` against the ten Step93 scenarios. **No real QEAX execution performed in this pass.**

## Existing tests identified
- `Importer/Testing/v0.8.19/imp009_output_acceptance.py`: whole-model transaction/version/source-map sanity, confirms acceptance remains pending.
- `Importer/Testing/v0.8.19/imp010_interface_flow_acceptance.py`: real-source FlowProperty carriers and source-local ledger comparison; expects 760 FlowProperties and 752 Class-owned.
- `Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py`: demands 249 original BindingConnector GUIDs, expected 23 Connection.exposes, 209 Interface.equals and 17 unresolved cross-owner rows.
- `Importer/Testing/v0.8.19/imp011_canonical_equals_acceptance.py`: expected 418 directed / 209 undirected equals links, symmetric and no self links, compared with review and source GUIDs.
- `66_Testing/consolidation/STEP82_IMPORTER_WORKBENCH_CI_GATE.md`: earlier CI missed compatibility checker; a subsequent PR43 validation workflow was added but actual successful execution is not established by this file.

## Test-case gap register
| Step93 scenario | Status by source inspection | Gap to close |
|---|---|---|
| 1 Class-owned | Partial | owner/Interface block reference and source-GUID assertion |
| 2 Part-owned | Partial | contextual part reference and same-owner check |
| 3 Typed/untyped | Partial | negative case: definitionless Interface cannot persist usage |
| 4 Ordinary Connector | Partial | exact Connection endpoint ownership, ambiguity/rejection fixture |
| 5 Binding exposure | Targeted test present | run real source + ambiguous-multi-connection negative |
| 6 Binding equals | Targeted test present | run; cross-owner and transitive-closure negative fixtures |
| 7 InformationFlow | Targeted test present | single carrier and endpoint role direction checks |
| 8 Invalid references | Not proved | fail-closed malformed IDs, wrong owners, dangling links |
| 9 Versions 0.1–0.4 | Static contract only established here | byte-identical nonmutating read then explicit upgrade test |
| 10 Provenance/rerun | Partial | second import preserves EA GUID->local ID and prevents duplicate records |

## Consolidation blocker classification
**Hard gates:** schema migration integrity, no lost/dangling references, source map stability, correctly classified BindingConnector/flow topology, and importer/Workbench version compatibility. These require actual passing evidence before merging governed runtime changes.

**Separate release gates:** macOS/Windows Obsidian GUI, real QEAX whole-model acceptance, compiled plugin provenance, release governance approval. Do not equate static/source tests to those gates.

**Nonblocking for preservation-only consolidation:** creating new test infrastructure or writing additional narrative docs, provided the existing source, manifests and historical evidence remain intact. Do not delete original branches or merge runtime based on this exception.

## Next Step 95
Inspect workflow wiring and current run results for existing IMP-009/010/011 and importer/Workbench static checker; distinguish source-only, synthetic CI, and actual QEAX acceptance. Implement the smallest missing fail-closed synthetic regression first on a validation branch. No main writes, releases, branch cleanup, or PR merge.
