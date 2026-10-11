# Consolidation Step 17 — Proposed document-registry reconciliation

**Status: REVIEW-ONLY, NOT APPROVED.** Prepared 2026-10-10 Pacific, based on exact Step 16 commit `d6343f6fa1e73fc8083e6e88b0541bd909ff9759` and release manifest Git blob `29a05fc71c2f25108f07927870ac5d3d3bdd618b`.

## Native release-check finding

The unchanged `Base Vault/Testing/check-release.py --workbench 55_Workbench` reported **32 FAIL and 4 WARN** on Step 16. This step reproduces the full unregistered Markdown set using the tracked Git tree and `documents:` entries, rather than relying on the truncated release-check log. All 32 missing paths are top-level `00_Workspace/*.md`; none are top-level files in `Importer/Definition/`.

**These are candidate registrations, not declarations of approved present authority.** Twenty-nine dated integration/consolidation checkpoints are proposed as `reference`, and the three explicitly unapproved W decision / registry redline documents as `proposal`. No document is proposed as `current`, `historical`, `superseded`, or `retired`. Assigning `historical` or `superseded` would trigger the native checker's explicit target/banner controls, so do not auto-apply those labels to snapshots.

## Exact proposed manifest rows (not applied)

Append these rows inside `documents:` in `Base Vault/Definition/mdse-release.yaml` after review and approval. **The live manifest remains unmodified in Step 17.**

```yaml
  - {path: "00_Workspace/Consolidation Step 01 - Workbench Remote Coverage 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 02 - Recovered Handoffs and Historical Branch Triage 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 03 - Workbench Historical Branch Dispositions 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 04 - Repository Authority and CI Transition Audit 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 05 - Public QEAX Metadata and Local Clone Audit 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 06 - Local Audit Hardening and Signoff 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 07 - Workbench Authority Cutover Preflight 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 08 - Actual Workbench Reference Audit 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 09 - Controlled Cutover and Rollback 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 09 - Proposed W Authority Decision 2026-10-10.md", status: proposal}
  - {path: "00_Workspace/Consolidation Step 10 - Workbench Provenance Aware Preflight 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 11 - Legacy Workbench Workflow Retirement 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 12 - Post Retirement Reference Audit 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 14 - Workbench Historical Documentation Review 2026-10-10.md", status: reference}
  - {path: "00_Workspace/Consolidation Step 15 - Exact Registry Redline and Promotion Stops 2026-10-10.md", status: proposal}
  - {path: "00_Workspace/Consolidation Step 15 - Proposed W Decision and Authority Signoff 2026-10-10.md", status: proposal}
  - {path: "00_Workspace/Consolidation Step 16 - W341 W342 Release Provenance Verification 2026-10-10.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 04B Persisted Workbench Import 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 05 Release Contract and Path Audit 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 06 Importer Workbench Compatibility 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 07 WB129 Local Model 05 Staging 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 08 Importer WB129 Acceptance 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 09 Persisted Importer WB129 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 10 Release Registry and Fixture 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 11 BOM Reconciliation 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 12 BOM Artifacts Recovery 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 13 Original BOM Archive Verification 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 14 BOM Original Git Integrity Complete 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 15 BOM Staged Source Integration 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 16 BOM Schema Governance Proposals 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 17 Post-BOM Real QEAX 2026-10-09.md", status: reference}
  - {path: "00_Workspace/GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md", status: reference}
```

## Path and immutable Git evidence

