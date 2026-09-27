---
uid:
type: Info
status: Working
workspace: EA Native Translator
---
# Translator Decision Log

This note summarizes methodology decisions without replacing the individual Translation Rule notes.

## Current decision model

- EA source types are evidence; the most specific engineering meaning wins.
- Translate semantic meaning rather than reproducing UML/SysML mechanics.
- Classify ambiguous source elements before translating relationships whose meaning depends on endpoint type.
- Use direct deterministic mappings where approved.
- Preserve unresolved connector direction through `map*Out / map*In` migration evidence.
- Do not silently guess or discard unresolved source relationships.
- Methodology notes are authoritative; canvases/Bases are views.

## 2026-09-27 relationship amendments represented here

- Use Case → Requirement `refine` → `drives / drivenBy`.
- Requirement → Function `refine` is unresolved rather than automatically `refines`.
- State / State Machine EA `satisfy` → Requirement `appliesTo` State / State Machine.
- Design may satisfy any Requirement type.
- Use Case → Function EA `Usage` → `realizedBy / realizes` for the approved endpoint combination.
- Use Case ↔ Thing Association → `hasParticipant`.
- Note/Info may collapse when one-to-one and low-reuse; retained Info uses `describes`.
- InformationFlow remains deferred pending Port review.
