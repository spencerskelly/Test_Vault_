# Importer Operating Contract

**Status:** Current baseline and release-hardening contract  
**Applies to:** EA → MDSE native importer, current candidate v0.8.14  
**Release target:** MDSE 0.8.0  
**Detailed semantic authority:** `Translator Definition.md` and the machine-readable schemas in `99_System/03_Schemas/`

## 1. Purpose

The importer is a deterministic, source-faithful transformation from an explicitly approved Sparx Enterprise Architect `.qea/.qeax` SQLite snapshot into an initialized, matching MDSE base vault.

It is not an EA model-cleanup tool and it is not allowed to infer engineering meaning merely to make the destination model look complete.

The core rule is:

> Translate only semantics supported by an approved deterministic rule. Preserve ambiguous source information as review evidence rather than silently discarding it or presenting uncertain meaning as accepted MDSE semantics.

This document defines the import pipeline, trust boundaries, run states and stability/usability expectations. It does **not** duplicate the element, connector, field, tag or package mapping tables. Those remain authoritative in their existing YAML/schema files and in `Translator Definition.md`.

## 2. Authority and conflict rule

Use these authorities in order for importer work:

1. `00_Workspace/00 - Current State.md` — current vs historical files and release state.
2. This document — importer pipeline, trust boundaries and acceptance model.
3. `Translator Definition.md` — detailed Stage-1 translation behavior.
4. Machine-readable schemas and mapping files in `99_System/03_Schemas/`.
5. Current W-decisions — rationale and amendments.
6. Importer implementation — what the candidate actually executes.
7. Historical importers/models — evidence only.

If current authorities disagree, that is an importer defect or governance defect to resolve. Do not pick whichever rule is easiest to implement.

## 3. Stage boundary

The existing two-stage model remains:

- **Stage 1 — native import:** deterministic/mechanical transformation, source preservation, identity allocation, model construction, evidence and validation.
- **Stage 2 — post-import model work:** engineering judgment, semantic reclassification, model cleanup and accepted review decisions.

The phases below subdivide Stage 1 operationally. They do not redefine Stage 2.

## 4. Non-negotiable invariants

1. **Read-only source.** The importer never writes to the EA database.
2. **Known source snapshot.** The exact source file used for a run must be identifiable and auditable.
3. **No silent loss.** Every governed source entity ends in an explicit terminal disposition.
4. **No unsupported inference.** Ambiguity becomes review evidence, not invented engineering meaning.
5. **Deterministic identity.** The same approved source and same release inputs produce the same engineering identities.
6. **Clean destination.** A whole-model import targets a fresh, matching MDSE base, never an edited/generated model.
7. **Schema match.** The importer and destination must agree on MDSE release and required schema versions.
8. **Pre-write validation.** Identity, paths, relationship references and Local Model records are validated before model files are created.
9. **Unambiguous completion.** A partial filesystem write must never look like a successful import.
10. **Mechanical success is not semantic acceptance.** Reconciliation can pass while the model still contains blocking review findings.
11. **Evidence is part of the result.** A generated model without its reconciliation/evidence package is incomplete.
12. **Acceptance requires repeatability.** A release-eligible importer must eventually pass deterministic rerun and headless validation gates.

Items not yet fully implemented or acceptance-proven by v0.8.14 are tracked in [[Importer Issue Register]].

## 5. Stage-1 pipeline

### Phase 0 — Run qualification

**Purpose:** determine whether an import is allowed to begin.

Current checks include the destination MDSE release, relationship schema, element schema, Local Model schema, controlled plugin stack, initialized `vault_uid`, rejection of an already-populated model root and rejection of prior import transaction state.

**Questions affecting usability/stability**
- Can a user accidentally import into the methodology workspace or an existing generated model?
- Can an uninitialized base receive a full model?
- Can an importer run against the wrong release or schema?
- Does the UI clearly explain why a destination was rejected?

**Gate:** destination is a fresh compatible base and no model write has occurred.

### Phase 1 — QEAX acquisition and integrity

**Purpose:** open the exact EA snapshot without modifying it.

