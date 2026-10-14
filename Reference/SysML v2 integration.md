# Engineering and Product Knowledge Model in Obsidian

Status: Proposed architecture for review  
Purpose: Define a shared engineering and product model that connects stakeholder needs, system architecture, implementation, assurance, and lifecycle documentation.

## 1. Vision

Build a connected engineering and product knowledge base in Obsidian that supports both formal modeling and freely written documentation.

The model will connect:

- Stakeholders and customer needs.
- Operational contexts, scenarios, and use cases.
- Requirements and constraints.
- Functions and behavior.
- Logical and physical designs.
- Objects, interfaces, and assemblies.
- Products, families, variants, and configurations.
- Verification, validation, and evidence.
- Failure modes, effects, risks, and controls.
- Manufacturing, installation, commissioning, service, and maintenance information.
- Documentation for engineers, technicians, partners, customers, and other stakeholders.

The governing principle is **ownership**: every authoritative fact or declaration has an identified source, while other notes and views reference it rather than independently duplicate it.

The goal is a complete engineering and product model—not to force every piece of knowledge into formal SysML.

## 2. Architecture

Use four coordinated layers:

|Layer|Responsibility|
|---|---|
|Engineering knowledge|Markdown descriptions, rationale, decisions, issues, procedures, research, and evidence|
|Formal system model|Native SysML v2 declarations for structure, behavior, requirements, interfaces, and analysis|
|Domain methodology|Modeling conventions, libraries, relationship meanings, failure-analysis rules, and review policies|
|Tooling and workflow|Obsidian plugin, model engine, indexing, navigation, change impact, document generation, and external integrations|

