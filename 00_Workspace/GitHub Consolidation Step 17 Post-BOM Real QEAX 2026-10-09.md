# GitHub Consolidation — Step 17: Post-BOM full frozen QEAX acceptance

**Recorded:** 2026-10-09 PDT
**Status:** FULL QEAX MODEL ACCEPTANCE **IN PROGRESS**. Source ancestry, source checks, frozen QEAX integrity and disposable Base Vault preparation PASS. Do not infer a final result until completion.
**Previous:** [[GitHub Consolidation Step 16 BOM Schema Governance Proposals 2026-10-09]]
**Review:** [draft integration PR #17](https://github.com/spencerskelly/Test_Vault_/pull/17)
**Authoritative run:** [GitHub Actions 38012181833](https://github.com/spencerskelly/Test_Vault_/actions/runs/38012181833)

## Frozen sources / exact test scope

- New isolated Test_Vault_ branch: `integration/bom-real-qeax-step17-2026-10-09`, forked from Step 16 schema-proposal branch SHA `bc1ade17f7e153d748ecd13a6d3b1d8655efd3a7`.
- New read-only workflow: `.github/workflows/bom-step17-real-qeax.yml` added at `12d36de03cdeb10fe88cc6cc8c15823abd90e3f5`.
- Actual source lineage asserted in Git: BOM merge `5d34b3898d7c0a56719435c75b2993b876fca3d6`, original Workbench/BOM branch `50e78c6924a1615d865e763ffdb39d1d2f338bad`, WB-129 original `8097f383c41617f879eac8e4ca19fab1d0cb7657`, importer v0.8.19 source `0494354ec40378e119b17c61fdf6e828844035e4`. Non-squashed BOM merge parentage checked.
- Full EA8647 real-QEAX source SHA `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c`; SQLite source record counts **35,969 objects / 21,822 connectors** are mandatory checks.
- Verified schema-proposal-only source and **31/31** original BOM handoff SHA-256 matches before import. Importer reader and Workbench current `WRITABLE_VERSION=0.5` are enforced.
- Three independently initialized disposable runtime Base Vaults prepared in `$RUNNER_TEMP/mdse-real-qeax/` for primary model, deterministic replay, and failure-path injection. All output remains on the runner; no generated model/QAEX source uploaded into GitHub.
- Reuses **exact existing** `66_Testing/real_qeax_execute.sh`, which runs full headless importer v0.8.19, deterministic output comparison, IMP-009/010/011 local topology/exposure/equality and Workbench `accept:real-vault:05` source-safe read/no-op candidate test.
- Runs BOM quantity/UOM 0.6 read-only and `variantOf` focused tests after full import; asserts **generated model, governed active schema, release manifest and writer stay Local Model 0.5/pre-release**, no implicit BOM schema promotion.

## Boundaries and release gates

This tests the **persisted, combined BOM 0.6-reader, WB-129 and importer source**, not the earlier pre-BOM Step 8 integration. A successful headless run validates full model compatibility, not interactive Obsidian UI first-open/edit/restart, controlled `variantOf` or 0.6 schema approval, Bootstrap pin/lock promotion, folder moves, or a production release.

The Step 16 proposal files remain under `99_System/03_Schemas/Proposals/`; active schemas (`local-model.yaml` 0.5 / `relationships.yaml` 1.36 / `element-types.yaml` 1.18) remain unchanged. No default repository branch or original BOM proposal branch is changed.

**To finish record:** fetch the final Actions job conclusion and substantive runtime logs, record deterministic inventory equality, IMP-009/010/011 results, Workbench status/record counts/no-op drift, sourceVaultUnmodified and no BOM writer promotion. If any check fails, document the exact failed gate and do not claim Step 17 pass.