The current importer reads `.qea/.qeax` directly as SQLite using a streaming page reader. It discovers SQLite tables and columns from the file and decodes rows without SQL, indexes or writes.

The source must be a closed/checkpointed EA snapshot. WAL-mode detection is a blocking preflight failure, and the exact selected QEAX is fingerprinted with streaming SHA-256 before an otherwise viable source can pass preflight.

**Questions affecting usability/stability**
- Is this the exact file the user intended?
- Can uncheckpointed WAL content make the snapshot incomplete?
- Is the source fingerprinted strongly enough to reproduce the run later?
- Can a schema/parser defect silently null a column?

**Gate:** source opens as supported SQLite, source-integrity conditions are satisfied, and the snapshot identity is recorded.

### Phase 2 — Source inventory and disposition

**Purpose:** account for what exists in the EA database before translating it.

Current whole-model baseline data includes the governed EA tables, object types, connector types and diagram types documented by `Translator Definition.md`. Field/tag/table dispositions live in the mapping YAML files.

Every discovered source table or record class must be either:
- consumed by a current rule;
- preserved as evidence/review;
- explicitly and intentionally dropped; or
- rejected because its disposition is unknown.

A previously empty table becoming non-empty must not pass unnoticed merely because the table name was already known.

**Questions affecting usability/stability**
- Are there source tables/features the importer discovers but does not disposition?
- Can a future EA feature begin carrying data without causing a hard review?
- Are exact source counts tied to the source model rather than unnecessarily tied to the importer engine?

**Gate:** every governed source category has an explicit disposition and source counts/types satisfy the approved source contract.

### Phase 3 — Translation planning

**Purpose:** decide the deterministic outcome of every EA entity before writing files.

Planning performs element classification, folding/suppression, package placement, Port resolution, NoteLink handling and connector classification. It produces a terminal rule/outcome for each planned source entity.

Planning must not depend on filesystem side effects.

**Questions affecting usability/stability**
- Does every element/connector/package/diagram receive exactly one outcome?
- Can the same source record be transformed by competing rules?
- Are fold/suppress decisions visible in evidence?
- Does ambiguity remain reviewable rather than disappearing?

**Gate:** zero unexplained source remainder; plan is deterministic and internally consistent.

### Phase 4 — Identity, naming and placement

**Purpose:** allocate stable MDSE identities and safe human-readable paths.

This phase allocates note IDs/UIDs and Local Model tokens, plans filenames/folders, handles duplicate/altered names, checks case-insensitive collisions, computes link targets and validates filesystem constraints.

Identity and locator are separate:
- ID/UID/local token = engineering identity;
- filename/path = human/filesystem locator.

Path/name changes must not silently alter semantic identity.

**Questions affecting usability/stability**
- Will a repeated import allocate the same identities?
- Are duplicate names understandable to engineers?
- Are paths usable on both macOS and Windows?
- Are mechanical folders degrading navigation?
- Is a path rule governed consistently across Ruleset, Translator Definition and code?

**Gate:** all identities are unique; every path is collision-free and legal; all forced alterations are reviewable.

### Phase 5 — Canonical semantic relationship construction

**Purpose:** translate approved EA relationship semantics into MDSE relationship fields.

The graph builder applies the connector mapping rules, writes inverses/symmetric mirrors and validates references.

A critical distinction is required:

- **canonical relationship:** endpoint/type combination is legal under current MDSE rules;
- **source relationship needing review:** EA evidence is preserved but the MDSE meaning is not yet accepted.

A review finding must not automatically make an otherwise illegal relationship authoritative model data.

**Questions affecting usability/stability**
- Can downstream tools distinguish accepted semantics from provisional source evidence?
- Are endpoint-rule violations kept out of the canonical graph?
- Are inverses/symmetric mirrors complete?
- Is `tracesTo` being used as an escape hatch instead of a review state?

**Gate:** canonical graph is schema-legal; unresolved mappings remain separately auditable.

### Phase 6 — Contextual / Local Model construction

**Purpose:** preserve contextual assembly/configuration structure that must not be flattened into reusable note-level relationships.

