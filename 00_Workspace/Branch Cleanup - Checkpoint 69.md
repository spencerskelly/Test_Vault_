# Branch Cleanup — Checkpoint BR-69: Importer Candidate Release Gate

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Candidate comparison: consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: SOURCE REVIEW; no release or source edit.

## Source files read

- `Importer/Definition/Importer Operating Contract.md`, blob `434529278ce25be1c549ffc77d549e76c962214a`
- `Importer/Definition/Importer Issue Register.md`, blob `f14f166b33f1c75d76999dc7272ce09979ce80c7`
- `Importer/Definition/Translator Definition.md`, blob `a44eeedc4133232efd527ca1174eced92cec359a`
- `Base Vault/Definition/mdse-release.yaml`, blob `6d06db25ed50ff390460c567b8fa769981aacc9e` (BR-68)

## Operating release contract

The contract demands a deterministic, source-faithful transformation from approved, read-only QEA/QEAX SQLite snapshot into a fresh initialized matching MDSE Base. Stage 1 is mechanical transformation; Stage 2 is governed engineering judgment, NOT silent mapping invention.

Twelve invariants: source read-only, identifiable source snapshot, terminal disposition for each governed entity, no unsupported inference, deterministic identity, clean destination, release/schema match, pre-write validation, unambiguous partial-failure status, separate mechanical and semantic approval, reconciled evidence, and deterministic repeat/headless acceptance.

Phases 0-6 include destination qualification, WAL rejection/source hashing, all-table disposition, translation planning, global filenames and nesting, canonical-versus-review relationship separation, and contextual Local Model generation.

## Issue register disposition from actual issue table

18 issues total:
- 10 CLOSED: IMP-001 through IMP-010; sources cite past aggregate fast CI and real-QEAX bridge evidence. No independent rerun in this checkpoint.
- 4 IMPLEMENTATION REQUIRED: IMP-011, IMP-014, IMP-015, IMP-017.
- 2 TEST REQUIRED: IMP-013, IMP-016.
- 1 DECISION REQUIRED: IMP-012.
- 1 DEFERRED: IMP-018.

**IMP-011** is a concrete semantic gate. Register states W-398 accepted source classification of 249 BindingConnectors as 23 resolved `Connection.exposes`, 209 same-owner canonical `equals` (191 + 17 + 1), 17 cross-owner review-only. It calls for Local Model 0.5 canonical equality, importer implementation, Workbench 0.5 handling, then real-model/Workbench rerun. Its status remains IMPLEMENTATION REQUIRED. Recorded bridge evidence is not equivalent to closing the issue.

**IMP-012** is marked DECISION REQUIRED for folder capacity; however later W-382 and manifest already declare `modelFilesPerFolderLimit: null` and no policy-level path-length limit. Determine whether the decision was accepted but register status not updated versus an unresolved behavior contradiction before changing source. Do not revert W-382 based on stale register text.

**IMP-013, IMP-016 and IMP-015** refer to old v0.8.16 real-model validation targets, although current register's closed items cite v0.8.19 real-source/Workbench runs. An evidence-by-feature audit must decide whether newer bridge runs actually meet each specific exit criterion before retiring these open entries. Do not automatically treat them closed.

## Documentation and governance drift

- Operating Contract header applies to importer v0.8.18; Release manifest and Issue Register both say candidate v0.8.19.
- Translator Definition says Current through W-394 while Issue Register references W-395, W-396, W-397 and W-398. That might mean the translator authority is stale; verify decisions/schema behavior and enforce same-commit authority update before ratification.
- Manifest importer `release: null`, candidate v0.8.19; cleanBase `repo: null`; releaseStatus `pre-release`. No authority to issue release.

## Release owner minimum completion sequence

1. Reconcile current W decisions, schemas, Translator Definition and Operating Contract with candidate 0.8.19. Record discrepancies as defects; do not silently rewrite governance text.
2. Complete/explicitly disposition IMP-011 through IMP-017, distinguishing superseded old acceptance wording from gaps that genuinely remain.
3. Rebuild/revalidate an approved initialized disposable Base, current pinned 0.8.19 import with source profile and authorized QEAX handling, fail-closed negative tests, deterministic full rerun, source/evidence reconciliation, and headless integrity validation.
4. Verify Local Model 0.5 BindingConnector equality and Workbench 0.1.18 compatibility against exact imported output.
5. Run Base/Workbench/Bootstrap release checks, actual Mac and Windows Obsidian first-open/operator acceptance, security/local contributor governance gates.
6. Obtain explicit importer and overall release owner approval before changing `tools.importer.release`, `tools.cleanBase.repo`, or `releaseStatus`.

## Handoff

BR-69 complete: Extracted source-grounded importer blocker/status matrix and exposed header/governance version drift. Current release remains blocked. No real QEAX fetched or importer tests run.
NEXT BR-70: Inspect W-398 and current Local Model 0.5 YAML/source to distinguish IMP-011 implementation gap from stale tracking, without changing governed model.
No merge, PR closure, branch deletion, release, archival or source modifications.
