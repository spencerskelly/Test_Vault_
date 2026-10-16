# MDSE v0.8 — Unified Development Continuation Contract (PROPOSAL)

**Prepared:** 2026-10-10  
**Status:** **PROPOSAL / REVIEW ONLY. NOT AN APPROVED W DECISION OR CURRENT RELEASE AUTHORITY.**  
**Context:** `Test_Vault_` consolidated development staging through Step 12, parent commit `af77492c895dc31d2b28b74d8ded15947d617298`. This document must not be presented as an issued release, a validated Obsidian engineering vault, or permission to archive the former standalone Workbench repo.  
**Proposed successor to:** `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md` and `00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`, for their *current execution and source-ownership instructions only*. Their original dated engineering decisions and source evidence are preserved.

## 1. Authority and boundary (candidate, pending ratification)

The proposed **single continuing development repository** is `spencerskelly/Test_Vault_`. Its tool-specific source roots are `Importer/` (EA native translator), `Bootstrap/` (activation and author initialization), `Base Vault/` (controlled release, config and packaged runtime), and `55_Workbench/` (Workbench source, tests, implementation and product definition). The shared model schemas, methodology, W decisions and AI authoring contracts remain governed by `99_System/` and the current registered definitions.

The former standalone Workbench repository, its branches and original CI runs remain preserved for source history. They are **not archived** by this proposal. Eight obsolete source-checkout workflows were moved byte-identically into `55_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/` *on consolidation staging only*; other branches may still contain their original workflow definitions. Old test results are historical evidence, not tests that can be claimed for new code.

### Authority precedence

- **Current governed source:** `Base Vault/Definition/mdse-release.yaml` for pinned release/version/configuration and document registry; `99_System/03_Schemas/` and `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` for semantics; approved `00_Workspace/Workspace Decision Log.md` decisions for changes in meaning.
- **Current engineering process:** `00_Workspace/00 - Current State.md`, `00_Workspace/MDSE Tool Definitions and Boundaries.md`, and `00_Workspace/MDSE Plan - Path to a Golden Model.md`, read in light of their expressly dated checkpoints. The latter two include historical guidance that must not override newer verified versions.
- **This document:** new recommended continuation instructions **only once formally approved and reclassified to `current`**. Until then its registry status is `proposal`, and old current registrations are not silently changed.
- **Preserved history:** earlier Workbench milestones, WB-128/WB-129 acceptance reports, W-325/W-328/W-329/W-341/W-342, old Oct 2/Oct 5 snapshots and BOM A-01–A-14 source-recovery evidence remain attributed to their dates and original commits. Do not rewrite them to make the present release appear older or newer than actually verified.

## 2. Reconciled staging versions — not final integrated release

| Contract | Verified candidate baseline from the staging manifest | Significance |
| --- | --- | --- |
| MDSE | `0.8.0`, `releaseStatus: pre-release` | No final issued engineering Base Vault |
| Relationships schema | `1.36` | Governed in `99_System/03_Schemas/relationships.yaml` |
| Element types | `1.18` | Governed in `99_System/03_Schemas/element-types.yaml` |
| Local Model | `0.5` | Earlier `0.2` and `0.4` handoff claims are dated evidence, not current staging pins |
| Importer | `v0.8.19` **candidate**, release field `null` | Deterministic candidate evidence does not establish release conformity |
| Workbench | `0.1.18` pinned; `55_Workbench/` source candidate | Keep runtime and generated plugin-lock provenance hash-controlled; no writer 0.6 authority |
| Bootstrap | `0.3.0` runtime; `0.3.1` source candidate | First-open, activation, persistence, Mac/Windows checks remain gating |
| Release lock | `.obsidian/plugin-lock.yaml` unchanged | Pinned 0.1.18 artifact source labels are frozen provenance, not instructions to re-fetch standalone implementation |

No local model-schema expansion or schema reinterpretation is introduced here. Where the October 2 continuation, older roadmap, or October 5 handoff describes `1.35/1.17/0.2` or Workbench's earlier 0.4 write target, those are **historical snapshots** and must not be used to overwrite the manifest's staging `1.36/1.18/0.5` values.

## 3. Where to work and what to read next

