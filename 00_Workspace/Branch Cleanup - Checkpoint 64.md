# Branch Cleanup — Checkpoint BR-64: Existing Step21 Evidence Test Coverage

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Candidate: consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
Audit PR: #41
Status: Complete static source inspection; no test execution.

## Source inspected
`66_Testing/consolidation/test_step21_evidence.py` Git blob `581dee57192d0c3b7e9ddb0b83216bcf167247cf`. The source contains **29** `test_*` methods in class `Step21EvidenceTests`.

## What is directly tested
- Canonical 16 G20 case IDs and default NOT RUN records on both target platforms.
- Incomplete/misformatted case evidence: missing refs, empty actual observation, invalid UTC timestamp, missing OS/Obsidian version, missing defect link for FAIL, absent observation on BLOCKED, unsupported status spelling, NOT RUN containing screenshot, duplicate case ID.
- Invalid platform, SHA-40 commit and SHA-256 plugin-lock string; target-platform mismatch and improper other-platform PASS.
- Reviewer approval cannot be prematurely applied; a syntactically complete record still sets `externalPromotionGatesCleared=false` and `releaseIssued=false`.
- Both reviewed Mac/Windows *syntactic* PASS records cannot authorize public main promotion or standalone archive.
- Pair rejects different source commit, plugin lock and synthetic fixture digest.
- Preparer rejects workspaces inside repo and rejects an existing private session directory without overwrite.
- Evidence JSON roundtrip retains all NOT RUN cases.

## Confirmed gaps in THIS file
1. **Warning disposition not tested:** no test injects checker exit zero with nonzero warnings and verifies reviewed warning disposition before session release/approval. The source preparer checks subprocess exit and a `0 fail,` text substring only; the user guide explicitly says to record four pre-release warnings.
2. **Late failed preparation not tested:** no test injects a failure after `prepare` has created its workspace, then asserts no session is accepted as prepared and no stale pending record may be used as evidence. There are tests for paths existing before execution, not interrupted post-creation state.
3. **Actual workstation GUI behavior not tested:** the 29 cases are Python tests; their green result is not human Obsidian acceptance. Required Mac/Windows session evidence remains NOT RUN by project documentation.

## Minimum nonduplicative follow-up (proposal only)
- N01: synthetic mocked `invoke(NATIVE,...)` returns `0 fail, 4 warn` / exit 0. Confirm the wrapper records a distinct unresolved warning review status and does not label generated session as release-qualified. The current wrapper is preparation-only; do not suppress useful template preparation unnecessarily—only enforce release-owner signoff boundary.
- N02: mocked mid-workflow failure after private workspace creation, verifying no successful-preparation marker and clear failure diagnostics, no overwrite of existing user files.
- N03: mismatched `--expected-commit` refuses session creation; this is implemented already but lacks explicit test in inspected suite.
- Keep all tests synthetic and isolated; no actual QEAX, active vault or remote modifications.

## Limitations
Static reading supports test method presence and assertions, not whether all 29 passed in a current run. CI workflow calls this suite, but this checkpoint did not run it. Do not claim the suite detects a failure mode it does not exercise.

**BR-64 output:** Test inventory checked and coverage gaps narrowed to release-warning approval, interrupted preparation and a missing explicit expected-commit test. No code changes.
**NEXT BR-65:** Prepare a minimal, separately reviewable three-test patch plan and choose the correct acceptance boundary; do not broaden the cleanup audit into a production-code rewrite without authorization.
No merges, PR closure, branch deletion, release, archive or QEAX access.
