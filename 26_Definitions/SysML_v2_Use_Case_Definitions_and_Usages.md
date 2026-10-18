---
title: SysML v2 Use Case Definitions and Usages
status: approved-mapping-implementation-pending
type: semantic-definition
updated: 2026-10-18
---
# SysML v2 — Use Case Definitions and Usages

[Master MOC](../MOC_MDSE_V2.md) · [Approved EA family](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) · [Include decision](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_USE_CASE_INCLUDE_APPROVED_2026-10-17.md) · [Extend decision](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_USE_CASE_EXTEND_APPROVED_2026-10-17.md).

**Approval:** existing October 17 family and connector decisions, reaffirmed October 18. **Native conformance:** generated examples and source-context semantics still require the pinned official SysML 2.0 parser/library before release. See [OMG SysML 2.0 Language](https://www.omg.org/spec/SysML/2.0/Language/PDF), §7.25 and the standard UseCases library.

## Native meaning and identity
- **UseCaseDefinition**: reusable specification of a goal-oriented interaction/behavior, with formal subject and optional actor parameters, objectives and owned behavior as modeled. One canonical reusable MDSE definition note; independent UID/symbol identity.
- **UseCaseUsage**: context-owned feature representing that use case in a particular subject or enclosing use case. It references an existing definition; repeated roles/contexts are distinct usage IDs, not cloned notes. Include/reuse does not assert definition specialization.
- **Subject and actors**: compatible modeled participant usages and role bindings; external EA Actor may map to a PartDefinition and a local actor-role usage when supported. Do not convert an Actor into an arbitrary native use case.
- **IncludeUseCaseUsage**: required included behavior in owning case; references the included case; retain source roles/qualified context and subject/actor binding. Native keyword `include use case` or `include` only in a legal owner and with official syntax.
- **Extend mapping**: approved optional conditional use case usage within base case, referencing extending definition. Preserve extension point/condition as source evidence, and create only legal native conditional participation constructs after conformance testing; do **not** assume an OMG-native binary «extend» connector or synthesize a guard.

## EA source mapping
| EA source | Native candidate / result | Gate |
|---|---|---|
| `UseCase` element | Reusable UseCaseDefinition | valid name/UID/owner; original EA GUID/provenance |
| `UseCase:include` connector | Parent-owned required IncludeUseCaseUsage | trusted direction + compatible definition and ownership + actor bindings |
| `UseCase:extend` connector | Contextually optional use case usage | extension point/condition semantics supported; else MDSE flagLink |
| Actor participation | Actor-role usage with referenced external PartDefinition | require explicit modeled role/context |
| unsupported generalization/dependency/diagram appearance | no automatic use-case semantics | retain source evidence and flag review |

## Workbench requirements
- Structural: cases under owning context as distinct usage nodes; clicking a usage opens the reusable definition and inverse Where Used.
- Visual: include, optional conditional participation, actor/subject and generalization have different symbols/legend; no generic line conflation.
- Navigation: usage ↔ definition, parent case ↔ included case, origin GUID, conditions and unresolved flags.
- Create/edit: first release read-only; later filtered native operation chooser and parser-validated AST updates to bottom `## SysML v2` text.
- Validation: reject cycles/unknown definitions/incompatible subject, invalid direction, unsupported condition, duplicate occurrence collapse; no semantics from EA package structure.
- Round trip: preserve one definition note, source connector identity per usage, deterministic source role and provenance. Unresolved connector → YAML `flagLink` + body explanation, not a native dependency.

## Acceptance fixtures
1. Case used by two owning contexts → one definition, two usages and correct where-used.
2. Include → required nested use-case construct, actor subject compatible; parse with official library.
3. Extend → optional conditional construct only when grammar supports evidence; otherwise flagLink.
4. Invalid actor binding and reversed source endpoint → no native emission, preserved source evidence.
5. No-op reimport preserves UID, usage ID, model text and note navigation.
6. Obsidian structural/visual panels show separate definitions/usages and approved operations.

## Current implementation gap
The previous canonical graph listed no UseCaseDefinition/UseCaseUsage. Add them to the typed graph and eligibility, then test serializer/official parser; definition presence does **not** establish complete SysML conformance.
