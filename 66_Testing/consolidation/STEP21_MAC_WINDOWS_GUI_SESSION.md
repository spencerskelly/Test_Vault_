# Consolidation Step 21 — Controlled Mac/Windows GUI evidence sessions

**Status: PREPARATION ONLY. No Obsidian GUI was opened; all G20-01 through G20-16 results remain NOT RUN.**  
**Parent:** Step 20 draft PR #37, source `fbaa400fd9613b7abf2d32cab09c0bdafe8cb8ce`. Use the latest reviewed Step 21 commit when preparing both test machines, recording its exact 40-character SHA.  
**Model under test:** only 12 synthetic MDSE notes, 3 Parts, 3 Interfaces, 1 Connection, 1 Flow. Governed schemas 1.36 / 1.18 / Local Model 0.5; Workbench 0.1.18 locked runtime.

## Operator preparation

Use a fresh, isolated checkout of the exact Step 21 draft branch and **a private writable output directory outside the checkout** on each system. Do not run this against Test_Vault_, Ampure_Data, PosiBattery, an imported production model, or an existing initialized vault. Do not download or unpack the publicly reachable QEAX ZIP.

Check that Git, Python 3 and PyYAML 6.0.2 are available. On macOS:

```sh
python3 -m pip install 'PyYAML==6.0.2'
python3 66_Testing/consolidation/step21_prepare_session.py \
  --platform macos \
  --workspace "$HOME/Documents/Step21_GUI_Mac"
```

On Windows in PowerShell from the repository root:

```powershell
py -3 -m pip install PyYAML==6.0.2
py -3 66_Testing/consolidation/step21_prepare_session.py --platform windows --workspace "$env:USERPROFILE\Documents\Step21_GUI_Windows"
```

Use **new output directories**; the command refuses to overwrite existing files or write private results under the repository. The helper builds a clean Base from the controlled r2 builder, invokes the unchanged native `check-release.py --workbench 55_Workbench --base <clean base>`, seeds the approved Step20 synthetic folder into a second disposable vault, verifies model links/Local Model and writes:

- `01_Clean_Uninitialized_Base/` — independent, untouched generated Base evidence
- `02_Synthetic_GUI_Vault/` — separate test copy to initialize and open in Obsidian
- `PRIVATE_GUI_RESULTS.json` — all sixteen cases initialized `NOT RUN`, with source-commit SHA, fixture snapshot SHA-256 and exact plugin-lock SHA-256
- `PRIVATE_* .log` and `README_PRIVATE_SESSION.txt` — preparation diagnostics and next actions, **local only**

The `--platform` argument specifies the intended host; the helper cannot verify a real operator or desktop Obsidian session. GitHub CI prepares disposable templates on Linux as a software check, **not** as Mac/Windows user acceptance. A successful preparation log is not GUI evidence.

## Actual Obsidian steps (on each operator's real host)

1. Record the exact checked-out SHA, OS version, application and plugin versions **as actually observed**, and a private operator alias. Keep screenshot/log references locally; do not commit personal paths or machine identifiers.
2. Back up `02_Synthetic_GUI_Vault/` before initialization. Change into that vault's directory and initialize **that copy only** using the generated `Initialize-Vault.sh` (macOS: `sh ./Initialize-Vault.sh "Step21 Mac Synthetic" <13-letter-author-code>`) or `Initialize-Vault.ps1` (Windows: `./Initialize-Vault.ps1 -Name "Step21 Windows Synthetic" -AuthorCode <13-letter-author-code>`). Replace the angle-bracket placeholder with an approved, unique 13-character lowercase ASCII code; do not type literal brackets.
3. Open the initialized synthetic folder as a *new vault* in Obsidian desktop 1.13.0+ on that host. Trust the bundled plugins for this isolated copy only. Do not connect sync or any remote Git repository.
4. Run `STEP20_GUI_ACCEPTANCE.md` from inside `88_Step20_Synthetic_GUI_Model/`. Exercise G20-01–G20-14, plus G20-15 on macOS or G20-16 on Windows. The other system's platform row remains `NOT RUN`.
5. For every observed result, fill the case's `status`, actual `observed` description, `observedAtUtc` in ISO-8601 UTC (for example `2026-10-11T23:00:00Z`) and one or more *private* `evidenceRefs`. A `FAIL` must also have a `defectRef`. Fill session-level actual `operatorAlias`, `osVersion`, `obsidianVersion`, `observedWorkbenchVersion`, `observedBootstrapVersion`, and `sessionStartUtc`.
6. Set `reviewerAlias` and `guiApproval: REVIEWED` only after a real reviewer has examined the full functional and platform results. Do not use automatic test output as reviewer evidence; do not change `securityAndLocalCloneGates` to clear release/security blockers.
7. Validate each private evidence worksheet from an isolated source checkout, without copying it into the repository:

```sh
python3 66_Testing/consolidation/step21_evidence.py --check "/private/path/PRIVATE_GUI_RESULTS.json"
```

After **both actual** platform sessions, validate their matching source/fixture/lock baselines:

```sh
python3 66_Testing/consolidation/step21_evidence.py --check "/private/mac/PRIVATE_GUI_RESULTS.json" "/private/windows/PRIVATE_GUI_RESULTS.json"
```

The validator prints **aggregate counts only**. It rejects fabricated-ready records missing actual observations, timestamps or evidence references, rejects cross-platform source/lock drift, and refuses to turn a single-platform pass into cross-platform approval. Even a complete reviewed evidence form does **not** authorize `main` promotion, release issue or standalone Workbench archival. Keep actual evidence in a controlled private location.

## Entry, exit and abnormal-result criteria

**Entry:** Build and native checker succeed on clean Base; synthetic structural validator succeeds; both source/fixture SHA-256s recorded; output directories are disposable; approved known-version plugins unchanged; test operator has a backup; no QEAX or production model in scope. The existing four pre-release native warnings must be recorded rather than silently deleted.

**Functional exit:** On each real OS, pass G20-01–G20-14 plus that platform's own G20-15/16 with real evidence. One `FAIL` or `BLOCKED` keeps that platform OPEN. The other OS's row cannot be satisfied by the first. GUI approval must come from a real owner after human observations; tool validation is only a format/consistency check.

**When blocked:** Capture observed/expected, approximate reproduction, defect reference, affected command/view and scrubbed logs, using private paths; do not modify the controlled plugin lock, governed schema, or historical decision. Restore the synthetic copy from its disposable backup before re-running. Leave incomplete cases `NOT RUN` or `BLOCKED`.

**Separate global stop gates:** the public QEAX/source-data owner-security disposition, workstation local unpushed/stash/worktree signoffs, document-control approval of the 32 staged registry statuses, the superseding W decision, the full matched importer/Base/Bootstrap/Workbench final release, protected `main` promotion and independent standalone-repository archive authorization remain **unapproved**. Step 21 does not close them.

## Recorded evidence state

| Requirement | Current status |
| --- | --- |
| Step 20 structural fixture | PASS in GitHub Actions (automated only) |
| Step 21 Mac private worksheet | TEMPLATE / NOT RUN |
| Step 21 Windows private worksheet | TEMPLATE / NOT RUN |
| G20 first-open, Workbench navigation/edit/restart | NOT RUN |
| Human GUI reviewer | NOT ASSIGNED / NOT APPROVED |
| All release and archival governance gates | OPEN |

**Next bounded step:** have a real Mac operator and real Windows operator execute their private sessions and record observations; only then compare GUI findings and decide the next actionable Workbench code fixes. Do not claim GUI validation from CI.