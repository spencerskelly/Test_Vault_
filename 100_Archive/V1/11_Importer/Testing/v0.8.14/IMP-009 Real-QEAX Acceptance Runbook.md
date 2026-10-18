# IMP-009 Real-QEAX Acceptance Runbook

**Applies to:** importer v0.8.14 / Local Model 0.3 / Workbench 0.1.17 candidate  
**Purpose:** close the remaining real-source and Workbench acceptance gate for definitionless contextual endpoints.  
**Vault:** disposable acceptance vault only. Do not reuse a failed or completed import destination.

## 1. Prepare a fresh integration base

From the root of the current `Test_Vault_` branch:

```sh
python3 "Base Vault/Tools/v0.8.0-r2/build-base.py" "/path/to/MDSE_IMP009_ACCEPTANCE"
```

If PyYAML is missing:

```sh
python3 -m pip install pyyaml
```

Initialize the generated base before import:

```sh
cd "/path/to/MDSE_IMP009_ACCEPTANCE"
./Initialize-Vault.sh "MDSE IMP-009 Acceptance" <13-char-author-code>
```

Expected:
- `.vault.yaml` keeps `mdse_release: "0.8.0"`;
- `vault_uid` is no longer `UNINITIALIZED`;
- the base contains Local Model schema 0.3;
- the controlled plugin payload contains Workbench 0.1.17.

## 2. Run importer v0.8.14

Open:

`Importer/Tools/v0.8.14/EA_to_MDSE_Native_Importer_v0.8.14.html`

Use a browser that supports the File System Access API.

1. Select the closed/checkpointed EA8647 `.qea/.qeax` source.
2. Confirm preflight has no blocking failure. WAL mode must be rejected.
3. Select the initialized fresh base from Step 1.
4. Run **WHOLE MODEL** import.
5. Do not reuse the destination if the run fails or is interrupted.

A successful filesystem run must finish with:
- `Import State.json` = `IMPORT_COMPLETE`;
- write status = `WRITE_PASS`;
- acceptance still = `ACCEPTANCE_PENDING` until the checks below complete.

## 3. Run the IMP-009 headless acceptance check

From the `Test_Vault_` repository root:

```sh
python3 "Importer/Testing/v0.8.14/imp009_output_acceptance.py" "/path/to/MDSE_IMP009_ACCEPTANCE"
```

Required result:

`RESULT: HEADLESS PASS`

The validator checks that:
- definitionless contextual Ports survived as Local Model 0.3 endpoints;
- they did not receive first-class note identity;
- the review CSV, Source Map and Markdown blocks agree;
- no definition/usage is persisted on those definitionless endpoints;
- persisted Local Model endpoint links resolve;
- W-377 connector review evidence resolves to exact EA Port Object IDs when exercised;
- legacy Added-Port / `portgroup:` evidence is absent.

Warnings that the source did not exercise a connection or W-377 connector case mean IMP-009 is **not fully proven**; choose a targeted real-source case before closing it.

The script prints a `MANUAL SAMPLE` for the Workbench check, preferring a definitionless endpoint used by a local connection.

## 4. Workbench read/edit/reload acceptance

Open the **same disposable vault** in Obsidian with the controlled plugin stack enabled.

1. Wait for **Workbench ✓** and occurrence data readiness.
2. Run **MDSE Workbench: Rebuild index**.
3. Run **MDSE Workbench: Check Local Model**. The sample endpoint must not produce a missing-definition error merely because it has no reusable Port definition.
4. Open the note/local endpoint printed as `MANUAL SAMPLE`.
5. Inspect it in the Local Model details and, where applicable, **Internal** or **Interfaces** view. Confirm the contextual endpoint and its supported connection topology are visible.
6. Through **Context / Local Model edit**, change only the sample endpoint's contextual `identifier` in this disposable vault (for example append ` IMP009-TEST`). Do not add a reusable definition.
7. Confirm the edit applies without introducing a Local Model finding.
8. Restart Obsidian.
9. Confirm Workbench reloads the endpoint and the edited identifier persists, with no synthetic reusable Port appearing.

This is a disposable vault; the acceptance edit is test data and must not be promoted into an engineering vault.

## 5. Close IMP-009 only when all gates pass

IMP-009 may move from `test required` to `closed` only when all are true:

- v0.8.14 whole-model real-QEAX write completed;
- headless validator returned PASS without an unexercised topology/connector warning relevant to W-377;
- Workbench 0.1.17 read/navigation/edit/reload passed on the same result;
- no synthetic Port note or legacy Added-Port behavior was observed;
- connector/review evidence remained traceable.

If any gate fails, keep the generated vault as disposable evidence, correct the importer/runtime rule, and rerun from a new fresh base.
