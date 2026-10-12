# Branch cleanup — checkpoint BR-14: recovery branch preservation assessment

Date: 2026-10-12
Status: PASS — net tree inventory and high-priority documentary evidence review; full commit audit pending
Source: `recovery/repository-consolidation-2026-10-09`
Candidate: `consolidation/step22-single-repo-cutover-2026-10-11`

## GitHub compare evidence
Compare base=Step22 and head=recovery branch yields `diverged`, source ahead 19, Step22 ahead 1804. **15 net added Markdown documents**, all under `00_Workspace/` and dated 2026-10-09, none modified binary/tool/code files according to net comparison.

## Fifteen documents absent from Step22
1. `GitHub Consolidation Step 04B Persisted Workbench Import 2026-10-09.md`
2. `GitHub Consolidation Step 05 Release Contract and Path Audit 2026-10-09.md`
3. `GitHub Consolidation Step 06 Importer Workbench Compatibility 2026-10-09.md`
4. `GitHub Consolidation Step 07 WB129 Local Model 05 Staging 2026-10-09.md`
5. `GitHub Consolidation Step 08 Importer WB129 Acceptance 2026-10-09.md`
6. `GitHub Consolidation Step 09 Persisted Importer WB129 2026-10-09.md`
7. `GitHub Consolidation Step 10 Release Registry and Fixture 2026-10-09.md`
8. `GitHub Consolidation Step 11 BOM Reconciliation 2026-10-09.md`
9. `GitHub Consolidation Step 12 BOM Artifacts Recovery 2026-10-09.md`
10. `GitHub Consolidation Step 13 Original BOM Archive Verification 2026-10-09.md`
11. `GitHub Consolidation Step 14 BOM Original Git Integrity Complete 2026-10-09.md`
12. `GitHub Consolidation Step 15 BOM Staged Source Integration 2026-10-09.md`
13. `GitHub Consolidation Step 16 BOM Schema Governance Proposals 2026-10-09.md`
14. `GitHub Consolidation Step 17 Post-BOM Real QEAX 2026-10-09.md`
15. `GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md`

## Four inspected records
- Step 13 (blob `63a401913fcfc10758f7a04550d993ac8decb0ee`) documents original archive verification and explicitly defers its outdated 27/31 persisted Git count to Step 14.
- Step 14 (blob `51cd4cdf6cb7f443ae4751f1d4ab233bb2a325ed`) reports 31/31 original BOM artifacts persisted and hash-verified, backed by cited Actions runs 38008742547 and 38008828655; BOM feature and controlled release still NOT approved.
- Step 18 (blob `81a4978e0ddbc01d5ac36a27a4dada499f05a632`) reports reproducible two-vault test kit/CI success but explicitly says manual desktop Obsidian tests NOT RUN. Preserve distinction.
- Step 6 (blob `cf7d17034f2ed32b29e59bd5bd67bfeaa84cc626`) records a real Local Model 0.5 schema vs Workbench 0.4 writer incompatibility, intentionally blocked; later reconciliation checks reviewed in BR-08/09.

## Decision

**HOLD branch deletion.** These 15 original historical checkpoint documents are not on the Step22 candidate tree. Preserve them byte-for-byte on a reviewed consolidation documentation branch or transfer via provenance-preserving merge/copy before closing the recovery branch; register as historical/reference documentation, not current source of authority. Do not reclassify older pass/fail states into current release assertions. Verify copied Git blob SHA values and document registry entries. A non-squashed history merge may be considered only after repository governance, PR review and Git ancestry analysis.

Nineteen source-exclusive commits have not been individually enumerated; that remains required before deletion signoff. No source changes, merges or branch deletions made in this checkpoint.

## Handoff
STEP: BR-14
STATUS: PASS — historic documents identified as preservation-critical
SOURCE: GitHub compare + four source file fetches, 2026-10-12
OUTPUT: this checkpoint on PR #41
CHECK: ahead 19 / behind 1804; 15 net added historical documents; four inspected
NEXT: BR-15 — preserve all 15 as exact historical copies, or first obtain/document commit-level provenance and document governance; then review Base/CI legacy branches.
OPEN: exclusive commits, historical document registration, local stashes/worktrees, security, approval and GUI testing
