# Consolidation Step 20 — Governed synthetic GUI fixture handoff

**Prepared:** 2026-10-11 Pacific. **Status:** synthetically generated and structurally validated, **HUMAN GUI NOT EXECUTED**.
**Parent:** Step 19 draft PR #36 / `b8bbad92dd9597d1153f27464c15f1b116602a07`.

## What Step 20 creates

A fresh, **uninitialized** copy of the controlled MDSE Base with one additional folder: `88_Step20_Synthetic_GUI_Model`. It contains 12 invented Draft notes with consistent governed first-class types, relationship inverses, and an Assembly-owned Local Model schema 0.5 region. Reusable CAN Interface and CAN Status Item Flow are first-class Object / Item Flow notes; contextual Parts, Interface occurrences, Connection and Flow are **not** misrepresented as new first-class notes.

Local Model records: 3 Parts (Controller, CAN Transceiver, HMI with multiplicity 2), 3 Interfaces (2 child context, 1 assembly boundary), 1 Connection (Controller CAN to transceiver, exposes boundary Interface) and 1 nested information Flow. Relationship graph additionally includes a Behavior Function, Requirement, design Condition, Verification, Use Case and Actor.

The generator uses governed relationships schema 1.36, element types 1.18, Local Model 0.5 and the original locked Workbench 0.1.18. No experimental `variantOf`, Local Model 0.6 quantity/units, alternate Workbench candidate plugin, or source-model archive is present.

## Reproduce locally from a clean isolated repo checkout

```sh
python3 -m pip install 'PyYAML==6.0.2'
python3 'Base Vault/Tools/v0.8.0-r2/build-base.py' ./step20-clean-base
python3 'Base Vault/Testing/check-release.py' --workbench 55_Workbench --base ./step20-clean-base
python3 66_Testing/consolidation/step20_synthetic_vault.py --base ./step20-clean-base --out ./step20-synthetic-gui
python3 66_Testing/consolidation/step20_validate_fixture.py --vault ./step20-synthetic-gui
STEP20_SYNTHETIC_VAULT=./step20-synthetic-gui python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step20_synthetic.py' -v
```

Use new empty local paths; the generator refuses an initialized or existing destination. Do **not** commit generated worktree contents or any user identity. The completed CI run makes a **notes-only ZIP** (`step20-synthetic-notes-only`) available under its Actions artifacts for seven days; download it and copy only the `88_Step20_Synthetic_GUI_Model` folder into a separately generated clean Base. It contains **15 text-only files**: 12 model Markdown notes, a test README, a pending GUI runbook, and JSON provenance. No vault binaries or plugin payload are uploaded.

## Verification scope and evidence

- The Step 19 controlled Base check is rerun **before** the synthetic folder is added. The modified synthetic GUI copy is not itself an unmodified release Base and is not passed to the release `--base` checker.
- `step20_validate_fixture.py` checks all 12 types/UIDs, relationship targets and inverse pointers, part/interface/connection/flow kinds, every scoped local block reference and the connected boundary `exposes` field.
- `test_step20_synthetic.py` adds 23 positive and fail-closed negative cases; edits and restores only files in a runner-local synthetic copy. The Step19 generated-base tamper tests are also repeated against the untouched clean Base.
- The SHA-controlled original plugin lock and all schema source files remain byte-identical in the synthetic vault. The runner checkout excludes QEAX, and all test identities/requirements are explicitly invented.
- A green structural CI pass means **the fixture is syntactically/semantically coherent enough for manual testing**, not that Workbench rendered Internal, Interface, Requirement or Where Used views, or that startup/edit/restart worked.

## Human GUI results — all NOT RUN

Follow `STEP20_GUI_ACCEPTANCE.md`, which is included inside the generated synthetic folder and in this repository. Cases G20-01–G20-16 require actual operator observations for first open, Bootstrap, Workbench readiness, Where Used, Internal boundary exposure, functional/requirement verification, controlled test edit, save/restart, and distinct Mac/Windows systems.

**Gating:** Source-data owner security review of public QEAX reachability; local contributor branch/stash/worktree signoffs; document-control approval of the 32 Step 18 registry statuses; approved superseding W source-authority decision; issued matching runtime release and real GUI signoff; protected public-main promotion; separate owner authorization before standalone Workbench read-only archive. All remain outstanding.

**Next bounded step:** conduct or arrange the G20 GUI runs using isolated synthetic fixture copies, record exact source/lock/app/OS versions and defects, and compare measured results without making up PASS statuses. Proceed to real importer-generated model acceptance only after the QEAX security owner explicitly authorizes it.
