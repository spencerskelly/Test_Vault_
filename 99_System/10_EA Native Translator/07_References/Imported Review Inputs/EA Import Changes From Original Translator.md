---
uid:
type: Info
status: Active
workspace: EA Native Translator
documentRole: Change Management
revision: 2.0
revisionDate: 2026-09-27
---

# EA Import Changes From Original Translator

## Purpose

This is the live change-management record for the native EA → Obsidian translator.

It records deliberate differences from the original semantic EA → MDSE translator, identifies conflicts or drift inside the current methodology workspace, and defines the readiness gate that must be satisfied before another broad import is run.

This note is part of the translator rule set. A material translator behavior must not exist only in code, a workbook, a sidecar, a chat, or an old handoff.

## Baseline being changed

The original translator was semantic-first. Its governing philosophy was to interpret EA content into the most useful MDSE meaning during translation, including semantic reclassification, consolidation, and relationship normalization.

Primary historical baselines include:

- `EA_to_MDSE_Translator_Primary_Reference_v1.0_GSE`
- `EA_to_MDSE_Translator_Cumulative_Handoff_v1.1_2026-09-04`

Those documents remain historical evidence. They are not allowed to override a later settled rule in this workspace.

## Current native-translator direction

The native translator is now intentionally more direct and source-faithful.

1. **EA source structure is explicitly defined before translation.**
   - Every supported EA `Object_Type`, stereotype/profile combination, property disposition, containment behavior, and connector participation must be documented.
   - Source-faithful element typing is the default. Semantic cleanup/reclassification is a later model change unless an explicit native-import rule says otherwise.

2. **MDSE structure is explicitly defined before translation.**
   - Every MDSE type, subtype, property contract, relationship, inverse/storage rule, and validation rule used by the importer must be defined.

3. **Translation is deterministic, not interpretive.**
   - A source construct is converted only by an approved rule.
   - Package/context evidence may affect a mapping only where an explicit precedence rule says it does.
   - The importer must not infer engineering meaning from vague EA structure.

4. **The next broad import is gated on definition completeness.**
   - Earlier workflows allowed Review/Deferred/`map*` evidence to be imported and resolved iteratively afterward.
   - That is no longer the intended path for the next import.
   - The EA and MDSE element/relationship contracts must be completed first, and all in-scope source patterns must have deterministic dispositions.

5. **The current migration direction is primarily one-way: EA → Obsidian.**
   - Obsidian/Git becomes the evolving engineering model after import.
   - Repeat synchronization from EA is not assumed safe until explicit synchronization/ownership rules are re-established.

---

# Change Summary From the Original Translator