Current Local Model 0.3 records include parts, endpoints, connections and flows. BindingConnector context may become temporary local `equals` evidence when deterministically reconstructable. Local Model 0.2 semantics remain frozen for existing content.

The importer must distinguish:
- reusable definition;
- contextual occurrence;
- contextual topology;
- uncertain source evidence.

For contextual EA Ports, the importer must reuse a reusable Port definition only when deterministic evidence supports it. Otherwise it preserves a definitionless Local Model 0.3 endpoint; it must not manufacture a reusable Port note merely to satisfy storage.

**Questions affecting usability/stability**
- Does an EA Part resolve to a valid reusable Object definition?
- Does a contextual Port need a reusable Port definition, or can it remain source-defined locally?
- Are nested/local ownership relationships representable without loss?
- Are BindingConnector endpoints reconstructable without using diagram placement as guessed semantics?

**Gate:** all written Local Model records validate; unrepresentable source structure is preserved as review evidence.

### Phase 7 — Secondary source content

**Purpose:** preserve useful EA information that is not the core semantic graph.

This includes source body text, retained tags, xref-derived source evidence, attributes/operations, linked documents and diagram reconciliation.

For v0.8, diagram artifacts are intentionally deferred, but every source diagram must reconcile.

Attachments are decoded mechanically and reconciled explicitly. A failed approved attachment is visible as a failed attachment import rather than silently missing.

**Questions affecting usability/stability**
- Is source text preserved without guessing missing/truncated content?
- Can attachment failures be traced back to the EA record?
- Do all diagrams have a terminal disposition?
- Are skipped tables/rows explicitly intentional?

**Gate:** all governed secondary content is written, intentionally skipped or explicitly failed/reviewable.

### Phase 8 — Pre-write validation and reconciliation

**Purpose:** prove the complete planned repository is internally consistent before creating model content.

Required checks include:
- source count/type reconciliation;
- unique note IDs and UIDs;
- unique Local Model identity tokens;
- unique case-insensitive paths;
- valid relationship targets;
- required inverses/symmetric mirrors;
- valid Local Model records;
- legal filesystem paths/components;
- terminal source dispositions;
- attachment and diagram reconciliation state.

**Questions affecting usability/stability**
- Can a run fail here before damaging the destination?
- Are semantic warnings clearly separated from structural failures?
- Is evidence concise enough that humans can identify root causes rather than reviewing thousands of duplicate rows?

**Gate:** structural plan is write-safe. Semantic acceptance may still be pending.

### Phase 9 — Vault write and transaction completion

**Purpose:** materialize the validated plan without allowing a partial write to masquerade as success.

The current importer writes a persistent transaction state before model output:

`IMPORT_IN_PROGRESS` → write notes/assets/evidence → write Run Manifest → `IMPORT_COMPLETE`

Caught write failures attempt `IMPORT_FAILED`; if even that update cannot be written, the earlier `IMPORT_IN_PROGRESS` remains authoritative. A Run Manifest is not authoritative without matching `IMPORT_COMPLETE`, and a destination containing prior transaction state is not reusable as a clean base.

Rollback is not required for disposable candidate bases if incomplete state is obvious and the run is discarded.

**Questions affecting usability/stability**
- What happens if the browser loses filesystem permission after 18,000 files?
- Can a PASS manifest exist before the last required file is written?
- Can a user accidentally open/reuse a partial vault?
- Does the next importer run refuse a dirty/incomplete destination?

**Gate:** all required writes succeed and completion state is atomically finalized.

### Phase 10 — Acceptance and handoff

**Purpose:** distinguish a mechanically complete import from a model eligible for engineering use.

The importer reports independent run dimensions rather than one generic PASS:

1. **SOURCE_PASS / SOURCE_WARN** — source preflight state.
2. **PLAN_PASS** — deterministic terminal plan and pre-write structural checks passed.
3. **WRITE_IN_PROGRESS / WRITE_PASS / WRITE_FAIL** — filesystem transaction state.
4. **SEMANTIC_CLEAR / SEMANTIC_REVIEW_REQUIRED** — semantic review state.
5. **ACCEPTANCE_PENDING** until external release gates are satisfied; final acceptance is a separate release decision.

