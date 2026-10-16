---
title: SysML v2 Translator and Workbench
status: planned
date: 2026-10-15
sourceRepository: spencerskelly/Test_Vault_
---
# SysML v2 Translator and Workbench

## V2 workspace navigation

**Location:** This is the numbered `29_` research/planning area. Active v2 definitions live in `26_Definitions/`, test documentation in `25_Testing/` and Workbench product work in `24_Workbench/`.

- [Definition README](../26_Definitions/README.md) — authoritative v2 decisions, OMG mapping, BOM contract and gated delivery plan.
- [Tools README](Tools/README.md) — planned translator, parser, BOM and Workbench source modules.
- [Testing README](../25_Testing/README.md) — acceptance fixtures and external conformance gates.
- [BOM Integration](../26_Definitions/BOM%20Integration.md) — BOM-ALT-001 and configuration/revision interpretation.

**Scope:** SysML v2 is authoritative for formal structure and relationships; the established main-element-to-note mapping remains. Keep shared source interpretation separate from version-specific translation. This README retains the earlier 24-step baseline as historical planning context; see [V2 Delivery Plan](../26_Definitions/V2%20Delivery%20Plan.md) for the active integrated sequence.

## Purpose
Create a browser-based HTML/JavaScript CSV-to-SysML v2 translator and interactive model workbench while preserving the existing MDSE pathway. EA source semantics and import normalization MUST be common, versioned, and reusable. Translation rules MUST be separate and independently versioned.

## Governance / architecture
EA CSV exports -> **Shared EA source schema** -> parsed validated source graph -> **profile-specific transformations** -> semantic target graph -> SysML v2 text / Obsidian notes / JSON / review report.

- Shared source schema covers CSV filenames, fields, column aliases, element identifiers, types, stereotypes, tagged values, packages, connectors, endpoints, multiplicities, ownership, notes, provenance and row counts.
- The common source graph MUST NOT silently impose MDSE or SysML v2 meaning on ambiguous EA records.
- MDSE translation profile preserves existing approved MDSE behavior. SysML v2 translation profile models definitions/usages, namespaces/features, ports/interfaces/connections, actions/states, requirements/verification, metadata extensions, and specialization.
- Separate profile tests, version numbers and diagnostics. Reuse ingestion, identity, integrity, provenance and reporting components.
- Preserve EA GUID and IDs as source provenance; stable MDSE/SysML identities follow explicit deterministic rules, not filenames.
- No silent discards: disposition is translated, translated-with-extension, unresolved, deliberately-excluded, or failed, with explanation.
- EA package organization is not automatically physical containment. Preserve the MDSE rule: Activities stereotyped 'function' remain Functions independent of folder. Existing 'exposes' relation requires explicit review as likely derived navigation.
- Do not place imported model data in the tooling repository; keep fixtures synthetic or sanitized.

## Plan and acceptance gates
### Phase 1 — baseline and standards (1–4)
1. Inventory current HTML translator and workbench; freeze baseline.
2. Inventory actual CSV exports and formalize shared source schema/manifest.
3. Pin OMG SysML v2/KerML/specification and parser/reference implementation revisions.
4. Author comprehensive EA-to-MDSE and EA-to-SysMLv2 mapping matrices for elements and relationships; mark lossy/ambiguous mappings. **Hard gate.**
### Phase 2 — source normalization (5–8)
5. Load split CSV files, check expected row counts and part completeness.
6. Normalize EA source graph without target-specific interpretation.
7. Establish reproducible source GUID and target UID mapping.
8. Validate dangling connectors, duplication, graph cycles, broken namespace references and provenance.
### Phase 3 — SysML v2 semantics (9–13)
9. Build semantic intermediate representation for definitions, usages, features, ownership and memberships.
10. Structural conversion: packages, parts, attributes, specialization, multiplicity.
11. Behavior conversion: actions, states, use cases.
12. Interfaces/connectivity: ports, interface contracts, connections and flows.
13. Requirements, verification and MDSE metadata extensions (issues, FMEA, variants).
### Phase 4 — independent outputs (14–17)
14. Serialize valid deterministic SysML v2 textual notation (.sysml).
15. Generate Obsidian Markdown vault and navigation with traceability.
16. Emit canonical JSON, conversion manifest, mapping disposition evidence.
17. Independently parse/validate SysML v2 text and cross-check identity and links across outputs. **Hard gate.**
### Phase 5 — HTML workbench (18–21)
18. Graph/element/relationship browser with reverse lookup and filters.
19. Side-by-side EA source, MDSE, SysML v2 result and confidence/status.
20. Human corrections as validated, auditable overrides distinct from imported sources.
21. Diff/review/approval workflows for consecutive exports and changes.
### Phase 6 — golden import (22–24)
22. Synthetic micro-model -> selected subsystem -> cleaned CSV dataset.
23. Deterministic repeat import + change handling + independent reference validation.
24. Golden fixture, documentation, release gate, version history and integration into Test_Vault_.

## Step 1 mapping workbook
Workbook **EA_SysMLv2_Step01_Elements_Relationships.xlsx** (delivered separately in conversation) includes two tabs: **Elements** and **Relationships**. The rows are an initial mapping vocabulary, *not an asserted complete enumeration of the user's current CSV exports*. Populate verified unique (EA Type, stereotype) and (connector type, stereotype) combinations and frequencies from exported CSV in Step 2. EA-common meaning is shared; MDSE and SysML v2 interpretations are distinct.

## Step 1 completion criteria
- All active HTML translator/workbench entrypoints, source paths, versions, dependencies, and tests inventoried.
- Shared EA source-contract defined without target model assumptions.
- Initial Elements and Relationships workbook reviewed and gaps listed.
- Baseline preserved on main; feature changes introduced only through reviewed commits.
- Repo contains tool code and documentation, not production EA model data.

## Standards
- https://www.omg.org/spec/SysML/2.0
- https://github.com/Systems-Modeling/SysML-v2-Release
