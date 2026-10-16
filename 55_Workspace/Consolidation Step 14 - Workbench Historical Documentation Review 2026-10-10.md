# Consolidation Step 14 — Workbench roadmap and README review notices

**Prepared:** 2026-10-10 Pacific. **Status: REVIEW-ONLY PROPOSAL; no new W decision, release, public-main merge, or standalone Workbench archive.**
**Parent:** `ee880ed5c7e44fe71f5ca2a55f3a04554a22a0b5` (Step 13 / draft PR #30).

## What changed

Only three mixed-purpose Workbench guidance documents received a **visible 2026-10-10 review notice immediately after the existing top heading**. Their original dated evidence—including the 2026-10-04 performance/stability step history, 2026-09-30 product-direction approval, WB-106/WB-128 milestone details, earlier Local Model 0.2/0.4 descriptions, and old repository source URLs—remains byte-for-byte intact after removal of that notice.

| Document | Pre-Step-14 original Git blob SHA | Review notice focus |
|---|---|---|
| `00_Workspace/Workbench Performance and Stability Roadmap.md` | `4f41a03020efe011260dbb884a4c279106814142` | Dated execution instructions to edit standalone Workbench are not the proposed route for current consolidation; keep all performance history intact |
| `55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md` | `0ff206b531c7659b4b46757554a7f1d6d4b1b53f` | Original approved V1 feature scope retained; historical 2026-10-02 implementation location is no longer the proposed candidate direction |
| `55_Workbench/docs/README.md` | `2dc82f816e4626982016ed9453c3c5fad8da3f32` | Warn that older 'Current v0.8' 1.35/1.17/0.2 and Workbench 0.1.15–0.1.16 claims are dated history, not current staging pin values |

The new notices present `spencerskelly/Test_Vault_/55_Workbench/` as a **proposed** source location, with staging pins MDSE `0.8.0 pre-release`, relationships `1.36`, element-types `1.18`, Local Model `0.5` and Workbench `0.1.18`. This does not mean those pins prove a released vault, a completed GUI test, or Local Model 0.6 authoring authority. An actual release must follow the governed release manifest and generated plugin lock.

## Preservation and regression method

- `66_Testing/consolidation/step14_doc_review.py` exposes only three exact-path banner allowances. It refuses missing/duplicate/displaced markers or missing proposal/versions/source warnings.
- **The three original files can be reconstructed byte-exactly** by removing only the marked Step 14 notice; the pre-Step-14 blobs above are the SHA commitments.
- `66_Testing/consolidation/test_step14_docs.py` checks proposed-not-approved wording, correct source route/pins, original historical hashes, release/decision lock preservation, review status and negative tamper cases.
- Existing Step 13 registry tests are updated to compare the original historical bytes after removal of these narrowly allowed notices. They still prove the two older registered `current` handoff/reconciliation documents are unchanged and the new continuation contract is merely a `proposal`.
- The existing release-preflight reference audit must continue to report **five needs-review documents**. Nothing is silently reclassified as `historical` or marked `current` by these notices.
- Branch-specific read-only Actions verification uses sparse checkout excluding the large public QEAX ZIP from the worktree, with no release promotion or model-content artifact upload.

## Review-gated follow-up

After formal product-owner review and the superseding W source-authority decision, decide whether to revise the current prose in these three documents and the two older `current` handoff/reconciliation files. Do not quietly delete/rewrite dated milestone evidence; use explicit approved supersession and a document registry update. The stability roadmap's original historical executor rules must be treated as dated, not a valid instruction to operate on the old standalone repo after cutover.

**Hard stops still open:** authorized public QEAX owner-security classification and exposure response if required; contributor local branches/stashes/worktrees audit sign-offs; issued W governance decision; complete importer/Base/Workbench/Bootstrap release and exact runtime plugin-lock checks; real Obsidian first-open/read/edit/restart; independent approval before read-only archiving `MDSE_Workbench`.

**Next:** Step 15 should prepare a W-decision/redline review bundle, with explicit owner sign-off fields and a no-merge gate; the source and historical evidence review is not equivalent to a governance ratification.