Mechanical completion must never be presented as semantic or release acceptance.

**Questions affecting usability/stability**
- Can a user tell whether PASS means “nothing was lost” or “engineering model is accepted”?
- Are review groups ranked and understandable?
- Can the import be reproduced?
- Can the result survive Workbench reload/restart without identity or relationship corruption?

**Gate:** explicit decision: restart, accept for review, or keep/freeze.

## 6. QEAX handling rules

The importer must follow these source rules:

- Read `.qea/.qeax` directly; do not translate through CSV as the runtime input path.
- Never modify the EA database.
- Treat EA GUID plus the governed source-model identifier as source provenance/identity.
- Preserve source values exactly where the rules say to preserve them; do not reconstruct text that appears truncated at source.
- Discover the full SQLite schema before translation.
- Govern every relevant table/field/tag/xref disposition.
- Fail rather than silently guessing when an expected source construct cannot be decoded deterministically.
- Keep source evidence sufficient to trace any generated note, local occurrence, relationship review or attachment result back to EA.
- Record a strong source fingerprint before release acceptance.
- Source-count baselines belong conceptually to the approved source-model contract, not to generic importer engine behavior. This separation is an open implementation item.

## 7. Evidence model

Evidence has two audiences and should be designed accordingly.

### Machine audit evidence

Exhaustive and lossless. Includes the Ledger, source counts, Source Map, attachment/diagram reconciliation and detailed transformation/review rows. Contextual-endpoint review evidence must retain machine-resolvable source identity: W-380 requires the EA Port Object_ID and persists the connector planner detail so a withheld W-377 relationship can be joined back to the exact source endpoint.

### Human review evidence

Grouped by root cause and decision. It should answer:
- what class of problem occurred;
- how many unique source entities are affected;
- what model areas are affected;
- representative examples;
- whether a code/rule change can resolve the entire group;
- whether the issue belongs to importer correction or Stage-2/manual review.

Repeated rows caused by the same source entity should not inflate the apparent review workload.

## 8. Current real-model evidence baseline

The v0.8.3 whole-model run in `spencerskelly/261002083` is the current large-scale observation baseline, not the release acceptance baseline.

Observed:
- 30,298 generated model notes;
- 92,758 relationship values;
- 2,030 Local Model parts;
- 2,484 Local Model endpoints;
- 460 Local Model connections;
- 53 Local Model flows;
- exact source-count/type reconciliation for the governed baseline;
- 2,924 diagrams explicitly deferred/reconciled;
- 2,232 semantic/review rows consisting of 1,012 Local Model warnings, 587 relationship endpoint findings, 384 provisional `tracesTo` findings and 249 BindingConnector findings.

The 1,012 Local Model warning rows collapse to 244 unique folded EA Parts, showing why grouped review evidence is needed.

v0.8.14 has not yet replaced this observation baseline with a whole-model real-QEAX run.

## 9. Change discipline

For any importer behavior change:

1. Identify the owning phase in this contract.
2. Identify the authoritative mapping/schema/Translator rule.
3. Record or update the applicable W-decision when semantics or Stage-1 behavior changes.
4. Update the authority and implementation in the same change set.
5. Add the smallest useful regression test.
6. Run planning/decode/static checks before another expensive whole-model import.
7. Update [[Importer Issue Register]].
8. Do not patch an old generated vault to simulate an importer correction.

## 10. Release definition

The importer is not release-conformant merely because it writes the full model.

Release eligibility requires:
- qualified and fingerprinted source;
- matched initialized base;
- deterministic plan/write;
- explicit terminal disposition for governed source data;
- canonical MDSE semantics free of unaccepted off-rule relationships;
- valid Local Model;
- attachment/diagram reconciliation;
- unambiguous transaction completion;
- grouped review evidence;
- headless integrity validation;
- deterministic repeated import;
- Workbench acceptance on the real imported model.

Until those gates pass, the importer remains an implementation candidate.
