# Consolidation Step 15 — Exact document-registry redline / promotion stop plan

**REVIEW ONLY / NOT APPLIED.** Date 2026-10-10. A new W decision is unassigned and not approved. All source files and the original Workspace Decision Log remain intact.
**Baseline:** Step 14 commit `49503104bc875d8a19d99b7248a000ddd9f00db5` and manifest Git blob `29a05fc71c2f25108f07927870ac5d3d3bdd618b`.

## Exact, future three-row registry replacement — only after explicit W approval

These are three separate exact matches in `Base Vault/Definition/mdse-release.yaml` and must be reviewed against the then-current manifest. Their placement elsewhere in the registry must remain unchanged.

```diff
-  - {path: "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md", status: proposal}
+  - {path: "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md", status: current}
-  - {path: "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md", status: current}
+  - {path: "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md", status: superseded, supersededBy: "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md"}
-  - {path: "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md", status: current}
+  - {path: "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md", status: superseded, supersededBy: "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md"}
```

Before approval, the proposed successor remains `proposal` and both old documents remain `current`. An in-memory preview is not a committed supersession. Preserve the old dated October 2 and October 5 Markdown bytes and their direct links. Full supersession requires linking each old registry row to the named successor.

## Adjacent changes that are NOT part of the three-row redline

- The Step 14 Workbench stability roadmap and product roadmap/README have review notices but remain five unresolved document-reference cases as of final Step 14 audit. Do not automatically change their status or erase old W/B milestone content to silence a checker.
- The release manifest currently pins `0.8.0 pre-release`, relationships `1.36`, element types `1.18`, Local Model `0.5`, Workbench `0.1.18` and importer `0.8.19` candidate. `candidateVersion: null` under Workbench is not approval of a future release.
- Source ownership in the Step 09 candidate moved to `Test_Vault_/55_Workbench/`; a governance decision does not authorize converting the old pinned Workbench plugin-lock source label to a new URL.
- W-341 user guide source-copy parity and W-342 candidate-vs-pinned gating need deliberate review using the actual release checker and final artifact; preserving these controls is mandatory.
- The eight old Workbench checkout workflows were removed from the active root workflow directory **on Step 11 staging** and preserved exactly under `55_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/`. The prior runs and other branches are unaffected.

## Proposed approval and sequencing — no automatic actions

1. Authorized QEAX source-data owner and security review the public-history exposure and decide incident/remediation disposition in a private controlled channel; do not copy or unpack the QEAX archive for these document/CI checks.
2. Workstation owners privately sign off dirty trees, untracked items, local-only branch commits, remote tracking freshness, stashes, extra worktrees, and BOM A-15 candidate material.
3. Governance owner reviews W-328/W-329 replacement scope and signs/assigns a valid new W-ID; Workbench owner signs product and source boundary. The original W log may only be appended following this approval.
4. Document-control owner approves the three exact registry row changes and any successor/README updates; explicitly preserve old content and links.
5. Release owner checks W-341 guide parity, W-342 candidate-vs-pinned gate, plugin lock hash, importer release conformity, full Base/Bootstrap/Workbench tests and final release manifest version matching.
6. Run real Obsidian GUI first-open/read/edit/restart/persistence on Mac and Windows from the **exact final accepted candidate**.
7. Only after these gates and protected reviewers approve may the entire ordered PR chain be promoted to `Test_Vault_/main`. Archiving standalone `MDSE_Workbench` remains an independent future authorization.

## Rollback

Prior to approval, leave the current three rows untouched. If a later authorized cutover must be reverted, use an audited Git revert of its exact commit and restore the original row statuses, while leaving the immutable October historical files and W decision log unchanged. Do not force-push, reset contributor clones, delete branches, or rewrite public history as an unapproved rollback.

**Readiness now:** BLOCKED. No approval details, W-ID, QEAX classification, contributor signoffs or GUI acceptance have been provided.
