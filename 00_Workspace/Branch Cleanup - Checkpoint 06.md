# Branch cleanup — checkpoint BR-06: remaining integration branches

Date: 2026-10-12
Status: PASS — ancestry triage only; no merge or deletion authorization
Comparison head: `consolidation/step22-single-repo-cutover-2026-10-11`

## GitHub comparison evidence

Each integration branch was passed as comparison base with Step 22 as head. `ahead` means Step 22 exclusive commits; `behind` means integration-branch exclusive commits.

| Branch | Status | Step 22 ahead | Branch-only commits | Disposition |
|---|---|---:|---:|---|
| `integration/importer-wb129-acceptance-2026-10-09` | ahead | 610 | 0 | Included |
| `integration/obsidian-ui-acceptance-step18-2026-10-09` | ahead | 41 | 0 | Included |
| `integration/release-contract-step10-2026-10-09` | ahead | 128 | 0 | Included |
| `integration/workbench-lm05-2026-10-09` | ahead | 615 | 0 | Included |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | diverged | 1806 | 1 | HOLD, inspect exclusive commit and content |
| `integration/workbench-subtree-2026-10-09` | ahead | 644 | 0 | Included |

## Cumulative

- BR-02 through BR-04: 21 earlier consolidation branch tips are ancestors of Step 22.
- BR-05 and BR-06: 9 of 12 integration branch tips are ancestors of Step 22.
- Three diverged integration branches (BOM A14 reconciliation, importer reconciliation, Workbench monorepo rehearsal) carry 2 + 6 + 1 = **9 branch-only commits** relative to Step 22. Not yet classified by content, usefulness, duplication or risk.
- Therefore 30 earlier branch tips are proven included, and three integration branches are on hold.

Ancestry preservation is not equivalent to approval for `main`, byte-for-byte content equivalence, open-PR closure approval, contributor-local unpublished work verification, or safety/release acceptance. No deletions or merges performed.

## Next bounded checkpoint

BR-07 — Inspect the first diverged integration branch (`integration/bom-a14-reconciliation-2026-10-09`), list its two exclusive commits and affected files, compare effects against Step 22 and preserve anything necessary. Do not merge blindly.

## Handoff

STEP: BR-06
STATUS: PASS
SOURCE: Live GitHub compare API, 2026-10-12
OUTPUT: this file in PR #41 consolidation branch
CHECK: 5 included, 1 diverged; cumulative 9/12 integration branches included
NEXT: BR-07
OPEN: Nine branch-only commits across three branches; remaining non-integration branches; PR closure policy; security/document-control and GUI release gates.
