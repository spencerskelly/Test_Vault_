# Consolidation Step 13 — Proposed document authority registry transition

**Prepared:** 2026-10-10. **Status:** REVIEW CANDIDATE ONLY; no governance decision has been issued. Do not change public `main` or archival state.
**Source baseline:** Step 12 `af77492c895dc31d2b28b74d8ded15947d617298`.
**Machine-readable ledger:** `66_Testing/consolidation/step13_registry_transition.json`.

## 1. Changes staged now (proposal registrations only)

- Add `00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md` with `documents: status: proposal`.
- Register this Step 13 transition document with `documents: status: reference`.
- **Do not promote** either document to `current`. Do not change the two outdated but currently authoritative registry entries without an approved W decision.
- Do not change the content of any historical handoff, roadmap, product definition, Workspace Decision Log, schemas, plugin lock or generator.

## 2. Exact proposed future supersession after approval

| Existing document | Existing status | Proposed future status | Review disposition |
|---|---|---|---|
| `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md` | current | superseded | Old copy-ready prompt sends implementation to standalone and contains pre-0.5 release/version guidance |
| `00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md` | current | superseded | Date-specific Oct 2 cross-repo contract is still registered current; preserve source semantics/history while replacing current execution authority |
| `00_Workspace/Workbench Performance and Stability Roadmap.md` | reference | reference | Preserve verified milestone sequence; separately supersede the old execution protocol, not its historical results |
| `55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md` | unregistered | reference_after_review | Approved historical product direction mixed with obsolete standalone implementation instruction; owner to review dated addendum |
| `55_Workbench/docs/README.md` | unregistered | current_after_rewrite_and_review | Living Workbench definition contains older Local Model and runtime claims; updated copy needs owner acceptance |

**Only after the new W decision is approved:** promote the new continuation contract from `proposal` to `current`, change the Oct 2 reconciliation and Oct 5 handoff from `current` to `superseded`, and set each `supersededBy` to the new contract. Keep those source files intact. Do not assert the old Workbench stability roadmap, build outline, or living README can be silently ignored; the roadmap has an actionable execution contract and the Workbench README contains superseded version claims, so their addenda/revisions must be reviewed separately.

## 3. Precedence and evidence

- The manifest has `manifestVersion: 2` and uses `current | reference | proposal | historical | superseded | retired`. Do not invent a new registration type.
- The staging manifest pins MDSE 0.8.0 `pre-release`, relationships 1.36, element types 1.18, Local Model 0.5, importer candidate 0.8.19 (release `null`), Workbench runtime 0.1.18 and Bootstrap 0.3.0, candidate 0.3.1.
- The prior October 2/5 docs contain dated 1.35 / 1.17 / 0.2 (or 0.4) descriptions. They remain attributable to the former design state; do not rewrite them as current implementation or retrospectively alter the W log.
- The proposed unified source root is `55_Workbench/` in the single development repo, but this is still an unmerged draft consolidation branch and not an issued governance decision.
- Preserve original SHA of each reviewed document in the ledger, and preserve `00_Workspace/Workspace Decision Log.md` Git blob `49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb`.

## 4. CI tests and rejection conditions

Run `python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step13_registry.py' -v` on a sparse checkout excluding the source-model archive. Tests must verify that removing only the two new manifest entries gives original Git blob `04f1fc2f4a087ccd2d1a49376c221979ee3469e3`, two old current entries remain current, and an in-memory future promotion changes *only* the three approved rows.

**Fail review** if anyone changes a released version, live semantic schema, runtime lock or generator, silently reclassifies an old document as historical, marks an unapproved proposal `current`, changes old W decisions, or claims full release acceptance from a candidate build.

## 5. Mandatory promotion and archival gates

QEAX source/public-history owner security review, local contributor branches/stashes sign-offs, new approved W decision, complete importer/Base/Workbench/Bootstrap matched-release tests, real Obsidian GUI first-open/read/edit/restart, and a separate explicit authorization for read-only standalone Workbench archive. Nothing in Step 13 satisfies those gates.

**Next bounded step:** obtain or produce governed reviewer-ready redline addenda for the remaining three mixed-purpose Workbench documents; update the current registry statuses only after the authority decision is approved.
