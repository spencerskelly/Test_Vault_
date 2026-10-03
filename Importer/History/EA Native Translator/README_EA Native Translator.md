---
uid:
type: Info
status: Active
workspace: EA Native Translator
---
> [!WARNING]
> **ARCHIVED (W-246, W-320).** This folder is the retired old translator workspace, kept as evidence. It has no authority. Current rules: [[Translator Definition]], [[MDSE Modeling Ruleset 1.23]]; registry: [[00 - Current State]].

# EA Native Translator

This folder is the living methodology workspace for translating native Sparx Enterprise Architect content into the MDSE vault model.

## Start here

For a new human or AI contributor:

1. [[AI Handoff - EA Native Translator]]
2. [[Translator Governance]]
3. [[Translator Definition Tracker]]

## Authority model

Human Approved decisions and implemented methodology contracts are authoritative for target semantics.

Raw EA evidence is authoritative about the source model.

Canvases, Bases, imported references, historical handoffs, and chats are supporting evidence/views and do not override approved decisions.

## Working principle

The native importer is **source-faithful and deterministic**.

- Define the exact EA source construct first.
- Preserve source provenance.
- Apply only approved element/property/relationship mappings.
- Do not infer engineering meaning from vague EA structure.
- Where semantic reclassification is valuable, define it explicitly as an approved import rule or post-import refinement.

## Sections

- [[README_EA Elements]] — EA source element constructs.
- [[README_EA Relationships]] — EA connector families.
- [[README_MDSE Elements]] — target MDSE type/subtype definitions.
- [[README_MDSE Relationships]] — target MDSE relationship definitions.
- [[README_Translation Rules]] — executable source→target mapping rules.
- [[README_Reviews]] — governance, tracker, readiness, decisions, change history.
- [[README_References]] — historical/imported references and evidence pointers.

## Source evidence

Raw source evidence is stored in:

`99_System/CSV_EA`

See [[EA Full Source Element Inventory]].

## Review workflow

1. Identify exact EA source data.
2. Find or create the relevant decision note.
3. Human approves semantics where a decision is required.
4. Implement the decision in MDSE contracts/Translation Rules.
5. Define or update verification fixtures.
6. Update [[Translator Definition Tracker]] and [[Translator Change Log]].