| Area | Original translator | Native translator / current direction | Change impact |
|---|---|---|---|
| Translation philosophy | Most specific engineering meaning wins; semantic classifier may override EA metaclass/stereotype. | Source-faithful/direct first pass. Reclassification requires an explicit rule or post-import model change. | Major architectural change. |
| Element typing | EA State/UseCase/Class/etc. could become a different MDSE semantic type based on engineering interpretation. | Preserve the source classification behavior defined for the exact EA construct; do not guess semantic intent. | Element rules must be exhaustive. |
| YAML type contract | Earlier native-change note proposed `type` directly from EA stereotype, else `Object_Type`. | Live workspace now also defines a canonical MDSE `type → subtype` taxonomy. Exact reconciliation is not yet fully specified for every EA construct. | **Must be resolved before import.** |
| MDSE terminology | `Thing` and `kind` were used historically. | `Thing` → `Object`; `kind` → `subtype`. | Settled terminology migration. |
| Physical Context | Earlier translator could convert Physical Context to Use Case / Where during import. | Keep the EA-derived source type during native import. Conversion to Use Case / Where is post-import unless explicitly ruled. | Removes semantic guessing. |
| Use Case subject | `subject / subjectOf` could identify a focal product/object. | Do not generate subject semantics automatically. | Post-import semantic refinement only. |
| Use Case / Context participation | Participation could be mixed with subject semantics and derived inverse navigation. | One-sided `participants` YAML on the owning Use Case/Context only. No reciprocal participant-note property. | Intentional exception to bidirectional storage. |
| Global relationship storage | Natural direction stored once; inverses commonly derived. | Approved global semantic relationships are written explicitly at both endpoints when both notes exist. | Direct navigation without derived inverse dependence. |
| Connector notes | Connector semantics were translated, with detail preserved as needed. | EA connectors never become standalone notes. Semantic links are YAML; approved connector detail is written into endpoint bodies. | Keeps vault lightweight. |
| Flow-control nodes | Mostly local Functional Flow constructs. | Still suppressed as standalone notes by default; preserve their meaning as local/body evidence. | No note explosion. |
| Item Flow / InformationFlow | Earlier translator had a first-class reconstruction strategy. | Currently Deferred/source-only pending a complete native rule. | Must be settled or explicitly excluded before next broad import. |
| Package hierarchy | Original semantic translator did not use EA packages as MDSE semantic hierarchy. | Preserve package path/hierarchy as source navigation/provenance as defined by the native importer. Do **not** infer MDSE semantic relationships from containment unless an explicit rule says so. | Source hierarchy and semantic hierarchy remain distinct. |
| Package-context rules | Package was mostly provenance/context evidence. | Explicit rules may use package context as a discriminator. Current examples include allocate precedence under `04 Product Function` and `05 Product Design`. | Package context is allowed only through an explicit rule. |
| BindingConnector | Not a stable native rule in the older translator. | `BindingConnector → equals / equals`. | Settled direct mapping. |
| Plain Connector | Earlier interface rules were more interpretive. | Plain EA Connector → symmetric `interfaces / interfaces` for the approved patterns. | Settled direct mapping. |
| Verification connector | Verification intent and test semantics had multiple representations. | EA Dependency «verify» testCase → Requirement → `verifies / verifiedBy`. | Settled direct mapping for approved endpoint pattern. |
| Non-Requirement refine | Older references used broader refinement semantics; intermediate handoffs also proposed other mappings. | Current r12 rules normalize approved non-Requirement refinement to `describes / describedBy`; `refines / refinedBy` is reserved for Requirement→Requirement. | Current matrix supersedes older intermediate handoffs. |
| Unknown relationships | Earlier process could preserve unresolved `map*Out/map*In` relationships and reduce them after a trial import. | Preserve evidence during rule development, but do not treat unresolved mappings as acceptable readiness for the next broad import. | Definition-first gate added. |
| Import lifecycle | Controlled repeat synchronization was a design goal. | Current migration is one-way first; repeat-import behavior is future work. | Prevents accidental overwrite of Git/Obsidian evolution. |
| Traceability | Identity, transformation, model-check, and pending-relationship registries. | Keep full traceability/exception evidence outside normal engineering notes, with no silent data loss. | Retained and expanded. |

---

# Current Workspace Review — 2026-09-27

## What is aligned

### EA element structure

The EA element area is substantially aligned with the new direction.

- EA elements are organized by exact `Object_Type`.
- Stereotype/profile variants are documented beneath the source type.
- The type READMEs and sampled stereotype notes explicitly state the **source-faithful native-import typing rule**.
- Connector-facing occurrence counts and relationship patterns are traceable.
- The notes correctly state the current coverage boundary: connector-facing element combinations are known, but isolated/unconnected `t_object` coverage is not yet certified.

### EA relationship inventory

The relationship inventory is strong and auditable.

Current r12 reconciliation records:

- **21,822** EA connectors;
- **30** raw Connector_Type / effective-stereotype pairs;
- **1,000** observed endpoint combinations;
- no unrecognized raw connector type/stereotype pair.

Every observed relationship combination currently has a Matrix Rule or an explicit Review/Deferred/Exception disposition.

### Translation rule structure

The Matrix Rules provide a good executable-rule shape:

- source connector/pattern;
- endpoint semantics;
- exact target relationship;
- direction/inverse behavior;
- body-detail preservation;
- status;
- review trigger;
- source basis.

This should remain the rule-level implementation contract.

### MDSE terminology

The live taxonomy now explicitly uses:

- `type`
- `subtype`
- `Object` instead of historical `Thing`

This terminology should be treated as current unless explicitly revised.

### Connector detail preservation

The r12 body-detail rules are well separated from relationship YAML semantics and define handling for:

- connector name;
- connector notes;
- source/target roles;
- multiplicity;
- constraints;
- guard;
- trigger/event;
- effect/action;
- flow-control detail;
- participation detail.

This is a good native-import pattern because it avoids connector-note proliferation without silently deleting meaningful source content.

