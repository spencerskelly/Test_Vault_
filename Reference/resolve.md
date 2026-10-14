The main thing to align on is a shared authoring contract: what a SysML section means, which note owns each assertion, how references resolve, and what the resulting traceability does—and does not—claim.

For your per-element and per-usage notes, I would prioritize **semantics** over formatting. Two teams can write syntactically valid SysML yet build incompatible models if they interpret “function,” “interface,” “satisfies,” or “assembly” differently.

SysML v2 supplies the formal concepts for requirements, behavior, structure, analysis, and verification. Your methodology must define how those concepts map to your engineering work and Markdown documents.[[omg](https://www.omg.org/sysml/sysmlv2/)]

## 1. The main alignment decisions

|Topic|What to agree on|Recommended starting rule|
|---|---|---|
|Element classification|What each note represents|Distinguish reusable definitions, contextual usages, requirements, behavior, interfaces, analyses, and documentation|
|Source authority|Which section owns a declaration|One authoritative declaration or assertion; other appearances are references or generated views|
|Context and ownership|Where a usage formally belongs|Record model ownership explicitly; do not infer it from folders or backlinks|
|Identity|What survives renames and moves|Separate note ID, model address, and persistent element identity|
|Reference resolution|How one note refers to another model element|Use engine-resolved SysML references inside model sections; wikilinks remain document navigation|
|Relationship meaning|What each traceability link asserts|Define endpoint rules, meaning, inverse labels, and review implications|
|Definitions versus usages|Whether a fact is shared or contextual|Common facts belong to definitions; product-specific facts belong to usages|
|Applicability|Which product/configuration the assertion concerns|Make product, variant, operating context, and baseline explicit where relevant|
|Model completeness|Whether missing links indicate an error|Define required coverage by element type and maturity|
|Change impact|What must be rechecked after a change|Separate automatic validation from human review and evidence renewal|
|Extensions|How non-core concepts are modeled|Use controlled libraries/conventions, not arbitrary relationship names|
|Tool baseline|Which syntax and semantics are supported|Pin the language, engine, libraries, and authoring-profile versions|

These are proposed methodology rules, not additional requirements imposed by SysML.

## 2. First settle the meaning of “SysML section”

Your approach can support a note for every usage. The section’s role must still be unambiguous.

I would define three roles:

|Section role|Editable?|Included in the formal workspace?|
|---|---|---|
|Authoritative source|Yes|Yes|
|Generated element view|Through controlled model-edit commands|No—its underlying source is already included|
|Illustrative example|Yes|No|

If a note owns a fragment that must be inserted into another element, give it a fourth explicit role: authoritative fragment.

For fragments, the profile must define:

- The formal parent.
- Namespace/import context.
- How the fragment is assembled.
- How duplicate declarations are detected.
- How diagnostics map back to the note.
- How refactoring updates the fragment and its references.

Do not silently mix complete source units and fragments. That is the biggest architectural ambiguity to resolve before implementation.

### Recommended ownership rule

> Each modeled note has a declared primary element and section role. Each formal declaration has exactly one authoritative source location.

A note may describe several related elements, but the plugin must know which element is its primary subject.

## 3. Define your engineering vocabulary before templates

Your teams need a short concept dictionary.

|Term|Proposed interpretation|
|---|---|
|Need|Desired stakeholder outcome—not necessarily a testable obligation|
|Use case|A goal-oriented interaction in an operational context|
|Requirement|An obligation with an identified subject and acceptance basis|
|Function|Intended behavior, separate from its chosen implementation|
|Design definition|Reusable specification of an implementation concept|
|Object usage|Application of a definition in a particular context|
|Interface|A specified interaction boundary or contract—not merely a document|
|Assembly|A contextual composition of usages and their relationships|
|Verification|Establishes whether specified requirements are met|
|Validation|Establishes suitability for intended needs and use|
|Failure assessment|Contextual analysis of a failure mode and its consequences|

Then specify the formal mapping for each term.

For example, “function” might map to action definitions and usages under your profile. “Interface” might refer to a port definition, an interface definition, or a contextual interaction. Those should not be treated as interchangeable.

SysML’s formal concepts provide the foundation, but “an interface note” is your document category—not enough information to determine the model construct.[[omg](https://www.omg.org/sysml/sysmlv2/)]

## 4. Make traceability relationships precise

I would create a relationship catalog before building the plugin’s graph.

Each entry should define:

```
Relationship name
Question it answers
Permitted source and target types
Formal SysML representation or domain extension
Direction and inverse display label
Applicability/context
Required supporting information
Change-impact policy
```

### The most important distinctions

|Relationship|Meaning|Does not automatically establish|
|---|---|---|
|Motivates|A need or concern explains why something exists|Complete requirement coverage|
|Constrains / has subject|Identifies what a requirement concerns|Satisfaction|
|Allocated to|Associates intended behavior with implementation|Correct implementation|
|Satisfies|Asserts that a design meets a requirement|Verified evidence|
|Verifies|Identifies a verification relationship|A passing result|
|Connected to|Establishes modeled connectivity|A specific flow or failure propagation|
|Carries / flows to|Identifies transferred content and direction|Full protocol behavior|
|Documents|Associates explanatory material|A formal design assertion|
|Mitigates|Identifies a claimed risk-reduction control|Demonstrated effectiveness|

The first column is a proposed readable vocabulary. Not every entry is a native SysML keyword.

In particular, preserve requirement subjects, satisfaction assertions, and verification as distinct formal concepts. Do not use `satisfy` as a generic “related to this requirement” link.[[docs.nomagic](https://docs.nomagic.com/spaces/SYSML2P/pages/254423086/2026x+Satisfy+requirement)][[wrwei.github](https://wrwei.github.io/tutorials/sysml/SysMLv2_Module9_Verification_EN.html)]

## 5. Resolve identity and naming separately

I would distinguish:

```
Document identity:
    NOTE-001842

Model address:
    namespace-qualified name of an element

Persistent model identity:
    identifier intended to survive refactoring
```

Agree on these behaviors:

- Renaming a Markdown file does not rename its model element.
- Moving a note does not change formal ownership.
- Renaming a model element is a refactoring operation.
- Moving an element between model owners may change its meaning.
- Display titles can be friendly; formal names must follow a controlled convention.
- Generated relationships bind to resolved elements, not title matching.

Also document the difference between namespace qualification and feature access. SysML uses `::` for namespace-qualified names and `.` for feature paths; treating them as interchangeable creates confusing references.[[voidaliot.github](https://voidaliot.github.io/sysml-v2-docs/language/02-textual-notation-syntax.html)]

Do not assume that an engine-generated ID is permanent. For example, the toolkit we reviewed documents ownership/name-derived identity and old-to-new ID reporting during transformations.[[github](https://github.com/Open-MBEE/sysml-toolkit)]

## 6. Make context part of the assertion

A relationship often needs more than two endpoints.

Consider:

> Controller satisfies the shutdown requirement.

You need to know:

- Which controller usage?
- In which product configuration?
- Under which operating conditions?
- Against which requirement version?
- With what assumptions?
- Based on what evidence?

For your model, I would define an applicability policy covering:

|Dimension|Example|
|---|---|
|Product|Charger family A|
|Configuration|High-power variant|
|Usage context|Controller in charging assembly|
|Operating mode|Active charging|
|Lifecycle state|Design baseline versus installed unit|
|Revision/baseline|Released configuration|
|Assumptions|Valid temperature input available|

Not every link needs all these fields. The profile should specify which are required for each type of assertion.

## 7. Separate model validity from engineering confidence

Avoid a single “valid” or “approved” flag.

Use independent states:

```
Syntax valid
References resolved
Semantic checks passed
Engineering reviewed
Evidence current
Released
```

For example:

- A satisfaction assertion can be structurally valid but unreviewed.
- A verification case can exist without having been executed.
- A passing test result can apply only to an earlier configuration.
- A failure mitigation can be modeled but not demonstrated.

The engine should report language checks. Your workflow layer should manage review, evidence, and release.

## 8. Define change impact by relationship meaning

Your automatic impacted-note review concept should be driven by semantic differences—not merely file modification or link adjacency.

|Change|Likely review scope|
|---|---|
|Shared port contract changes|Applicable usages, connections, consumers, tests|
|Requirement acceptance criterion changes|Satisfaction assertions, verification cases, results|
|Behavior guard changes|Scenarios, tests, failure-response assessments|
|Product applicability changes|Included/excluded requirements, analyses, documents|
|Failure-control assumption changes|FMEA assessment and supporting evidence|
|Description typo changes|Usually documentation only|

Each review notification should explain the dependency:

> Review required because this verification result depends on the timeout criterion that changed.

Also agree on propagation boundaries. A connection alone should not imply that every change or failure propagates across it.

## 9. Define required coverage without forcing meaningless links

A complete model is not one where every note links to everything.

Set coverage expectations by type and maturity.

Examples:

- A released requirement has a clear subject, rationale, applicability, and verification approach.
- A released interface identifies participants, exchanged content, limits, and relevant failure behavior.
- A safety-relevant function has defined failure-response obligations and associated evidence.
- A technician procedure identifies applicable configurations and the architecture it describes.
- A failure assessment identifies context, effects, controls, and assessment assumptions.

Allow explicit states such as:

```
Not yet modeled
Not applicable—with rationale
External dependency
Unresolved
Intentionally omitted at this abstraction level
```

Otherwise, dashboards will confuse incompleteness with irrelevance.

## 10. Keep extensions controlled

For needs, decisions, issues, evidence, FMEA, supplier qualification, and technician documentation, decide whether each concept is:

1. Native SysML.
2. A formal domain-library extension.
3. A Markdown/workflow record bound to model elements.

Do not create a custom formal type merely because a note needs a category.

For FMEA, define the assessment method, context, controls, ratings, and relationship rules explicitly. Safety-analysis extensions are separate from simply having a core SysML model.[[omg](https://www.omg.org/cgi-bin/doc?syseng/25-03-05.pdf)][[omg](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML)]

## Minimum reference package

Before team rollout, I would require these six artifacts:

1. Concept dictionary: what your engineering terms mean.
2. Note/source contract: section roles, authority, ownership, extraction.
3. Identity and namespace policy: naming, references, renames, moves.
4. Relationship catalog: meaning, endpoints, formal mapping, inverse labels.
5. Assurance and change policy: validity, review, evidence, impact.
6. Validated reference model: one complete slice from need through design, interface, verification, failure analysis, and technician documentation.

Use that reference slice as the acceptance test for both the methodology and the plugin. The strongest test is whether two engineers can independently extend it and produce compatible ownership, relationships, and review behavior—not just text that parses.