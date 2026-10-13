# Branch Cleanup — Checkpoint BR-36: WB106 commit candidate exclusion

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Engineering candidate: consolidation/step22-single-repo-cutover-2026-10-11
Historical ref: wb106-release-integration
Status: PARTIAL — confirmed two *non-exclusive* WB106-related commits; eight exclusive commits remain unenumerated

## New exact ancestry proof

Two GitHub text-search matches for WB-106 were fetched as commits, then each compared as a base to both branch tips:

| Commit | Subject | To WB106 | To Step22 | Verified interpretation |
|---|---|---|---|---|
| 095e847855e08f644d97c625f1bfc497b80e51ae | Expand WB-106 gate to structured editor | diverged, ahead=8 / behind=1 | ahead=1951 / behind=0 | Commit is on Step22 ancestry, **NOT** on WB106 ancestry; not one of eight exclusive WB106 commits |
| e02f16910971e369a4c2de5ad5bec60f4f142b8c | Update Workbench roadmap to WB-106 v0.8 gate | ahead=200 / behind=0 | ahead=2144 / behind=0 | Commit is ancestor of BOTH branch tips; not exclusive |

Commit file scopes reported:
- 095e847: `00_Workspace/00 - Current State.md`, `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md`, `00_Workspace/MDSE Plan - Path to a Golden Model.md`, `00_Workspace/Workspace Decision Log.md`.
- e02f169: `MDSE Workbench/03 - Build Outline and Roadmap.md`.

This corrects the former uncertainty in BR-13/BR-35 about these search hits: neither belongs to the eight branch-only WB106 commits. Search by message is **not** a substitute for the exact `candidate..WB106` log.

## Tooling boundary

Available GitHub connector compare returns ahead/behind counts, merge base and changed-file stats but does not expose the full SHA enumeration of branch-exclusive commits. Global commit search returns unrelated matches and cannot establish exclusive membership. The eight WB106-only commits remain unknown; do not manufacture a list or assert the branch is deletion-safe.

## Read-only resolution procedure

From a trusted *clean, disposable* clone with both refs explicitly fetched:
```bash
git log --format='%H %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/wb106-release-integration
git log --format='%H %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/integration/importer-reconciliation-2026-10-09
git log --format='%H %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/integration/bom-a14-reconciliation-2026-10-09
git log --format='%H %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/integration/workbench-monorepo-rehearsal-2026-10-09
```
Expected branch-only counts, based on verified connector comparisons: 8 / 6 / 2 / 1. Capture the exact SHAs, message, affected paths, diff and disposition per commit. Compare full tip trees separately; merge-base-relative compare lists alone do not prove candidate-tip absence.

## Safety / next
WB106 and all divergent branches remain HOLD. No old auto-pushing WB106 CI activation, old release lock replacement, branch deletion, PR closure or main promotion.
NEXT BR-37: obtain and review exact exclusive-commit enumeration or pivot to security/local-work signoff evidence while preserving branches.
