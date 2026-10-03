# Handoff Prompt — MDSE v0.8 Implementation

Use this file to start a new chat. Section "Starting a Workbench chat" is a copy-ready prompt for Workbench work; the rest is the general context for any continuation.

## Starting a Workbench chat

Copy this into the new chat, with a fresh fine-grained GitHub token for each repository the chat must push to (`MDSE_Workbench` always; `Test_Vault_` too if the chat will vendor the build into the base):

> Continue MDSE Workbench development. Code: `spencerskelly/MDSE_Workbench` (main). Authority and release chain: `spencerskelly/Test_Vault_` (main). Read first, in this order: `Test_Vault_/99_System/10_Docs/00 - Current State.md`; `Test_Vault_/99_System/10_Docs/MDSE Plan - Path to a Golden Model.md` section 9, Workbench items W1 to W6; `MDSE_Workbench/WB106_IMPLEMENTATION_CONTRACT.md`, including "Implementation status (0.1.16)"; `MDSE_Workbench/RELEASE_NOTES.md`; `Test_Vault_/MDSE Workbench/02 - Workbench Decision Log.md` from WB-105 onward. The goal is to finish WB-106 in this order: W1 occurrence-aware Structure, Interfaces, Where Used and Requirements views, using `LocalModelIndex.occurrencesOf`, `recordsOf` and `refForLink` in `src/core/localmodel.ts`; W2 read-only Local Model popup (WB-105); W3 Local Model findings in Review. Keep `src/core` free of Obsidian imports and add a test for each view. Then release (W4): bump the version, `npm run build`, copy `main.js`, `manifest.json` and `styles.css` into `Test_Vault_/99_System/09_Tools/runtime-plugins/mdse-workbench/`, run `update-plugin-lock.py`, set `version` and `wb106Version` in `mdse-release.yaml`, run `check-release.py --workbench <clone>` and `build-base.py` plus `check-release.py --base`, log `WB-n` and `W-n` decisions, update Current State, the plan and the Workbench test sheet. Pass tokens only as command headers, never into a file or git config. Ask one question at a time; analyse the data before asking.

## Authority

Work from `spencerskelly/Test_Vault_` main as the semantic/importer authority and `spencerskelly/MDSE_Workbench` main as the plugin implementation.

