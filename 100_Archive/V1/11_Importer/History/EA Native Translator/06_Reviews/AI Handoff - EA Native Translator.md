---
uid:
type: Info
status: Active
workspace: EA Native Translator
documentRole: AI Handoff
---
# AI Handoff — EA Native Translator

## Mission

Develop a deterministic, auditable translator from Sparx Enterprise Architect source data into the lightweight MDSE model used in Obsidian.

The goal is **not** to reproduce EA, UML, or SysML inside Obsidian. The goal is to preserve source evidence while translating only explicitly approved semantics into the smaller MDSE vocabulary.

## Current architecture

### Source

EA/QEA/QEAX is the migration source.

Current evidence bundle:

`99_System/CSV_EA/`

Manifest source:

`EA_2026_09_06_endgame.qeax`

Evidence counts include:

- 35,969 elements;
- 21,822 connectors;
- 249,892 object properties;
- 1,387 packages;
- 2,924 diagrams.

### Target

Obsidian notes using the MDSE taxonomy.

Current nomenclature:

- `type` = top-level MDSE semantic type;
- `subtype` = approved specialization/classification;
- `Object` replaces historical MDSE `Thing`;
- `kind` is deprecated.

**EA Object** and **MDSE Object** are different concepts and must be explicitly distinguished in translator material.

## Translation philosophy

### Native import

Native import is source-faithful and deterministic.

Do not infer semantic meaning because an EA stereotype, folder name, or connector happens to sound similar to an MDSE concept.

### Semantic mapping

Create an MDSE semantic type, subtype, property, or relationship only through an approved rule/contract.

### Post-import refinement

Semantic cleanup/reclassification may occur after import where explicitly identified. It must not be silently folded into native-import code.

## Authority

Read [[Translator Governance]].

Human Approved decision notes outrank AI proposals, historical handoffs, imported review documents, and generated canvases.

## Workspace map

- `01_EA Elements` — exact EA source element constructs.
- `02_EA Relationships` — raw EA relationship families.
- `03_MDSE Elements` — target MDSE type/subtype contracts.
- `04_MDSE Relationships` — target MDSE relationship contracts.
- `05_Translation Rules` — executable source→target rules.
- `06_Reviews` — governance, tracker, decisions, readiness, change history.
- `07_References` — historical/imported evidence and source references.
- `99_System/CSV_EA` — raw EA evidence bundle.

## Current source coverage

Full source evidence now proves:

- 31 raw EA Object_Types;
- 72 raw Object_Type/Stereotype combinations;
- connector-facing r12 coverage of 1,000 endpoint combinations;
- 30 raw connector type/stereotype pairs.

See [[EA Full Source Element Inventory]].

## Current status

Source evidence is substantially complete.

Translator definition is **not yet import-ready**.

Primary work now is:

1. finish EA element disposition contracts;
2. finish MDSE element contracts;
3. map source properties/tagged values;
4. resolve relationship Review/Deferred cases or explicitly exclude/error them;
5. define verification fixtures;
6. use Requirement as the first fully defined end-to-end translation case.

## Requirement pilot

Requirement is the current pilot for "fully defined translation."

Use:

- `01_EA Elements/Requirement/CANVAS_Requirement Translation Review.canvas`
- `01_EA Elements/Requirement/Decisions/`

Human decisions should be edited directly in those decision notes.

## Critical modeling semantics already established

- Requirement `appliesTo` = scope/applicability.
- Function and Design may `satisfies` Requirements.
- State/State Machine do not directly satisfy Requirements.
- Test/Verification uses `verifies`.
- Generalization uses `subtypeOf / supertypeOf`.
- Structural composition uses `partOf / hasPart`.
- Use Case = externally controlled behavior/scenario.
- Function = product-controlled behavior.
- Package hierarchy is navigation/provenance, not semantic hierarchy.
- Do not silently guess when source meaning is unclear.

## Working protocol for another AI

Before changing files:

1. Fetch latest GitHub `main`.
2. Read governance/tracker.
3. Read the relevant element/relationship decision notes.
4. Inspect the corresponding raw EA evidence.
5. Identify whether the proposed change is source evidence, human decision, implementation, or generated view.
6. Ask a focused question when a semantic decision is required.
7. Do not invent a settled rule.

After changing files:

1. update the element/relationship-specific note;
2. update implementation rules;
3. update verification if applicable;
4. update [[Translator Definition Tracker]];
5. update [[Translator Change Log]];
6. ensure canvases/views reflect the notes rather than becoming the sole authority.
