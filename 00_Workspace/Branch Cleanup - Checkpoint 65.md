# Branch Cleanup — Checkpoint BR-65: Minimal Step21 Negative-Test Implementation Plan

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Candidate: consolidation/step22-single-repo-cutover-2026-10-11 at 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: IMPLEMENTATION SPECIFICATION ONLY — existing 29 tests and runtime remain unchanged.

## Grounded baseline

BR-63 reviewed `66_Testing/consolidation/step21_prepare_session.py` (blob `ca675504709bf1cde00c2c97ee967224c160a466`) and evidence validator `step21_evidence.py` (blob `c3fb98d401b2bf698a03e782a46f868532690b42`).
BR-64 read all `66_Testing/consolidation/test_step21_evidence.py` (blob `581dee57192d0c3b7e9ddb0b83216bcf167247cf`): 29 test methods; no dedicated checker-warning, post-workspace failure or expected-commit mismatch test.

**Acceptance boundary:** Step21 session preparation is not MDSE release approval. A pre-release warning should not be silently declared approved. Session creation may remain possible with recorded warnings, but never turn a prepared template into operator evidence or release authority.

## Three narrowly scoped tests, in priority order

### N01 — release checker warnings are visible and not approval
Fixture: use a disposable temp root and mocked subprocess responses for the builder, checker, generator and structural validator. Simulate successful checker exit 0 with stdout `0 fail, 4 warn`; ensure no real governed plugin paths, QEAX, Git remotes or Obsidian processes are touched.
Existing behavior: `step21_prepare_session.invoke` tests only return code and `prepare` looks for substring `0 fail,`; therefore this text does not block preparation. **Do not write a test that asserts a new mandatory blocker before agreeing on behavior.**
Desired new behavior proposal: preserve warning count and a distinct `WARNING_REVIEW_PENDING` in a private handoff record/log (outside generated Base), or record explicit human-reviewed disposition before any downstream candidate acceptance. All GUI rows remain NOT RUN; `guiApproval` remains NOT_APPROVED; never set release/archival permission.
Pass criterion: no successful pre-release checker run with warnings can be *represented* as released, zero-warning, or human-approved.
Owner choice required before production change: warning count capture only, versus refuse prepare until a private warning disposition exists.

### N02 — interrupted session preparation fails closed
Fixture: use a disposable path that does not exist before invocation; stub controlled calls or inject a failure during synthetic generation/structural validation **after** `work.mkdir` and clean Base stage; include a unique sentinel outside workspace.
Existing behavior: exception may leave private partial directory and logs; it does not automatically produce a completed `PRIVATE_GUI_RESULTS.json`.
Desired invariant: nonzero process result / exception, no successful `STEP21_SESSION_PREPARED` line, no usable `PRIVATE_GUI_RESULTS.json` with observed PASS or REVIEWED, and sentinel/existing repository unchanged. Leave safe diagnostics intact; never recursively delete an arbitrary user path.
Pass criterion: partial creation cannot be mistaken for a successful prepared or approved session.
Do not claim atomic rollback is implemented.

### N03 — exact source SHA mismatch rejected before writing
Fixture: patch `git_commit` to a synthetic valid 40-character SHA and call `prepare(<new temp path>, platform='macos', expected_commit=<different valid SHA>)`.
Existing behavior: `prepare` compares `expected_commit` before `work.mkdir` and raises `ValueError` on mismatch.
Pass criterion: raises the expected error and destination remains nonexistent. This is an inexpensive regression test for an already-implemented safety guard. Repeat for Windows parameter only if platform-specific path differs (none visible in this precondition).

## Suggested change scope for a separate reviewed PR

- Tests only initially: add `test_expected_commit_mismatch_no_directory_created` and `test_interrupted_preparation_not_accepted` to `66_Testing/consolidation/test_step21_evidence.py`.
- For warning review, first agree the concrete acceptance contract and then add `test_checker_warnings_remain_unapproved`. Introduce the minimum implementation only if a test proves the desired status cannot currently be represented.
- Keep unchanged: `Base Vault/Definition/mdse-release.yaml`, `Base Vault/Testing/check-release.py`, plugin lock, 16 G20 evidence IDs, controlled runtime scripts, QEAX source, old standalone Workbench repo.
- Verify with `python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step21_evidence.py' -v` and, after approved changes, the existing Step21 sparse CI. These tests are not real GUI acceptance.

## Minimal execution ledger

| Item | Spec prepared | Implemented | Executed |
|---|---|---|---|
| N01 warnings review | YES | NO | NO |
| N02 interrupted preparation | YES | NO | NO |
| N03 expected-commit mismatch | YES | NO | NO |
| 29 existing Step21 tests | READ | NOT MODIFIED | NOT RERUN |
| Mac and Windows operator GUI | REQUIRED | N/A | NOT RUN |

## Owner review and handoff

Review whether Step21's warning state should be a visible pending disposition or a preparation stop; choose a private evidence field and no new file in generated Base. Then create a separate scoped topic PR for tests. Do not silently alter audit branch's purpose or claim that a proposed test is running.

BR-65 outcome: Three precise synthetic fixtures, expected behavior and bounded change set defined. No code, CI or PR status changed.
NEXT BR-66: Return to a distinct demonstrable cleanup/release evidence item or implement approved tests in a separately reviewed topic branch if authorized. Avoid further rewordings of this spec.