| Proposed status | Source file | Original Git blob SHA |
|---|---|---|
| reference | `00_Workspace/Consolidation Step 01 - Workbench Remote Coverage 2026-10-10.md` | `338061988a4a2188fa748f6693ee15dec4400173` |
| reference | `00_Workspace/Consolidation Step 02 - Recovered Handoffs and Historical Branch Triage 2026-10-10.md` | `dd0e072ef4d3727aa1c8c7220200e3aec5bc6f60` |
| reference | `00_Workspace/Consolidation Step 03 - Workbench Historical Branch Dispositions 2026-10-10.md` | `22864b0c9dd4a009fcf1a5f7be9af67d55dfb8d2` |
| reference | `00_Workspace/Consolidation Step 04 - Repository Authority and CI Transition Audit 2026-10-10.md` | `23aa523c42f07dafe2fe3edc7990d302ef146451` |
| reference | `00_Workspace/Consolidation Step 05 - Public QEAX Metadata and Local Clone Audit 2026-10-10.md` | `7a497fa5e9bd0acf33d2c52228b63057262ffe41` |
| reference | `00_Workspace/Consolidation Step 06 - Local Audit Hardening and Signoff 2026-10-10.md` | `ff03fad8d5f19f1b4bd3759e977fa9c98faa51bd` |
| reference | `00_Workspace/Consolidation Step 07 - Workbench Authority Cutover Preflight 2026-10-10.md` | `c11000bf7dcf0ad0f509c4273fda8bff74e9a2ae` |
| reference | `00_Workspace/Consolidation Step 08 - Actual Workbench Reference Audit 2026-10-10.md` | `0eb95178998cc97d93d1fb1fb923ef623f820d2e` |
| reference | `00_Workspace/Consolidation Step 09 - Controlled Cutover and Rollback 2026-10-10.md` | `b936c060b5e49ef7fd56b02f43e29cb72d8e44c3` |
| proposal | `00_Workspace/Consolidation Step 09 - Proposed W Authority Decision 2026-10-10.md` | `656fab2222379043552f34a62f7f7ec37ec7b3bf` |
| reference | `00_Workspace/Consolidation Step 10 - Workbench Provenance Aware Preflight 2026-10-10.md` | `43002398122bb1d7af2a58f528038a88c9260fd3` |
| reference | `00_Workspace/Consolidation Step 11 - Legacy Workbench Workflow Retirement 2026-10-10.md` | `7084a8882abb830141adf398e61c7ab8cded3086` |
| reference | `00_Workspace/Consolidation Step 12 - Post Retirement Reference Audit 2026-10-10.md` | `6c30cad5959ffb32a1af67c0c9ffafcd9b5f5dc1` |
| reference | `00_Workspace/Consolidation Step 14 - Workbench Historical Documentation Review 2026-10-10.md` | `2b3ba1af0f4f697344e35c77334e39a9a37dc0d7` |
| proposal | `00_Workspace/Consolidation Step 15 - Exact Registry Redline and Promotion Stops 2026-10-10.md` | `a345311173b86c8f46598c59e1e7cb480d4735ff` |
| proposal | `00_Workspace/Consolidation Step 15 - Proposed W Decision and Authority Signoff 2026-10-10.md` | `d53cc1028f3983e87d8c73e7cf85a8ed1a9ed2e0` |
| reference | `00_Workspace/Consolidation Step 16 - W341 W342 Release Provenance Verification 2026-10-10.md` | `5d40e977e395215380ec11f3b38f726ea1e9d5b0` |
| reference | `00_Workspace/GitHub Consolidation Step 04B Persisted Workbench Import 2026-10-09.md` | `7c3dc3a51495d5e9edbb2bd60f58f5de106ae2eb` |
| reference | `00_Workspace/GitHub Consolidation Step 05 Release Contract and Path Audit 2026-10-09.md` | `774d3959507a8684533f2717f16d244c5a4efcab` |
| reference | `00_Workspace/GitHub Consolidation Step 06 Importer Workbench Compatibility 2026-10-09.md` | `cf7d17034f2ed32b29e59bd5bd67bfeaa84cc626` |
| reference | `00_Workspace/GitHub Consolidation Step 07 WB129 Local Model 05 Staging 2026-10-09.md` | `531531f475c106efb5e1617edf8626bbf83f0847` |
| reference | `00_Workspace/GitHub Consolidation Step 08 Importer WB129 Acceptance 2026-10-09.md` | `2db622f6bfb6f5cb81fb627674d7553dc20fb68c` |
| reference | `00_Workspace/GitHub Consolidation Step 09 Persisted Importer WB129 2026-10-09.md` | `268071d83c800577924bbe92056a9fb6d330904d` |
| reference | `00_Workspace/GitHub Consolidation Step 10 Release Registry and Fixture 2026-10-09.md` | `c18cc684ff41d4460fdee18d55361900988f24c4` |
| reference | `00_Workspace/GitHub Consolidation Step 11 BOM Reconciliation 2026-10-09.md` | `854872ddf504e7252ca70d0d90bd0a52f78d68e3` |
| reference | `00_Workspace/GitHub Consolidation Step 12 BOM Artifacts Recovery 2026-10-09.md` | `ed276a95778ca3f70da469870d98567b3eff0d21` |
| reference | `00_Workspace/GitHub Consolidation Step 13 Original BOM Archive Verification 2026-10-09.md` | `63a401913fcfc10758f7a04550d993ac8decb0ee` |
| reference | `00_Workspace/GitHub Consolidation Step 14 BOM Original Git Integrity Complete 2026-10-09.md` | `51cd4cdf6cb7f443ae4751f1d4ab233bb2a325ed` |
| reference | `00_Workspace/GitHub Consolidation Step 15 BOM Staged Source Integration 2026-10-09.md` | `85f6e0d0db3d90eb8744f90b71ff6641611224db` |
| reference | `00_Workspace/GitHub Consolidation Step 16 BOM Schema Governance Proposals 2026-10-09.md` | `a73dc7707cbe03d1e554db16ea00f7bad661a09e` |
| reference | `00_Workspace/GitHub Consolidation Step 17 Post-BOM Real QEAX 2026-10-09.md` | `566a380eb3bac153be31787f611e5764daa8eaaf` |
| reference | `00_Workspace/GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md` | `81a4978e0ddbc01d5ac36a27a4dada499f05a632` |

