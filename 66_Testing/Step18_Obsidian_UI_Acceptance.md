# Step 18 — Obsidian first-open and BOM A-14 manual acceptance

**Status: READY FOR HUMAN EXECUTION, ALL GUI RESULTS PENDING.** Creating a test kit or passing GitHub CI does **not** constitute an Obsidian UI pass. Do not use a production vault or move this source to `main`.

**Source baseline:** Step 17 full QEAX accepted on `12d36de03cdeb10fe88cc6cc8c15823abd90e3f5`, [run 38012181833](https://github.com/spencerskelly/Test_Vault_/actions/runs/38012181833). Original QAEX source 35,969 objects / 21,822 connectors; the existing headless check passed but did **not** launch Obsidian. Active MDSE Local Model 0.5 writer; relationships 1.36; experimental BOM 0.6 reader and candidate `variantOf` are **not governed releases**.

## Preparation: three distinct questions, two disposable vaults

Use the **`step18-obsidian-ui-acceptance-kit` GitHub Actions artifact** produced from this Step 18 branch, which contains a README, provenance JSON, and two fully separate vault folders. The generated kit contains no actual QEAX file and **no** full imported real model. Never install it over Test_Vault_, Ampure_Data, PosiBattery, or the original Workbench repositories.

1. **`01_Controlled_Base`** tests the existing controlled plugin payload, lock checks, Bootstrap first-open and user registration. It contains no plugin code overlay. Pre-release manifest pins Bootstrap **0.3.0** while lock/payload is candidate **0.3.1**; record any expected warning. **Do not call Bootstrap release accepted** until that pin/lock decision is governed and no unexpected warnings remain.
2. **`02_BOM_Candidate_Test_Only`** intentionally overlays the *newly built Step 17 source* Workbench `main.js` and the original `manifest.json` / `styles.css` into a copy of the clean Base. Its candidate `main.js` **does not match the controlled plugin lock**, and its disposable-only `relationships.yaml` adds an **unapproved** `variantOf` oneWay Object→Object relationship under a clearly marked test version 1.37. Bootstrap release-check drift is therefore **expected** and must be preserved as evidence. This is an isolated functional trial, **not** release validation.
3. For the **true EA source** case (M04), make a *third local disposable copy* from an independently reconstructed/imported full-QEAX vault, and deliberately install the same candidate Workbench there after capturing hashes. The kit's synthetic interface fixture cannot substitute for the specific source-owned definitionless Interface which the importer names in its review output. No full QEAX or generated 28,273-file model is embedded in the kit.

**Local setup before each first open:** Extract to a user-writable sandbox folder, run the bundled `Initialize-Vault.sh "Step18 Test Vault" testfixturexx` from *inside each vault* (on Windows use `Initialize-Vault.ps1 -Name ... -AuthorCode testfixturexx`). Replace the test author code with your own distinct 13-letter-or-hyphen code if desired. Initialize **local Git only, with no remote**, make one baseline commit, and leave `.vault.yaml` tied to the generated pre-release value. Use Obsidian desktop **1.13.0 or newer**. Then select *Trust author and enable plugins* for each test copy only. Do not connect any production sync service.

**Before each test:** Log exact vault path, platform/OS, Obsidian version, manifest SHA and pinned source commit, Workbench binary SHA, Bootstrap `Show release check`, plugin enablement and console errors. Record **Observed**, **PASS/FAIL/BLOCKED**, elapsed time, screenshot/log path and recovery action. Keep a Git diff of all changed files and a before-test disposable backup.

## Manual execution matrix (nothing has been executed here)

| ID | Vault | Action | Expected acceptance / blocker |
|---|---|---|---|
| B01 | Controlled | Open newly initialized vault; trust and enable the bundled plugins | No unexpected plugin-load error; all required plugins appear; record actual load result |
| B02 | Controlled | Open **MDSE Bootstrap: Show release check** | Candidate Bootstrap 0.3.0 pinned vs 0.3.1 lock warning remains visible; record all warnings. Do not claim release OK |
| B03 | Controlled | Complete first-user author registration | Exactly one person note, correct unique code/UID and no unrelated tracked settings modification |
| B04 | Controlled | Repeat registration with same author and attempt invalid/colliding code | No duplicate person note; invalid or colliding code rejected |
| B05 | Controlled | Run Workbench **Show diagnostics** and open **Review** | Startup reaches ready state and no unexpected failures or indefinite loading; capture time/console |
| B06 | Controlled | Close and restart Obsidian, reopen Review | No data loss or startup error; record cold/warm behavior and any cache state drift |
| M01 | Candidate | Open candidate vault; run Workbench diagnostics and Bootstrap release check | Workbench candidate loads; **locked Workbench binary mismatch and test-only schema drift are expected**. No silent correction of plugin lock |
| M02 | Candidate | Open `Assembly 0.5` Internal/Interfaces; locate definitionless contextual Interface | It exists as an occurrence with no new first-class Interface note; note exact view and availability of edit control |
| M03 | Candidate | Change *only* the contextual Interface identifier using supported Workbench UI, save, close and reopen; restart Obsidian and repeat | Identifier persists after restart, record remains definitionless, no Local Model parser errors; Git diff limited to the source assembly note and expected per-machine state |
| M04 | Real-QEAX | Repeat the specific importer review-listed **definitionless Interface** identifier edit/restart on independently rebuilt frozen full QEAX output | Must confirm on actual governed source model. Synthetic M02–M03 is **not a substitute**. Fail or block if frozen source unavailable |
| Q01 | Candidate | Open `Assembly 0.6 READ ONLY`, inspect Wire Part | Workbench reader recognizes `quantity: 0.3500000001`, `unitOfMeasure: m`, `multiplicity: 2` as strings; expected derived exact amount 0.7000000002 m if displayed; **no automatic editing or 0.6 writer enabled** |
| Q02 | Candidate | Attempt unsupported structural/quantity edit in 0.6 region (without Apply), inspect Review | Must not silently write `schema=0.6` or down-convert quantities into `schema=0.5`. Cancel. Compare original file bytes |
| Q03 | Candidate | On a disposable **copy** of the 0.6 note, remove UOM, use quantity 0, and separately test a bad UOM | Reader flags `part.unit-required`, `part.quantity-invalid`, `part.unit-unknown` (or explicit equivalent UI finding); restore source between attempts |
| V01 | Candidate | Open Product A with valid `variantOf: "[[Family]]"`; inspect Review | Experimental oneWay edge resolves to exactly one Object; no stored inverse, no `subtypeOf`/assembly edge. If disabled by unapproved schema consumer, mark BLOCKED |
| V02 | Candidate | Change Product A to malformed `variantOf: Family`, then missing target and a link to `[[Non Object]]` | Expected `variant.format`, missing-target `variant.target-missing` or `variant.unresolved`, and `variant.endpoint-invalid`; record exact observed codes |
| V03 | Candidate | Point Family back to Product A, then restore; restart Obsidian with malformed `variantOf` and inspect Review | `variant.cycle` on cycle, no false inverse/extra subtype; malformed format finding persists through restart and clears on correction |
| S01 | All | Save baseline and after-test Git diff, Obsidian/plugin logs, timings, screenshots; inspect `.vault.yaml`, plugin-lock and plugin binary | No writes to real source, `main`, or locked plugin payload; no hidden config promotion. All intentional candidate drifts documented |

**Acceptance rule:** B01–B06 and M01–M04 require actual observations; Q01–Q03 and V01–V03 must either pass or identify a real unapproved-governance blocker. A BLOCKED result is **not PASS**. Only a human running desktop Obsidian can mark these manual items complete. Do not turn the pre-release Bootstrap warning or deliberate candidate plugin hash mismatch into a silent waiver.

## Evidence form — create one copy per execution

```yaml
step: 18
status: NOT_RUN
sourceCandidate: 12d36de03cdeb10fe88cc6cc8c15823abd90e3f5
platform: ""
obsidianVersion: ""
vaultRole: "" # 01_Controlled_Base / 02_BOM_Candidate_Test_Only / Real-QEAX
workbenchArtifactSHA256: ""
bootstrapArtifactSHA256: ""
controlledPluginLockSHA256: ""
pluginReleaseCheckObserved: ""
testId: ""
timestamp: ""
result: NOT_RUN # PASS | FAIL | BLOCKED | NOT_RUN
observed: ""
diffFiles: []
screenshotsOrLogs: []
failureOrBlocker: ""
reviewer: ""
```

Store evidence only in a separate, intentionally shared review folder or draft PR after removing any personal author credentials; do not upload full imported QEAX content or local workstation secrets. Keep all required artifacts and original historical BOM 31/31 SHA checks unchanged.

## Outcome boundaries / next step

CI can verify **kit generation, locked controlled payload, candidate overlay SHA, local test schemas, fixture syntax, package integrity and all Workbench regression tests**. CI cannot prove Obsidian interactive startup, plugin author registration, UI editing/restart, performance or trust dialogs.

After the human fills the evidence form, reconcile actual failures and schema/Bootstrap approval decisions. Only when accepted and release checker issues are resolved should a controlled plugin release be considered. **This Step 18 is a manual test handoff, not a release approval.**
