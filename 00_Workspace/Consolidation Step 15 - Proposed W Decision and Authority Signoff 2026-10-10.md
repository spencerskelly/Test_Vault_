# Consolidation Step 15 — Proposed W decision: single MDSE tool-development authority

**Status:** PROPOSED FOR REVIEW — NOT APPROVED, NOT ASSIGNED A W NUMBER.  
**Prepared:** 2026-10-10 Pacific time.  
**Candidate parent:** `Test_Vault_` Step 14 commit `49503104bc875d8a19d99b7248a000ddd9f00db5` (draft PR #31).  
**Decision owner, reviewers, approval ID, and approval date:** **UNASSIGNED**. No implied signature, delegated authorization, or approval exists.

## Proposed decision text — do not copy into the approved Workspace Decision Log yet

> **W-ID PENDING · PROPOSAL — Workbench source ownership consolidates into Test_Vault_.** Subject to an approved controlled source-authority cutover, `spencerskelly/Test_Vault_` is the single continuing MDSE tool-development repository. Workbench source, tests, product/interface definitions, and build inputs are governed under `55_Workbench/` within that repository. Importer, Bootstrap, Base Vault release tooling, and shared `99_System/` semantic governance retain their respective existing responsibilities. Workbench continues to own its **product and interface behavior**, but does not independently redefine model semantics, the importer mapping, or the controlled runtime-release manifest. The original standalone Workbench repository is retained unarchived, with complete commits, branches and prior Actions evidence, until separate security, contributor-work, release and GUI acceptance gates and a separately authorized **read-only archival** are satisfied. Historical plugin-lock source identifiers remain immutable pinned-artifact provenance, not active development checkout instructions. This decision supersedes **only the source repository/implementation-location clauses** of W-328 and W-329, and clarifies dependent location descriptions in W-341/W-342; it does not change their underlying release-pinning, user-guide parity, candidate-versus-runtime, or semantic controls.

### Decisions in the approved log that must be preserved

| Existing decision | Relevant original assertion | Proposed boundary — no retroactive rewrite |
| --- | --- | --- |
| **W-328 (2026-10-03)** | Test_Vault_ owns importer/Bootstrap/Base/schema governance; standalone Workbench repo owns Workbench implementation/test/release artifacts. | Change only the Workbench **source implementation root** to `Test_Vault_/55_Workbench/`; preserve the other tools’ scope and semantics authority. |
| **W-329 (2026-10-03)** | Each tool owns its Definition, Tools, Testing, History and source location; Workbench is standalone. | Change only standalone-vs-top-level Workbench placement. Preserve separation of tool areas, versioned history, workflow/branch review discipline. |
| **W-341 (2026-10-03)** | A release-managed Workbench user guide is copied to generated vaults; source/packaged guide parity is checked. | A later *approved* guide source-path adjustment is necessary. **Do not replace** the guide copy or drop exact comparison rules during governance review. |
| **W-342 (2026-10-03)** | Pre-release Workbench candidate may differ from the pinned runtime and the release checker must distinguish them. | Continue separating candidate source from pinned runtime; **never** infer issued release from staging branch build. |

**Original W decision log must remain byte-identical:** Git blob `49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb`.

## Proposed implementation after ratification — NOT APPLIED

1. Record a new W decision with the *next valid identifier assigned by the governance owner*. Do not guess it, renumber earlier decisions, or merge this proposal text automatically.
2. Approve the Step 13 unified continuation contract, currently registered `proposal`, only after reviewing the reconciled `1.36 / 1.18 / 0.5` model pins and importer `0.8.19` candidate, Workbench `0.1.18`, Bootstrap `0.3.0` runtime / `0.3.1` candidate.
3. Apply the **three-row document registry change**, with exact path anchors: proposal continuation contract `proposal → current`; Oct 5 handoff `current → superseded`; Oct 2 reconciliation `current → superseded`, each with an explicit `supersededBy` to the new contract. The redline is in the companion Step 15 review document. The original Oct 2/5 source Markdown stays intact.
4. Review the three Step 14 roadmaps/README notices with the Workbench product owner. Resolve living instructions separately, preserving all milestone body bytes unless an explicit reviewed successor is approved.
5. Validate W-341 user guide path/parity and W-342 candidate-vs-pinned semantics against actual source, check-release and the generated lock. Existing Workbench `0.1.18` plugin-lock and generator bytes **must not change** as a side effect of this governance proposal.
6. Review the eight frozen historical CI workflow copies. Staging retirement does not change earlier branches; complete CI transition and lineage signoff before archiving anything.

## Approval checklist (all unapproved)

| Gate | Responsible review (role, not a fabricated individual) | Present state | Required evidence |
| --- | --- | --- | --- |
| W-decision text and new ID | MDSE methodology/governance owner | **NOT APPROVED** | Reviewed text, unique W-ID, dated decision |
| Workbench source/product boundary | Workbench product/code owner | **NOT APPROVED** | `55_Workbench/` source, tested version pairing, WB decision mapping |
| Document registry supersession | Release/document-control owner | **NOT APPROVED** | Three approved exact-row edits, rollback and valid `supersededBy` |
| W-341 guide parity / W-342 runtime-vs-candidate checks | Release engineering | **NOT APPROVED** | Exact release pins, lock/package and user guide equivalence |
| Public QEAX exposure and owner classification | Source-data owner plus security | **NOT APPROVED** | Private classification and disposition of public-history reachability |
| Contributors’ local clones and A-15 work | Workstation/repository owners | **NOT APPROVED** | Private signoff of unpushed commits, stashes, branches, worktrees, BOM A-15 sources |
| Integrated importer/Base/Workbench/Bootstrap | Integration/release validation owners | **NOT APPROVED** | Exact release build and schema/artifact SHA evidence on final proposed commit |
| Mac and Windows Obsidian GUI | User acceptance representatives | **NOT APPROVED** | Real first-open, navigation, safe edit, restart and persistence results |
| Protected promotion of stacked PR chain | Repository maintainer and approver(s) | **NOT APPROVED** | Reviewed ordered stack, merge/rollback plan, baseline SHA and CI run evidence |
| Separate standalone read-only archival | Authorized repository owner | **NOT APPROVED** | Explicit post-cutover archival authorization; history remains recoverable |

A governance-text approval is **not** an archival approval. Before all gates are complete, retain both `main` branches, maintain standalone repository visibility/state, and do not erase Git history or enable unsupported Local Model `0.6` writing. Never publish unredacted contributor workstation output or QEAX model bytes as PR artifacts.

## Hard-stop acceptance logic

Every **required** gate must be explicitly approved with an attributable reference; unknown, not-started, blocked and pending states are failures. Security classification must precede any attempt to promote publicly reachable source-model content. Test results on an older commit cannot substitute for checks on the reviewed promotion commit. The companion JSON is deliberately initialized to `NOT_APPROVED` for every gate, and the verification script asserts that **no merge/archive-ready conclusion is currently possible**.

## Rollback and traceability

This entire Step 15 review package may be closed without modification to either `main`. A later accepted source-authority change should be a reviewed, revertible commit on the approved branch; record the original repo heads, exact W approval, changed registry-row IDs, user-guide lineage, build hashes and CI run IDs. The historic eight GitHub workflows remain recoverable as the same exact blobs; the generated runtime lock remains unchanged.

**Next bounded step:** demonstrate a controlled approval/readiness checklist with actual signoffs in private owner-controlled records, validate W-341 source-guide equivalence and release pin handling, and prepare promotion sequencing only after the explicit security and local-work stop gates.
