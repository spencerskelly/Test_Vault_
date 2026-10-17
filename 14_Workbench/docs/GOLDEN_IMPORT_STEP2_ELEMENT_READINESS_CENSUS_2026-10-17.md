# Golden Import Step 2 — Element family readiness census (2026-10-17)

Status: audited **family-level** classification, not row-level acceptance or parser conformance.

Source: local-only `EA_2026_10_15_endgame_mini.qeax`, fixture SHA-256 `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`; read-only SQL `SELECT Object_Type, COALESCE(Stereotype,''), COUNT(*) FROM t_object GROUP BY 1,2`. Existing authority: `SYSML_V2_PHASE2_ELEMENT_FAMILY_MATRIX.md`. No source rows, names or GUIDs committed.

| Disposition | Families | Elements | Interpretation |
|---|---:|---:|---|
| Conditional, approved semantic direction | 23 | 7,044 | Still needs usage/definition and typed source evidence |
| Review | 23 | 3,360 | Specific source semantics required |
| Evidence-only | 13 | 927 | Preserve original records; do not invent native constructs |
| Deferred | 1 | 116 | Variant semantics require decision and valid source evidence |
| **Total** | **60** | **11,447** | Exhaustive, no unmatched family |

## Approved-direction families and counts
- Requirements (eight including base): 2,638; RequirementDefinition / RequirementUsage, preserve constraints as requirements where modeled as requirements.
- Activities and functional activity stereotypes (five): 1,032; ActionDefinition / ActionUsage.
- UseCase: 857; UseCaseDefinition / UseCaseUsage.
- State and System State: 744; StateDefinition / StateUsage.
- Hardware Component: 868; PartDefinition candidate.
- Physical Component: 276; PartDefinition candidate.
- Class:block: 326; PartDefinition candidate.
- Class:Module: 166; PartDefinition candidate.
- Software Component and Software Unit: 124; PartDefinition candidate pending exact architecture.
- Platform: 13; PartDefinition candidate.

## Review families and counts
Package 1,388; Signal:Logical Signal 485; InformationItem 413; Object 341; Class:System Partner 149; Activity:testCase 119; Class:Electrical & Material Interface 114; Class:Data Interface 110; Action 57; Class:Physical Context 43; Actor 36; Class:Mechanical Interface 36; Class:Generic Physical Interface 19; Port 16; Class 13; Part:FlowProperty 6; Signal:Software Parameter 4; Trigger 4; ProxyConnector 3; Constraint 1; Event 1; Part 1; Signal:Physical Signal 1.

**Package is a distinct namespace/provenance concern**: native namespace target is largely clear; do not infer physical containment or vault placement from EA package hierarchy. Excluding Package leaves 1,972 source elements in semantic-review families.

## Evidence-only families and counts
Note 366; Issue 207; Artifact:Image 93; Change 63; StateNode 55; Artifact:Document 51; Text 42; Decision 23; Synchronization 11; Class:Business Line 8; Boundary 3; Sequence 3; Text:NavigationCell 2.

These are not to be silently dropped. Diagram control elements (Decision, Synchronization, StateNode) may hold evidence needed to derive native behavior *only where executable source context supports it*. Preserve originals and separately record derived projections.

## Explicitly deferred
Class:Physical System Variant: 116. Native variation/redefinition must not be inferred from name or stereotype alone.

## Step 2 acceptance gate
1. Per-row immutable source ledger for all 11,447 object rows; one disposition per row.
2. Typed classifier uses exact EA type/stereotype, relevant attributes and explicit source roles; no implicit catch-all.
3. Definition vs usage, classifier, owner, semantic namespace, aliases, and source provenance resolved or explicitly deferred; no conflation of package nesting with part ownership.
4. Each of the 60 families has a runtime rule ID with rule version, evidence requirements and negative synthetic tests.
5. No unsupported SysML construct, automatic variant assumption or model evidence leakage into GitHub.
6. Re-run this census after changes; totals and fixture checksum must agree.

## Highest-impact next rule work
1. Deterministic Package -> namespace/provenance handling (1,388 records).
2. Signal/InformationItem differentiation (899 records total).
3. Object classifier/usage + ownership (341 records).
4. System Partner / Actor role mapping (185 records).
5. Interfaces, ports and flow properties (301 records).
6. Verification case and action context (176 records).
7. Physical System Variant 116 explicitly stays deferred until source-justified variation.
8. Evidence-only records must be kept discoverable outside canonical SysML source.

**This closes the aggregate inventory, not Step 2 implementation.**