---
uid:
type: Info
status: Active
workspace: EA Native Translator
documentRole: Program Tracker
lastUpdated: 2026-09-27
---
# Translator Definition Tracker

## Purpose

Single high-level tracker for translator definition progress.

This note records **what work is complete or still required**. Specific semantic decisions remain in their element, relationship, or decision notes.

## Status vocabulary

- **Evidence Complete** — source evidence is available and reconciled.
- **Defined** — methodology contract exists.
- **In Progress** — definition work has started but is incomplete.
- **Blocked by Decision** — human semantic decision required.
- **Implemented** — dependent rules/contracts are reconciled.
- **Verified** — verification fixture/result confirms implementation.
- **Not Started** — no complete definition yet.

## Program tracker

| Area | Status | Evidence / definition | Next action |
|---|---|---|---|
| EA source evidence bundle | Evidence Complete | `99_System/CSV_EA` | Treat as immutable source evidence |
| Full EA element inventory | Evidence Complete | [[EA Full Source Element Inventory]] | Add/complete per-construct import dispositions |
| EA connector inventory | Evidence Complete | r12 + 21,822 connectors | Resolve Review/Deferred families |
| EA element source notes | In Progress | 31 raw Object_Types / 72 raw combinations known | Reconcile source-only constructs and property rules |
| EA relationship source notes | Defined for inventory | 30 raw connector pairs / 1,000 endpoint combinations | Regenerate summaries after rule changes |
| MDSE type/subtype taxonomy | Defined | [[MDSE Type and Subtype Taxonomy]] | Expand each type into complete importer contract |
| MDSE element contracts | In Progress | Definitions exist, contracts incomplete | Required/optional properties, body, validation, placement |
| MDSE relationship vocabulary | In Progress | Core relationships exist | Define every property emitted by Matrix Rules |
| Translation Matrix Rules | In Progress | 79 current rules | Resolve/exclude all non-settled in-scope patterns |
| Source property/tag mapping | Not Started | 249,892 object-property rows + summary available | Start with Requirement |
| Requirement end-to-end definition | In Progress | Review canvas + decision notes + source audit | Human review of subtype/property mapping |
| Verification fixtures | In Progress | Requirement fixtures started | Bind fixtures to approved decisions/rules |
| Import readiness gate | Not Ready | Source complete; semantics incomplete | Do not broad-import until gate is satisfied |
| Repeat synchronization EA↔Obsidian | Not Started | Not part of current one-way migration | Define only after one-way import is stable |

## Current relationship readiness

Current r12 disposition counts:

| Disposition | Connector instances |
|---|---:|
| Settled | 14,444 |
| Review | 4,556 |
| Deferred | 2,813 |
| Endpoint exceptions | 9 |

Under the current definition-first policy, the **7,378 non-settled/exception instances are pre-import work** unless a pattern is explicitly excluded or converted to an import error.

## Current element-source expansion from CSV evidence

The connector-driven source folder set missed these full-source constructs:

- ActionPin
- ActivityParameter
- ActivityPartition
- StateMachine
- Artifact «CustomDocument»
- Class «Environmental Interface»
- Signal «Environmental Effect»
- Signal «Physical Signal»
- Text «NavigationCell»

Individual source notes are being added for these constructs.

## Requirement pilot tracker

| Requirement area | Status |
|---|---|
| Full source inventory | Evidence Complete |
| Stereotype/subtype decision | In Progress |
| Property/tag inventory | Evidence available; mapping Not Started |
| Relationship mappings | In Progress |
| Body/provenance mapping | In Progress |
| Verification fixtures | Fixture Defined for initial cases |
| Human approval | Pending |
| Translator implementation | Partial |
| Verification against implementation | Not Verified |

## Import readiness gate

A broad import is permitted only when:

- every in-scope source element construct has an explicit disposition;
- every source property class has an explicit disposition;
- every in-scope relationship pattern has a deterministic mapping, explicit ignore, source-only policy, or import error;
- every emitted MDSE type/subtype/property is defined;
- every emitted MDSE relationship is defined;
- body/provenance retention rules are defined;
- validation/model checks are defined;
- representative regression fixtures exist.

## How to use this tracker

Update this note when a body of work changes state.

Do **not** document detailed semantic decisions here. Put those where they belong and link to them from this tracker.
