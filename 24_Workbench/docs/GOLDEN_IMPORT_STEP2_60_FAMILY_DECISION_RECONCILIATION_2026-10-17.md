# Golden Import Step 2 — Approved 60-family matrix reconciliation

Date: 2026-10-17. Status: **decision coverage audit complete; runtime implementation and row-level acceptance pending**.

This document reconciles the original `SYSML_V2_PHASE2_ELEMENT_FAMILY_MATRIX.md` against subsequent explicit approvals in `GOLDEN_IMPORT_STEP2_*_APPROVED_2026-10-17.md` and user instructions. The old matrix is a *historical candidate inventory*, not current translation authority where superseded. No fixture rows or proprietary model identities are committed.

## Global rules
- One MDSE note per reusable definition. Local typed/untyped usages live in owning model and generate no extra notes. Source classification `type`, `subtype`, `eaType`, `eaStereotype` retained in YAML; source provenance preserved.
- EA packages import as organizational folders, not SysML semantic packages or containment. Explicit model ownership must be independent.
- Source connectors are separately evaluated by approved relationship registry. Deferred semantics preserve evidence and review diagnostics, never silently disappear.

## Current mapping, grouped by exact EA families

### Native reusable definitions (40 source families, including conditional Physical Context)
- `Requirement`, `Requirement:requirement`, `Requirement:designConstraint`, `Requirement:functionalRequirement`, `Requirement:extendedRequirement`, `Requirement:Functional`, `Requirement:Webasto Requirement`, `Requirement:performanceRequirement` -> RequirementDefinition.
- `Activity`, `Activity:System Function`, `Activity:Hardware Function`, `Activity:Software Function`, `Activity:Module Function` -> ActionDefinition; owning contextual usage when source evidence supports.
- `UseCase` -> UseCaseDefinition; actor/case usages local.
- `State`, `State:System State` -> StateDefinition; local usages within workflow.
- `Class:Hardware Component`, `Class:Physical Component`, `Class:block`, `Class:Module`, `Class:Software Component`, `Class:Software Unit`, `Class:Platform`, `Class:Physical System Variant`, `Class:Business Line`, unstereotyped `Class` -> PartDefinition.
- `Class:System Partner`, `Actor` -> external PartDefinition; Actor may have native actor-role usages in cases.
- `Object` -> PartDefinition. Valid previous instance-classifier reference maps to native specialization (not typing); unresolved/incompatible target flagged. Preserve original classifier in provenance.
- `Class:Electrical & Material Interface`, `Class:Data Interface`, `Class:Mechanical Interface` -> InterfaceDefinition.
- `Class:Generic Physical Interface` -> PortDefinition with typed PortUsage in owner.
- `Signal:Logical Signal`, `Signal:Physical Signal` -> ItemDefinition.
- `Signal:Software Parameter` -> AttributeDefinition.
- `Activity:testCase` -> VerificationCaseDefinition with explicit valid verify relationships.
- `Constraint` -> ConstraintDefinition.
- `Event` -> OccurrenceDefinition.
- `Class:Physical Context` -> if composite context, native PartDefinition with typed contained PartUsages and MDSE type Context; if a single external referenced part, external PartDefinition. Ambiguous source classification flagged.

### Native local usages / behavior (7 source families)
- `Action` -> owned ActionUsage, untyped allowed with `UNRESOLVED_ACTION_TYPE`.
- `Part` -> owned PartUsage, untyped allowed with `UNRESOLVED_PART_TYPE`.
- `Port` -> owned PortUsage, untyped allowed with `UNRESOLVED_PORT_TYPE`.
- `Part:FlowProperty` -> ItemUsage owned by port; retain explicit direction, typing when known.
- `StateNode` -> independent StateUsage local to workflow.
- `Synchronization` -> local fork/join workflow construct based on actual incoming/outgoing control-flow evidence.
- `Trigger` -> local transition trigger.

### MDSE note / attachment / view / organizational / no native node (13 source families)
- `Package` -> folder only.
- `InformationItem` -> description-only MDSE note with links; not native ItemDefinition.
- `Note` -> MDSE note with YAML element links.
- `Issue` -> MDSE Issue note with source-backed affected-element YAML links.
- `Change` -> MDSE change note with YAML element links.
- `Decision` -> descriptive MDSE note, source-backed connections/guards and YAML links; no inferred executable branching.
- `Text`, `Text:NavigationCell` -> MDSE notes, simplified names, original URL in YAML, YAML links.
- `Artifact:Image`, `Artifact:Document` -> attachments referenced in element YAML.
- `Sequence` -> reference-only interaction/workflow view, preserving order/participants/messages, no inferred executable succession.
- `ProxyConnector` -> reference to original connection/endpoints; no invented port/part or separate usage note.
- `Boundary` -> remove from generated model (still disposition-ledgered).

## Reconciliation outcome / questions not yet decided
The enumerations above account for all 60 distinct exact source-family names from the original matrix; the grouping is **40 native definition families + 7 local usage/behavior families + 13 non-native/reference families = 60**. The source SQL census remains the authoritative source-row count.

**Single potential remaining modeling decision:** what MDSE subtype should label `Class:Physical Context` when it is a single external part versus a multi-part context? Native mapping is already approved; do not block import on subtype label until schema matching is implemented. No other missing semantic-family decision identified.

## Implementation blockers (not user semantic questions)
1. Machine-readable ruleset superseding the dated Phase 2 candidate matrix.
2. Row-level classification for 11,447 source elements with source-evidence contract and stable target identities.
3. Owned local usages, independent of organizational package hierarchy, with unresolved-owner diagnostics.
4. Native serializer/parser validation, including untyped usages, fork/join, actor role, and Object specialization.
5. MDSE note/attachment/view writer and YAML link/provenance validation, repeat-import safety.
6. Connector direction/eligibility evaluation remains independent of family eligibility.

**Do not mark Step 2 production-complete based on this classification audit.** It completes semantic decision reconciliation only.