Read in this order:
0. `99_System/10_Docs/00 - Current State.md` (registry of current vs historical files)
1. `99_System/10_Docs/MDSE Plan - Path to a Golden Model.md` (what to do next, gates, run log, decisions needed)
2. `99_System/10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`
3. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` and Workspace Decision Log through W-326
4. `Translator Definition.md`
5. `relationships.yaml` 1.35
6. `element-types.yaml` 1.17
7. `local-model.yaml` 0.2
8. `AI_INSTRUCTIONS.md`
9. MDSE Workbench product/architecture/roadmap notes and the standalone plugin code.

Do not use `20260930`, `261001`, or the old base-vault repository as continuation authorities. They are reference/assessment artifacts only.

## Lean runtime base

Do not manually curate or copy the methodology workspace into the engineering vault. `mdse-release.yaml` is the one machine-readable build authority; `build-base.py` generates the positive runtime file set and `check-release.py --base` verifies it. The generated base does not contain Current State or the release manifest. Its `.vault.yaml` contains `mdse_release: 0.8.0`, and initialization must preserve it. The base is a controlled plugin release (W-322): all runtime plugins ship inside it, pinned and hashed in `.obsidian/plugin-lock.yaml`, with generated settings; MDSE Bootstrap 0.3.0 (`MDSE Bootstrap/`) checks it and registers authors. Never hand-edit generated files (`06_Fileclasses`, the lock, plugin `data.json`); regenerate with the scripts in `99_System/09_Tools/`. The final issued base must pin a WB-106-capable Workbench release.

## Current target

Matched MDSE/base/importer release:
- `mdse_release: 0.8.0`
- relationships 1.35
- element-types 1.17
- local-model 0.2
- importer: `99_System/09_Tools/EA_to_MDSE_Native_Importer/v0.8.6/EA_to_MDSE_Native_Importer_v0.8.6.html` (candidate; older importers are archived and may not generate a model)

Workbench is independently versioned. Current 0.1.16 reads Local Model 0.1/0.2, gives records `ModelRef` identity and writes a findings report (WB-111); it writes links Obsidian-style (WB-112). WB-106 is not complete: the occurrence-aware views, the Local Model popup and Review integration remain.

## Settled model

Reusable definitions are first-class notes. Contextual uses are Local Model occurrences.

- part -> Object definition
- endpoint -> Port definition
- flow -> Item Flow definition
- contextual connections belong to the assembly/context that forms them
- flows belong to one local connection
- persisted local references are native Obsidian block links
- Local Model records use kind-prefixed native block IDs
- `definition` is occurrence-to-definition semantics; it is not `subtypeOf`
- `subtypeOf/supertypeOf` remains reusable-definition specialization
- Requirements may `appliesTo` addressable local records
- repeated note-level relationship targets never mean quantity

## Identity

Every independently referenceable entity uses one globally unique 30-character identity token namespace.

Notes store the token in `uid`. Local Model records store it in:
- `part-<token>`
- `ep-<token>`
- `conn-<token>`
- `flow-<token>`

For EA8647 first import:
- source key = `EA8647 + EA GUID`;
- EA creation time exactly as written; no timezone conversion;
- missing milliseconds -> `000`;
- missing/unusable author -> `skellyspencer`;
- missing creation time starts at `20260911000000001`;
- +1 ms collision handling;
- same-seed ordering by EA GUID lexical order;
- derived locals use causing-source seed and deterministic local ordering;
- Source Map is authoritative after allocation;
- Source Map identity conflicts are hard errors and never auto-repaired.

## Local Model 0.2 / W-314

Part and endpoint occurrences may carry `usage: standard | variant | option`; omission means standard.

`abstract: true` is a sparse optional reusable-definition property. Absence is false; abstractness is not inherited.

Candidates for variant/present option are the concrete transitive `subtypeOf` family rooted at the occurrence definition. Do not persist candidate lists.

Do not put usage on connections or flows.

## Naming/path

- duplicate: `~2`, `~3`, ...
- forced alteration: `~a`, `~b`, ... using lowercase Excel-column sequencing
- both: `~a~2`
- same convention for files and folders
- numeric markers -> duplicate review
- alphabetic markers -> altered-name review
- old ID-based duplicate filename rule is superseded
- no length-driven shortening (W-324); hard stop 400 characters; only the 255-byte filesystem limit forces a cut
- shorten redundant folders before filenames
- a folder containing an identically named authoritative note may reduce to the shortest unambiguous identifier/designator
- a path over 400 blocks; paths over 212 go to `Review - Long Paths.csv` for Post-Import Task 9
- links go to the file name, or the shortest unique path where the name is not unique (W-324)

## Reruns

EA-owned translated fields/relationships may refresh. MDSE identity, existing file path/name, MDSE-only relationships and human-added content are preserved.

Removed EA-owned relationships are removed and logged. Disappeared EA entities are preserved and flagged, not deleted. Human edits overwritten in EA-owned fields are logged.

## Attachments / diagrams

Failed approved attachment import is non-blocking but explicitly logged.

Initial diagram generation is deferred, but every source diagram must reconcile. Unreconciled diagrams are blocking.

## Retired import outputs

Do not recreate empty legacy:
- Identity Registry.csv
- Model Checks.csv
- Pending Relationships.csv
- Transformation Log.csv

unless a future unique use is explicitly approved.

## Implementation order

The order of work, the gates and the open decisions are in [[MDSE Plan - Path to a Golden Model]]. In short: verify the v0.8.6 run (plan sections 4 and 5); finish WB-106 and release it (W1 to W4); add the importer's run diff, determinism check, headless validation and tests (I1 to I4); put the rule-level post-import decisions into the importer (plan section 6); then make the keep run, do the note-level post-import work and work through the golden checklist (plan section 7).

The first whole-model run is eligible to keep only after the importer, final-base and WB-106 gates all pass.
