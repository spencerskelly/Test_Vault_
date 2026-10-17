# SysML v2 Relationship Reference — Workbench Definitions Panel
Date: 2026-10-17
Status: Approved UX requirement and review index; NOT yet complete normative conformance audit or implemented UI.
See sibling SYSML_V2_*_APPROVED_MAPPING.md documents for migration detail.

## Required Workbench UX
- Keep the editor open and unsaved user work intact. Info icon beside any offered relationship plus global 'Definitions' button opens a nonmodal docked or dismissible popover/side panel; close/reopen without loss of selection, line gesture, zoom, filters or pending changes.
- Focus panel on relationship under hover/selection. Provide search by term, alphabetic browsing, related/conversely confused relationships, one-click contextual compare (2 columns), back navigation and links to full local Markdown definition.
- Show short plain-language definition first, followed by official metamodel term, source and target eligibility, role/direction, ownership, creation result, valid syntax, graphical representation, examples and 'not the same as' distinctions.
- Use accurate context: state/action/part vs definition/usage and owning workflow. Show why an option is disabled or absent without offering invalid selection.
- Panels source their content from in-vault versioned relationship registry, not UI literals; cached index allowed. Definitions can be referenced offline.
- Per construct store: canonical ID, normative SysML version & citation, status (draft / approved mapping / formally validated / implemented), eligible metaclasses, owner/context, possible feature/port/event requirements, notation with verified parser examples, migration variants with rule IDs and exceptions, validation diagnostics, source provenance, Workbench view rendering, and links to impact backlog.
- Comparing constructs must NOT flatten perform/exhibit (owned usages), feature typing, membership and other native constructs into ordinary binary connectors.
- Every documented rule lists impacts to EA translator, BOM translator, Workbench, vault definitions, validation and follow-up tasks.
- All view filters are presentation-only, independent per view; model and view remain separate. Workflow notes carry local model and separate custom Canvas.
- Provide keyboard access, scrolling, resizing and open definition in an adjacent tab optional; default does not navigate away.

## Reviewed mappings and concise distinctions
| Construct | Short definition | Not equivalent to | Rule / status |
|---|---|---|---|
| Part/feature membership | An owned or referenced feature in its legal context | Binary connection | Previous review; consolidated normative entry needed |
| PerformActionUsage | Object's owned usage of action behavior | Generic Allocation | SYSML_V2_EA_ALLOCATION_ELEMENT_TYPE_DECISION.md; approved |
| ExhibitStateUsage | Object's owned usage of state behavior | Generic Allocation or state transition | SYSML_V2_EA_ACTIVITY_DESIGN_ALLOCATIONS.md; approved |
| AllocationUsage | Architectural mapping between model features | Perform, Exhibit, Connection | SYSML_V2_EA_ALLOCATION_ELEMENT_TYPE_DECISION.md; approved |
| FlowUsage | Transfer between compatible directed features with payload when modeled | Connection, Message, SuccessionFlow | SYSML_V2_FLOW_APPROVED_MAPPING.md; approved |
| Message (specialized Flow) | Communication relating send and receive events | Undifferentiated physical flow | SYSML_V2_MESSAGE_AND_VISUAL_FILTERS.md; approved |
| SuccessionUsage | Temporal ordering of occurrences | Dependency | SYSML_V2_SUCCESSION_APPROVED_MAPPING.md; approved |
| SuccessionFlowUsage | Transfer plus ordering semantics | Generic Flow or Succession | SYSML_V2_SUCCESSION_APPROVED_MAPPING.md; approved |
| TransitionUsage | Trigger/guard/effect state-based change | Generic Succession | SYSML_V2_STATE_TRANSITIONS_APPROVED_MAPPING.md; approved |
| InterfaceUsage | Specialized connection between ports | Any port-to-port Connection | SYSML_V2_INTERFACE_APPROVED_MAPPING.md; approved |
| Dependency | Client relies on supplier without stronger implied semantics | Allocation, Connection, Succession | SYSML_V2_DEPENDENCY_APPROVED_MAPPING.md; approved |
| Binding | Equality/binding semantics of compatible features | Connection/Flow | Earlier review decision; consolidated normative entry needed |
| Port definition/usage/conjugation | Typed interactions of boundary features | Generic interface arrow | Earlier review; consolidated normative entry needed |
| Requirement verification | Verification case relation to requirement intent | Test execution result | Earlier review; consolidated normative entry needed |
| Requirement derivation | Derivation among requirements | Generic Dependency | Earlier review; consolidated normative entry needed |
| Requirement decomposition | Owned/nested and referenced requirement usages | Derivation | Earlier review; consolidated normative entry needed |
| Constraint/assertion | Expresses and applies constraints | Requirement or calculation | Earlier review; consolidated normative entry needed |
| Calculation | Typed numerical/derived evaluation model | Constraint | Earlier review; consolidated normative entry needed |
| Attribute/Enumeration/Quantity | Definition, usage, value, literals, kinds and units | Generic tag | Earlier review; consolidated normative entry needed |

## Documentation audit: known remaining work
- Current repo contains decision documents for Flow, Message/filters, Succession, Transition, Interface, Allocation/Perform/Exhibit, Workbench, Workflow; Dependency has dedicated file as of this decision.
- Previously reviewed topics (Binding, requirements, constraints, calculations, attributes, quantity units, port distinction etc.) are referenced in conversation but do not yet have an individually verified normative definition entry in this directory. DO NOT label 'all complete'.
- Verify exact v2.0 textual syntax, metamodel constraints, normative reference and conformance tests; previous explanatory examples may be simplified, and a number of EA mappings are contextual rather than one-to-one.
- Build comprehensive list of *all* native relationship/feature operations; this reviewed index is not a complete SysML v2 language inventory.
- Explicitly separate standards concepts from Workbench projections and MDSE/EA legacy meaning.
- Generate a single shared metadata registry consumed by translator and Workbench help/eligibility views.

## Follow-ups
HELP-01 Inventory prior decisions and deduplicate/resolve inconsistent rules.
HELP-02 Formal normative review of all entries with linked OMG metamodel clauses/examples.
HELP-03 Create machine-readable registry plus versioned individual Markdown definition notes in vault.
HELP-04 Generate documentation/eligibility menus/info popovers from same registry.
HELP-05 Add hover and context selection, dockable persistent panel, compare, search and keyboard behavior.
HELP-06 Add client/source-target/ownership/direction explanations and exception flags.
HELP-07 Link each definition to EA/BOM translator impact and rule provenance.
HELP-08 Automated catalog completeness, native semantic validation and UI regression tests.
HELP-09 Include examples from actual EA corpus and approval-state annotations after model audit.
HELP-10 Add save/reload/undo test while definitions panel is open.
