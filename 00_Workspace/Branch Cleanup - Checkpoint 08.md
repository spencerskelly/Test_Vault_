# Branch cleanup — checkpoint BR-08: importer reconciliation divergence

Date: 2026-10-12
Status: PARTIAL — branch net tree examined, six individual exclusive commits not yet enumerated
Candidate: `consolidation/step22-single-repo-cutover-2026-10-11`
Diverged branch: `integration/importer-reconciliation-2026-10-09`

## GitHub comparison
Compare base=Step 22 and head=importer reconciliation: status diverged, ahead=6 (branch-exclusive), behind=644 (Step22-exclusive). The net comparison reports only two added files on the importer branch:

1. `.github/workflows/importer-monorepo-merge-rehearsal.yml` — blob SHA `612cc78ee5c839def7dae9b343ef9c2f8dd9b8d2`, 182 lines.
2. `66_Testing/check_importer_workbench_localmodel.py` — blob SHA `95c29b377ad8c7a0596e1c164db2e6bb66168b52`, 59 lines.

Both files were fetched from the diverged branch and read.

## Interpretation and disposition

**Workflow**: branch-specific, non-writing merge rehearsal; pins expected importer SHA 0494354... and integration baseline 75eff60...; fetches a pinned importer branch in the same repository, simulates merge without committing, checks manifest/schema pins (Local Model 0.5, relationships 1.36, element types 1.18), runs importer tests, generates a disposable Base, runs the release checker as diagnostic, and checks Workbench tests. DO NOT activate this historical workflow in the consolidated CI; preserve it as historical evidence.

**Validator**: valuable fail-closed check. Reads release manifest, Local Model schema, and `55_Workbench/src/core/localmodel.ts`; parses READABLE_VERSIONS and WRITABLE_VERSION, then checks that schema compatibility declarations match the Workbench reader/writer and release pin. DO NOT blindly merge; verify whether Step22 already contains an equivalent validator. If not, port the behavior into Test_Vault_'s current supported in-repo validators, with regression fixtures. If Workbench is not an approved editor, adapt the check to the actual supported importer/editor rather than retaining a mandatory Workbench dependency.

**Six exclusive commits remain unenumerated**; these two files represent the net differences between branch tips, not an exhaustive review of intermediate commit effects.

## Handoff
STEP: BR-08
STATUS: PARTIAL — two net additions inspected, individual six commits pending
SOURCE: GitHub compare and exact file reads, 2026-10-12
OUTPUT: this file on PR #41
CHECK: diverged (branch ahead 6, Step22 ahead 644); two net added files, source file blob SHAs captured
NEXT: BR-09 — inspect one remaining diverged integration branch (`integration/workbench-monorepo-rehearsal-2026-10-09`) and compare replacement validator existence in Step22
OPEN: commit-by-commit audit, validation parity, PR disposition, security/document reviews, local contributor checks and Obsidian GUI acceptance.
