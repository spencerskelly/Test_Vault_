# Step 20 — Synthetic MDSE Obsidian GUI acceptance (NOT EXECUTED)

**Status:** READY FOR CONTROLLED MANUAL EXECUTION, ALL RESULTS **NOT RUN**. **Source:** isolated Step 20 candidate after Step 19 draft PR #36. This is synthetic documentation; **not** real Ampure/EA/QEAX data, an issued engineering Base Vault, production model, or W approval.

## 1. Installation / provenance

Generate the clean Base using the exact CI-reviewed commit; do not extract or read the public QEAX model. From a clean **isolated** copy of `Test_Vault_`, run:

```sh
python3 -m pip install 'PyYAML==6.0.2'
python3 'Base Vault/Tools/v0.8.0-r2/build-base.py' /tmp/step20-clean-base
python3 'Base Vault/Testing/check-release.py' --workbench 55_Workbench --base /tmp/step20-clean-base
python3 66_Testing/consolidation/step20_synthetic_vault.py --base /tmp/step20-clean-base --out /tmp/step20-synthetic-gui
python3 66_Testing/consolidation/step20_validate_fixture.py --vault /tmp/step20-synthetic-gui
```

On Windows, substitute **user-writable disposable local directories** and the appropriate `py -3` Python executable. The builder and seed tool **refuse to overwrite** an existing non-empty or initialized vault; choose a new output directory. No remote Git, production sync service, company vault or sensitive model file should be attached.

The copied vault intentionally has an **additional synthetic folder** and is therefore not an unmodified release Base artifact; run the native `--base` release checker on the clean base *before* seeding, not against the modified GUI fixture. The fixture retains the exact controlled plugin binaries/lock and 1.36/1.18/0.5 schemas.

Before the GUI test, make a separate backup of the synthetic output, then initialize **only the disposable copy** with its bundled `Initialize-Vault.sh` / `Initialize-Vault.ps1`, using a valid test author code. Record the resulting UID in the **private acceptance log** (not the public GitHub PR). The original generated base should remain `UNINITIALIZED`. Open the isolated initialized folder in Obsidian 1.13.0 or later, trust plugins only in that known test copy, and do not install uncontrolled plugin updates.

## 2. Expected synthetic model and assertions

The fixture includes 12 `Draft` first-class notes: an assembly, controller, CAN transceiver, HMI, reusable CAN Interface, CAN Status Item Flow, status-reporting Function, functional Requirement, test Verification, design Condition, Use Case, and Actor. All notes have unique class IDs and 30-character synthetic UIDs; no first-class Port or Connection note is invented.

- **Structure / Where Used:** the assembly owns three `hasPart` reusable Objects. The corresponding Objects have `partOf` back references; the HMI has contextual multiplicity `2` in Local Model.
- **Internal:** the assembly owns 3 Part occurrences, 3 Interface occurrences, 1 Connection and 1 nested Flow. Two Interfaces belong to child Parts, and one is on the assembly boundary.
- **Interfaces:** the single context-owned Connection joins the two internal endpoint occurrences and has `exposes` to the assembly-boundary Interface. `exposes` must **not** generate a second Connection. The Flow has `endpointA: transmit`, `endpointB: receive`.
- **Functions and requirements:** assembly `performs` a function; function and design `satisfies` the requirement; verification `verifies` the requirement. Inverses are present in the synthetic notes.
- **Use Case:** external test operator is a participant; Use Case `realizedBy` the reporting function.

These are expectations for observation; the structural validator can confirm note data but cannot prove Workbench displays or edits each concept correctly. Local Model `schema=0.5` is governed; `0.6` quantities/units and experimental `variantOf` are **intentionally omitted**.

## 3. Required operator evidence

Record for **each** row: tested Git SHA/PR and Base lock SHA, OS version, Obsidian version, Workbench/Bootstrap observed versions, test fixture path (private), operator, UTC timestamp, *Actual*, **PASS / FAIL / BLOCKED / NOT RUN**, screenshots/log references with sensitive data removed, and a defect link when applicable. Initial status for **all rows is NOT RUN**.

