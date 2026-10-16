Use YAML for the note’s management and integration metadata, SysML v2 for authoritative engineering meaning, and the Markdown body for explanation, rationale, procedures, and evidence.

The governing rule should be **authority**: each fact has one editable source, even if it appears in several views.

Importantly, “not built into core SysML” does not automatically mean “put it in YAML.” SysML v2 supports metadata definitions for organization-specific information, and model documentation can carry natural-language statements. Use those mechanisms when the information needs to travel with the exported model.[[ibm](https://www.ibm.com/docs/en/systems-engineering/1.6.0?topic=extension-metadata-support)][[sysml.visual-paradigm](https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-2-defining-the-mission-use-cases-and-requirements/)]

## 1. Recommended division

|Location|Primary purpose|Placement test|
|---|---|---|
|YAML|Manage and locate the document|Does this describe the note, its workflow, publishing, or integration?|
|SysML section|Define the engineering model|Does this affect the system’s meaning, relationships, constraints, behavior, or analysis?|
|Markdown body|Explain and communicate|Does this explain why, describe uncertainty, present evidence, or guide a person?|

This is a responsibility boundary—not a restriction on what each format can technically store.

Obsidian properties are particularly suited to small, atomic values: text, links, lists, numbers, dates, and checkboxes. Rich Markdown is not rendered in properties, and nested properties are better handled in source mode. That supports keeping YAML relatively flat and concise.[[obsidian](https://obsidian.md/help/properties)]

## 2. Relationships: where they should live

The following is my proposed placement policy. Formal mappings still need to be validated against your selected engine and domain libraries.

|Relationship or association|Authoritative location|Explanation|
|---|---|---|
|Definition → usage typing|SysML|Determines what a usage is|
|Assembly → owned part usage|SysML|Establishes formal composition and context|
|Definition → specialization|SysML|Changes inherited model meaning|
|Component → port|SysML|Establishes its modeled interaction boundary|
|Port → port connection|SysML|Defines connectivity|
|Source → destination item flow|SysML|Defines transfer, payload, and direction|
|Function → implementing design allocation|SysML|Engineering architecture relationship|
|Requirement → subject|SysML|Identifies what is constrained|
|Design → requirement satisfaction|SysML|Formal assertion, not just a navigation link|
|Verification case → requirement|SysML|Formal assurance relationship|
|State → transition → state|SysML|Behavior|
|Product → variant/configuration selection|SysML|Where it defines modeled product variability|
|Failure mode → effect → control|SysML extension|Formal analysis meaning under a defined FMEA profile|
|Need → use case → requirement traceability|SysML or qualified extension|Keep formal if used for coverage and impact analysis|
|Note → represented model element|YAML|Document-to-model binding|
|Note → responsible team|YAML|Workflow responsibility|
|Note → reviewer|YAML|Review routing|
|Note → related decision or issue record|YAML or body|Administrative association unless formally modeled|
|Note → publication collection|YAML|Document organization|
|Note → audience|YAML|Publishing/filtering metadata|
|Explanation → supporting source|Body|Citation, quotation, context, interpretation|
|Procedure → related architecture|Body link; YAML for indexed associations|Navigation unless it asserts a formal engineering dependency|

Native SysML supports structure, behavior, and requirements; requirement subjects, satisfaction, and verification must retain their separate meanings.[[blogs.sw.siemens](https://blogs.sw.siemens.com/teamcenter/sysml-v2-guide/)][[docs.nomagic](https://docs.nomagic.com/spaces/SYSML2P/pages/254423086/2026x+Satisfy+requirement)][[wrwei.github](https://wrwei.github.io/tutorials/sysml/SysMLv2_Module9_Verification_EN.html)]

### Avoid these authoritative YAML relationships

I would not make the following editable YAML fields compete with SysML:

```
parts:
ports:
connected_to:
flows_to:
typed_by:
satisfies:
verifies:
```

They could exist as generated search properties, but not as a second authoring surface unless the plugin explicitly writes edits back into the formal model.

### YAML relationships need their own vocabulary

Prefer document-specific names:

```
model_ref:
reviewers:
related_decisions:
open_issues:
source_records:
publication_sets:
```

Do not use a generic `related` field for everything. It loses meaning and cannot support reliable impact rules.

## 3. Descriptive information: where it should live

|Information|Recommended home|Qualification|
|---|---|---|
|Stable note ID|YAML|Identifies the document|
|Formal element name and ownership|SysML|YAML may select the element, not redefine it|
|Human-readable note title|Body heading|YAML aliases can support search|
|Formal model description|SysML `doc`|Description should accompany exported model|
|Short document summary|YAML, optional|For listings; must not introduce new engineering obligations|
|Requirement’s normative statement|SysML documentation|Keep the authoritative “shall” statement with the requirement|
|Mathematical acceptance constraint|SysML|Typed expressions and model references|
|Requirement rationale|Body|May be exported into model documentation if required|
|Design rationale and alternatives|Body|Supports human reasoning|
|Engineering assumptions|SysML if part of analysis; body for explanation|Do not leave consequential assumptions only in informal prose|
|Operating limits and units|SysML|Engineering values, not loose text properties|
|Review owner/status/date|YAML|Workflow|
|Intended documentation audience|YAML|Publishing|
|Procedure steps, cautions, troubleshooting|Body|Human-facing instructions|
|Test specification|SysML plus body|Formal obligations in model; detailed instructions in body|
|Test result narrative and attachments|Body or external evidence record|YAML can index result metadata|
|Formal verification result association|SysML or qualified extension|Needed for assurance traceability|
|FMEA ratings and controls|Formal extension/analysis record|Do not treat safety meaning as arbitrary note metadata|
|Research notes and supplier discussion|Body|Unapproved knowledge|
|File paths, external URLs, source-system IDs|YAML where short and queryable|Body explains their relevance|

SysML documentation can contain a natural-language requirement statement alongside a subject and formal constraint. Therefore, keeping the requirement text only in Markdown would unnecessarily weaken model portability.[[sysml.visual-paradigm](https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-2-defining-the-mission-use-cases-and-requirements/)]

## 4. What genuinely does better in YAML?

Some information could be expressed through SysML metadata but is usually more convenient in YAML.

### Good YAML candidates

```
note_id: NOTE-001842
document_kind: model-source
model_section_role: authoritative
primary_symbol: Charging::Controller
document_owner: Controls Engineering
review_status: draft
review_due: 2026-11-01
audiences:
  - engineering
  - service
publication_sets:
  - charger-service-reference
aliases:
  - Charge Controller
```

These fields describe your vault and its workflow. They do not define the controller’s engineering behavior.

SysML metadata can represent process and tool-extension information, but placing every editorial field in the model would couple the formal model to your documentation platform.[[ibm](https://www.ibm.com/docs/en/systems-engineering/1.6.0?topic=extension-metadata-support)]

### Important distinctions

|YAML field|Different formal concept|
|---|---|
|`document_owner`|Model-element ownership|
|`review_status`|State-machine state|
|`publication_products`|Formal product applicability|
|`primary_symbol`|Declaration and identity of the model element|
|`audiences`|Formal stakeholder/viewpoint modeling|
|`document_revision`|Product/design revision|

Name fields so those differences are visible.

### No core modeling feature is inherently better in YAML

For your goal of staying close to SysML, I would not move parts, requirements, ports, flows, states, constraints, or formal allocations into YAML merely because the property editor is easier.

If users need a simpler editing interface, build a form that edits the SysML source. That preserves one formal representation.

## 5. Handling information that SysML does not directly track

Use this decision sequence:

```
Is it engineering meaning?
    No → YAML or Markdown.

    Yes → Is there a suitable native SysML construct?
              Yes → Use it.
              No → Is it important for formal analysis,
                   traceability, exchange, or impact?
                       Yes → Define a qualified extension.
                       No → Keep it in Markdown,
                            optionally indexed through YAML.
```

### Examples

|Information|Treatment|
|---|---|
|“Reviewed by Alex last Friday”|YAML/workflow|
|“Supplier recommends this alternate”|Body, with source and qualification status|
|“This alternate is permitted in configuration B”|Formal configuration model|
|“This failure control reduces the assessed risk”|FMEA extension with assumptions/evidence|
|“This technician guide discusses the interface”|Document association|
|“This procedure verifies a requirement”|Formal verification relationship, not just `related_requirements`|

For FMEA, a controlled extension is preferable to an ad hoc YAML schema if the data drives engineering analysis. Safety-analysis concepts are extension territory, and compatibility with native v2 must be established.[[omg](https://www.omg.org/cgi-bin/doc?syseng/25-03-05.pdf)][[omg](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML)]

## 6. One note showing the boundaries

This example illustrates the layout. The YAML is a proposed document schema; the model references and declarations must resolve in your selected workspace.

````
---
note_id: NOTE-00421
document_kind: model-source
model_section_role: authoritative
primary_symbol: ChargingRequirements::ShutdownOnLostTemperature
document_owner: Controls Engineering
review_status: draft
audiences:
  - engineering
  - verification
related_decisions:
  - "[[Temperature Timeout Decision]]"
open_issues:
  - "[[Define Temperature Message Validity]]"
---

# Shutdown on lost temperature information

## Authoritative model

```sysml
package ChargingRequirements {

    requirement def ShutdownOnLostTemperature {

        subject charger : Charging::WarehouseCharger;

        doc /*
         * While charging, the charger shall disable charging
         * if no valid battery temperature information has been
         * received for 500 ms.
         */
    }
}
```

## Rationale

The charger must not continue relying on indefinitely stale
temperature information.

The selected timeout requires confirmation against battery-message
timing and the shutdown response budget.

## Formalization status

The normative statement is modeled.
An executable timing constraint has not yet been added.

The absence of that constraint must not be interpreted as
automatic verification of the requirement.

## Verification considerations

Exercise missing, stale, and invalid temperature information
while charging.

The formal verification case and its requirement relationship
will be modeled separately.

## Related engineering evidence

- [[Battery Message Timing Measurements]]
- [[Temperature Timeout Decision]]

## Open questions

- Does timeout recovery require a new charging authorization?
- How is invalid information distinguished from missing information?
````

Here:

- YAML routes and manages the document.
- SysML owns the normative obligation.
- Markdown explains the reasoning and unfinished work.
- The prose does not silently create satisfaction or verification assertions.

The use of `doc` for a natural-language requirement is consistent with published SysML v2 examples. The example remains subject to your engine and authoring-profile validation.[[sysml.visual-paradigm](https://sysml.visual-paradigm.com/docs/sysml-v2-studio-kick-start-guide/cohesive-system-model-in-8-views/step-2-defining-the-mission-use-cases-and-requirements/)]

## 7. Generated YAML: useful, but clearly non-authoritative

You may want Bases or other property-driven views to filter model information.

Allow the plugin to publish fields such as:

```
derived_model_kind: requirement-definition
derived_verification_count: 2
derived_unresolved_reference_count: 0
derived_model_status: resolved
```

Rules:

1. Use a reserved prefix.
2. Treat these fields as disposable caches.
3. Regenerate them from the model.
4. Do not use them as formal input.
5. Show whether they are current.
6. Prefer the plugin index for large or complex relationship collections.

This makes YAML a convenient query projection without turning it into a competing model.

## 8. The policy I would adopt

Write these rules into the reference:

1. Formal engineering relationships and values are authoritative in SysML.
2. Model documentation that must travel with the model belongs in SysML documentation or metadata.
3. Document workflow, publishing, and integration fields belong in YAML.
4. Rationale, procedures, research, and detailed evidence belong in Markdown or linked records.
5. Engineering-critical information outside native SysML uses a documented extension—not arbitrary YAML by default.
6. Generated properties and views are never independent authorities.
7. When information appears in multiple places, the profile identifies its source and generation direction.
8. Changes to relevant YAML or Markdown records can still trigger review; formal placement is not the only determinant of engineering importance.

This gives you a useful boundary: SysML defines what the model asserts, YAML manages how the document participates in the environment, and Markdown explains and communicates the engineering behind it.