# GitHub Consolidation — Step 17: Post-BOM full frozen QEAX acceptance

**Recorded:** 2026-10-09 PDT
**Status:** **PASS — actual persisted BOM+WB-129+importer full frozen QEAX determinism, topology and Workbench 0.5 real-vault acceptance completed successfully.** Candidate-only; manual Obsidian/release approval remains pending.
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

## Final GitHub Actions verdict — independently checked

[Run 38012181833](https://github.com/spencerskelly/Test_Vault_/actions/runs/38012181833), job `114094414009`, **completed / success**. All steps passed. The full real-QEAX import was carried out against the *actual persisted Step 16 BOM source*, with no new source merges or generated-model commits.

**Source + deterministic output:** Frozen QEAX SHA-256 verified, **35,969 objects**, **21,822 connectors**. Both fresh model imports produced **28,273 nonvolatile files**; comparison: `onlyA=0`, `onlyB=0`, `changed=0`, `DETERMINISM PASS`. The headless importer transaction recorded `IMPORT_COMPLETE` and `WRITE_PASS`; the injected failure-path case was exercised in the shared headless importer script.

**Importer topology and model status:** IMP-009 source/review integrity reported **25 checks, 0 warnings**, 1,051 definitionless contextual Interfaces (no extra Port notes) and **1,545 resolvable local endpoint block references**, accepted with semantic model acceptance explicitly still **PENDING**. IMP-010 hierarchy and Interface FlowProperty accepted; 752 interface-owned FlowProperty definitions, 0 exact-copy warnings. IMP-011 BindingConnector review: **249 source and 249 review rows**, **209 canonical Interface.equals pairs / 418 directed links**, **23 Connection.exposes**, 17 cross-owner review-only bindings; acceptance **PASS**.

**Workbench real-vault read/no-op acceptance:** `status: PASS`, `acceptance: candidate-only`, `localModelVersion: 0.5`, `sourceVaultUnmodified: true`, `failures: []`. Parsed **27,813 Markdown files**, **803 Local Model regions**, **2,055 parts**, **4,387 endpoints**, **552 connections**, **72 flows**, **1,051 definitionless endpoints**, **23 exposures**, **209 equals pairs**; matched Run Manifest. **0 parse errors**, **4 no-op edit samples**, **0 formatting drift**.

**Post-BOM candidate regression and version safety:** Read-only 0.6 quantity/UOM and Object `variantOf` focused suites with cache tests **30/30 PASS**. Active/generated schema and manifest remain `0.5` / `pre-release`; no 0.6 marker or writer was silently promoted. The Step 16 proposal integrity and all 31 frozen BOM source hashes also passed.

**Manual gates not performed by headless CI:** the importer logged a required real Obsidian Interface contextual-identifier edit and application restart test; this is **not** a passed UI test. In addition, experimental 0.6 reader and `variantOf` are not yet governed write schemas, Bootstrap first-open is pending, and the 4 controlled-release warnings must still be resolved. No generated output, source QEAX or original asset archive was uploaded from the ephemeral runner.

**Next bounded Step 18:** stage a reproducible **manual Obsidian acceptance checklist** based on the accepted disposable QEAX vault, with definitionless Interface editing/restart, BOM quantity/variantOf read-only behaviors, and Bootstrap startup/lock provenance. Decide on independent W-governance of proposed schemas; do not modify main or issue a release before these checks.
