# Branch Cleanup — Checkpoint 95: Verified CI evidence (2026-10-14)

Read-only GitHub Actions inspection for PR43 validation head. No merges, branch deletion, release or QEAX/GUI acceptance implied.

## Actual completed runs

- [Run 38614565590](https://github.com/spencerskelly/Test_Vault_/actions/runs/38614565590): importer-workbench-contract job 116026213229 **success**. Its source-only compatibility step "Block incompatible importer and Workbench Local Model source" succeeded.
- [Run 38613661950](https://github.com/spencerskelly/Test_Vault_/actions/runs/38613661950): all **eight jobs success**, including importer-static-contract 116023186747; importer-and-governance-smoke 116023186613; workbench-source-build 116023186867; plus five other governance/base/synthetic jobs.
- PR #43 remains open on head `integration/p03-legacy-compat-tests-20261013`, SHA `ea176532dd738765c8fdbf89c34fb59f330a2b82`.

## Evidence interpretation
- Workbench npm test and build CI **passed**, with no artifact publication.
- Importer v0.8.14–v0.8.18 static regressions, v0.8.19 compile-only checks and selected IMP009/010 self-tests **passed**.
- Source-profile and importer/Workbench Local Model compatibility **passed**.
- The step labeled "IMP-009 through IMP-011 validators" invokes self-tests and Python compilation; it **does not** execute `imp010_interface_flow_acceptance.py`, `imp011_binding_review_acceptance.py`, or `imp011_canonical_equals_acceptance.py` against an actual QEAX-generated vault.
- Therefore expected 249 BindingConnectors (23 exposes / 209 equals / 17 unresolved), 760 FlowProperties and 752 Class-owned cases remain **asserted expectations, not newly verified output**.

## Gate ledger
| Gate | Outcome |
|---|---|
| Static importer–Workbench contract | PASS (run 38614565590) |
| Source Workbench tests/build | PASS (run 38613661950) |
| Selected importer synthetic tests/compile | PASS (same run) |
| Actual QEAX run + IMP010/011 assertions | NOT PROVEN |
| Source-to-target rerun identity / 0.1–0.4 byte-identical read | NOT PROVEN |
| macOS and Windows Obsidian GUI | NOT PROVEN |
| Release approval and governed artifact provenance | NOT PROVEN |
| Full branch consolidation and deletion | HOLD |

Next Step 96: inspect full importer test invocation coverage and select a runnable fail-closed synthetic test for ambiguous BindingConnector mapping or legacy nonmutating reads. Keep separate execution evidence for real QEAX and GUI gates.
