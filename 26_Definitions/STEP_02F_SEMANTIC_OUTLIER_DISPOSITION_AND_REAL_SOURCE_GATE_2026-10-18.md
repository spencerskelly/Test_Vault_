# STEP-02F — Approved Semantic Outlier Disposition and Verified Real-Source Gate

**Date:** 2026-10-18. **Status: TOOL + SYNTHETIC TESTS IMPLEMENTED; independent real QEAX disposition PREVIEW completed. EXACT committed Phase 8 full-source gate remains NOT RUN against this QEAX in a verified local Git checkout.** This is not native SysML certification, Workbench round-trip acceptance, or a golden import.

[STEP-02E handoff](STEP_02E_REAL_SOURCE_LEDGER_PARITY_AND_OUTLIERS_2026-10-18.md) · [Source scope lock](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md) · [Approved aggregate grouping](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md) · [Approved flagLink rules](../24_Workbench/docs/GOLDEN_IMPORT_UNRESOLVED_RELATIONSHIP_FLAGLINK_APPROVED_2026-10-17.md)

## Evidence and checks

A fresh **independent SQLite read-only** classification preview was run on the local \`EA_2026_10_15_endgame_mini.qeax\`. Its source inventory matched STEP-02E: 11,447 elements, 14,688 connectors and 1,389 packages. No EA diagrams were read, generated, or interpreted. No private connector rows/GUIDs/attachment bodies/model content were published.

A post-gate disposition tool and five synthetic fail-closed tests are now tracked in the V2 methods repo:

- [Post-gate private classifier](../25_Testing/v2_step02f_semantic_outlier_disposition.py) — requires the exact Phase 8 **verified** private \`gate.local.json\` and corresponding 24-column ledger, validates identity and row count, writes atomic private full-row classification plus aggregate; rejects staging failures.
- [Synthetic tests](../25_Testing/test_v2_step02f_semantic_outlier_disposition.py) — exclusive categories, duplicate source GUID rejection, unverified gate rejection, count inconsistency rejection, and grouped Boundary trace retention. **5/5 passed locally** with synthetic records. CI wiring/status still requires verification.

**Independent source preview (exclusive partition, NOT a verified output from the committed gated executable):**

| Candidate routing bucket | Rows | Meaning |
|---|---:|---|
| \`native_candidate_unverified\` | 10,867 | Approved family candidates; no parser or use-site certification |
| \`aggregation_group_gate\` | 2,252 | Must reuse 2,267-row approved typed-use/flagLink group reconciliation, excluding 12 Changes and 3 InformationItem flags |
| \`reference_only\` | 413 | 220 NoteLink and 193 Sequence, never native relationships |
| \`connection_evidence_review\` | 397 | Association/Connector connectivity evidence is still required |
| \`mdse_descriptive_link\` | 350 | Non-native trace/dependency/refinement evidence retained on owning notes/attachments |
| \`semantic_role_review\` | 255 | Non-native allocation candidates: choose MDSE descriptive link or flagLink by source role |
| \`workflow_context_review\` | 69 | Preserve Decision/Issue activity-flow context; native succession not yet proven |
| \`conditional_usage_review\` | 41 | Trigger/Synchronization usage/behavior context (49 rows touch conditional kinds across buckets) |
| \`non_native_context_review\` | 24 | Other non-native endpoints require a descriptive-link or explicit unresolved decision |
| \`mdse_hierarchy\` | 12 | Change-to-Change descriptive hierarchy, no PartUsage |
| \`flaglink_candidate\` | 7 | One reversed Trigger→Requirement allocation; three InformationItem aggregation links; three document-endpoint requirement-derivation links |
| \`boundary_reference\` | 1 | Reversed Boundary↔Module trace belongs in aggregated Boundary note |
| **Total** | **14,688** | **Exclusive source coverage, no data dropped** |

**The seven flagLink candidates above are NOT the complete count of unresolved relations.** The 2,252 aggregation gate includes most of the previously identified **56 provisional aggregation flagLinks** (a separate approved aggregate-group review), while 255 non-native allocations, workflow relationships and other conditional candidates still await role evidence. Do not substitute 7, 56, 946, or 14,275 for a final project-wide unresolved count. Not every candidate requires human review. Preserve source connector identity for every eventual YAML \`flagLink\` and write its explanation in the owning note body.

**Direction:** 433 non-explicit directions remain grouped as 395 Associations, 27 NoteLinks, 9 Connectors, plus the two focused outliers. Non-directed Association/NoteLink evidence is not itself a semantic failure. The two exceptional cases do not justify inventing native allocations or dependencies.

## Operator acceptance (required, not yet claimed)

From an **exact verified checkout** of \`Test_Vault_\`, pin the private source fingerprint and use fresh output directories **outside** the repository:

\`\`\`bash
shasum -a 256 "/path/to/EA_2026_10_15_endgame_mini.qeax"
python3 25_Testing/run_gated_v2_approved_phase8.py \
  --qeax "/path/to/EA_2026_10_15_endgame_mini.qeax" \
  --source-sha256 "<LOCAL_SHA256>" \
  --out "/path/outside/Test_Vault_/private_phase8_gate"

python3 25_Testing/v2_step02f_semantic_outlier_disposition.py \
  --gated-dir "/path/outside/Test_Vault_/private_phase8_gate" \
  --out "/path/outside/Test_Vault_/private_step02f" \
  --repo-root "."
\`\`\`

Acceptance requires exact committed code identity; Phase 8 \`verified=true\`, 14,688 source connector rows, all 24 original fields checked, no unmatched families, full SHA attestation, exactly one ledger record per source connector, grouped semantic results compared to the independent counts above, no diagram access and no source/ledger commits. The STEP-02F classifier **refuses to run against an unverified gate**.

## Remaining precise work

1. Execute **the exact committed Phase 8 runner** on the supplied QEAX from a verified checkout, then the committed STEP-02F classifier; compare private outputs and publish **only aggregate** results.
2. Integrate the **existing** 2,267-row aggregation decision with the 2,252-row pending aggregation bucket (1959 PartUsages, 148 ActionUsages, 76 StateUsages, 10 UseCaseUsages, 6 ItemUsages, 12 Change hierarchies, 56 flagLinks). Do not reopen approvals; note that the group mapping is provisional pending native parser acceptance.
3. Reduce 255 non-native allocations and 69 workflow-context cases using approved note ownership and actual source roles; issue distinct \`flagLink\` entries only when genuinely unresolved.
4. Implement YAML + body explanation emission and Workbench navigation/round-trip, followed by official SysML v2 parse and golden-import acceptance.
5. Keep EA diagrams disabled until the toolset tests and golden import are complete. Keep V2 code independent of archived V1 runtime.

**Next step after STEP-02F acceptance:** STEP-02G — bind approved disposition outcomes to native/MDSE output representation with provenance-preserving round-trip tests, still with diagrams excluded.