---

# Current Workspace Gaps / Conflicts

These items should be treated as change-control work, not implementation discretion.

## 1. Top-level philosophy is stale

`README_EA Native Translator.md` still says to “translate engineering meaning” as the working principle.

That language reflects the original semantic translator more than the current source-faithful native-import direction.

**Required change:** revise the top-level principle so it distinguishes:

- source-faithful element import;
- deterministic approved relationship mapping;
- post-import semantic cleanup.

## 2. Translator Decision Log is stale

`Translator Decision Log.md` still states:

- EA source types are evidence and “most specific engineering meaning wins”;
- semantic meaning should override UML/SysML mechanics;
- ambiguous source elements should be classified before dependent relationship mapping.

Those statements conflict with the current source-faithful element rule.

It also contains relationship amendments that have since been superseded by the current r12 matrix. Examples include older handling for Use Case→Requirement refine and Requirement→Function refine.

**Required change:** revise the Decision Log from the current Matrix Rules, not from intermediate handoffs.

## 3. Relationship family READMEs contain drift

Some generated EA Relationship family summaries still show older dispositions/mappings even where later Matrix Rules 72–79 or other r12 amendments now have precedence.

Examples include older allocate summaries that still describe generic “Thing performs Function” behavior where package-context rules now apply first.

**Required change:** regenerate relationship summaries/canvases from the authoritative current rule matrix after precedence is finalized.

## 4. Open Decisions list contains settled topics

`Translator Open Decisions.md` still lists BindingConnector / Connector as unresolved even though current rules define:

- BindingConnector → `equals / equals`;
- Connector → `interfaces / interfaces`.

**Required change:** remove settled topics from the open queue and retain only genuinely unresolved decisions.

## 5. EA element coverage is not complete enough for the new import gate

Current element completeness is certified only for EA type/stereotype combinations that occur as connector endpoints.

The workspace explicitly does **not** yet certify a complete inventory of isolated/unconnected `t_object` rows.

**Required change:** generate a full source-element inventory and prove every supported EA element combination has a definition/disposition.

## 6. MDSE element notes are definitions, not yet complete importer contracts

The MDSE element notes generally define:

- meaning;
- type/subtype nomenclature;
- approved subtype list.

Most do not yet completely define:

- required vs optional YAML properties;
- identity/UID behavior;
- naming/file-name rules;
- folder placement;
- body schema;
- allowed relationship domains/ranges;
- cardinality;
- defaults;
- validation;
- source-property disposition;
- source EA mapping rules.

**Required change:** expand each MDSE element definition into a complete contract before import.

## 7. MDSE relationship vocabulary is incomplete relative to the Matrix Rules

The Matrix Rules currently emit relationship names that do not all have corresponding complete relationship-definition notes.

Known examples include:

- `participants`;
- `equals`;
- `interfaces`;
- `verifies / verifiedBy`;
- `performedBy`;
- `affectedBy`;
- `stateOf / hasState`;
- `applies`;
- `dependencyOf`;
- `derivedBy`;
- `satisfiedBy`.

There is also a terminology mismatch: the MDSE relationship folder currently defines `hasParticipant`, while the settled native rule uses one-sided `participants`.

**Required change:** every relationship property that code can emit must have one canonical MDSE relationship contract.

## 8. MDSE relationship definitions are too thin for code generation

Existing relationship notes usually define semantic meaning, but many do not define all of:

- source/domain types;
- target/range types;
- inverse property;
- symmetric vs directional behavior;
- one-sided exception behavior;
- cardinality;
- YAML serialization;
- duplicate suppression;
- self-link policy;
- validation behavior;
- deprecated aliases;
- Matrix Rule references.

**Required change:** add these fields to every translator-visible relationship definition.

## 9. Current source relationship coverage is not import-ready under the new policy

r12 currently reports:

- **14,444 Settled**
- **4,556 Review**
- **2,813 Deferred**
- **9 Endpoint Exceptions**

That means **7,378 connector instances** are not currently Settled.

Major unresolved families/topics include:

- ControlFlow;
- Sequence;
- StateFlow;
- InformationFlow / Item Flow;
- explicit EA Nesting;
- Usage patterns;
- include patterns;
- State/StateMachine satisfaction;
- Design→Functional Requirement satisfaction;
- RAAML RecoveryRequirement;
- RAAML ASILDecompose;
- StandardProfile Responsibility;
- mixed trace/dependency/realisation patterns;
- source endpoint exceptions.

