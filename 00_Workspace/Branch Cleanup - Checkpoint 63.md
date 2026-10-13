# Branch Cleanup — Checkpoint BR-63: Step21 GUI Evidence Tooling Review

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Candidate: consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: SOURCE REVIEW ONLY; no GUI session executed.

## Exact Step21 source inventory

Verified Step20 to Step21 comparison shows five introduced files:
- `.github/workflows/consolidation-step21-gui-evidence.yml` — blob `78c185e694bee3c9e4a6fe7e7e2a68a55ef13c82`
- `66_Testing/consolidation/STEP21_MAC_WINDOWS_GUI_SESSION.md` — blob `305e5e00661c332726435e950fa7fc1fa13d3b5c`
- `66_Testing/consolidation/step21_evidence.py` — blob `c3fb98d401b2bf698a03e782a46f868532690b42`
- `66_Testing/consolidation/step21_prepare_session.py` — blob `ca675504709bf1cde00c2c97ee967224c160a466`
- `66_Testing/consolidation/test_step21_evidence.py` — not inspected in full in this checkpoint. PR #38 describes 29 validation tests; no independent count from source was performed here.

All four named source files above were fetched directly from Step22. The candidate retains Step21 files, and the Step21-to-Step22 comparison lists only four added Step22 files.

## Verified controls

- Preparer enforces new private output folder **outside** checkout and refuses overwrite; obtains Git HEAD and optionally checks `--expected-commit`.
- Preparer executes controlled r2 Base builder, `check-release.py --workbench 55_Workbench --base <clean>`, synthetic fixture generator and structural validator, then compares generated plugin lock bytes to authority and hashes the fixed 12-note synthetic snapshot.
- Preparer produces separate clean uninitialized Base and synthetic GUI vault, plus 16-case NOT RUN private JSON. It does not launch Obsidian, initialize author code, create remote or upload evidence.
- Evidence validator demands consistent synthetic-only schema, 40-hex source SHA, 64-hex lock/fixture digests; 16 ordered G20 cases; actual text/time/private refs for terminal results; defect reference for FAIL; source/fixture/lock match across Mac and Windows.
- Reviewer-marked complete cases still yield `externalPromotionGatesCleared: False`, `releaseIssued: False`; cross-platform validator always returns `publicMainPromotionAllowed: False`, `standaloneArchiveAllowed: False`.
- Workflow is `contents: read`, branch scoped, sparse-checkout excludes QEAX ZIP, runs validation on Linux in target-platform *template* mode, and does not upload sensitive artifacts.

## Confirmed gaps / quality boundary

1. **Real GUI execution pending.** The operator guide explicitly states both platform worksheets and all GUI cases NOT RUN, reviewer not assigned. Linux CI cannot observe Mac/Windows Obsidian behavior.
2. **Pre-release warning disposition is not enforced in preparer.** `invoke` requires checker exit zero; preparer also requires substring `0 fail,` in stdout. It does not parse/require formal disposition for nonzero warning count before generating a worksheet. The human instructions say to record four existing pre-release warnings. A validated session template therefore indicates readiness for observation, not release approval.
3. **Partial private workspaces may persist after failed preparation.** `prepare` creates output before invoking builder/checker/generator; exceptions can leave a private diagnostic folder. This is not evidence of publishing a validated vault. Operator must distinguish failed staging from a prepared copy; never automatically remove a user path.
4. **Platform argument is declarative.** Documentation correctly warns that `--platform macos/windows` does not verify the physical OS or human session. Only real host operator records count as GUI evidence.
5. **Human reviewer identity is not authenticated by JSON fields.** Validator checks presence and logical completeness; it cannot prove actual human identity or independently verify screenshots. External controlled review is necessary.

## Small scoped improvement proposals (NOT IMPLEMENTED)

- Record release warning count and private approval/disposition reference as a mandatory Stage21 entry checklist before human GUI session signoff; leave current pre-release warnings visible.
- Add a synthetic negative test for checker exit-zero with nonzero warnings and for interrupted preparation, asserting they cannot be misreported as released or observed GUI PASS.
- Preserve `expected_commit` in operator commands for the reviewed baseline (currently optional), especially to prevent cross-platform drift.
- When results are available, compare the two private reviewed G20 worksheets at identical source/lock/fixture SHA, then separately resolve W/governance, QEAX security, local Git and main promotion gates.

## Outcome and next

BR-63 completed source inspection and identified one testable evidence-control gap without changing controlled code. No real Mac or Windows session, QEAX access, CI run, merge, deletion, PR approval or archive performed.

NEXT BR-64: Review the existing 29-case Step21 test file for current coverage of the warning-handling and interrupted-preparation gaps before proposing any duplicated tests.
