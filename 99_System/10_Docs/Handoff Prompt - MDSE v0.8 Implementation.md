# Handoff Prompt — MDSE v0.8 Implementation

Copy the prompt below into a new chat.

---

Continue the MDSE native EA → Obsidian work from **`spencerskelly/Test_Vault_` main**. Do not reopen settled methodology without conflicting real evidence.

Read first:
1. `99_System/10_Docs/MDSE v0.8 Design Check - 2026-10-01.md`
2. `99_System/10_Docs/EA Native Importer Comprehensive Handoff - 2026-10-01.md`
3. Workspace Decision Log W-293 through W-313
4. `Translator Definition.md`
5. `MDSE Modeling Ruleset 1.22.md`
6. `relationships.yaml` 1.35
7. `element-types.yaml` 1.16
8. `local-model.yaml` 0.1
9. Workbench WB-105/WB-106 and Architecture and Model Boundary
10. `spencerskelly/MDSE_Workbench` main

## Goal

Build the first potentially keepable synchronized release pair:
- `EA_to_MDSE_Native_Importer_v0.8.0.html`
- clean base vault with `mdse_release: "0.8.0"`

Initial v0.8 imports the complete Stage-1 semantic model plus approved attachments. It creates no diagrams; all diagrams reconcile as intentionally deferred. A later idempotent pass imports selected EA diagram types.

## Do not change these model rules

- reusable engineering definitions are first-class notes;
- contextual uses are Local Model records owned by the containing note;
- part occurrence → Object `definition`;
- endpoint occurrence → Port/interface `definition`;
- flow occurrence → Item Flow `definition`;
- every assembly owns connections formed below its boundary;
- parent assemblies connect to child boundary endpoints, not through to child internals;
- boundary endpoint `exposes` inner endpoint when confirmed;
- EA BindingConnector remains temporary `equals` review evidence until engineering meaning is confirmed;
- flows are authored once under the connection that carries them;
- Requirement `appliesTo` may target a local occurrence;
- only Function/Design `satisfies` Requirement;
- Verification `verifies` Requirement;
- repeated YAML relationship targets are not quantity;
- `multiplicity: N` is only for contextually interchangeable copies.

## Canonical Local Model

Use `local-model.yaml` schema 0.1 and W-302 markers.

Stable IDs:
- `part-*`
- `ep-*`
- `conn-*`
- `flow-*`

The local ID is also the native Obsidian block ID. Human headings stay readable.

Persist local references as native block links:
- `part: [[#^part-id|Part]]`
- `parent: [[#^ep-id|Interface]]`
- `endpointA/B: [[#^ep-id|Interface]]`
- `exposes: [[#^ep-id|Inner Interface]]`
- temporary local `equals` uses the same form.

`definition` stays a normal note link.

EA provenance does not go in Local Model engineering records. Write it to `99_System/11_Import/Local Model Source Map.csv`.

Inherited pins/contacts/sub-interfaces stay implicit until independently addressed.

## Importer

Accepted fallback/safety baseline: v0.5.2 / relationship schema 1.35.
Current assessment candidate: v0.7.

Build v0.8 from the safe baseline/candidate work, but do not preserve v0.7's obsolete Local Model rendering.

Required corrections:
- W-302 managed markers;
- canonical headings/fields;
- block ID = local ID, no separate `loc-...` anchor;
- no EA GUID lines in Local Model;
- native block links instead of bare local addresses;
- lazy inherited-member materialization;
- contextual temporary BindingConnector `equals`;
- W-310 multiplicity semantics;
- W-308 connector folder normalization;
- W-309 regulatory folder normalization;
- zero Industrial connector model-note paths >260 characters after normalization before choosing the global hard limit;
- meaningful Alias for URL/machine-noise names;
- complete approved `t_document` attachment handling;
- initial diagram deferral and later selectable diagram pass;
- final review/evidence outputs and terminal reconciliation;
- importer/base v0.8.0 compatibility check.

Do not fix path problems with blind truncation or opaque filename hashes.

## Workbench keepability gate

Workbench 0.1.14 is still note/path based. Before keeping the v0.8 full import it must:
- parse Local Model schema 0.1;
- index note and local-record identity through ModelRef;
- preserve `#^local-id` fragments in semantic links;
- show/navigate the Local Model dropdown;
- make Structure, Interfaces, Where Used and Requirements occurrence-aware;
- protect the governed Local Model region from ordinary body editing;
- report malformed markers, duplicate IDs, broken local links, invalid definitions/endpoints, orphan flows and unresolved local applicability;
- stop showing repeated relationship entries as engineering quantity.

Structured Local Model editing may follow later.

## Real-source acceptance examples

Prove with actual EA data:
- reusable assembly used in multiple contexts;
- two internal parts with an internal endpoint connection;
- multiple flows on one connection;
- boundary endpoint with temporary `equals` to an internal endpoint and review path to `exposes`;
- parent connection to child boundary endpoint;
- nested interface member materialized only when addressed;
- Requirement targeting a local record;
- grouped multiplicity and individually addressable repeated parts;
- connector/regulatory path normalization;
- approved attachment;
- diagrams reconciled but omitted;
- stable local IDs on rerun;
- no conveyed-flow loss;
- W-292 state ownership unchanged;
- no invalid Port subtypes;
- zero unexplained source remainder.

## Still open

Do not silently decide:
- exact opaque local-ID suffix/collision rule;
- final global path limit after corrected planning;
- promotion rule from local occurrence to reusable first-class definition;
- fallback when BindingConnector assembly context cannot be reconstructed;
- disposition of redundant legacy/header-only import CSVs.

If one becomes blocking, explain the exact engineering need, options/tradeoffs, recommend the simplest scalable choice, and ask one focused question.

Next workspace decision number: **W-314**.

The goal is not just a successful import. It is a durable MDSE that remains understandable in native Obsidian, preserves reuse and contextual identity, and lets Workbench safely navigate and analyze the model.
