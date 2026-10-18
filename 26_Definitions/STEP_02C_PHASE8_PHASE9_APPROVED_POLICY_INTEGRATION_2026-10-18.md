# STEP-02C — Integrate Approved Mapping into Existing Phase 8/9

Status: implementation and synthetic CI verified on 2026-10-18. Not a native parser or golden-import acceptance.

[Master MOC](../MOC_MDSE_V2.md) · [STEP-02B resolver](STEP_02B_APPROVED_FAMILY_RESOLVER_AND_LOCAL_GROUP_CHECK_2026-10-18.md) · [Diagram deferral](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md)

## What was implemented
- [Phase 8 read-only normalizer](../24_Workbench/registry/runtime/normalize_qeax_phase8.py) now recognizes the exact, versioned [60+26 approved family registry](../24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json). It uses the existing row evidence, CSV ledger and atomic staging. The old candidates remain historical fixture support, not current policy.
- [Phase 9 source-direction bridge](../25_Testing/phase9_source_direction_bridge.py) recognizes approved-policy review rows. It validates raw source rows and refuses to treat unresolved orientation as certified specialization.
- [Synthetic integration regression](../25_Testing/test_v2_approved_phase8_phase9_integration.py) covers shared aggregation, descriptive InformationItem, Object as PartDefinition, exact Realisation:deriveReqt, NoteLink, Sequence, unmatched types, raw roles/cards, atomic output, and diagram independence.
- [CI workflow](../.github/workflows/v2-migration-executable-repair.yml) passed the new test in [run 39166307354](https://github.com/spencerskelly/Test_Vault_/actions/runs/39166307354).

## Critical safety boundary
The approved policy reports one source connector row per ledger row with GUID/PK, original endpoints, direction, source/target stereotypes, role strings, cardinalities and aggregation flags. It preserves an explicit review status and all relevant evidence. Shared aggregation is not rejected merely for being shared; independent ownership and native type validity still need review. InformationItem no longer becomes ItemDefinition. Sequence from source diagrams is excluded. Unknown family rows are reported, never silently matched to wildcard rules.

The native-emission and native-certification flags remain false. Successful family matching never implies approved native syntax or correct semantics for an individual connector.

The historical Phase 8 candidate registry and provisional Phase 9 endpoint matrix remain unchanged for reproducibility. The approved path branches on registry schema, so prior fixture tests remain supported. **The old run_gated_phase8.py orchestration still depends on a legacy profiler and old ledger schema and must not be treated as the golden-import entry point.**

## Next: STEP-02D — Gated Approved Normalization and Real-Source Outlier Measurement
1. Wire the diagram-free QEAX preflight and approved resolver into the single gated, atomic Phase 8 runner; retire reliance on missing legacy profiler modules for current usage.
2. Validate every private ledger row and its source checksum/counts before publication, preserving source evidence without copying a permanent source archive.
3. Run the actual reduced QEAX with row-level aggregate diagnostic counts, no exported private model rows or EA diagrams.
4. Reuse Phase 9 direction/ownership tests for exact semantic exception groups; keep native parser and note-writer acceptance separate.
5. Present only outlier rules and quantified review backlogs, not a new family-definition review.
