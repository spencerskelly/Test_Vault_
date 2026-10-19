# V2 note mapping matrix — EA → MDSE note → native SysML v2

> **Generated file — do not edit.** Source: `26_Definitions/tools/build_v2_mapping_matrix.py`. Edit the governed sources it joins, then regenerate. Status columns show what is approved and what is still only a candidate; nothing here enables emission.

## How to read a note

Every v2 note has the same shape. See [ADR-V2-06](ADR_V2_06_NOTE_FORMAT_2026-10-18.md).

| Zone | Owner | Contents |
|---|---|---|
| Frontmatter | importer sets, humans may add | `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, then `sourceRole`, `primarySymbol`, then relationship fields |
| **User zone** (top) | **humans** | title, note text, `## Notes`, aliases, former ids |
| `## Source: EA` | importer | EA GUID and kept EA values (translated notes only) |
| **`## SysML v2`** (bottom) | **importer / Workbench** | exactly one fenced `sysml` block: the authoritative model text |

## Governed note types

| type | id prefix | subtypes |
|---|---|---|
| Object | `OBJ-NNNNN` | electrical, circuit, mechanical, software, firmware, part, interface |
| Item Flow | `IFLOW-NNNNN` | information, energy, material |
| Behavior | `BEH-NNNNN` | function, activity, action, step |
| Functional Flow | `FFLOW-NNNNN` | — |
| Condition | `COND-NNNNN` | state, state machine, mode, design |
| Requirement | `REQ-NNNNN` | functional, design, standard, stakeholder, engineering |
| Use Case | `UC-NNNNN` | what, where, why, when, who |
| Actor | `ACT-NNNNN` | — |
| Failure Mode | `FM-NNNNN` | — |
| Issue | `ISS-NNNNN` | engineering issue, lifecycle risk |
| Info | `INFO-NNNNN` | — |
| Verification | `VER-NNNNN` | test, analysis, inspection, demonstration |
| Procedure | `PROC-NNNNN` | test, assembly, configuration, commissioning, calibration, maintenance, repair, decommissioning |
| Setup | `SETUP-NNNNN` | — |
| Plan | `PLAN-NNNNN` | — |
| Result | `RES-NNNNN` | — |
| Document | `DOC-NNNNN` | — |
| Artifact | `ART-NNNNN` | — |
| modelCheck | `MC-NNNNN` | StateNode, Change, Boundary, Decision, ActivityPartition, Trigger, Synchronization, Sequence, ActionPin, ProxyConnector, Event, ActivityParameter, Package |
| Diagram | `DIA-NNNNN` | custom, logical, use case, composite structure, statechart, activity, sequence, package |

## Element families (31 EA object types, 60 resolver families)

`Native` is the approved candidate from the family resolver. `parser` and `emit` stay `no` until the official parser accepts the output (STEP-00 gate).

