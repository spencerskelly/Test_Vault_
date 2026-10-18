# Step 80 — Historical PR dependency closeout sequence (2026-10-14)

Status: **read-only PR metadata verified; plan only**. GitHub reports each listed PR as open/draft/mergeable, but mergeability is NOT governance approval or release acceptance.

## Verified dependency graph

- PR #6: `main` ← `recovery/repository-consolidation-2026-10-09` (`ffca1a2b8e8fe54da2191309f52a34286ad34648`).
  - PR #7: recovery ← `integration/workbench-monorepo-rehearsal-2026-10-09` (`79dac2f69f97c3ac9ae8a1735640666e4047badb`).
  - PR #8: recovery ← `integration/workbench-subtree-2026-10-09` (`75eff6007af46e19f36f76b38df44658ac381ba5`).
    - PR #9: workbench-subtree ← `integration/importer-reconciliation-2026-10-09` (`28215a58ff4757ad833ff54a4edf67dd35f13eb0`).
- PR #14: `integration/release-contract-step10-2026-10-09` ← `integration/bom-a14-reconciliation-2026-10-09` (`92a466df64b485b2f396a380593cc79ff161300f`).

Current consolidation stack is separate:
- PR #39: Step21 ← Step22 (`58ab10870f11757cf1bf367ecd5868be9b60933d`).
- PR #41: main ← consolidation audit (`05cd85e9eab812b2d5650ee0166eeb8f933d7a55`).
- PR #42: main ← lean CI (`4eaddbd1364633ba21038dc85a51a76c374d354d`).
- PR #43: Step22 ← active validation (`4b448541e1ddaabe5590d7fd4ac1d2946e8a3290`).

## Dependency-safe closeout proposal

1. **Preserve:** obtain authorization to create exact-tip historical archive tags from Step78; verify tags and non-executable workflow archives, and separately retain original PR and CI-run URLs. Do not infer preservation of unpublished local work.
2. **PR #7 and #9 first:** map their original rehearsal checks to current approved tests, document supersession and obtain reviewer authorization before closure or retargeting. PR #8 must remain until its Workbench history has an approved durable successor.
3. **PR #8:** verify original subtree ancestry and contents against Step22 and decide whether to close superseded PR or replace with an explicitly reviewed engineering cutover. Its base recovery branch must stay available throughout this review.
4. **PR #6 last in recovery stack:** only after #7 and #8 cease depending on recovery as base and preserved ancestry is durable, decide closure/retarget. Do not delete recovery while it is their base.
5. **PR #14 independently:** retain BOM A14 evidence and its source branch until original A01–A14 source/fixture evidence and current semantic acceptance are reconciled; no silent release promotion.
6. **Integrate by approved destination:** once audited, merge/rebase only approved changes into main, maintaining source-level provenance. PR #41 audit, #42 CI and #39 cutover require independent review; PR #43 stays a validation branch unless its changes are curated into an approved integration PR.
7. **Retire only after gates:** re-fetch SHA, verify durable ref, no open dependent PR base/head need, record owner authorization, remove branch in controlled small batch, recheck archival ref.

## Required verification still outstanding

- Current active CI coverage for legacy importer checker and unique rehearsal merge choreography is not proven equivalent.
- Real-QEAX import, macOS/Windows Obsidian GUI and release artifact approval remain separate acceptance holds.
- Branch reductions should not strand unrelated still-open historical PR references.

**No PR altered, tag created, branch deleted, merge performed, release issued, artifact replaced, or model modified.**

## Step 81

Produce a *decision-ready*, PR-by-PR supersession/evidence matrix focused on #7/#8/#9 and determine which checks must be carried forward into authoritative CI versus archived, before requesting any PR closure approvals.