Under the new “fully define before import” direction, these are **pre-import work**, not post-import cleanup.

## 10. Source-faithful typing vs MDSE type/subtype needs one explicit contract

The previous native change note said permanent YAML `type` should prefer the EA stereotype, otherwise EA `Object_Type`.

The live workspace now defines a canonical MDSE `type → subtype` taxonomy.

Those two statements are not automatically compatible.

**Required change:** for every EA element construct, explicitly define:

- source identity;
- imported canonical `type`;
- imported `subtype` if any;
- preserved EA provenance;
- whether the result is a native EA-derived type or an MDSE semantic type;
- whether later semantic reclassification is permitted/expected.

Do not let importer code resolve this ambiguity implicitly.

## 11. Package hierarchy needs a precise non-semantic rule

Current direction preserves EA package hierarchy for source navigation/traceability, while the broader MDSE methodology says package containment is not itself a semantic relationship.

This is compatible only if stated precisely.

**Required rule:**

- package path/ownership may be retained for navigation, placement, provenance, and explicit rule context;
- package containment does not automatically create `partOf`, `parent`, `appliesTo`, `subject`, or any other MDSE semantic relationship;
- a package name may affect translation only through a documented precedence rule such as current allocate rules 72/73.

---

# Current High-Precedence Relationship Changes

The following r12 rules are important because they supersede older generic or intermediate translator behavior.

## Allocate precedence

Apply the explicit precedence rules before generic allocate interpretation.

- **Rule 72:** source under `05 Product Design` → `designOf / hasDesign`
- **Rule 73:** source under `04 Product Function` → `performedBy / performs`
- **Rule 74:** either endpoint Issue → normalize to `affects / affectedBy`
- **Rule 75:** either endpoint InformationItem → normalize to `describes / describedBy`
- **Rule 76:** residual State involvement → `stateOf / hasState`
- **Rule 77:** Requirement ↔ Activity → Activity `satisfies` Requirement
- **Rule 78:** Requirement ↔ Class/Artifact → Requirement `appliesTo`
- **Rule 79:** Requirement ↔ Object → Requirement `appliesTo`

These package/endpoint rules must be implemented through explicit precedence, not through “best semantic interpretation.”

## Connector behavior

- **Rule 40:** BindingConnector → symmetric `equals`
- **Rule 41:** Connector → symmetric `interfaces`

## Verification

- **Rule 63:** Dependency «verify» testCase → Requirement → `verifies / verifiedBy`
- other verify endpoint patterns remain Review until explicitly resolved.

## Refinement vocabulary

Current r12 narrows `refines / refinedBy` to Requirement→Requirement.

Approved non-Requirement refinement uses `describes / describedBy`.

This supersedes intermediate handoffs that proposed other mappings for those endpoint combinations.

---

# Definition of Complete — EA Elements

Before the next broad import, every in-scope EA element construct must have a definition that answers all of the following.

1. Exact `Object_Type`.
2. Exact stereotype/profile resolution, including no-stereotype behavior.
3. Full-source occurrence count, including isolated/unconnected elements.
4. Import eligibility: Import / Source-only / Ignore / Error.
5. Canonical imported type.
6. Canonical imported subtype, if any.
7. EA provenance fields retained and where they are stored.
8. Source properties/fields:
   - YAML;
   - body;
   - source-only;
   - ignored;
   - transformed.
9. Nested/owned element behavior.
10. Package path/placement behavior.
11. Naming and duplicate-name resolution.
12. Identity/UID and EA GUID behavior.
13. Allowed relationship participation.
14. Body-generation rules.
15. Validation rules and exceptions.
16. Explicit post-import semantic-cleanup candidates, where applicable.

No importer fallback should invent an element mapping that is not represented by such a definition.

---

# Definition of Complete — EA Relationships

Every observed in-scope EA relationship combination must define:

1. raw Connector_Type;
2. effective stereotype/profile;
3. source EA endpoint construct;
4. target EA endpoint construct;
5. source/target direction;
6. package/context precedence;
7. exact Matrix Rule;
8. exact disposition:
   - semantic YAML mapping;
   - source/body-only preservation;
   - explicit Ignore;
   - explicit import Error;
