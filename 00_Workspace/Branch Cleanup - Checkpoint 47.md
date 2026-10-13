# Branch Cleanup — Checkpoint BR-47: Exact Workflow Tree Enumeration Boundary

**Date:** 2026-10-12
**Repo:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Step22 candidate:** `consolidation/step22-single-repo-cutover-2026-10-11` @ `58ab10870f11757cf1bf367ecd5868be9b60933d`
**Status:** PARTIAL — exact workflow directory list not yet obtainable from connected interfaces; do not claim exhaustive CI inventory.

## New verification

- Inspected available connected GitHub operations. They can read a **known file** at a named ref, search indexed code on the default branch, and read workflow runs by known commit/run identifiers. They do **not** expose a read-only recursive Git tree/directory listing operation in this environment.
- Tried fetching `.github/workflows` at the exact Step22 branch using `fetch_file`. Connector correctly returned **InvalidInputException: path points to a directory, not a file**. This is not proof that the directory or workflows are missing.
- Attempted public GitHub REST tree URL lookup through web access at SHA `58ab108...`; this environment could not access that URL. Do not infer the repo is absent or private from this transport error.
- Existing `.github/workflows/consolidation-step22-cutover.yml` remains a **directly fetched file** at Step22 (blob `e23e950f81ea5dcdc88789fbd7a3eddfe05ad478`). It runs only cutover inventory checks, not complete MDSE release validation; see BR-43–BR-46.
- No other workflow should be asserted absent from the Step22 tree based on guesses or default-branch code search.

## Safe exact-tree capture procedure (approved clean local checkout)

```bash
set -euo pipefail
git remote get-url origin
git fetch --no-tags origin '+refs/heads/consolidation/step22-single-repo-cutover-2026-10-11:refs/remotes/origin/consolidation/step22-single-repo-cutover-2026-10-11'
ref='origin/consolidation/step22-single-repo-cutover-2026-10-11'
test "$(git rev-parse "$ref")" = '58ab10870f11757cf1bf367ecd5868be9b60933d'
git ls-tree -r --name-only "$ref" -- .github/workflows
```

Review filenames for sensitive information prior to publishing audit logs. For **each** enumerated workflow file, read with `git show "$ref:.github/workflows/FILE.yml"` locally; capture path, triggers/branches/path filters, commands, platform, security permissions and exact job checks. Never execute the old write-enabled WB106 integration workflow or materialize protected QEAX archive just to inspect CI coverage.

## Test matrix needing exhaustive wiring evidence

| Required acceptance | Code exists | Confirmed actual Step22 workflow invocation |
|---|---|---|
| Historical standalone repo inventory and 14 retirement tests | Yes | Yes: scoped Step22 workflow, historical success |
| Base Vault release checker (basic) | Yes | Unverified |
| Workbench fixture/user-guide parity `--workbench` | Yes | Unverified |
| Deterministic Base builder and parity `--base` | Yes | Unverified |
| Importer, Bootstrap and Workbench end-to-end tests | Tests/documentation exist, exact current suite inventory not done | Unverified |
| Real model QEAX import | Depends on owner/security approval | No approval to run |
| Mac/Windows Obsidian GUI acceptance | Manual procedure | Not established by CI |
| W/document approval and local clone security | Human governance | Not CI-automatable |

## Decision / next action

To avoid another nominal inventory pass, **BR-48** should move to a directly verifiable source-quality gate (e.g. actual generated Base release source/test quality or importer contract), or consume a sanitized full exact-tree listing if obtained through an authorized local checkout. Do not add duplicate CI until real workflow inventory is complete.

**BR-47 result:** Explicitly tested directory read and public tree access boundaries, grounded only known workflow and supplied deterministic local enumeration procedure. No exhaustive workflow listing or release tests performed.

**No mutation:** No merge, PR closure, branch deletion, workflow edit, release promotion, repo archive, or model-content access.
