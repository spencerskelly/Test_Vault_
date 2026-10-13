# Branch Cleanup — Checkpoint 23: PRs 26–32

Date: 2026-10-12
Status: PASS for seven-PR triage, not release or approval
Repo: spencerskelly/Test_Vault_
Staging: consolidation/step22-single-repo-cutover-2026-10-11
Audit PR: #41

## Live PR classification
Open PR search confirms PRs #26–#32 remain open. Review API returns 0 submitted reviews for all seven; inline threads, discussion, requested reviewers and latest CI outcomes were not independently inspected.

| PR | Scope | Proposed disposition | Required gate |
|---|---|---|---|
| #26 | Step09 proposed source-owner cutover in manifest and six current navigation docs, root CI branch filters, proposed W decision | Conditional successor candidate | Confirm latest root CI, W governance approval, security/local/GUI gates |
| #27 | Step10 fail-closed reference-scanning policy: active checkout refs vs three SHA-pinned provenance labels, historical refs | Preserve security/control regression | Confirm no blind allowlist exemptions or missing workflow blockers |
| #28 | Step11 byte-for-byte archival relocation of 8 standalone checkout workflows out of runnable .github/workflows | Preserve exact-byte retirement evidence | Confirm all 8 SHA matches and newest verifier 22-test result |
| #29 | Step12 real-checkout reference scan: initially 0 active blockers, six documents for review; later proposed 5 reviewed and 3 verified provenance | Preserve diagnostic and remaining review list | Recheck final scan, classify mixed-purpose docs |
| #30 | Step13 unified continuation contract PROPOSAL and 2 new manifest document registration rows | Governance HOLD | Superseding approved W decision and 3-row transition before promoting proposal to current |
| #31 | Step14 three historical guidance notes annotated NOT APPROVED with original body preserved, 94 reported tests PASS | Documentary supersession candidate | Five current guidance files still require owner review |
| #32 | Step15 unapproved W decision proposal, not-applied 3-row registry redline, 12-gate all-NOT_APPROVED register | GOVERNANCE HOLD | Explicit individual signoffs, including QEAX owner/security, local clones, full CI, Mac/Windows Obsidian acceptance |

## Detailed observations

- PR #26 reports frozen Workbench 0.1.18, relationships 1.36, elements 1.18, Local Model 0.5 and pre-release state; no approval to write 0.6 or archive standalone repo.
- PR #27 explicitly treats active historic workflow checkout references as **blocking** until retired; pinned provenance is exempted only on exact SHA match.
- PR #28 moves 8 historic workflows byte-identically to an archive outside executable workflow directory; several old workflows had write/push permissions. Its initial 7-workflow verifier was amended for all 8; ensure latest validation before closure.
- PR #29 distinguishes dated historical references from genuinely active dependency, with a conservative outstanding five-document review gate.
- PR #30 leaves old October 2/5 documents registered current while the unified proposed contract awaits W approval.
- PR #31's annotations do not rewrite original evidence or grant approval.
- PR #32 keeps every one of 12 approvals NOT_APPROVED and does not modify approved W decision log.

## Required precedence

1. Close operational old-workflow safety differences only after PR #28 successor verification and pin consistency.
2. Preserve exact-hash provenance and reference scanner tests from #27–#29.
3. Do not turn the #30 unified contract into active governing current documentation or implement #32's W redline until owners approve.
4. Resolve public QEAX historical exposure/security review, contributor local sign-offs, exact release testing and actual Mac/Windows Obsidian UI acceptance.
5. Mark candidate PRs superseded only after successor equivalence, reviewer/comment/CI checks and explicit approval; no mass closing.

## Handoff
STEP: BR-23
STATUS: PASS for PRs #26–#32, 28 of 36 open PRs now individually triaged in BR-20..23
NEXT: BR-24 — review PRs #33–#39 plus #41; identify final current consolidation candidate gates
OPEN: seven prior outstanding promotion blockers plus latest CI and reviewer metadata
