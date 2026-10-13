# Branch Cleanup — Checkpoint BR-35: WB106 exclusive-commit evidence gate

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit: PR #41
Engineering candidate: consolidation/step22-single-repo-cutover-2026-10-11
Historical branch: wb106-release-integration
Status: PARTIAL — eight branch-exclusive commits unresolved, release-file evidence verified

## Verified comparisons
Step22 → WB106 Git compare: DIVERGED, **8 WB106-only commits**, **1952 candidate-only commits**, with seven branch-side changed paths:
- .github/workflows/wb106-runtime-integration.yml
- .obsidian/plugin-lock.yaml
- 00_Workspace/00 - Current State.md
- 00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md
- Base Vault/Definition/mdse-release.yaml
- Base Vault/Runtime/Plugins/mdse-workbench/main.js
- Base Vault/Runtime/Plugins/mdse-workbench/manifest.json

Warning: a GitHub diverged compare file list is a branch-side delta against common merge base, **not** proof of target tip missing files.

## Direct tip checks
| Path | WB106 blob | Step22 blob | Interpretation |
|---|---|---|---|
| Base Vault/Runtime/Plugins/mdse-workbench/manifest.json | ec4c18a259d902b3f36bb60f324261e44d42c5f4 | a5852e592eafa027f52c2d052497293aec51a107 | old plugin v0.1.17 vs candidate v0.1.18 |
| .obsidian/plugin-lock.yaml | 5194497334e90b72f22575f514337b2bbd218e4c | c430670577318457972a154012d08c6d28e6d11b | different controlled lock bytes; DO NOT copy older lock |
| Base Vault/Definition/mdse-release.yaml | 9793b4becbc19d138753549c86c37f4eb2b0d7b2 | 6d06db25ed50ff390460c567b8fa769981aacc9e | different governed release metadata, do not overwrite candidate |
| .github/workflows/wb106-runtime-integration.yml | 7c6963790fbbebca94a47c2d1b7a05b96dcaac07 | no tip-preservation assertion from this pass | legacy push-triggered write-enabled CI; contents: write + bot git push, DO NOT reactivate |

## Commit enumeration boundary
GitHub search for `WB-106` returned two commits:
- 095e847855e08f644d97c625f1bfc497b80e51ae — Expand WB-106 gate to structured editor
- e02f16910971e369a4c2de5ad5bec60f4f142b8c — Update Workbench roadmap to WB-106 v0.8 gate

These **have not been proven to be among the 8 WB106-exclusive commits**. GitHub commit search is not equivalent to `git log Step22..WB106`. Do NOT infer that six unidentified commits can be discarded or that these search hits define their branch membership.

## Recommended exact resolution
Run trusted local Git with both remote refs fetched:
```bash
git fetch origin '+refs/heads/wb106-release-integration:refs/remotes/origin/wb106-release-integration' '+refs/heads/consolidation/step22-single-repo-cutover-2026-10-11:refs/remotes/origin/consolidation/step22-single-repo-cutover-2026-10-11'
git log --format='%H %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/wb106-release-integration
git diff --name-status origin/consolidation/step22-single-repo-cutover-2026-10-11 origin/wb106-release-integration
```
Review each exclusive commit with `git show --stat <sha>` and relevant diffs, ensuring provenance/acceptance evidence is retained. Use read-only disposable clone or clean worktree; do not publish local machine inventory or protected model data.

## HOLD / next
WB106 remains **HOLD**. The old auto-pushing workflow, obsolete plugin 0.1.17 release metadata and historical lock must not replace candidate state. No branch removal until all 8 commits individually classified, PR and local contributor evidence reviewed, QEAX confidentiality decision, W/document governance and actual Obsidian GUI acceptance considered.

STEP: BR-35
NEXT: BR-36 — obtain full unique commit set for WB106 and 3 divergent integration branches with a trusted Git log mechanism, or continue identifying exact tip-side evidence without unsafe promotion.
NO ACTION: 0 branches removed, 0 PRs closed, 0 merges, 0 release promotions.
