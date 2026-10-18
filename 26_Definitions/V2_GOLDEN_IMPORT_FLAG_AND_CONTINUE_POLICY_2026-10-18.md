# V2 Golden Import — Flag-and-Continue Policy

Date: 2026-10-18
Status: user-approved implementation direction; implement in importer, Workbench, validation, and golden import checks.
Scope: EA -> native SysML v2 -> MDSE/Obsidian, including reduced QEAX and subsequent complete QEAX. EA diagrams remain excluded.

## Goal

Prioritize a usable, navigable end-to-end model over perfect semantic resolution of a small number of source data exceptions. Preserve questionable source evidence; never silently drop data or invent native SysML v2 constructs. Do not stall the golden-import critical path for isolated questionable connectors or elements.

## Dispositions

- Native: source evidence and endpoint context support an approved SysML v2 construct. Parser-verified native serialization remains a separate requirement.
- MDSE descriptive relationship/note: source semantics are meaningful but not native SysML v2. Preserve in the relevant owning note, not as made-up native syntax.
- `flagLink`: a specific unresolved connector. Keep one independently traceable record per source connector, including endpoints, original direction, family, source connector GUID/ID, roles, multiplicity, aggregation, reason code, and an explanatory note-body entry. Do not imply hierarchy, containment or connection semantics.
- `flagNote`: source element or note with unresolved type, interpretation, placement, merge, or required source evidence. Preserve original content, source element identity and provenance, intended links where known, and human-readable problem/review action. When the issue is merely an invalid native declaration, preserve the source meaning in an MDSE note rather than dropping it. The exact YAML schema is to be validated in importer and Workbench tests.

Do not equate 'deferred parser acceptance' with unresolved source semantics. Avoid mass-producing flags from the untested native candidates.

## Import failure levels

1. **Fatal / stop import**: unreadable or corrupt QEAX; source/profile/hash mismatch in a pinned gate; non-unique or unusable source identities; source evidence or provenance loss; ledger/count corruption; inability to generate a coherent and navigable vault; unexpected diagram access; unsafe overwrite; unparseable core emitted model; untraceable dropped connectors/elements.
2. **Localized semantic / flag and continue**: unsupported native endpoint or relation, ambiguous direction/owner, non-native note semantics, unclear stereotype, isolated parser-rejected declaration when the source can be faithfully preserved as MDSE note/link. Generate `flagLink` or `flagNote` with reason and source identity; then finish the remaining import.
3. **Warnings / continue**: missing optional multiplicity, omitted optional metadata, source formatting issues, non-critical placement preferences. Log and preserve source where useful.

Do not let a single native parser rejection poison an entire import batch. Isolate the rejected declaration, create an auditable MDSE fallback, revalidate the batch and proceed. Do not mutate the native parser or counterfeit successful validation.

## Review strategy and acceptance

- First complete end-to-end element and connector handling, note generation, navigation, Workbench structural/visual views, validation, and reproducible import.
- Keep summary counts: total imported; native/MDSE/flagLink/flagNote; parser failures contained; unresolved by reason and family; source rows accounted for; source rows dropped (must be zero).
- The 56 previously identified aggregation exceptions and other isolated questionable source connectors are **candidates** for flags, not blockers and not necessarily 56 final flagLinks. Group policy and actual source evidence determine final disposition.
- Use a bounded review queue after functional golden import; do not require manual adjudication of every candidate prior to functional acceptance.
- Stable flags across reimport, no duplicate active source relationship representations, promotion from flag to approved semantics with provenance retained.
- Gate functional acceptance on complete source accounting, preservation, navigability, stable identity, core native parser success, local fallback correctness, and zero silent losses; **not** on zero flags.
- Native emission is authorized only for declarations that have independently passed the native gate. MDSE flags are not native SysML syntax.
- When later importing the complete QEAX, use the same policy and report increased flag volumes by family rather than reopening previously approved mappings without new evidence.

## Near-term implementation order

1. Wire `flagLink` and `flagNote` fallbacks into the existing v2 pipeline, preserving source lineage.
2. Synthetic test malformed endpoints, ambiguous aggregation, duplicated links, isolated native parse failures, and stable reimport.
3. Keep the current pinned read-only QEAX source gate; verify in a checked-out main copy separately from semantic flags.
4. Generate the first end-to-end working model (diagrams disabled), measure actual flags and note/link coverage.
5. Review only high-impact recurring categories or any failure threatening model coherence; retain remaining isolated flags for follow-up.
6. Validate Obsidian and Workbench presentation, navigation and review/resolve behavior before declaring functional golden-import acceptance.

This policy supplements existing approved mapping and flagLink decisions; it does not retroactively imply native parser acceptance.
