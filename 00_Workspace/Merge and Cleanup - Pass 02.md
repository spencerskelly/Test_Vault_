# Merge and Cleanup — Pass 2: Exact Sequence and Baseline Risk

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Status: MERGE PLAN ONLY — NO MERGE, RELEASE, ARCHIVE, BRANCH DELETION OR PR CLOSURE.

## New critical finding (live GitHub branch comparisons)

| Comparison | Ahead | Behind | Changed files returned | Meaning |
|---|---:|---:|---:|---|
| `main` -> Step20 `consolidation/step20-synthetic-gui-model-2026-10-11` | 1806 | 0 | 300 (API list capped) | Large unmerged history; cannot infer total file scope from truncated list |
| Step20 -> Step21 `consolidation/step21-gui-evidence-sessions-2026-10-11` | 1 | 0 | 5 | Only five added GUI evidence-session files |
| Step21 -> Step22 `consolidation/step22-single-repo-cutover-2026-10-11` | 2 | 0 | 4 | Only four added cutover/audit files |

The initial Step20 comparison's 300 returned files contain 290 added and 10 other changes, but **do not represent the full 1806-commit change set**. Do not describe a merge of PR #39 as four-file or nine-file relative to `main`.

## Practical integration routes, contingent on approval

### Route A — full stacked integration (only after baseline accepted)

1. Freeze exact `main`, Step20, Step21, Step22 commit IDs and obtain full comparison from a local `git diff --name-status main...step20` / `git log --oneline main..step20` in a clean read-only clone; compare with existing historical preservation inventory.
2. Classify the **1806-commit inherited history**, including live branch writes and any historical sensitive QEAX metadata. The 300-file GitHub compare cap makes this necessary.
3. Verify actual PR base/head/draft, protection, release boundary and CI checks in GitHub UI for #37, #38, #39. Determine whether PRs are truly stacked on their predecessor branches or all target main; do not assume from descriptions.
4. Independent review approves baseline source and governed data boundaries, then Step20 synthetic fixture, Step21 prep (5 additions), and Step22 cutover (4 additions).
5. Merge only the explicitly approved PRs using a method preserving intended history; check `main` and runtime manifest after each operation. Preserve `releaseStatus: pre-release`. No MDSE 0.8.0 release inferred.
6. Defer standalone archival and all branch deletion until separate approval.

### Route B — limited integration if 1806-commit baseline not reviewable

1. Keep Step22 and historical branches unchanged.
2. Establish an owner-approved **new** integration branch from the current `main` with explicit inclusion criteria.
3. Apply selected docs/test tooling to that new branch only after confirming their dependencies and preserving exact original commits/PR links. The Step21 preparer requires Step20 generator and governed Base/Workbench structure; blind copying nine files onto stale main is unsafe.
4. Run narrow tests and required CI on new branch and submit an independent review. Do **not** silently replace full controlled runtime, source mapping, schema or importer candidate with outdated main content.
5. Decide whether this limited PR is actually valuable before proceeding; don't create it merely to conceal the unmerged historical baseline.

### Route C — keep candidate staged for review; do not merge yet

If governance and security gate owners have not classified history, preserve the full candidate and continue use in a controlled branch. This is safer than publishing large changes to main without review.

## Merge gates (each required)

- Full inherited `main`->Step20 changes inventoried and preservation ledger checked.
- Exact PR topology, branch protection and required check results verified live.
- QEAX public-history security ownership decision and contributor unpublished-work attestation.
- Independent human review with actual submitted GitHub approval or explicit documented repository owner's review policy.
- Explicit owner go/no-go for the named PR and exact SHA.
- Correct source/status semantics maintained: MDSE release manifest stays pre-release; no W-proposal automatically ratified.
- No required safety tests falsely inferred from Step21/22 narrow CI. Keep real Mac/Windows GUI and importer/Workbench release qualification separate from repository consolidation unless touched changes require them.

## What can be decided now

- Small Step21 and Step22 *incremental* file scope and ancestry are verified.
- Full baseline merge readiness remains **UNKNOWN / HOLD** due to 1806 inherited commits and truncated file inventory.
- No justification for branch deletion is established from merge ancestry alone.
- Recommend Route A only with baseline inventory and approvals; otherwise Route C, with Route B only for independently valuable bounded changes.

## Pass 3 handoff

Use the preexisting branch ledger to classify 33 ancestor retirement candidates + 2 temporary CI probes separately from eight divergent held branches, then define exact evidence and owner-authorization conditions for any deletion batch. Do not remove refs in Pass 3.