9. source YAML property;
10. target/inverse YAML property;
11. symmetric/one-sided behavior;
12. connector body-detail behavior;
13. duplicate suppression;
14. self-link behavior;
15. missing-endpoint behavior;
16. validation rule.

For the next broad import, an observed in-scope pattern should not remain merely Review or Deferred.

---

# Definition of Complete — MDSE Elements

Every MDSE element used by the importer must define:

1. canonical `type`;
2. approved `subtype` values;
3. folder and prefix;
4. definition/semantic boundary;
5. required YAML;
6. optional YAML;
7. default values;
8. identity/UID behavior;
9. naming/file-name behavior;
10. body structure;
11. allowed relationships;
12. relationship cardinality where constrained;
13. validation;
14. import-source mappings;
15. deprecated names/aliases;
16. post-import edit ownership.

---

# Definition of Complete — MDSE Relationships

Every relationship property that can be written to a model note must define:

1. canonical property name;
2. meaning;
3. domain/source types;
4. range/target types;
5. inverse property, if any;
6. symmetric vs directional behavior;
7. one-sided vs bidirectional storage;
8. cardinality;
9. YAML serialization form;
10. duplicate behavior;
11. self-link policy;
12. source Matrix Rule(s);
13. validation rules;
14. deprecated aliases/migration behavior.

The Matrix Rules must not emit a relationship that is absent from this catalog.

---

# Import Readiness Gate

Do not run the next broad import until all of the following are true.

- [ ] Full `t_object` inventory has been reconciled, including isolated/unconnected elements.
- [ ] Every observed EA element type/stereotype combination has an explicit disposition and element contract.
- [ ] Every observed EA relationship endpoint combination in scope has a deterministic final disposition.
- [ ] Review/Deferred relationship patterns required for the import scope are resolved.
- [ ] Missing-endpoint cases have explicit error/exception handling.
- [ ] Every YAML relationship emitted by a Matrix Rule exists in the canonical MDSE relationship vocabulary.
- [ ] Every MDSE element type/subtype emitted by the translator has a complete MDSE element contract.
- [ ] EA source typing → MDSE `type/subtype` behavior is explicit for every imported construct.
- [ ] Package hierarchy/navigation behavior is explicit and does not create undeclared semantics.
- [ ] Current Matrix Rule precedence is represented consistently in relationship READMEs/canvases.
- [ ] Top-level README, Decision Log, Open Decisions, and rule summaries agree with the live rules.
- [ ] No deprecated `Thing`, `kind`, `hasParticipant`, automatic `subject/subjectOf`, or superseded relationship wording can be emitted by current importer logic unless explicitly preserved as historical evidence.
- [ ] Dry-run validation confirms source counts and rule coverage.
- [ ] No code path implements a material transformation that is not represented in the live Markdown rule set.

---

# Required Consistency Checks

Before implementation is considered release-ready, automated checks should verify at least:

1. every Matrix Rule relationship name resolves to one MDSE Relationship definition;
2. every Matrix Rule endpoint construct resolves to an EA Element definition;
3. every imported target type/subtype resolves to an MDSE Element definition;
4. each observed source relationship combination resolves to exactly one final rule after precedence;
5. no two Settled rules can match the same source combination at the same precedence;
6. no source element or relationship is silently dropped;
7. bidirectional relationships produce both declared properties when required;
8. one-sided `participants` never writes a reciprocal participant property;
9. symmetric relationships such as `equals` and `interfaces` are normalized without duplicate/self-link noise;
10. rule summaries/canvases are generated from the current rule definitions rather than manually diverging;
11. full-source inventory counts reconcile to the source database/export;
12. every deliberate deviation from the original translator appears in this change-management note.

---

# Change-Control Workflow

For any future translator behavior change:

1. identify the affected EA construct, MDSE construct, and Matrix Rule(s);
2. update the authoritative methodology note first;
3. explicitly mark the old behavior as amended/superseded rather than silently relying on an old handoff;
4. update related Matrix Rule(s);
5. update this change-management note and increment its revision;
6. regenerate derived READMEs/Bases/canvases from the authoritative notes where practical;
7. run consistency checks;
8. only then change translator code;
9. capture the rule revision in the dry-run/import manifest.