Use the approved consolidated repository branch and these paths instead of starting new Workbench implementation in the old standalone clone:

1. `00_Workspace/00 - Current State.md` and `00_Workspace/MDSE Tool Definitions and Boundaries.md`: current/mixed checkpoints, explicit staging limitations.
2. `00_Workspace/MDSE Plan - Path to a Golden Model.md` and `00_Workspace/Post-Import Tasks.md`: user-facing G2/Golden Model acceptance and post-import requirements.
3. `Base Vault/Definition/mdse-release.yaml`, `.obsidian/plugin-lock.yaml`, `Base Vault/Testing/`: pinned runtime contract, generated lock and release verification.
4. `Importer/Definition/Translator Definition.md` and `Importer/Definition/Importer Operating Contract.md`: translation semantics, run states and evidence.
5. `55_Workbench/docs/Definition/`, `55_Workbench/package.json`, and current `55_Workbench/` source/tests: Workbench behavior, WB decisions, ModelRef UI and Local Model compatibility.
6. `00_Workspace/Workspace Decision Log.md` and `99_System/03_Schemas/`: approvals and semantic authority.
7. `00_Workspace/Consolidation Step 12 - Remaining Workbench Reference Dispositions 2026-10-10.json`: five unresolved older living/handoff documents. The archived test reports remain readable but are not current implementation instructions.

## 4. Remaining critical path, without release shortcuts

1. **Security/source classification:** authorized owner must classify the publicly reachable EA/QEAX ZIP and decide whether exposure response/public-history remediation is necessary. The historical public branch and object reachability cannot be cleared by merely excluding it from a current checkout.
2. **Unpushed local work:** every active developer workstation, branch without upstream, dirty tree, worktree and stash must be reviewed and signed off privately. Local clone audit scripts are available but have not been executed across contributors.
3. **Governance:** assign and approve a new W decision explicitly superseding *only the source-authority clauses* of W-328/W-329; ratify this continuation contract and the document registry transition. Original W decisions stay byte-identical.
4. **Documentation:** reconcile the five unresolved Step 12 files using their exact source hashes; preserve original milestone/version statements where they are genuinely historical. Do not mark the outdated current handoff/reconciliation as superseded until the replacement is approved.
5. **Integration:** repeat Workbench typecheck/test/build, importer output + release-conformance checks, controlled Base build/lock/payload SHA verification, Bootstrap Mac and Windows first-open checks, and real Obsidian GUI create/read/edit/restart acceptance on a signed candidate.
6. **Promotion:** only after the above gates and reviewer approval, merge the reviewed consolidation PR chain into the approved authoritative target; **archival is a separate deliberate action**. Retain the standalone repository in read-only history rather than deleting it.

## 5. Copy-ready proposed continuation instructions

> Continue MDSE v0.8 consolidation in `spencerskelly/Test_Vault_` on the reviewed staging branch. The proposed Workbench implementation root is `55_Workbench/`; original standalone Git history and frozen artifact provenance remain preserved. Read the current manifest and schemas before assuming versions: release `0.8.0` **pre-release**, relationships `1.36`, element types `1.18`, Local Model `0.5`, importer `v0.8.19` candidate, Workbench pinned `0.1.18`, Bootstrap runtime `0.3.0` and candidate `0.3.1`. Complete one bounded, recorded review step at a time. Preserve W/WB history and existing plugin-lock bytes. Do not activate Local Model 0.6 writing, merge public `main`, close source-exposure concerns, or archive the former standalone repository without their explicit approvals. Remaining gates are the public QEAX owner review, contributor local work sign-off, current-doc supersession, released matched artifacts, and real Obsidian GUI first-open/read/edit/restart.

**This is a review-only prompt and will become operative solely on explicit ratification.** Its existence as a file does not make it the source of authority.

## 6. Review and controlled rollback

The transition ledger in `00_Workspace/Consolidation Step 13 - Document Registry Transition Plan 2026-10-10.md` records the exact status and successor updates to make after approval. This candidate does not rewrite any of the five Step 12 source files, their Git blobs, the W log or the generated plugin lock. If the proposal is rejected, remove/revert its two `documents:` registrations and this proposed file in the review branch; do not edit historical decisions or force-push shared Git history.
