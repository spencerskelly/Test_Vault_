# MDSE v2.0 — Controlled Engineering Pilot: execution plan
Date: 2026-10-18
Status: IN PROGRESS — STEP 1
Source branch: main (migration PR #47 merged at ccac8c906d8eea78ae098a7f3128fd0592229e6f)
Implementation branch: feat/v2-integrated-pilot-20261018

## Mission
Deliver a stable, upgradeable, loss-resistant engineering environment: clean Base Vault, QEAX/CSV mechanical Importer, centrally managed Bootstrap, usable Obsidian Workbench. Demonstrate a real reduced-QEAX import into a disposable vault; edit and reopen a native SysML v2 model with the actual Workbench plugin. Do not reopen approved semantic decisions. V1 is archived reference, not a release blocker.

## Safety and source-of-truth contract
- SysML v2 section in each model note: authoritative system semantics. Emit only standards-validated native text, never silently reinterpret unsupported concepts. Maintain provenance and unresolved/review ledger.
- YAML: identity, source GUID, model kind, version, classifications, importer metadata and author provenance; controlled ownership.
- Remaining note body: engineer-owned descriptions, rationale, test results and notes; never automatically replace.
- Existing source and local changes: reconcile by stable UID + source GUID; dry-run diff, conflict report, backup/journal, atomic write/rollback; no auto-delete; same source twice must be a no-op.
- Git main: approved release authority; develop on branches, verify CI and acceptance evidence, merge only when safe.
- No proprietary QEAX or extracted source rows in public repo. Synthetic tests and aggregate evidence only.
- Changes to approved SysML v2 element/relationship mappings need separate decision review; not part of this stabilization plan.

## Product boundaries
- 20_Base Vault: reproducible empty vault, schema, templates, folders, and supported Obsidian settings. Own configuration *definition*, not deployed updates.
- 21_Importer: QEAX/CSV adapters → normalized source → canonical graph → mapping/evidence → validated native SysML v2 and Markdown → safe existing-vault reconciliation.
- 23_Bootstrap: plugin deployment, centrally managed UX/UI configuration, upgrades/repair/rollback, stable author identity (not passwords or credentials).
- 24_Workbench: views and navigation, create/edit/connect, validation, save/undo/reopen; all write operations respect note ownership.
- 25_Testing: unit, integration, parser, Obsidian UI, repeated import, upgrade, recovery.
- 26_Definitions: contracts, release pin manifest, change log, test evidence, compatibility and acceptance criteria.
- 100_Archive/V1: historical only. No active V2 runtime dependency.

## Work passes — execute in order, one bounded step per 'y'
Each step must end with a verifiable commit or test evidence and a clean handoff. 'Complete' requires witnessed tests, not just added scripts.

1. **Baseline and shared contracts [IN PROGRESS]** — inventory current active assets, identify stubbed components, freeze baseline SHA, publish this plan and note ownership/release compatibility contract. Exit: plan and contracts committed; explicit gaps, acceptance checks and next step.
2. **Base Vault reproducible package** — build real clean Obsidian vault with supported plugins/theme/templates/folders and versioned settings; manifest hashes. Exit: clean launch on target platforms tested or exact manual blockers reported.
3. **Importer adapters** — QEAX and CSV normalized into identical source schema, handle schema differences and preserved source GUIDs, package ownership. Exit: equal synthetic graph for both adapters and profile check against local reduced QEAX.
4. **Canonical graph and semantic gates** — consume pinned approved rules and direction/role evidence, preserve unknown/rejected connectors, verify no unsupported native emission. Exit: deterministic graph and complete disposition ledger.
5. **Native SysML v2 note writer** — output authoritative SysML v2 sections/YAML/engineer notes; generate only independently parser-validated declarations. Exit: parser positive/negative suite and reproducible fixture notes.
6. **Incremental vault importer** — stable identities, conflict-aware three-way reconciliation, dry-run plan, journaling and rollback, no deletion by default. Exit: second identical import no-op; engineer edits preserved.
7. **Golden local import** — import reduced QEAX (or constrained, representative scope) into disposable Base Vault; file/relationship tally and errors; never publish sensitive rows. Exit: openable vault and aggregate quality report.
8. **Bootstrap first install** — install supported plugin packages/config and initialize author ID and vault identity with no credentials committed. Exit: clean install and health check.
9. **Bootstrap upgrade/repair** — signed/hashed release manifest, managed vs user-owned settings merge, backup and rollback. Exit: populated-vault upgrade test preserving content/config preferences.
10. **Workbench navigation** — open imported notes, hierarchy, definitions/usages, ports/connections, references and diagnostics in Obsidian. Exit: witnessed browse/search/navigation.
11. **Workbench controlled editing** — create/edit/modify Part definitions/usages, ports and connections; semantic validation, preview, undo, persistence. Exit: reopen confirms syntax, graph and engineer notes unchanged.
12. **End-to-end regression** — clean install → import → edit → repeat import → update → reopen → recover; Windows/macOS acceptance and version compatibility. Exit: all critical checks pass, no unresolved data-loss bugs.
13. **Pilot release** — tag versioned Base/Importer/Bootstrap/Workbench, publish user update/rollback instructions, reviewed PR to main. Exit: reproducible release and test team handoff.

## Stop-ship defects
Unintended loss/duplication, corruption of authoritative SysML, unapproved relationship semantics, source identity instability, unhandled partial writes, settings overwritten without consent, unable to roll back, or unsupported versions silently installed.

## Evidence rule
For each step update status here with commit SHA, tests run and outcomes, remaining risks, and next smallest action. Never label tests PASS from code creation alone.

## Step 1 baseline findings (2026-10-18)
- main has the V2 migration merged (PR #47), but runtime integration has not been demonstrated.
- Base Vault: test-only builder in 20_Base Vault/build_v2_test_base.py; not proven installable Obsidian plugin/config release.
- Importer: QEAX preflight and V2 candidate projection in 21_Importer; registry disables automatic native emission; no safe existing-vault write path yet.
- Bootstrap: 23_Bootstrap/README.md placeholder; V2 install/upgrade plugin not demonstrated.
- Workbench: canonical graph and registry runtime in 24_Workbench; Obsidian plugin interaction/editing not demonstrated.
- Testing: synthetic tests and fixture definitions exist; full imported-vault/UI/save/reopen acceptance is not established.
- Historical 26_Definitions/V2_MIGRATION_MERGE_GATES_2026-10-18.md still states staging blocked: superseded *for branch merge only* by PR #47; unresolved application release gates remain.

## Next action (Step 2)
Inventory and package actual Obsidian Base Vault settings/plugins from active V2 assets or controlled, explicitly designated reference builds; implement versioned managed settings manifest; test clean install without writing into any existing engineer vault.