**Code implements the live Markdown rule set. The code is not the source of truth for translator semantics.**

---

# Change Ledger

| Change ID | Date | Change | Status |
|---|---|---|---|
| NT-CHG-001 | 2026-09-26 | Native importer separated from original semantic translator; semantic cleanup moved toward post-import modeling. | Active |
| NT-CHG-002 | 2026-09-26 | Physical Context remains source-faithful during native import; no automatic Use Case / Where conversion. | Active |
| NT-CHG-003 | 2026-09-26 | Removed automatic `subject / subjectOf`; standardized local Use Case/Context `participants`. | Active |
| NT-CHG-004 | 2026-09-26 | Approved global semantic relationships written explicitly in both endpoint notes; local participation is one-sided exception. | Active |
| NT-CHG-005 | 2026-09-26 | Connector notes suppressed; connector metadata preserved through endpoint YAML/body rules. | Active |
| NT-CHG-006 | 2026-09-26 | Current migration treated as primarily one-way EA → Obsidian; repeat synchronization deferred. | Active |
| NT-CHG-007 | 2026-09-27 | MDSE terminology changed from `Thing` to `Object`; `kind` to `subtype`. | Settled |
| NT-CHG-008 | 2026-09-27 | Source-faithful element typing made explicit across EA element definitions. | Active |
| NT-CHG-009 | 2026-09-27 | BindingConnector maps to `equals`; plain Connector maps to `interfaces` for settled native patterns. | Settled |
| NT-CHG-010 | 2026-09-27 | Dependency «verify» testCase→Requirement maps to `verifies / verifiedBy`. | Settled |
| NT-CHG-011 | 2026-09-27 | Non-Requirement refinement standardized to `describes / describedBy`; `refines` reserved for Requirement→Requirement. | Settled |
| NT-CHG-012 | 2026-09-27 | Allocate package/endpoint precedence formalized in Rules 72–79. | Settled |
| NT-CHG-013 | 2026-09-27 | Package hierarchy clarified as source navigation/provenance/context, not an automatic MDSE semantic hierarchy. | Active |
| NT-CHG-014 | 2026-09-27 | Next broad import changed to **definition-first**: EA and MDSE elements/relationships must be fully defined before import. | Active |
| NT-CHG-015 | 2026-09-27 | Existing Review/Deferred relationship inventory is now a pre-import completion backlog rather than an acceptable broad-import cleanup strategy. | Active |
| NT-CHG-016 | 2026-09-27 | Live Markdown methodology is designated as the executable translator specification/test oracle; code must not introduce undocumented semantics. | Active |

---

# Immediate Pre-Import Backlog

Priority should be driven by what blocks a complete deterministic import, not by writing more translator code.

1. Generate the complete EA `t_object` element inventory and add missing isolated constructs.
2. Resolve the EA-source → imported MDSE `type/subtype` contract for every source construct.
3. Complete MDSE element contracts.
4. Complete the MDSE relationship vocabulary, including all properties emitted by Matrix Rules.
5. Resolve remaining Deferred/Review relationship families and endpoint combinations.
6. Reconcile Matrix Rule precedence into all EA relationship summary notes and canvases.
7. Revise the stale top-level README, Decision Log, and Open Decisions note.
8. Add automated consistency checks for the four-definition layers:
   - EA Elements;
   - EA Relationships;
   - MDSE Elements;
   - MDSE Relationships.
9. Run a source-only dry validation after the rule set is complete.
10. Only then run the next broad EA → Obsidian import.

---

# Revision History

| Revision | Date | Change |
|---|---|---|
| 1.0 | 2026-09-26 | Initial record of deliberate native-import deviations from the original semantic translator. |
| 1.1 | 2026-09-26 | Source-faithful Context handling; one-sided `participants`; removed automatic `subject/subjectOf`. |
| 2.0 | 2026-09-27 | Moved change governance into the live native-translator workspace; incorporated source-faithful element direction, MDSE Object/subtype terminology, current r12 relationship rules and precedence, one-way lifecycle, full-folder review findings, and the new definition-complete import gate. |

## Governance Rule

Every future material deviation from the original translator, and every later amendment to the native translator, must be recorded here or in a linked topic-specific change note.

No material semantic behavior may exist only in translator code, a spreadsheet, a sidecar dataset, an old handoff, or a conversation.
