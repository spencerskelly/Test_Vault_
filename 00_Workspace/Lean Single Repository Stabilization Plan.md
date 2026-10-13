# Test_Vault_ — Lean Single-Repository Stabilization Plan

Date: 2026-10-13
Status: ACTIVE IMPLEMENTATION PLAN; NO MERGE / DELETE / ARCHIVE AUTHORIZATION
Source evidence: user-supplied Step22_Integration_Inventory.zip, Step22_Integration_Review.md, Step22_Modified_Deleted_Paths.csv.
Frozen main: 19f565859e4b9fb7ae63004f1b6f0a7de1b9144e
Frozen Step22: 58ab10870f11757cf1bf367ecd5868be9b60933d
Audit PR #41.

## Goal and non-negotiable acceptance

One concise **authoritative Test_Vault_** with (normally) main plus one integration branch, optional one short-lived feature branch; functional Workbench in `55_Workbench/`, governed importer, schemas, runtime payload, tests and user-facing docs; release remains pre-release until separately qualified. Recoverable unique histories and reference artifacts must survive outside the active branch set. Do not lose locally unpublished work. Avoid activating old dangerous CI. Never assume branch deletion erases QEAX history.

## Verified input

- `main` is ancestor of Step22; compare ahead 1809, behind 0.
- 60,528 changed paths: 60,460 added; 47 modified; 21 deleted.
- 60,249 in `55_Workbench/`; 60,033 in `55_Workbench/vault/`. Other key buckets: Importer 88, Testing 50, Workspace 49, 99_System 44, Actions 26, Base Vault 9, Definitions 9.
- Workbench code paths include at least `55_Workbench/src/` (59) and `55_Workbench/test/` (47); do not classify entire Workbench tree as discardable.
- Public candidate adds `EA_2026_09_06_endgame.qeax.zip`, which requires authorized confidentiality/retention review without opening it.
- Source path report is not a semantic verification, and Step22 has a large inherited history.

## Architectural decision

**Do not merge frozen Step22 wholesale into public main yet.** Choose an owner-reviewed curated integration against current main. Source code + controlled semantic system + tests and necessary runtime assets are candidates for active source. Historical generated vault contents and sensitive model material require separate authorized classification. Keep Step22 staging until all unique history is reachable from durable owner-approved refs.

## Work packages (small, auditable steps)

### P01 — Preservation baseline and data-owner/security HOLD
Inventory exact SHAs of main/Step22 and 46 refs; classify public QEAX historical exposure and `55_Workbench/vault/` provenance **without reading confidential contents**. Owner authorizes either retention in a secured model archive, history-preserving archival ref/repo, or further quarantine/remediation. No Git history rewriting without specialized reviewed security plan.

### P02 — Lean active-tree inclusion manifest
Use the uploaded `files.tsv` complete path list. Write a machine-readable CSV/JSON allowlist by exact prefix/file with classes `ACTIVE_SOURCE`, `ACTIVE_RUNTIME`, `ACTIVE_TEST`, `ACTIVE_DOC`, `REFERENCE_ARCHIVE`, `SECURITY_HOLD`, `NEEDS_REVIEW`. Never assume all 60,033 vault files belong in main; never throw them away. Any wildcard inclusion must be corroborated against the actual source tree.

### P03 — Semantic compatibility review for 68 M/D paths
Review all 47 modified and 21 deleted paths, especially `99_System/03_Schemas`, removed `99_System/05_Templates` and `99_System/06_Fileclasses`, nine removed `Definitions/Properties`, plugin lock, Base release/checker, importer mapping, Workbench. For each deleted semantic element, record replacement/alias/migration and tests; default to NEEDS_REVIEW, not deletion authorization.

### P04 — Prepare curated integration branch from updated main
After P01–P03 gates, create `integration/lean-authority` from verified current main. Add reviewed source files selectively from candidate, preserving file provenance in a manifest. Do **not** merge or cherry-pick entire Step22 range; that inherits data/historical artifacts. Keep old refs throughout. Do not overwrite main or unreviewed vaults.

### P05 — Make Workbench self-contained
Verify all needed source/build/manifest/package/tests in `55_Workbench/`; compare runtime plugin payload and lock SHA-256; ensure build/release workflows reference Test_Vault_ rather than old MDSE_Workbench. Historical `55_Workbench/vault/` should be a separate classified dataset, not a hidden hard dependency.

### P06 — Importer and local model authority
Pin importer 0.8.19 candidate and governed Local Model 0.5 reader/writer rules; check `Connection.exposes`, symmetric `Interface.equals`, and no 0.6 writer activation; run negative/positive synthetic fixture tests and import smoke tests where authorized. BOM `variantOf` remains proposal until governed acceptance.

### P07 — Build/test matrix
Run base builder to disposable directory and `check-release.py --workbench ... --base ...`; verify lock and copied files. Run focused Workbench/build tests, importer model tests, CI safety/permissions, and Mac/Windows Obsidian smoke checks if needed for touched runtime. Track pass/fail/warn and owner dispositions. Do not claim MDSE release issued.

### P08 — PR and governance integration
Review exact integration diff, branch rules, tests and sensitive history with authorized reviewers. Close/supersede old PRs with links only after preserving evidence. Merge approved curated PR into main with explicit permission. Keep unapproved W decisions/document registry proposals non-ratified.

### P09 — Branch retirement in small batches
Once main holds accepted source, anchor approved histories by durable main ancestry or immutable preservation tags/ref and audit 8 divergent held branches (39 branch-relative exclusive commit occurrences). Attest unpushed local work and verify PR head/base. Delete only explicitly named authorized refs in batches up to three, verifying surviving refs after each. Two CI probes are not necessarily ancestry-safe. Target 1–3 active branches without manufacturing an archive branch for each old branch.

### P10 — Retire standalone Workbench only after validation
Require copied source/build/test parity, no operational dependency on standalone, contributor signoff and recoverable old 19-branch history. Owner may then archive (read-only, reversible) old repo, not delete it. This is independent of MDSE 0.8.0 release issuance.

## Immediate implementation order

1. P01: record exact data-classification decision needed for `55_Workbench/vault/` and QEAX history. This is an actual merge blocker.
2. P02: create a reviewed inclusion/exclusion manifest from uploaded 60,528-path inventory, not just another narrative report.
3. P03: perform all 68 path-level compatibility decisions, then construct the curated branch and run tests.

## Definition of stable

Approved main represents exactly one active source of truth; all controlled source versions/manifest relationships line up; no unresolved HIGH severity semantic deletion or data/security introduction; automated and operator validation is recorded; old unique history is permanently recoverable; branch count <=3 except temporary documented holds; standalone Workbench is safely archived only once independence verified.

### This checkpoint changes only the planning document. No runtime, CI, release, PR state, branch or artifact has been changed.
