# Branch cleanup — checkpoint BR-13: WB106 exclusive workflow safety

Date: 2026-10-12
Status: PARTIAL — historical workflow and manifest reviewed; eight exclusive commits not yet exhaustively enumerated
Compare: `consolidation/step22-single-repo-cutover-2026-10-11` → `wb106-release-integration`, 8 WB106-only commits and 1952 Step22-only commits.

## Newly inspected

- `.github/workflows/wb106-runtime-integration.yml` on WB106: Git blob `7c6963790fbbebca94a47c2d1b7a05b96dcaac07`. This is a branch-scoped legacy CI workflow with **contents: write** permissions. It regenerates the plugin lock, invokes a release checker, then commits and pushes lock files directly on the historical branch. It is **not** an appropriate promotion or CI policy for the current multi-stage Test_Vault_ consolidation candidate. Preserve as history; do not copy to active workflows.
- `Base Vault/Runtime/Plugins/mdse-workbench/manifest.json` on WB106: blob `ec4c18a259d902b3f36bb60f324261e44d42c5f4`, version `0.1.17`. Step22's already-reviewed release manifest and lock select `0.1.18`.
- Commit search found `095e847855e08f644d97c625f1bfc497b80e51ae` (Expand WB-106 gate to structured editor) and `e02f16910971e369a4c2de5ad5bec60f4f142b8c` (Update Workbench roadmap to WB-106 v0.8 gate), but **these search hits are not established as members of the eight branch-exclusive commits**. Do not use them as an exclusive-commit list. The available compare connector yields counts and net files, not a full commit enumerator.

## Decision

No bulk merge or generated lock file copying. WB106 remains **HOLD / historical release candidate** pending full exclusive-commit identification and any actual missing-feature comparison. The legacy write-enabled workflow is not suitable for reactivation; any replacement must use reviewed in-repo CI and controlled PR promotion.

## Next bounded work

BR-14 — inspect the `recovery/repository-consolidation-2026-10-09` branch's distinctive net changes, prioritizing source/evidence preservation and unresolved local-work/security flags. Continue with other divergent Base/CI branches. For complete commit-by-commit audits, use a repository clone command `git log --oneline <candidate>..<old_branch>` or an API method that enumerates commit records, then inspect each diff and record SHAs.

## Handoff
STEP: BR-13
STATUS: PARTIAL (workflow safety PASS; complete commit enumeration OPEN)
SOURCE: GitHub branch file fetch and prior BR-12 comparison
OUTPUT: this file on PR #41
CHECK: inspected exact legacy write-enabled CI workflow and 0.1.17 manifest
NEXT: BR-14
OPEN: WB106 eight branch-only commits; recovery branch; Base/CI exclusive changes; PR and release approvals; unpushed local changes.