## Review criteria and non-goals

- The machine-readable `step17_registry_proposal.json` keeps a proposed status, short rationale, exact original Git blob, and `PENDING_DOCUMENT_CONTROL_APPROVAL` for each file.
- `step17_registry_review.py` enumerates both native checker scopes from the checked-out Git tree; verifies exact paths and blobs; simulates all 32 inserts **in memory**, and confirms the simulated uncovered-path count reaches zero without changing one byte of the manifest. The tool intentionally has **no apply/push/merge mode**.
- A simulated registration closure does **not** mean the entire release would pass. Existing importer/Bootstrap/clean Base warnings, true generated-vault acceptance, governance, and security gates are independent.
- Original GitHub integration test reports are dated evidence; the stored test claims are not re-run or upgraded to current release acceptance by registering their Markdown records.
- The Step 15 W decision and registry redline are proposals even if their content contains a possible future instruction. They must not be marked `current` until a new W decision is issued and separate promotion checks are satisfied.
- Do not store contributor local paths, QEAX source-model bytes, or private security classification in public review artifacts. The QEAX ZIP remains reachable in public Git history pending its owner's disposition; it is **not** read by these checks.
- No changes to original W-328/W-329/W-341/W-342, live schema `1.36/1.18/0.5`, Workbench pinned `0.1.18`, plugin lock, Local Model 0.6 writer, or standalone repository settings.

## Approval and rollback

1. Document-control and MDSE methodology owner review the 29 reference / 3 proposal classifications and verify the listed source hashes against the intended promotion tip.
2. After approval, apply exactly the proposed 32 rows to a **separate** reviewed manifest cutover PR; update the original source hash ledger if any source content changes, rather than allowing a stale reconciliation.
3. Run the complete native `check-release.py` and ensure no unregistered Markdown remains; any non-registration error is an independent blocker. Rerun schema, importer, Bootstrap, Workbench package, guide-copy, lock and actual GUI checks on the final intended promotion commit.
4. If registry classifications are rejected, discard the proposal without touching the source registry. Do not relabel everything as current just to silence a failing check.

**Remaining:** QEAX owner/security classification, local contributors' stashes/unpushed work sign-offs, ratified superseding W decision and document review, full integrated release/build checks, real Obsidian GUI first-open/read/edit/restart, explicit protected promotion, and separate standalone archival authorization.