SysML v2 provides the formal modeling foundation, including definitions and usages, requirements, behavior, analysis, verification, variability, and views. It does not prescribe the complete engineering methodology or provide every operational tool.[[omg](https://www.omg.org/spec/SysML/2.0/About-SysML)][[shop.elsevier](https://shop.elsevier.com/books/modeling-systems-with-sysml-v2/friedenthal/978-0-443-52599-5)]

## 3. Model Structure and Traceability

The model should support a traceability network rather than enforce a single linear hierarchy.

A typical reasoning path is:

```
Stakeholder
    → expresses customer need
    → motivates use case or operational scenario
    → informs requirements
    → constrains functions and behavior
    → drives design and architecture
    → is implemented by product elements
    → is checked through verification and validation
    → is supported by evidence and documentation
```

Failure analysis intersects this network:

```
Function, object, or interface
    → has potential failure mode
    → produces contextual effects
    → is addressed by controls and design changes
    → generates or strengthens requirements
    → requires verification and supporting evidence
```

Support many-to-many relationships. A requirement may concern multiple functions and interfaces; one design may address multiple requirements; one test may provide evidence for several claims.

## 4. Core Model Categories

|Category|Intended content|
|---|---|
|Stakeholder|Role, concerns, responsibilities, information needs|
|Customer need|Desired outcome, problem, value, originating context|
|Operational context|Environment, actors, assumptions, operating conditions|
|Use case and scenario|Goals, interactions, sequences, exceptions|
|Requirement|Obligation, subject, rationale, applicability, acceptance criteria|
|Function and behavior|Actions, states, interactions, inputs, outputs|
|Design definition|Reusable logical or physical design|
|Object usage|A particular role or application of a definition|
|Interface|Boundary, contract, ports, interactions, exchanged items|
|Assembly|Owned usages, connections, configuration, integration constraints|
|Product|Offered system and its applicable engineering content|
|Product configuration|Selected variants, versions, options, applicability|
|Verification|Checks that specified requirements are met|
|Validation|Evidence that the product addresses intended needs and use|
|Failure analysis|Failure modes, causes, effects, controls, assessments|
|Documentation|Explanations, procedures, decisions, references, records|

These are organizational categories. The methodology must specify how each maps to SysML constructs, domain extensions, or Markdown-only records.

## 5. Definitions, Usages, and Assemblies

Separate reusable definitions from their contextual usages.

```
Controller definition
    ├── Controller usage in Charger A
    └── Controller usage in Charger B
```

A shared definition owns common capabilities, ports, and constraints. Each usage owns its role, selected configuration, local relationships, and contextual analysis.

Distinguish:

- Assembly structure: what a system contains.
- Assembly process: how it is built, integrated, and checked.
- Product configuration: which alternatives and revisions apply.
- Built-unit record: what was installed in a particular manufactured unit.

Do not assume that an architectural assembly tree is automatically a manufacturing BOM or build procedure. Define the mappings explicitly.

## 6. Note and Source Ownership

Each significant element or usage may have its own note.

However, a documentation home is not necessarily an independent SysML source unit. Nested declarations must retain their formal owning context; Markdown folders and wikilinks do not establish SysML ownership.[[support.ptc](https://support.ptc.com/help/modeler/r10.1/en/Modeler/sysml2/overview_of_sysml2.html)][[omg](https://www.omg.org/spec/SysML/2.0/Beta4/Language/PDF)]

Support these note classes:

|Note class|Formal source responsibility|
|---|---|
|Definition note|Owns a complete reusable declaration|
|Assembly/context note|Owns cohesive usages, connections, and flows|
|Behavior note|Owns cohesive behavior declarations|
|Element-view note|Documents an element declared elsewhere|
|Knowledge/procedure note|Contains narrative, workflow, or evidence|

Each modeled note may have a SysML section, but its role must be explicit:

1. Authoritative source: editable and included in model extraction.
2. Element view: generated or selected from authoritative source.
3. Illustrative example: excluded from extraction.

If every usage note must independently own its declaration, introduce a formal fragment-composition mechanism. Specify parent identity, namespace context, duplicate handling, source mapping, and write-back before adopting that approach.

## 7. Markdown Authoring Contract

A proposed minimum note structure is:

```
---
note_id: NOTE-000001
document_kind: model-source
primary_symbol: Products::ExampleAssembly
review_status: draft
owner: Engineering
---

# Example assembly

## Purpose

## Authoritative model

## Rationale and assumptions

## Decisions and open issues

## Verification and evidence

## Stakeholder documentation
```

Rules:

- Use stable document IDs independent of filenames.
- Keep formal model facts in authoritative SysML source.
- Keep workflow properties in YAML.
- Keep explanation and incomplete thinking in Markdown.
- Do not create a second editable copy of a model fact in YAML.
- Do not interpret ordinary wikilinks as formal assertions.
- Preserve standard SysML syntax inside authoritative blocks.
- Make extracted source usable outside Obsidian.
- Treat qualified model names as addresses, not guaranteed permanent identities.

## 8. Relationship Methodology

Store each relationship once and display appropriate labels at both ends.

Examples include:

|Relationship|Human-facing views|
|---|---|
|Ownership|Has part / Part of|
|Typing|Typed by / Used as type by|
|Need traceability|Motivates / Motivated by|
|Requirement subject|Applies to / Constrained by|
|Satisfaction|Satisfies / Satisfaction asserted by|
|Verification|Verifies / Verified by|
|Functional allocation|Allocated to / Implements allocated function|
|Documentation|Documents / Documented by|
|Failure control|Mitigates / Mitigated by|

These labels are proposed presentation conventions, not interchangeable SysML keywords.

Every relationship must retain:

- Its semantic kind.
- Its endpoints and context.
- Its authoritative origin.
- Whether it is authored, inherited, derived, or suggested.

Distinguish topology, transfer, and domain meaning. A connection is not automatically a power supply relationship, a failure-propagation path, or a protective-earth bond.

## 9. Requirements and Architecture

Requirements may concern products, assemblies, functions, interfaces, or contextual usages.

Keep separate:

- What the requirement constrains.
- What design asserts satisfaction.
- What verification checks the requirement.
- What validation addresses the originating need.
- What evidence supports the conclusions.

SysML requirement subjects, satisfaction assertions, and verification constructs provide formal distinctions for these relationships. Satisfaction is not itself a test result.[[docs.nomagic](https://docs.nomagic.com/spaces/SYSML2P/pages/254423086/2026x+Satisfy+requirement)][[wrwei.github](https://wrwei.github.io/tutorials/sysml/SysMLv2_Module9_Verification_EN.html)]

Cross-cutting requirements should remain connected to all relevant architecture elements rather than being forced into one folder or owner.

## 10. Failure Analysis

Implement FMEA through an explicit domain profile or qualified library.

Core SysML v2 supplies the system-modeling foundation, but a complete FMEA methodology requires additional failure-analysis concepts, conventions, and tooling. RAAML provides relevant safety-analysis concepts, but native v2 compatibility must be established rather than assumed.[[omg](https://www.omg.org/cgi-bin/doc?syseng/25-03-05.pdf)][[omg](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML)]

Each contextual assessment should identify:

- Analyzed element and function.
- Operating context.
- Failure mode.
- Potential causes.
- Local, next-level, and end effects.
- Prevention and detection controls.
- Mitigations and recommended actions.
- Assessment method and ratings.
- Derived requirements.
- Verification and evidence.
- Responsible owner and review status.

Separate reusable failure knowledge from product-specific assessment.

Generate FMEA worksheets from linked records. Do not maintain an unrelated spreadsheet as a competing authority. Do not infer failure propagation or risk ratings solely from architectural connectivity.

## 11. Documentation and Stakeholder Views

Create views tailored to audience, product configuration, and lifecycle stage.

|Audience|Typical information|
|---|---|
|Engineering|Architecture, requirements, interfaces, rationale, analysis|
|Manufacturing|Build instructions, configuration, inspection, test|
|Technicians|Installation, commissioning, diagnostics, replacement, safety|
|Service teams|Symptoms, fault isolation, recovery, maintenance|
|Partners|Interface contracts, integration obligations, supported configurations|
|Customers|Capabilities, operating limits, procedures|
|Product teams|Needs, use cases, product coverage, validation|
|Quality and assurance|Traceability, evidence, unresolved risks, approvals|

Combine generated model content with authored explanations and procedures.

Documentation must identify applicability and baseline. Access restrictions require suitable publishing or access-control mechanisms; view filters alone are not security boundaries.

## 12. Change Impact and Review

When authoritative content changes:

```
Detect change
    → identify semantic differences
    → resolve and validate affected dependencies
    → refresh derived views
    → identify potentially invalidated claims and evidence
    → create review tasks with reasons
```

Automatic analysis does not replace engineering approval.

Maintain distinct states for:

- Syntax and semantic validity.
- Review completion.
- Evidence currency.
- Release approval.

Examples:

- Interface timing changes trigger review of consumers, tests, and FMEA controls.
- Shared definition changes identify applicable usages.
- Requirement changes flag satisfaction claims and verification coverage.
- Behavior changes flag related failure-response analyses.
- Narrative edits trigger only the relevant document-review policy.

Record why each item requires review. Avoid indiscriminate review of every linked note.

## 13. Plugin and Engine Responsibilities

The Obsidian plugin owns:

- Source extraction and document identity.
- Markdown-to-model source mapping.
- Navigation and stakeholder views.
- Relationship presentation.
- Workflow and impact policies.
- Safe source edits.
- Export and publication.

The SysML engine owns:

- Parsing and name resolution.
- Supported semantic validation.
- Inheritance and specialization interpretation.
- Model queries and refactoring capabilities.

Evaluate Open-MBEE’s `sysml-toolkit` for embedded static tooling and `OpenSysML` for a companion service and execution. Their documented capabilities, limitations, and specification baselines differ, so qualify one selected baseline rather than assume interchangeability.[[github](https://github.com/Open-MBEE/OpenSysML)][[github](https://github.com/Open-MBEE/sysml-toolkit)]

Keep repository integration optional until synchronization and authority rules are defined.

## 14. Scale and Baselines

Use incremental indexing and dependency-aware analysis, not full-vault processing after every keystroke.

Provide:

- Shared libraries with explicit versions.
- Product/configuration applicability.
- Bounded graph views.
- Visible unresolved references.
- Clear handling of incomplete drafts and stale results.
- Rebuildable indexes.
- Reviewable changes.
- Versioned source, evidence, and documentation baselines.

A baseline must identify enough information to reproduce the model and its outputs, including source revisions, libraries, engine version, configuration, and relevant evidence.

## 15. Reference Package and Delivery Plan

Create a versioned reference vault containing:

1. Normative Markdown authoring profile.
2. Model taxonomy and domain conventions.
3. Ownership, identity, and namespace rules.
4. Relationship projection catalog.
5. FMEA profile.
6. Change-impact and review policy.
7. Stakeholder documentation templates.
8. Engine capability matrix.
9. Validated worked examples.
10. Positive and negative conformance tests.
11. Export, baseline, and migration procedures.

Implement progressively:

|Phase|Outcome|
|---|---|
|1|Note identity, authoritative sections, extraction, cross-note resolution|
|2|Architecture and traceability views|
|3|Verification, validation, evidence, and contextual FMEA|
|4|Semantic change impact and review workflow|
|5|Stakeholder documentation and baseline publication|
|6|Controlled graphical editing, repository integration, optional execution|

## 16. Acceptance Criteria

The approach is ready for team adoption when it can demonstrate that:

- Every authoritative model element has a clear owner.
- Shared definitions and contextual usages remain distinct.
- Requirements link to appropriate architecture and assurance elements.
- Failure analyses retain context and explicit assumptions.
- Generated views do not create duplicate authority.
- Incomplete drafts remain editable without presenting stale results as current.
- Changes identify affected claims and required reviews.
- Stakeholder documents have correct applicability and baseline.
- Extracted models validate outside Obsidian.
- Representative product models perform acceptably at expected scale.

The intended outcome is one connected engineering knowledge environment: formal enough for traceability and automated analysis, flexible enough for engineering discussion, and structured enough to publish dependable information for every stakeholder.