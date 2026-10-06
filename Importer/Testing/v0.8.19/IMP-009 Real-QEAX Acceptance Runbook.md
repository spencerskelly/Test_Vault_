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

The automated bridge checks out the **accepted Workbench 0.1.18 artifact source commit** `b0c4e2c6bdfb96d36f51d8152b17be22592ef174` and runs three Workbench gates against the imported vault. This replaces the earlier stale `f51ed...` pin, which predated WB-128's disposable structured-edit gate by 14 commits.

```sh
npm --prefix _wb128 run accept:real-vault:scan -- \
  "/path/to/MDSE_IMP009_ACCEPTANCE" "/tmp/wb128-readonly-scan.json"

npm --prefix _wb128 run accept:real-vault -- \
  "/path/to/MDSE_IMP009_ACCEPTANCE" "/tmp/wb128-real-vault-acceptance.json"

npm --prefix _wb128 run accept:real-vault:edits -- \
  "/path/to/MDSE_IMP009_ACCEPTANCE" "/tmp/wb128-real-vault-edit-acceptance.json"
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
- Workbench no-op structured-edit planning produces no formatting drift;
- the WB-128 disposable edit gate copies a real imported Local Model 0.4 note, creates a definitionless Interface, requires Review before Apply, creates/reconnects a Connection, edits the Interface, and proves Apply / Undo / Redo / Delete round trips remain structurally parseable;
- the disposable edit gate proves the original imported note is byte-for-byte unchanged.

The structured-edit gate intentionally modifies only a temporary copy of a real imported note, so acceptance cannot contaminate the candidate vault.

## 5. Obsidian startup/UI coverage

A separate exact-artifact Workbench startup gate runs the CI-built plugin inside Obsidian and proves the controlled plugin becomes readable/core/occurrence-ready with commands available. The current accepted evidence is Workbench run `37409833814` on 12,000 notes, with startup acceptance PASS.

For IMP-009, the combination is stronger and more repeatable than requiring a one-off manual edit:

1. the importer validator proves the **actual 1,051 definitionless Interfaces** exist, remain definitionless, are traceable to exact EA source IDs, and participate in real persisted topology;
2. the Workbench real-vault gates prove that exact imported model parses and renders occurrence topology;
3. the Workbench disposable structured-edit gate proves the accepted writer can create/edit/reload a definitionless Interface using a copied real note without manufacturing a reusable definition;
4. the exact-artifact Obsidian startup gate proves the controlled plugin starts and exposes its commands in Obsidian.

A manual UI spot-check of the validator's `MANUAL SAMPLE` is still useful before promoting a golden vault, but it is **not an IMP-009 closure blocker** unless automated evidence shows a UI-specific regression.

## 6. Closure rule

IMP-009 may move from `test required` to `closed` when:

- the current v0.8.19 real-QEAX import passes;
- `imp009_output_acceptance.py` returns `HEADLESS PASS` on that output;
- Workbench 0.1.18 read-only and semantic real-vault gates pass on the same output;
- Workbench 0.1.18 disposable structured-edit acceptance passes using a copied real imported note;
- controlled exact-artifact Obsidian startup acceptance remains green;
- no synthetic reusable Port/Interface note or legacy Added-Port behavior is observed;
- connector/review evidence remains traceable to the exact contextual source Ports.

If any gate fails, keep the output only as disposable evidence, fix the owning rule/tool, and rerun from a newly generated Base.