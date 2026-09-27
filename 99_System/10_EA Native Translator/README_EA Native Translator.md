---
uid:
type: Info
status: Working
workspace: EA Native Translator
---
# EA Native Translator

This folder is the living methodology workspace for translating native Sparx Enterprise Architect content into the MDSE vault model.

## Authority model

The methodology notes are authoritative. Bases and canvases are views over those notes and may be regenerated. Source documents, spreadsheets, and older handoffs are evidence, not competing authorities.

## Working principle

Translate engineering meaning rather than mechanically reproducing EA/UML/SysML structures. Apply deterministic mappings where semantics are settled. Where semantics are not settled, preserve migration evidence and flag review rather than guessing.

## Sections

- [[README_EA Elements]] — EA metaclass/stereotype combinations observed or supported.
- [[README_EA Relationships]] — EA connector families.
- [[README_MDSE Elements]] — target MDSE element definitions used by the translator.
- [[README_MDSE Relationships]] — target MDSE relationship definitions relevant to import.
- [[README_Translation Rules]] — executable methodology decisions connecting source and target.
- [[README_Reviews]] — open decisions, change log, and review workflow.
- [[README_References]] — current source references and precedence notes.

## Review workflow

1. Identify the EA source construct and endpoint semantics.
2. Find the applicable Translation Rule.
3. Follow a settled rule without reinterpretation.
4. If no settled rule applies, preserve the source evidence using the current unresolved-mapping convention and add a review item.
5. Promote a repeated pattern to a direct rule only when meaning is consistent enough for deterministic translation.

## Visual review

Open [[CANVAS_EA Native Translator]] for the top-level architecture. Each MDSE target element also has a dedicated translation canvas showing known EA source paths and relationship behavior.