| ID | View / action | Expected outcome | Actual evidence | Status |
|---|---|---|---|---|
| G20-01 | Verify clean Base, source hash and disposable test copy | Native check 0 FAIL; 10 controlled plugins and correct lock; no QEAX, no production remote | Pending | NOT RUN |
| G20-02 | Initialize disposable copy using platform-appropriate initializer | Exactly one unique vault UID, valid author code and retained release marker | Pending | NOT RUN |
| G20-03 | First open in Obsidian; enable trusted bundled plugins | No unexpected trust/initialization errors; note app and plugin versions | Pending | NOT RUN |
| G20-04 | Bootstrap release check and Workbench readiness | Expected pre-release warnings recorded; Workbench eventually usable without silent lock repair | Pending | NOT RUN |
| G20-05 | Navigate Step20 Assembly, Controller and CAN Transceiver | Correct 12 synthetic notes; links open exactly intended notes | Pending | NOT RUN |
| G20-06 | Open Assembly Structure and Where Used | Three component definitions appear, Controller/HMI where-used returns assembly context; no duplicate Part | Pending | NOT RUN |
| G20-07 | Open Assembly Internal | 3 Parts, 3 Interfaces, 1 Connection, 1 nested Flow displayed or documented candidate limitation | Pending | NOT RUN |
| G20-08 | Inspect Interfaces / boundary exposure | Two internal endpoints connected once, boundary Interface exposed, no duplicate Connection | Pending | NOT RUN |
| G20-09 | Inspect contextual multiplicity | HMI occurrence multiplicity 2, not two different reusable HMI definitions | Pending | NOT RUN |
| G20-10 | Open Function and Requirement | Performed-by/satisfies and satisfied-by appear; no requirement satisfaction from unrelated State | Pending | NOT RUN |
| G20-11 | Open Verification and Use Case | Requirement verification and operator participation resolve; Use Case realized-by Function | Pending | NOT RUN |
| G20-12 | Safe UI edit (synthetic note only) | Change one approved Draft description/property; save and confirm Workbench updates | Pending | NOT RUN |
| G20-13 | Restart and persistence | Close/reopen Obsidian, data persists; rebuilt Workbench index resolves links and Local Model | Pending | NOT RUN |
| G20-14 | Negative test on extra disposable copy | Invalid temporary reference is flagged by Workbench Review; revert, no metadata/lock changes | Pending | NOT RUN |
| G20-15 | Mac run | Capture complete macOS first-open/edit/restart results and defects | Pending | NOT RUN |
| G20-16 | Windows run | Capture complete Windows first-open/edit/restart results and defects | Pending | NOT RUN |

## 4. Limits, blockers, and acceptance authority

**No G20 result has been executed.** Automated CI that builds notes and checks YAML is not equivalent to Workbench GUI acceptance. The controlled Workbench 0.1.18 guide explicitly labels some Internal/candidate capabilities as preview; classify GUI behavior that cannot be demonstrated as **BLOCKED or FAIL**, not silently PASS.

A synthetic model can verify that basic graph navigation is available, but **cannot replace** real imported-EA model acceptance, schema/translator fidelity on production files, complete BOM A-15 tests, or user-performed Mac/Windows startup. Earlier experimental `variantOf`/Local Model `0.6` tests are separate and are **not approved** by this kit.

Hard stops remain: public QEAX source-data/security disposition; contributor local-branch/stash/worktree signoffs; document-control approval of 32 registry rows; approved superseding W decision; fully matched importer/Base/Bootstrap/Workbench final release; independent Obsidian GUI signoffs; protected public-main promotion review; separate owner authorization to archive standalone Workbench.

**When a test fails:** preserve a redacted excerpt and local diff, avoid committing user identity/per-machine state, restore from original synthetic backup, and create an issue with tested SHA, reproducer and an exact observed vs expected result. Do not change production schemas or lock to hide failures.
