# IMP-009 Real-QEAX Acceptance Runbook

**Applies to:** importer v0.8.19 / Local Model 0.4 / Workbench 0.1.18  
**Purpose:** prove that EA Ports without deterministic reusable definitions remain usable contextual Interfaces, preserve supported local topology, and do not recreate synthetic reusable Port notes.  
**Vault:** disposable acceptance vault only. Do not reuse a failed or completed import destination.

## Acceptance boundary

IMP-009 is about **contextual Interface identity and usability**, not whether every semantic review item in the imported model is resolved. A passing import may remain `SEMANTIC_REVIEW_REQUIRED / ACCEPTANCE_PENDING` because later P1 issues still exist.

The gate must prove all of the following on the current source and current runtime pair:

- a definitionless EA Port is written as a Local Model 0.4 `Interface` occurrence, not as a first-class Port note;
- its EA GUID/Object_ID remains traceable through import evidence and Local Model Source Map;
- definitionless Interfaces can participate in persisted Connection topology;
- current W-384 connector/review evidence resolves back to exact definitionless source Object_IDs;
- Workbench 0.1.18 parses the whole real vault, resolves the same counts, and can navigate the occurrence topology;
- a controlled Workbench edit/reload check does not manufacture a reusable Interface definition.

## 1. Prepare a fresh integration base

From the current `Test_Vault_` branch:

```sh
python3 "Base Vault/Tools/v0.8.0-r2/build-base.py" "/path/to/MDSE_IMP009_ACCEPTANCE"
```

The Base must retain:

- `mdse_release: "0.8.0"`;
- Local Model schema **0.4**;
- controlled Workbench **0.1.18**;
- `vault_uid: UNINITIALIZED` until explicit initialization.

Initialize through the governed initializer/importer path before model writes. Do not pre-populate a shared vault UID in a distributable Base.

## 2. Run importer v0.8.19

Use:

`Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html`

against the accepted closed/checkpointed EA8647 source.

Required mechanical result:

- preflight `PASS`, with no WAL mode;
- whole-model plan `PASS`;
- `Import State.json` = `IMPORT_COMPLETE`;
- `runStatus.write` = `WRITE_PASS`;
- `runStatus.acceptance` remains `ACCEPTANCE_PENDING` until the broader release gates are closed.

Never reuse a failed or completed destination for another import.

## 3. Run current IMP-009 headless acceptance

```sh
python3 "Importer/Testing/v0.8.19/imp009_output_acceptance.py" "/path/to/MDSE_IMP009_ACCEPTANCE"
```

Required result:

`RESULT: HEADLESS PASS`

The validator checks the current 0.4 contract, including:

- manifest/review count agreement for definitionless contextual Interfaces;
- every definitionless review row maps to the exact EA Port/local-endpoint Ledger row;
- definitionless Interface rows have no first-class `uid`/`id`;
- every definitionless local ID maps one-to-one through Local Model Source Map;
- Local Model records use `### Interfaces` under schema 0.4;
- definitionless Interface records contain neither `definition` nor definition-dependent `usage`;
- persisted local endpoint links resolve and the real source exercises definitionless Interfaces in Connections;
- current W-384 connector/review evidence is traceable to exact definitionless source Object_IDs;
- no legacy `Review - Added Ports.csv`, `portgroup:` evidence, or first-class `type: Port` notes are present.

The script prints a `MANUAL SAMPLE`, preferring a definitionless Interface used by a real Connection.

## 4. Run controlled Workbench 0.1.18 real-vault gates

The automated bridge checks out the same Workbench 0.1.18 acceptance source used by WB-128 and runs both real-vault gates on the imported vault:

```sh
npm --prefix _wb128 run accept:real-vault:scan -- \
  "/path/to/MDSE_IMP009_ACCEPTANCE" "/tmp/wb128-readonly-scan.json"

npm --prefix _wb128 run accept:real-vault -- \
  "/path/to/MDSE_IMP009_ACCEPTANCE" "/tmp/wb128-real-vault-acceptance.json"
```

Required results:

- Local Model 0.4 parser errors = 0;
- Local Interface and definitionless-Interface counts equal the Run Manifest;
- broken local block references = 0;
- first-class Port notes = 0;
- legacy Port relationship fields = 0;
- a real occurrence Structure sample renders;
- a real `Connection.exposes` sample renders;
- a real conveyed-flow sample renders;
- Workbench no-op structured-edit planning produces no formatting drift.

These tests exercise Workbench core behavior against the real generated vault without modifying engineering content.

## 5. Final Workbench UI edit/reload check

Open the **same disposable vault** in Obsidian with controlled Workbench 0.1.18.

1. Wait for Workbench readiness and rebuild the index if necessary.
2. Run **Check Local Model**; the `MANUAL SAMPLE` must not report a missing-definition error merely because it is definitionless.
3. Open the sample in Local Model / Internal / Interfaces and confirm its Connection topology is visible.
4. Change only that Interface occurrence's contextual `identifier` (for example append ` IMP009-TEST`). Do not add a reusable definition.
5. Confirm the edit succeeds without creating a Local Model error.
6. Restart Obsidian.
7. Confirm the changed identifier reloads and no synthetic reusable Interface/Port note appears.

This edit is test data. Never promote the disposable acceptance vault as engineering authority.

## 6. Closure rule

IMP-009 may move from `test required` to `closed` only when:

- the current v0.8.19 real-QEAX import passes;
- `imp009_output_acceptance.py` returns `HEADLESS PASS` on that output;
- both Workbench 0.1.18 automated real-vault gates pass on the same output;
- the UI edit/reload check passes on the printed definitionless sample;
- no synthetic reusable Port/Interface note or legacy Added-Port behavior is observed;
- connector/review evidence remains traceable to the exact contextual source Ports.

If any gate fails, keep the output only as disposable evidence, fix the owning rule/tool, and rerun from a newly generated Base.