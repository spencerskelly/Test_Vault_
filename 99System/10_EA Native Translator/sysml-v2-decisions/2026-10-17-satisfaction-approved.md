# APPROVED — Native SysML v2 Requirement Satisfaction
Date: 2026-10-17
Status: APPROVED — Relationship #18

## Plain language and meaning
A Satisfaction is an explicit assertion that a compatible model feature meets a requirement, with appropriate requirement subject and applicable constraints. It does not, by itself, provide passed-test evidence. An allocated function or design may contribute without automatically satisfying every system-level requirement.

## Scope
- Support native SysML v2 requirement definitions/usages and satisfy requirement assertions involving valid functional action usages, design/part usages, and assembled solutions, when applicable requirement subjects and contexts permit.
- Do not enforce an arbitrary design-only restriction. Functions may genuinely satisfy behavior-focused requirements.
- Evaluate the requirement's declared subject, constraint scope, satisfying feature, and owner; distinguish asserted satisfaction from verified compliance.
- Native syntax and subject legality must be checked with conforming SysML v2 tooling before production export.

## EA migration
- Preserve EA stereotype «satisfy» relationships as native SysML v2 satisfaction when compatible, whether EA source is Function or Design.
- Flag ambiguous or invalid cases (e.g. contribution rather than satisfaction, incompatible subject, unresolved target) for correction, rather than inventing a different relationship or silently dropping it.
- Retain only the source evidence needed for migration/diagnostics; once corrected, SysML v2 syntax in note is authoritative.
- EA Copy aliases are consolidated first; satisfaction references canonical elements while preserving distinct usages.

## Workbench
- Structural: requirement, subject, satisfying feature, owner/context, asserted satisfaction and validation state; navigate in either direction.
- Visual: distinct satisfy relationship; distinguish Function vs Design satisfying subjects without implying test pass.
- Inspector: constraint applicability, native syntax, unresolved ambiguity and verification evidence links where available; clearly label claim vs verification.
- Text/structural/diagram edits change authoritative SysML v2 syntax in owning Obsidian note; synchronize all views.
- One canonical reusable definition per type, individual usages do not require Markdown notes.

## Example
Charger output-voltage regulation requirement may be satisfied by charger structure; a narrowly scoped required control behavior may be satisfied by a corresponding action. Merely allocating voltage regulation to controller does not prove either requirement.

## Documentation comparisons
Satisfaction vs Allocation (responsibility), Verification (test methodology/evidence), Dependency (reliance), Function contribution/refinement (not necessarily satisfaction), and Requirement subject.

## Next relationship
Native Verification Case definitions/usages and verify relationship; distinguish defining a verification method from recording execution results and status.
