# Handoff Prompt — MDSE v0.8 Implementation

Use this prompt to continue implementation in a new chat.

## Authority

Work from `spencerskelly/Test_Vault_` main as the semantic/importer authority and `spencerskelly/MDSE_Workbench` main as the plugin implementation.

Read in this order:
1. `99_System/10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`
2. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`
3. Workspace Decision Log through W-319
4. `Translator Definition.md`
5. `relationships.yaml` 1.35
6. `element-types.yaml` 1.17
7. `local-model.yaml` 0.2
8. `AI_INSTRUCTIONS.md`
9. MDSE Workbench product/architecture/roadmap notes and the standalone plugin code.

Do not use `20260930`, `261001`, or the old base-vault repository as continuation authorities. They are reference/assessment artifacts only.

## Current target

Matched MDSE/base/importer release:
- `mdse_release: 0.8.0`
- relationships 1.35
- element-types 1.17
- local-model 0.2
- importer: `EA_to_MDSE_Native_Importer_v0.8.0.html`

Workbench is independently versioned. Current 0.1.14 predates Local Model support.

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
- maximum repository-relative path = 212 characters
- shorten redundant folders before filenames
- a folder containing an identically named authoritative note may reduce to the shortest unambiguous identifier/designator
- remaining >212 after normalization is blocking

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

1. Build canonical v0.8 importer writer/source map against schemas 1.35/1.17/0.2.
2. Implement 212-character path/naming planner and remeasure real QEAX.
3. Complete attachment, diagram-reconciliation and final evidence outputs.
4. Produce a new clean v0.8 base; do not mutate the old base repo into the release.
5. Validate representative real EA cases.
6. Implement Workbench WB-106: ModelRef, Local Model 0.1/0.2 parser, block-fragment preservation, region protection, findings, and occurrence-aware core views.
7. Then add W-314 read-only variation, candidate resolution and temporary session configuration.
8. Do not define persisted named configurations/model numbers/compatibility matrices until the later configuration phase.

The first whole-model run is eligible to keep only after both the importer/base gates and WB-106 read/navigation gate pass.
