# Step 07 controlled Workbench cutover — review-only proposed edits

**This is a cutover proposal, not an applied patch or approval to archive.**

Baseline: `Test_Vault_` consolidation Step 06 at `090266d642e39584c2ebd9fc87e7d74d9b07cefb`. All proposed edits below must be reconciled against actual latest source at apply time. Do not edit generated plugin lock or authorize Local Model 0.6 writing.

## Atomic future cutover proposal

1. **Manifest:** `Base Vault/Definition/mdse-release.yaml` declares `tools.workbench.repo` and `repos.workbench` as `spencerskelly/MDSE_Workbench`. Replace *those current authority fields* with `spencerskelly/Test_Vault_` when governance approves, document `55_Workbench/` as the source root without silently changing the release manifest's schema. Keep `releaseStatus: pre-release`, pinned Workbench 0.1.18, Local Model 0.5 and plugin lock unchanged.
2. **Current documents:** update root `README.md`, `00_Workspace/MDSE Tool Definitions and Boundaries.md`, `00_Workspace/00 - Current State.md` so they unambiguously name `Test_Vault_/55_Workbench/` as the only active implementation location. Retain old decisions and handoffs as historical citations.
3. **CI:** root `.github/workflows/mdse-monorepo-workbench-ci.yml` already uses `working-directory: 55_Workbench`, `npm ci`, `npm run typecheck`, `npm test` and `npm run build`. Its current automatic push trigger is only `integration/workbench-subtree-2026-10-09`. Update triggers for approved current staging PRs and `main` *only after the merge topology is decided*; retain read-only GitHub permission and artifact upload, never automatic Git pushes.
4. **Release alignment CI:** root `mdse-release-alignment-preflight.yml` also needs current trigger coverage. Preserve its warning-only audit semantics in pre-release and future strict mode on an approved release gate.
5. **Historical workflows:** eight root workflow files still reference standalone `MDSE_Workbench`. They contain historical exact-source/CI evidence. Preserve frozen provenance and quarantine obsolete triggers separately; do not repoint a historical test to new input and imply it is the same evidence.
6. **Path audit:** integrate the separately tested `audit_workbench_authority.cjs` as a new *candidate* dependency classifier before revising `66_Testing/check_release_alignment.py`. It classifies old repository references in known current docs, active root workflows and executable tools as blocking; known history as informational; unknown documents as `needs_review`. Exact detector scripts are reported separately rather than silently ignored. Strict exit code 2 means unresolved active/unknown refs.
7. **Validation before cutover:** run this 33-test suite, full checkout version of the scanner, `python3 "Base Vault/Testing/check-release.py" --workbench "55_Workbench"`, Workbench `npm ci/typecheck/test/build`, importer/release alignment, CI artifact hash verification and actual Obsidian GUI first-open/edit/restart acceptance. Require QEAX owner/security classification and sign-offs of all active local clones before merging public `main` or archiving standalone.

## Candidate run commands

```sh
node --test 66_Testing/consolidation/test_workbench_authority.cjs
node --check 66_Testing/consolidation/audit_workbench_authority.cjs
node 66_Testing/consolidation/audit_workbench_authority.cjs --root . --output /tmp/mdse-authority-audit.json
node 66_Testing/consolidation/audit_workbench_authority.cjs --root . --strict
```

**Expected today:** `--strict` should fail on real pre-cutover `Test_Vault_` because active legacy references are deliberately still present; failure is a useful guard, not a reason to bypass the security or source-authority gates.

## Technical limitations

This is a Git-tracked path search using a case-sensitive exact repository string. It does not find dynamically concatenated URLs, untracked/local-only source, historical commit contents that are not in the current tree, or undisclosed external build automation. Matching only a known historical path is not proof that the file cannot be read by active code. Detector self-reference allowlisting must be maintained and reviewed if those scripts' behavior changes. No full repository/Obsidian runtime acceptance was run in this step.