| EA type | EA count | Note outcome (decision) | Native SysML v2 (resolver family → kind, disposition) | parser | emit |
|---|---:|---|---|---|---|
| Requirement | 13,988 | **Requirement**; subtype by rule: EA package path of the element, first match wins (old tool rule R-01, D-049, with W-115 change… (W-115) | Requirement → RequirementDefinition, native_candidate<br>Requirement:requirement → RequirementDefinition, native_candidate<br>Requirement:designConstraint → RequirementDefinition, native_candidate<br>Requirement:functionalRequirement → RequirementDefinition, native_candidate<br>Requirement:extendedRequirement → RequirementDefinition, native_candidate<br>Requirement:Functional → RequirementDefinition, native_candidate<br>Requirement:Webasto Requirement → RequirementDefinition, native_candidate<br>Requirement:performanceRequirement → RequirementDefinition, native_candidate | no | no |
| Port | 4,387 | **no note** — Local Model record (Interface); see W-384 (W-384) | Port → PortUsage, native_candidate | no | no |
| Part | 3,137 | stereotype FlowProperty (760) → Item Flow note, one each (W-132); its direction becomes transmits (out 171), receives (in…<br>PDATA1 names a Class (2,055) → folded into the assembly as a hasPart entry, plus a source-section line when the Part has…<br>PDATA1 names an Activity, State or Signal (219) → folded into the owner as a hasChild entry (W-137, W-149)<br>no usable block: PDATA1 missing from the export o… → Object note, subtype part, unnamed ones part 1, part 2 (W-138) (W-136) | Part → PartUsage, native_candidate<br>Part:FlowProperty → ItemUsage, native_candidate | no | no |
| InformationItem | 2,825 | sits in IPC ! / 03 Product Requirement / Regulatory Requirements → **Requirement**/standard<br>sits in any other package → **Info** (W-115) | InformationItem → —, mdse_note | no | no |
| Class | 2,737 | **Object**; subtype `interface` for recognized classes, else none (W-384) | Class:Hardware Component → PartDefinition, native_candidate<br>Class:Physical Component → PartDefinition, native_candidate<br>Class:block → PartDefinition, native_candidate<br>Class:Module → PartDefinition, native_candidate<br>Class:Software Component → PartDefinition, native_candidate<br>Class:Software Unit → PartDefinition, native_candidate<br>Class:Platform → PartDefinition, native_candidate<br>Class:Physical System Variant → PartDefinition, native_candidate<br>Class:Business Line → PartDefinition, native_candidate<br>Class → PartDefinition, native_candidate<br>Class:System Partner → PartDefinition, native_candidate<br>Class:Electrical & Material Interface → InterfaceDefinition, native_candidate<br>Class:Data Interface → InterfaceDefinition, native_candidate<br>Class:Mechanical Interface → InterfaceDefinition, native_candidate<br>Class:Generic Physical Interface → PortDefinition, native_candidate<br>Class:Physical Context → PartDefinition, native_candidate | no | no |
| Activity | 1,668 | stereotype is testCase → **Verification**/test<br>stereotype includes function, regardless of package location → **Behavior**/function<br>under 04 Product Function → **Behavior**/function<br>all remaining Activities → **Behavior**/activity (W-384) | Activity → ActionDefinition, native_candidate<br>Activity:System Function → ActionDefinition, native_candidate<br>Activity:Hardware Function → ActionDefinition, native_candidate<br>Activity:Software Function → ActionDefinition, native_candidate<br>Activity:Module Function → ActionDefinition, native_candidate<br>Activity:testCase → VerificationCaseDefinition, native_candidate | no | no |
| UseCase | 1,667 | **Use Case**; subtype by rule: EA package the element sits in, under IPC ! / 01 Product Use Case (W-140) (W-140) | UseCase → UseCaseDefinition, native_candidate | no | no |
| Package | 1,386 | the package has a Notes description → a folder, plus a modelCheck note with subtype Package named like the package inside that …<br>any other package → a folder only, no note (W-147) | Package → —, folder_only | no | no |
| State | 1,112 | stereotype identifies a mode → **Condition**/mode<br>element sits in 05 Product Design or below it → **Condition**/design<br>all remaining States → **Condition**/state (W-384) | State → StateDefinition, native_candidate<br>State:System State → StateDefinition, native_candidate | no | no |
| Signal | 623 | **Item Flow** (W-131) | Signal:Logical Signal → ItemDefinition, native_candidate<br>Signal:Physical Signal → ItemDefinition, native_candidate<br>Signal:Software Parameter → AttributeDefinition, native_candidate | no | no |
| Object | 545 | **Object** (W-135) | Object → PartDefinition, native_candidate | no | no |
| Artifact | 459 | eaType Document → **Artifact**<br>eaType Image → **Artifact**<br>eaType CustomDocument → **Artifact** (W-143) | Artifact:Image → —, attachment_link<br>Artifact:Document → —, attachment_link | no | no |
| Note | 431 | **Info** (W-145) | Note → —, mdse_note | no | no |
| Action | 323 | **Behavior**/action (W-384) | Action → ActionUsage, native_candidate | no | no |
| Issue | 264 | **Issue** (W-144) | Issue → —, mdse_note | no | no |
| StateNode | 73 | **modelCheck**/StateNode (W-146) | StateNode → StateUsage, native_candidate | no | no |
| Change | 65 | **modelCheck**/Change (W-146) | Change → —, mdse_note | no | no |
| Text | 61 | **Info** (W-145) | Text → —, mdse_note<br>Text:NavigationCell → —, mdse_note | no | no |
| Actor | 44 | **Actor** (W-144) | Actor → PartDefinition, native_candidate | no | no |
| Boundary | 44 | **modelCheck**/Boundary (W-146) | Boundary → —, aggregate_boundary_note | no | no |
| Decision | 34 | **modelCheck**/Decision (W-146) | Decision → —, mdse_note | no | no |
| ActivityPartition | 28 | **modelCheck**/ActivityPartition (W-146) | — | no | no |
| Trigger | 27 | **modelCheck**/Trigger (W-146) | Trigger → —, conditional_review | no | no |
| Synchronization | 14 | **modelCheck**/Synchronization (W-146) | Synchronization → —, conditional_review | no | no |
| Sequence | 11 | **modelCheck**/Sequence (W-146) | Sequence → —, reference_only | no | no |
| ActionPin | 6 | **modelCheck**/ActionPin (W-146) | — | no | no |
| ProxyConnector | 5 | **modelCheck**/ProxyConnector (W-146) | ProxyConnector → —, reference_only | no | no |
| StateMachine | 2 | **Condition**/state machine (W-384) | — | no | no |
| Constraint | 1 | **Info** (W-145) | Constraint → ConstraintDefinition, native_candidate | no | no |
| Event | 1 | **modelCheck**/Event (W-146) | Event → OccurrenceDefinition, native_candidate | no | no |
| ActivityParameter | 1 | **modelCheck**/ActivityParameter (W-146) | — | no | no |

## Relationship families (26)

| EA family | EA count | Approved direction | Native SysML v2 operation | Disposition | Evidence required | parser | emit |
|---|---:|---|---|---|---|---|---|
| Generalization | 3,735 | specialization | Specialization | conditional_native_candidate | direction_and_endpoint_evidence | no | no |
| Abstraction:allocate | 2,605 | native allocation | AllocationUsage | conditional_native_candidate | semantic_roles | no | no |
| Aggregation | 2,267 | owned PartUsage where physical containm… | TypedOwnedUsage | conditional_native_candidate | ownership_and_endpoint_category | no | no |
| Dependency:satisfy | 1,330 | native satisfy | SatisfyRequirementUsage | conditional_native_candidate | requirement_and_objective | no | no |
| Realisation | 883 | part-to-action perform; part-to-require… | ContextualPerformOrAllocate | conditional_native_candidate | endpoint_roles | no | no |
| Dependency:refine | 596 | Dependency plus Refinement metadata | DependencyWithRefinementEvidence | conditional_native_candidate | source_qualifier | no | no |
| Dependency | 429 | native Dependency | Dependency | conditional_native_candidate | endpoints_and_roles | no | no |
| Dependency:trace | 414 | Dependency with trace provenance | DependencyWithTraceEvidence | conditional_native_candidate | source_qualifier | no | no |
| Association | 395 | ConnectionUsage if connectivity proven;… | ConnectionUsage | conditional_native_candidate | actual_connectivity | no | no |
| UseCase:extend | 378 | conditional optional case usage | ConditionalUseCaseUsage | conditional_native_candidate | extension_context | no | no |
| ControlFlow | 271 | Succession with source guards | SuccessionUsage | conditional_native_candidate | source_action_occurrences | no | no |
| Dependency:deriveReqt | 232 | requirement derivation | RequirementDerivation | conditional_native_candidate | requirement_endpoints | no | no |
| NoteLink | 220 | MDSE YAML links; no native relationship | — | reference_only | metadata_only | no | no |
| UseCase:include | 219 | required nested case usage | RequiredUseCaseUsage | conditional_native_candidate | owning_use_case | no | no |
| Sequence | 193 | reference-only interaction | — | reference_only | non_diagram_source_reference_only | no | no |
| StateFlow | 171 | state transition | TransitionUsage | conditional_native_candidate | state_context | no | no |
| Nesting | 137 | approved nested state/activity/port/req… | ContextualNestedUsage | conditional_native_candidate | native_owner_context | no | no |
| Usage | 128 | generic Dependency unless independently… | DependencyUnlessStrongerEvidence | conditional_native_candidate | source_intent | no | no |
| Dependency:verify | 47 | verification | VerifyRequirementUsage | conditional_native_candidate | verification_case_and_requirement | no | no |
| Dependency:RecoveryRequirement | 10 | requirement derivation | RequirementDerivation | conditional_native_candidate | requirement_endpoints | no | no |
| Connector | 9 | port-to-port ConnectionUsage | ConnectionUsage | conditional_native_candidate | port_compatibility | no | no |
| Abstraction:Derive | 6 | requirement derivation | RequirementDerivation | conditional_native_candidate | requirement_endpoints | no | no |
| Abstraction:trace | 5 | Dependency with trace provenance | DependencyWithTraceEvidence | conditional_native_candidate | source_qualifier | no | no |
| Usage:Responsibility | 4 | allocation when role is evidenced | AllocationUsage | conditional_native_candidate | responsibility_roles | no | no |
| Abstraction:Refine | 3 | Dependency plus Refinement metadata | DependencyWithRefinementEvidence | conditional_native_candidate | source_qualifier | no | no |
| Realisation:deriveReqt | 1 | requirement derivation only with compat… | RequirementDerivation | conditional_native_candidate | requirement_endpoints_and_role | no | no |

## Where EA values go (properties)

Dispositions are per EA field and tag. `property` becomes frontmatter; `body` becomes a `- <tag>: <value>` line in `## Source: EA`; `structure` is consumed by the translator; `archive`/`drop` are not in the note.

| Source | property | body | structure | archive | drop | pending |
|---|---:|---:|---:|---:|---:|---:|
| EA field: tObject | 2 | 4 | 7 | 8 | 36 | 0 |
| EA field: tConnector | 0 | 6 | 10 | 14 | 49 | 0 |
| EA field: tPackage | 0 | 1 | 5 | 1 | 16 | 0 |
| EA tagged values | 0 | 38 | 3 | 0 | 80 | 0 |

Fields decided as frontmatter properties: `tObject.Object_Type`, `tObject.Stereotype`. Tagged values decided as frontmatter properties: **none**.

### Tagged values kept as `## Source: EA` lines (38), most populated first

| EA tag | rows with a value | real values | group |
|---|---:|---:|---|
| id | 5,012 | 5,012 | Identity |
| SysML1.4::text | 2,685 | 49 | — |
| SysML1.4::id | 2,391 | 2,391 | Identity |
| Webasto MBDV Profile::Priority | 2,373 | 118 | Requirements |
| text | 681 | 351 | — |
| User Story | 118 | 118 | — |
| MFG PN | 101 | 101 | Identity |
| Applicability Comment | 45 | 45 | Requirements |
| Product Management Comment | 37 | 37 | — |
| CMF | 15 | 15 | Physical and cost |
| Cable Compatibility | 15 | 15 | Electrical |
| Style | 13 | 13 | Physical and cost |
| Webasto MBDV Profile::Applicability Comment | 11 | 11 | Requirements |
| Engineering Comment | 10 | 10 | — |
| Quantity | 10 | 10 | Physical and cost |
| SignalType | 10 | 10 | Electrical |
| PN | 7 | 7 | Identity |
| Brand | 6 | 6 | Identity |
| Piece Cost | 6 | 6 | Physical and cost |
| Current Max | 5 | 5 | Electrical |
| PartNumber | 4 | 4 | Identity |
| Sales Comment | 4 | 4 | — |
| Occurence | 3 | 3 | Failure mode |
| PN Change Level | 3 | 3 | Identity |
| Severity | 3 | 3 | Failure mode |
| Material | 2 | 1 | Physical and cost |
| Webasto MBDV Profile::External Reference | 2 | 2 | Requirements |
| Weight (g) | 2 | 2 | Physical and cost |
| source | 2 | 2 | Requirements |
| verifyMethod | 2 | 2 | Requirements |
| CurrentOutMax | 1 | 1 | Electrical |
| Detection | 1 | 1 | Failure mode |
| Positions | 1 | 1 | Physical and cost |
| PowerMax | 1 | 1 | Electrical |
| VoltageInMax | 1 | 1 | Electrical |
| VoltageInMin | 1 | 1 | Electrical |
| VoltageOutMax | 1 | 1 | Electrical |
| VoltageOutMin | 1 | 1 | Electrical |

## Open mapping items detected in the sources

- **InformationItem** (2,825): The 2,383 InformationItems in the package 03 Product Requirement / Regulatory Requirements become Requirement notes with subtype standard (W-115). The other 442 are not decided.
- **Class:System Partner** resolver review note: external_part
- **Actor** resolver review note: external_part
- **Action** resolver review note: UNTYPED_ALLOWED_REVIEW_FLAG
- **Part** resolver review note: UNTYPED_ALLOWED_REVIEW_FLAG
- **Port** resolver review note: UNTYPED_ALLOWED_REVIEW_FLAG
