# Step 22 — Single-repository Workbench cutover and reversible shutdown

**Proposed operating policy from 2026-10-11:** **Use `spencerskelly/Test_Vault_` for all NEW MDSE Workbench code, model interface and test development. Stop beginning work in the standalone Workbench repository.** Until consolidation PRs are promoted, target the pinned consolidation branch from Step 21 (or a new topic branch based on it); **do not mistake `Test_Vault_/main` for an integrated Workbench source checkout**.

**Scope:** Only the repository development location is being retired. This does **not** ratify pending W/Workbench source-authority decisions, schema proposals, BOM quantities, Local Model 0.6 writing, an engineering release or GUI acceptance. New design decisions can be reviewed after the source home is unambiguous.

## Verified remote-source inventory

On 2026-10-11, the complete GitHub file tree of Workbench `main` (`59fc6219b1d0586900aa7d38685e7087a9d47fec`) and the consolidated `Test_Vault_/55_Workbench/` at Step 21 (`952aaecfc16891f2155b78f174340fd70e764683`) were compared by path and exact Git blob SHA.

| Test | Verified count |
| --- | ---: |
| Old Workbench main files | 60,193 |
| Consolidated Workbench candidate files | 60,249 |
| Exact same path **and** Git blob SHA | 60,175 |
| Source paths absent from consolidated candidate | **0** |
| Same path with changed source content | **18** |
| Additional consolidated candidate paths | 56 |

The 18 differences include Workbench source and test revisions made on consolidation staging, `package.json`, and intentional authority/documentation changes. **Do not overwrite these newer staged files with older standalone branch tips** just to make hashes equal.

The remote has **19 branches, three open draft PRs, and no independent open issues**. A frozen, Git-SHA-anchored inventory is at `66_Testing/consolidation/step22_legacy_workbench_inventory.json` and preserves all 19 ref names/tip SHAs, #6/#7/#15 details, exact base/candidate SHA and proposed owner decisions. Old GitHub history is preserved by keeping the original repo in read-only/archive state; do not delete it.

| Old draft PR | Disposition |
| --- | --- |
| [#6](https://github.com/spencerskelly/MDSE_Workbench/pull/6) Local Model 0.5 equals | Preserve as historical/proposed; replacement coding occurs in `55_Workbench/` with governance review |
| [#7](https://github.com/spencerskelly/MDSE_Workbench/pull/7) WB-129 test alignment | Preserve source/test evidence; later targeted regression, no old-branch auto-merge |
| [#15](https://github.com/spencerskelly/MDSE_Workbench/pull/15) BOM A-01–A-14 recovery | The remote tip's code, original BOM notes, source manifest and artifacts already have corresponding paths in consolidated staging; keep proposals unratified |

The older BOM A14 baseline-check workflow originally at `.github/workflows/bom-a14-baseline-check.yml` is preserved at `55_Workbench/docs/Reference/ARCHIVE_BOM_A14_BASELINE_CHECK.yml`, **exact matching Git blob** `3c58fa778d60b7e3d425f67972c136da726b7740`.

## What we can do NOW to work in one place

1. **Stop editing the standalone repository.** Prefer a dated handoff/deprecation notice in the old `README.md` that directs contributors to the tested consolidation branch, while preserving existing content. Disable old edit/build scheduling only after all target branches are captured.
2. **Use the same working root for all topics:** `Test_Vault_/55_Workbench/` for Workbench; `Importer/` for EA translation; `Base Vault/` for controlled runtime; `Bootstrap/` for first-open; `99_System/` for governed semantics. Build a new topic branch off the current tested consolidation SHA and keep final changes in draft PRs until authority is promoted.
3. **Retain historical references, don't transplant older code over newer candidates.** Three old open PRs are recorded as unapproved/historical. The BOM/variant proposed authoring updates and Local Model 0.6 remain separate design-review topics.
4. **Have any workstation users verify there is no unique unpushed work.** Check `git status --short`, `git branch -vv`, `git stash list`, and `git worktree list` in the old local clone. Archive is *reversible*, but archived GitHub repos do not accept normal pushes. Private unresolved local work can be moved to an isolated topic branch inside `Test_Vault_`, keeping source attribution.
5. **Archive standalone Workbench through its GitHub repository settings** once local-work owners are satisfied. Do not **delete**, change visibility, remove protected source/branch records, or erase old PRs. If an unexpected source change is later required, unarchive for recovery and track the change back in the unified repository. A historical archive remains externally readable but is no longer an active workplace.
6. **Promote the stacked Test_Vault_ consolidation PR chain separately**, only after the proposed source-authority W decision, public QEAX owner/security review, document-registry classifications, and protected merge review. The archive of the **old** repo is not by itself permission to promote unsafe material into `Test_Vault_/main`. The present Step21 branch and its CI are a safe recoverable development baseline while this happens.

## Explicit GitHub archive control

In the standalone GitHub repository: **Settings → General → Danger Zone → Archive this repository**, confirm the GitHub prompt. This requires repository administration rights. The GitHub connector actions available in this session have source-file, branch and PR mutation capabilities but **no action to change a repository's archived setting**. Do not report the repository as archived until the GitHub metadata says `archived: true`.

## Stop conditions

- **No destructive branch deletion** or forced rewrite of the 19 old remote branch tips.
- Do not claim external workstation coverage from a GitHub-only inventory.
- Do not declare `Test_Vault_/main` complete until its approved cutover has actually merged.
- Do not contaminate live Local Model 0.5 with experimental 0.6 writers or treat old BOM proposals as approved.
- Preserve W decision history and the frozen Workbench artifact source labels in the plugin lock.
- QEAX source/public-history security disposition and human Obsidian GUI acceptance remain open independent of old-repo archival.

**End state sought:** only `Test_Vault_` accepts new changes; Workbench is a source subdirectory, the old standalone repo is a frozen historical archive, and new decisions are handled as reviewed changes in the single active repo.

## Completed shutdown preparation — verified 2026-10-11

- **Old repository root README now redirects all new development to Test_Vault_.** Original text was retained after a prominent transition notice. New old-main commit: `721814d8204fc2f0e69e7e2523f70dc0fe3603dd`; README blob: `390cc113332d2ebe456473036c9c7ca5046006e8`.
- **Old Workbench open draft PRs #6, #7 and #15 were closed WITHOUT MERGE** with comments linking to [Test_Vault_ issue #40](https://github.com/spencerskelly/Test_Vault_/issues/40). This preserves the exact branches and original discussion while ensuring no active review work remains there.
- The 19 old branch tips and previous `main` hash in `step22_legacy_workbench_inventory.json` are a **pre-redirect historical snapshot**. The new README notice advances old `main` by exactly one documentation-only commit; do not falsely report the old baseline SHA as its current tip.
- [Test_Vault_ issue #40](https://github.com/spencerskelly/Test_Vault_/issues/40) now tracks the only remaining repository shutdown action and the deferred local-work signoffs.
- The connected GitHub actions **cannot set repository archived=true**. At this checkpoint GitHub reports the old repository remains **unarchived**. The owner must use its archive setting; do not report completed archival until verified.
- This is a **development-location cutover**, not a public `Test_Vault_/main` promotion, an approved new W decision, or actual Obsidian GUI acceptance.
