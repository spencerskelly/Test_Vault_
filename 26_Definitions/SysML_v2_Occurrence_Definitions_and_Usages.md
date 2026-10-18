---
title: SysML v2 Occurrence Definitions and Usages
status: approved-mapping-implementation-pending
type: semantic-definition
updated: 2026-10-18
---
# SysML v2 — Occurrence Definitions and Usages

[Master MOC](../MOC_MDSE_V2.md) · [Approved Group 3 causation and occurrences](../24_Workbench/docs/SYSML_V2_CAUSATION_OCCURRENCES_APPROVED_MAPPING.md) · [Approved EA family](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md).

**Approval:** native Option A approved October 17, reaffirmed October 18. **Conformance:** emitted real model and library causation constructs require pinning and parser validation. Normative references: [OMG SysML 2.0 Language](https://www.omg.org/spec/SysML/2.0/Language/PDF), §7.9.2–7.9.5, and the standard Cause-and-Effect Domain Library (library-specific exact types must be pinned).

## Semantic classification
- **OccurrenceDefinition**: reusable kind of happening in time, with identity and featuring context. An EA explicit `Event` is a candidate only when it describes a semantic occurrence, not raw telemetry.
- **OccurrenceUsage**: owned, scoped occurrence in an owning model. Reusing a definition never duplicates its note; each occurrence usage has stable owner-scoped ID.
- **EventOccurrenceUsage**: occurrence usage that references an occurring event, with the correct native reference-subsetting semantics; not the same as a signal, message, log record or state.
- **Time slice**: scoped temporal portion of an owning occurrence, with valid time-slice portion kind and featuring context.
- **Snapshot**: instantaneous scoped portion of an occurrence, with valid snapshot portion kind and native portion constraints. Not a static diagram snapshot.
- **Individual occurrence**: explicitly individual modeled happening, not automatic conversion from instance-classifiers or rows; individual typing must satisfy native constraints.
- **Causation**: only approved native standard-domain-library constructs, not arbitrary binary `causes`. Succession only establishes temporal ordering, not causation.

## Source evidence
| Input | Allowed result | Review case |
|---|---|---|
| EA `Event` explicitly modeled as happening | OccurrenceDefinition; local usage if context evident | missing scope/classifier/identity |
| Native authored occurrence/use case/action/state | typed definition/usage as modeled | illegal owner, unresolved symbol |
| EA trigger/state machine event | event occurrence/reference when correctly modeled | trigger/event conflation |
| time tag or log timestamp | evidence only | never invent TimeSlice/Snapshot from timestamp |
| ControlFlow or Transition | approved Succession/Transition only | never infer causation |
| BOM revisions/quantities | source-specific evidence only | never infer duration/causal link |

## Workbench representation
- Structural: definition and owned usage separate, event/time slices nested under legal owning occurrence; roles/duration/scope shown where native.
- Visual: event, occurrence, time slice, snapshot, succession, message, transition, and causation each selectable independently with different help/legend.
- Navigation: source identity → occurrence feature → typed definition; timeline/causal view only projects parsed source and provenance.
- Editing (later): filtered controls must create type-correct native text and parser-validated atomic changes, not standalone Canvas edges.
- Traceability: per-source-row disposition, model UID, qualified symbol and reverse references, no untrusted library name substitution.
- Review: invalid scope/typing/causation yields MDSE-only flagged review with original evidence, not fabricated native syntax.

## Official textual reference shapes (schematic; verify before production emission)
```sysml
occurrence def OvertemperatureEvent;
occurrence eventContext : OvertemperatureEvent;
```
Syntactic demonstration only; scope and library import references are not certified by this note.

## Acceptance fixtures
1. Occurrence definition + two distinct owned usages under legal owners.
2. Correct EventOccurrenceUsage reference and scope; illegal endpoint rejected.
3. Timeslice and snapshot each legal only under owning occurrence; parser/semantic pass.
4. Succession without causation, and explicit causation with pinned domain-library construct.
5. Event log/BOM row does not synthesize OccurrenceDefinition or causal link.
6. Original EA event GUID/owner preserved; flag review on missing identity.
7. Structural/visual/timeline round trip and no-op reimport preserve IDs.

## Current implementation gap
Add OccurrenceDefinition/OccurrenceUsage/EventOccurrenceUsage to typed graph; implement required legal usage/ownership/standard-library checks. Native cause-and-effect grammar awaits exact pinned library names; do not introduce custom native relation.
