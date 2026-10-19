# MDSE Rules Register

Status: DRAFT for owner review, 2026-10-19. One list of every rule in the repo that drives effort, by phase and area. Supersedes nothing yet: Ruleset 1.23 and the Decision Log stay in force until the owner baselines Ruleset 2.0 from this register.

**Phases.** P1 = EA import + Base Vault/Bootstrap + read-only Workbench. P2 = BOM import and merge/approval. P3 = Workbench editing. Later = third-party documents, validation, GSE BOMs, diagrams, cross-vault. Standing = always applies, no build effort.

**Status.** Active = in force. Proposed = not approved. Open = undecided. Stale = names things later removed. Partly superseded / check = a later decision changed part of it.

**P1 steps.** 0 Decisions, 1 Model definition, 2 Importer: EA to notes, 3 SysML text and parser, 4 Base vault and Bootstrap, 5 Read-only Workbench, 6 Acceptance on real QEAX.

Sources: Decision Log W-01 to W-398 and its Open section; V2 ADRs, contracts, mapping audits and schemas; Ruleset 1.23 via the Ruleset 2.0 draft; owner decisions of 2026-10-19. Where rows overlap, the newer decision wins; contradictions are in the Conflicts section. The 51 CI workflows and the STEP/PASS documents are evidence of runs, not rules, and are not listed.

## Phase plan

| Phase | Step | Rules |
|---|---|---|
| Standing | - | 61 |
| P1 | 0 Decisions and governance | 8 |
| P1 | 1 Model definition | 85 |
| P1 | 2 Importer: EA to notes | 99 |
| P1 | 3 SysML text and parser | 19 |
| P1 | 4 Base vault and Bootstrap | 12 |
| P1 | 5 Read-only Workbench | 4 |
| P1 | 6 Acceptance on real QEAX | 8 |
| P2 | - | 28 |
| P3 | - | 3 |
| Later | - | 19 |

## Standing rules (always apply) (61)


### AI processes

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-058 | Active | Every AI process has a written instruction file and an ID. The index is in `AI_INSTRUCTIONS.md`. | R-12.1 (MDSE definition) |
| REG-059 | Active | AI processes do not edit model files unless the process is a note-creation process under R-2.x. Changelog review (AI-CR-01) is report-only. | R-12.2 (`99_System/02_AI/processes/AI_Process_Changelog_Review.md`) |
| REG-060 | Active | AI does not create or split vaults. It may recommend a split. | R-12.3 (1.23 §12) |
| REG-061 | Active | AI does not invent source facts. | R-12.4 (`AI_INSTRUCTIONS.md`, 1.23 §6) |

### Base vault, Bootstrap, release

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-028 | Active | Each importer and its clean base vault are a matched pair with one release version, checked before planning or writing (mdse_release in .vault.yaml). | W-299 |
| REG-029 | Active | During pre-release the Base pins Workbench 0.1.16 while the standalone candidate is 0.1.17; mdse-release.yaml records candidateVersion. | W-342 |
| REG-030 | Active | Controlled runtime dependencies need explicit value: essential = Bootstrap, Workbench, Templater, Advanced Canvas, Obsidian Git; provisional = Fileclass, Breadcrumbs; review for retirement = Dataview. | W-354 |
| REG-031 | Active | Plugin stack reviewed as a dependency surface; Dataview removed from the controlled runtime after replacement and startup-cost gates passed (no Dataview queries in the vault; Bases + Workbench cover it). Conflicts with older docs that still name Dataview (C-14). | W-361,W-370 |
| REG-032 | Active | Pre-release integration base may pin the declared Workbench candidate (0.1.17, then 0.1.18 as first WB-106-capable release with Local Model 0.4); an issued release may not. | W-379,W-386 |

### Classes and types

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-019 | Active | MDSE entities are Object (not Thing). Notes use type and subtype (not kind). EA's own metaclass is written EA Object. | W-02 |

### Governance and documents

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-033 | Active | Claude may push directly to main on Test_Vault_. Topics are decided one at a time. | W-07 |
| REG-034 | Active | AI_INSTRUCTIONS.md is the one set of AI instructions. AGENTS.md at the root is a pointer to it. | W-23 |
| REG-035 | Active | One clean Translator Definition file states what the stage 1 translator must do and is updated whenever a change is made. The import reads the .qeax directly; CSV files only defined the rules. | W-246,W-247 |
| REG-036 | Active | Obsidian-native-first policy: prefer representations native to core Obsidian, then conventional Markdown/YAML, and use custom syntax only when needed. Local Model records use native block IDs. | W-306 |
| REG-037 | Active | 00 - Current State.md is the single entry point and registry for the methodology workspace; mdse-release.yaml is its machine-readable twin and the single release/build authority. check-release.py verifies both. The lean engineering base intentionally omits them. | W-320,W-321 |
| REG-038 | Active | Documentation clean-up: outdated material archived with banners; a plan to a golden model is the sequencing document. | W-326 |
| REG-039 | Active | Tool authority: Test_Vault_ governs importer, Bootstrap, base builder, schemas and tool boundaries; MDSE_Workbench governs Workbench source and releases. Test_Vault_ top-level folders are per tool (Importer/, Bootstrap/, Base Vault/, 00_Workspace/, Cross-Vault/); 99_System/ is shared semantics and rules. | W-328,W-329 |
| REG-040 | Proposed | One coordinated release manifest pins compatible Base Vault, Importer, Bootstrap, Workbench and SysML rule/schema versions and hashes. Base owns default assets and managed settings; Bootstrap owns installation and upgrades; Workbench owns interactive model writes; Importer owns import reconciliation. No tool overwrites another tool's user-owned data. Author identity is provenance, not authentication; credentials stay in OS or service stores, never shared YAML. | V2-58 (Shared Note and Release Contract) |
| REG-041 | Active | Twelve goals G01 to G12. First release = G01 to G08 (governance, SysML catalog, canonical graph/UID, EA translator, parser/note writer, Base Vault, read-only Workbench, CI/golden acceptance). Later = G09 editing/reimport/merge, G10 BOM, G11 Bootstrap/team updates, G12 cross-vault. Five evidence gates: approved scope 20%, executable integration 30%, automated tests 20%, real fixture + parser/GUI verification 20%, versioned release/docs 10%. Percentages are planning estimates, not pass rates. A passing synthetic test never increments a parser, GUI or release gate. G01 done-when: every active rule has one canonical home and no contradictory active definitions (this register is that step). | V2-61 (Program Goals) |
| REG-042 | Active | Priority order: (1) canonical decisions, index and links; (2) verify executable entrypoints and CI, pin parser/source/registry; (3) wire a small approved EA slice through serializer, note writer, disposable vault and read-only Workbench; (4) scale coverage, then later phases. | V2-62 (Program Goals priority) |
| REG-043 | Active | Tool ownership: Workbench owns UI behavior, disposable index, ModelRef navigation, schema-valid edit transactions and Review disposition (not semantics, importer mapping or release packaging). Bootstrap owns safe activation repair, release verification and author registration. Importer owns source translation, naming/identity allocation and import evidence (not editing or plugin management). Base builder owns the runtime payload, governed plugin config and pins/hashes. Cross-vault is deferred (archived resolver is reference only). A tool may not silently broaden or redefine model semantics; archived material never overrides a current source. | V2-63 (Tool Boundaries) |
| REG-044 | Active | Shared contracts all tools obey: relationships.yaml, element-types.yaml, local-model.yaml, Ruleset + Decision Log precedence, ModelRef, native Obsidian links and block IDs (preserve block fragments), release manifest and plugin lock. Comparison protocol: a semantic change needs a W-decision first; Workbench-only UX changes use the WB decision path. CONFLICT: the page says Workbench source moves into Test_Vault_ 55_Workbench (provisional) while W-328 says MDSE_Workbench is authoritative. | V2-64 (Tool Boundaries) |
| REG-045 | Proposed | A rule changes only by a dated decision that names the rule it replaces. Superseded rules are marked, not deleted. | R-13.1 (this draft) |
| REG-046 | Proposed | Each rule in this Ruleset has an enforcing test or is listed as a gap. | R-13.2 (this draft) |

### Identity (uid, id)

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-001 | Active | Templates serve hand-authored and translated notes and are the single definition of a class. Every note gets uid and id filled automatically. Outside material keeps its own identification. Duplicate ids are handled by a periodic AI sweep. | W-06 |
| REG-002 | Active | Author code is 13 characters: last name then first name, lowercase letters only, truncated to 13, padded right with hyphens. | W-10 |
| REG-003 | Active | Authors are mapped from EA Author values to codes in authors.yaml. Login and display names of one person are one author. | W-11 |
| REG-004 | Active | uid timestamp (yyyyMMddHHmmssSSS) is local time, not UTC. Translated notes carry EA creation time exactly as stored. | W-13 |
| REG-005 | Active | Every id uses a five-digit number (for example REQ-00042). An id is never reused. | W-15 |
| REG-006 | Active | A note is retired, not deleted: status Retired, id stays reserved. A validator flags gaps in numbering. | W-18 |
| REG-007 | Active | Templates fill uid and id through two Templater snippets. id is the prefix plus highest existing number plus one, counting retired notes and formerIds. | W-20 |
| REG-008 | Partly superseded / check | AI-created notes (no user instruction) use an AI author code; notes made under a user's direction use the user's code. | W-21 |
| REG-009 | Active | AI author code is tool name, then ai, then hyphens to 13 characters. Tool names longer than 11 letters are cut to 11. | W-22 |
| REG-010 | Active | People are one note each in 99_System/04_People, from a Person template (code, name, timezone, previousCodes, eaNames). | W-25 |
| REG-011 | Active | The id snippet and AI instructions count ids listed under ## Former ids when finding the highest number. | W-259 |
| REG-012 | Active | One global 30-character identity-token namespace spans notes and Local Model records; a token is never reused. The kind prefix (part-, ep-, conn-, flow-) is not a separate namespace. A promoted local entity keeps its token. | W-315 |

### Naming and folders

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-027 | Active | Full-import usability amendments: folder structure is navigation, no count-based splits, about 5 to 6 folder levels, a one-child folder collapses only when it has no independent value. | W-297 |

### Note format and templates

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-013 | Active | The old eaGUID appears only at the bottom of the note body, for traceability. Not a frontmatter property. | W-03 |
| REG-014 | Partly superseded / check | Note properties in fixed order: type, subtype, id, uid, status, eaType, tags. Only tags holds more than one value. | W-97 |
| REG-015 | Active | Relationship fields follow tags in the order of relationships.yaml and may hold lists. | W-126 |
| REG-016 | Active | Legacy folder values are removed from element-types.yaml, except Diagram (72_Diagrams). | W-242 |
| REG-017 | Active | Notes in 99_System carry no type or subtype but keep id, uid and status. | W-243,W-244 |
| REG-018 | Active | Hand-made class templates end with ## Notes, ## Aliases and ## Former ids, in that order (modelCheck excepted). | W-265 |

### Relationships

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-020 | Active | supersedes/supersededBy is kept for elements replaced by another note. Nothing in the import writes it. | W-191 |
| REG-021 | Active | Relationship endpoint rules (allowed source and target classes) live on each relationship in relationships.yaml. | W-272 |
| REG-022 | Active | Inverse relationship fields are written by the translator and Workbench, not Nodian. The forward field wins when they disagree. | W-275 |
| REG-023 | Active | Relationship endpoint rules by family: structure (hasPort, includes/includedIn for shared aggregation), requirements (satisfies, derivedFrom, refines, verifies, appliesTo requirement to any), behavior and allocation, interfaces and flows (exposes/exposedBy), triggers (triggeredBy/triggers), description and issues (drives any to any, affects incl. Use Case, describes), state fields (initialState, finalState). The definition-note key appliesTo is renamed usedOn. | W-277,W-278,W-279,W-280,W-281,W-282,W-283,W-284,W-285,W-286 |
| REG-024 | Active | tracesTo is the provisional relationship: anyone may create it, and every link is a Review finding until replaced. | W-288 |
| REG-025 | Partly superseded / check | hasState/stateOf is restored. An Object hasState a State or State Machine, never hasChild. | W-291,W-292 |
| REG-026 | Active | State and State Machine never satisfy a Requirement. Only Function and Design satisfy. A state-scoped requirement uses appliesTo State or State Machine. Tools must not infer or display state satisfaction. | W-327 |

### Schemas

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-056 | Active | Schema versions in force: element-types 1.18, relationships 1.36, local-model 0.5. Classes: Object, Item Flow, Behavior, Functional Flow, Condition, Requirement, Use Case, Actor, Failure Mode, Issue, Info, Verification, Procedure, Setup, Plan, Result, Document, Artifact, modelCheck, Diagram. modelCheck is a holding class for EA elements with no approved mapping and is not created by hand; Diagram uses folder 72_Diagrams (V1 holdover). Relationship fields follow tags (after governed optional properties). Paired, symmetric and one-way relationship vocabulary lives only in relationships.yaml. | V2-65 (Schemas) |
| REG-057 | Active | authors.yaml: defaultTimezone America/Los_Angeles; AI authors claudeai-----, chatgptai----, rovoai-------, geminiai-----; a user-directed note uses the user's code even if an AI wrote it; the generic unmapped fallback sparxeaauthor is overridden by skellyspencer for the EA8647 import. | V2-66 (Schemas) |

### Scope

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-049 | Active | One vault only. No cross-vault links. Final vault holds engineering notes plus a few definitions and diagrams. Methodology and translation material stays out of it. Test_Vault_ is a workspace, not the built vault. | W-01 |
| REG-050 | Active | Final folder structure follows the EA package structure. 99_System is kept and edited topic by topic. Legacy empty model folders were removed. | W-04 |

### SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-051 | Active | New development goes in the v2 workspace (numbered 20+ folders). V1 is frozen reference evidence. A v2 change never modifies 10_*, 11_* or other v1 areas without explicit cross-version approval; shared changes must be compatible with both pipelines. | V2-01 (Architecture Decisions) |
| REG-052 | Active | Safety: QEAX, BOM originals, private ledgers, EA identifiers and generated real model content stay out of public Test_Vault_. Never claim native certification from source normalization or parser-only syntax acceptance. | V2-11 (Baseline 10) |
| REG-053 | Active | Public repos hold synthetic content only. No real product names, BOMs, drawings, customers, revision histories or source exports. Real models are imported only in a private/local environment. A scan is a backstop, not a guarantee. spencerskelly/v2_test is the user-authorized disposable synthetic integration repo; Test_Vault_ stays the method and tool authority. | V2-25 (Functional Parity) |
| REG-054 | Active | Phased release: first usable release is validated EA import plus read-only Workbench; graphical editing and the BOM importer are later phases but their interfaces are kept. Hybrid managed configuration: core plugin and schema compatibility is centrally governed, approved personal preferences survive updates, with versioned ownership, migration, dry-run diff and rollback before distribution. Cross-vault: design IDs, links and resolver now, ship after single-vault validation. | V2-40 (ADR-V2-01 to 04; Release Architecture) |
| REG-055 | Active | Non-negotiable: approved mappings are not reopened because implementation is incomplete; native OMG SysML v2 only, with non-native MDSE evidence and review flags distinct; V2 builds independently of archived V1; each source element and connector gets an auditable disposition with zero hidden drops; syntax parsing, semantic validation, end-user UI and package/release acceptance are different gates. | V2-42 (Release Architecture) |

### Testing and acceptance

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-047 | Active | Workbench candidate CI runs a 60,000-note semantic-cache scale smoke (completion/memory regression gate, not timing). | W-368 |
| REG-048 | Active | Canvas geometry is presentation only. It never creates a semantic relationship. | R-11.2 (`AI_INSTRUCTIONS.md`) |

## Phase 1: EA import, Base Vault/Bootstrap, read-only Workbench (235)


### 0 Decisions and governance: Open decisions

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-262 | Open | Inverse-field regenerate script: language, location, when it runs; whether Nodian is removed (W-275, W-287). | OPEN-01 |
| REG-263 | Open | Bootstrap must implement author registration: the first-use popup saves a code locally but does not create the person note; install-time name entry should create .obsidian/author-code.txt by the same rule as the snippet; where the Bootstrap source lives. | OPEN-05 |
| REG-264 | Open | What makes a vault ready for finishing touches (golden definition). | OPEN-09 |
| REG-265 | Open | Where do the stable 30-character tokens for usages live in SysML text? Recommendation: SysML short names, part <'2026...'> controller : Controller; must be accepted by the pinned parser first (not verified). | OPEN-V2-Q1 (ADR-V2-06) |
| REG-266 | Open | Keep frontmatter relationship fields as a derived mirror of the SysML block (written only by Workbench in the same transaction) or drop them? Recommendation: keep, so "what satisfies REQ-x" can be queried without parsing SysML. Directly affects Rovo queryability. | OPEN-V2-Q2 (ADR-V2-06) |
| REG-267 | Open | Adopt sourceRole and primarySymbol as governed v2 property names? Recommendation: yes. | OPEN-V2-Q4 (ADR-V2-06) |
| REG-268 | Open | Reinstate a blocking path-length report (never shortening) for SharePoint, and at what limit? Recommendation: 400 decoded characters plus a sync-root budget. (C-12) | OPEN-V2-Q5 (ADR-V2-06) |
| REG-269 | Open | How will Rovo read the model? The Atlassian SharePoint connector lists Word, Excel, PowerPoint, PDF and web pages, not Markdown. Confirm with Atlassian; if .md is not indexed, generate a Rovo-readable projection. | OPEN-V2-Q6 (ADR-V2-06) |

### 1 Model definition: Classes and types

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-099 | Active | An element whose eaType has no approved mapping gets type modelCheck, subtype blank, eaType kept, and is not dropped. | W-100 |
| REG-100 | Active | Requirement subtype comes from the EA package path (first match wins). A new engineering subtype covers all Engineering Requirements regardless of stereotype. | W-115,W-116 |
| REG-101 | Active | All Signal elements become Item Flow notes with blank subtype. | W-131 |
| REG-102 | Partly superseded / check | Each FlowProperty Part becomes its own Item Flow note; hasFlow and flowOf link a Port to its pins. | W-132,W-133 |
| REG-103 | Active | Each EA Object becomes its own Object note, none folded. | W-135 |
| REG-104 | Active | Class becomes Object mechanically with blank subtype; correction is a stage 2 job. | W-139 |
| REG-105 | Active | UseCase becomes Use Case; subtype comes from the package (what, when, where, who). | W-140 |
| REG-106 | Active | Artifact stays Artifact; stereotype gives the subtype (document, image). | W-143 |
| REG-107 | Partly superseded / check | Issue, Actor and StateMachine map straight to their MDSE classes. | W-144 |
| REG-108 | Active | Note, Text, Constraint and other InformationItems become Info notes; one rule names every unnamed element. | W-145 |
| REG-109 | Active | Thirteen small EA element types become modelCheck notes (prefix MC) with the EA type as subtype. A package is a folder; only a package with a Notes description also gets a modelCheck/Package note. | W-146,W-147,W-181 |
| REG-110 | Partly superseded / check | Subtype lists cut: Port only proxy and full; Function, Design, Info, Document, Artifact have no subtypes; Context and Transition classes removed. Requirement subtypes stay and come from the package. | W-237,W-238 |
| REG-111 | Active | A Physical Context stays an Object block with its parts. | W-239 |
| REG-112 | Active | Port, Function, State, Design and Step classes removed. EA Ports are occurrence endpoints only. Reusable Interface Classes are Object / interface. Behavior and Condition taxonomy replaces them. Local Model 0.4 writes sections Parts, Interfaces, Connections; 0.3 frozen. Supersedes much of the class mapping in W-14 to W-137 and Ruleset 1.23 sections 5 and 8. | W-384 |
| REG-113 | Active | EA Part carrier rows inherit semantic ownership of their resolved target. Folded Parts whose target is Behavior or Condition write the note-level ownership relationship, not a structural Part record (203 carriers: 142 Activity to Behavior, 60 State to Condition). Supersedes the W-137 assumption. | W-396 |
| REG-114 | Active | Port-owned Signal carrier Parts that are exact copies of reusable FlowProperty definitions fold to the FlowProperty Item (16 rows). | W-397 |

### 1 Model definition: Identity (uid, id)

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-062 | Active | Translated notes carry the original EA creation time and author in uid. Each person enters their name once; the author code is generated by one written rule at install (Bootstrap) and on first template use. | W-09 |
| REG-063 | Active | EA elements with no usable author get the code sparxeaauthor. | W-12 |
| REG-064 | Active | Translated notes get ids numbered per class prefix in EA creation order, ties by EA GUID, no gaps. Deterministic. Numbers permanent after final migration. | W-14 |
| REG-065 | Active | External requirement ids use the source's own designator (for example UL2594_13.1). Otherwise STD-##### or STK-#####. | W-17 |
| REG-066 | Active | id is either an internal vault identifier or an external document-and-section identifier. No other value goes in id. Other useful identifiers are kept in the body near the eaGUID. | W-27 |
| REG-067 | Active | Requirements that share an external designator take internal STD or STK ids, and the designator is kept as a Designator line in the source section. | W-82 |
| REG-068 | Active | Standard requirements take STD-#####; stakeholder requirements take STK-#####; other Requirement subtypes keep REQ-#####. Numbered in EA creation order, ties by EA GUID. No designator parsing. Withdraws the external-id form of W-17 for standards. | W-203,W-204 |
| REG-069 | Active | Source lineage EA8647; source identity is EA8647 + EA GUID, kept in importer provenance only. First allocation uses EA Created as written (no time zone conversion, missing ms = 000), the normalized EA author code, or skellyspencer if unusable. | W-316 |
| REG-070 | Active | Every model note has an immutable 30-character `uid` in the form `yyyyMMddHHmmssSSS` plus a 13-character author code. The `uid` never changes after creation. | R-1.1 (1.23 §16.1, `AI_INSTRUCTIONS.md`) |
| REG-071 | Active | `id` is `PREFIX-NNNNN`, with the prefix from the class in `element-types.yaml`. Never reused. | R-1.2 (`AI_INSTRUCTIONS.md`) |
| REG-072 | Active | The primary reusable engineering type is `Object`. `Thing` is deprecated. | R-1.3 (1.23 §1.1) |
| REG-073 | Active | `type` is the semantic class. `subtype` is an approved classification within that type. `kind` is deprecated. | R-1.4 (1.23 §1.1) |
| REG-074 | Active | `subtypeOf` is used only for a reusable invariant semantic distinction. Ordinary data or configuration variation is not a `subtypeOf`. | R-1.5 (1.23 §2) |
| REG-075 | Active | Notes in `99_System` carry no `type` or `subtype`. | R-1.6 (1.23 §1.1 (W-243)) |
| REG-076 | Active | Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, then specialization, then decomposition, then a new concept. | R-1.7 (1.23 §1) |

### 1 Model definition: Local Model (V1) / usages (V2)

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-226 | Active | Reusable Object uses are local part occurrences when contextual identity matters. Local endpoints, connections and flows are addressable records; the connection owns its local flows. | W-293,W-294 |
| REG-227 | Active | Local Model content is a distinct governed note region with its own Workbench surface. | W-298 |
| REG-228 | Active | Local Model: explicit managed-region markers; type-prefixed stable local IDs derived deterministically from EA source identity; canonical record pattern with EA provenance kept out of engineering notes; reusable interface members inherited implicitly; multiplicity only for indistinguishable copies; assemblies own the connections below their boundary. | W-302,W-303,W-304,W-305,W-310,W-311 |
| REG-229 | Active | Persisted Local Model references use native Obsidian block links ([[#^ep-42bd90\|J4]]); definition stays a note wikilink. local-model.yaml is the machine-readable contract that importer and Workbench both read. | W-312,W-313 |
| REG-230 | Active | Local Model usage is standard, variant or option (omitted = standard), on parts and endpoints only, never connections or flows. Local Model 0.2 is the writer format; element schema 1.17 adds sparse optional abstract: true (absent = false, not inherited). | W-314,W-319 |
| REG-231 | Active | A contextual endpoint may exist without a reusable Port definition. Port reuse resolves only by PDATA3 evidence (W-114.1) or exactly one same-named Port on the reusable block (W-114.2). Otherwise local-endpoint-only, no synthesized Port note, connectors touching it are review-only, and review CSVs carry EA Object_ID. | W-377,W-378,W-380 |
| REG-232 | Active | In Local Model 0.4 a connection may carry exposes to boundary Interface endpoints owned by the current context; it is not another connection. | W-385 |
| REG-233 | Active | Same-context EA BindingConnectors are canonical Local Model equality/binding, not delegation or a synthetic connection. equals is promoted under Local Model 0.5 (249 BindingConnectors reconciled). | W-398 |
| REG-234 | Active | Usage semantics: standard = required, uses definition; variant = required, resolves to exactly one concrete definition in the subtypeOf family; option = may be absent. Candidates come from subtypeOf (transitive), a non-abstract root is itself a candidate, optionality is never intrinsic to the definition, no assembly-to-every-subtype links, usage does not extend to connections/flows/transitions, saved configurations distinguish unresolved from absent, product/model-number coding is configuration knowledge not definition knowledge, cross-variant compatibility syntax is deferred. | W-314,W-319 (open list) |
| REG-235 | Active | Local records use a kind prefix and a 30-character token: `part-`, `ep-`, `conn-`, `flow-`. The token is globally unique and never reused. | R-8.1 (1.23 §15.7, §16.1) |
| REG-236 | Active | Persisted references use native Obsidian block links. The block ID equals the local ID. | R-8.2 (1.23 §15.7) |
| REG-237 | Active | Part and endpoint records may carry `usage: standard \| variant \| option`. Omission means `standard`. Connections and flows carry no `usage`. | R-8.3 (1.23 §15.7) |
| REG-238 | Stale | The Local Model writer format is the `writableVersion` in `local-model.yaml` (currently 0.5). Readers support 0.1 to 0.5. Reading an older version never rewrites it. | R-8.4 (`local-model.yaml`, W-384, W-398) |
| REG-239 | Open | Local Model usages are SysML usages in v2. Stable tokens for v2 usages are an open question (ADR-V2-06 Q1). | R-8.5 (Ruleset 2.0 draft) |

### 1 Model definition: Note format and templates

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-077 | Active | Every property has its own definition note: what it is, how determined, what it impacts. | W-08 |
| REG-078 | Active | Property definition notes live in Definitions/Properties, one per property, named exactly as the property. A Base lists them. | W-19 |
| REG-079 | Partly superseded / check | A translated note ends with a Source: EA section. EA GUID line is first; other kept EA values go below it, one per line. Only real values are written. | W-28 |
| REG-080 | Active | Translated notes carry a temporary eaType property below type, subtype and id. Removed or moved after review. | W-31 |
| REG-081 | Partly superseded / check | Seven properties on every note: uid, id, type, subtype, status, eaType, tags. aliases and formerIds are body content, not properties. control and boundary are not carried. | W-88 |
| REG-082 | Partly superseded / check | Body order of a translated note: Note, text wording, four labeled comment texts, user section, aliases and formerIds, multi-line Priority values, then Source: EA with tag lines in five fixed groups. Written down in Definitions/Note Layout.md. | W-98,W-101,W-103,W-104,W-105,W-106,W-107,W-110,W-111 |
| REG-083 | Active | A Name line (when the file name differs from the EA name) goes above the EA GUID line. Source: EA starts three blank lines below other content. | W-99 |
| REG-084 | Active | Each class template lists only the few relationship fields its notes nearly always have, empty, and no inverse fields. Requirement and Object templates list none. | W-182,W-222,W-223,W-224,W-225,W-226,W-227,W-228,W-229,W-230,W-231 |
| REG-085 | Partly superseded / check | The translator writes an empty ## Notes heading as the user section. Aliases and Former ids blocks follow it only when they have entries. | W-206,W-207 |
| REG-086 | Partly superseded / check | Order of lines in Source: EA: element values first, then structure-derived lines, then link lines. The kept body lines are defined in one table in Definitions/EA Source Section.md. | W-208,W-209 |
| REG-087 | Active | Template relationship-field decisions: Issue and Failure Mode list affects; State and Actor list none; State Machine lists hasChild; Transition listed source, target, trigger (class later removed); nine other templates list none. | W-232,W-233,W-234,W-235,W-236,W-240,W-241 |
| REG-088 | Active | Definitions notes carry no type or subtype. Definition notes exist for the common properties and the forward relationship fields (41 notes). | W-262,W-263 |
| REG-089 | Proposed | Note layout: frontmatter in governed order (type, subtype, id, uid, status, eaType, tags, sourceRole, primarySymbol, relationship fields), user zone, three blank lines, ## Source: EA, then ## SysML v2 always last with one fenced sysml block plus a one-line hint. A note owns its definition and the usages it owns in the same block. A second sysml fence is an error. A described package gets a modelCheck/Package note with no SysML block. Fixtures use fixture: true and ids 99000 to 99999. | V2-55 (ADR-V2-06) |
| REG-090 | Proposed | Who may change what: the user zone is never rewritten by the importer or Workbench; governed frontmatter refreshes EA-owned keys on rerun with overwrites logged (conflicts with the owner's approval-only rule, C-4); ## Source: EA is rewritten by the importer; ## SysML v2 is rewritten from the canonical graph, edited by Workbench transactionally, and edited by humans only with the parser check. Source: EA is now second to last (it was last in V1). | V2-56 (ADR-V2-06) |
| REG-091 | Active | A model note is created from the class template in `99_System/05_Templates`. Template properties keep their order (`type`, `subtype`, `id`, `uid`, `status`, `tags`). | R-2.1 (`AI_INSTRUCTIONS.md`) |
| REG-092 | Active | Template fields are always present in a note. | R-2.2 (decision recorded in the MDSE definition, 2026-10-19) |
| REG-093 | Active | A source field that has no data and is not a template field is not written to the YAML. | R-2.3 (decision recorded in the MDSE definition, 2026-10-19) |
| REG-094 | Proposed | A note has two zones. The user zone is above the first managed heading and is never rewritten by tooling. The managed footer is below it. | R-2.4 (ADR-V2-06) |
| REG-095 | Proposed | `## SysML v2` is the last `##` section and holds exactly one fenced `sysml` block. A second `sysml` fence is an error. | R-2.5 (ADR-V2-06) |
| REG-096 | Active | `status` is set to the template default. Only a person advances it. | R-2.6 (`AI_INSTRUCTIONS.md`) |
| REG-097 | Active | `eaGUID` appears only at the bottom of notes translated from EA. It is not in frontmatter. | R-2.7 (`AI_INSTRUCTIONS.md`, MDSE definition principles) |
| REG-098 | Active | Notes are never deleted. A note is retired by setting `status` to Retired. The `id` stays reserved. | R-2.8 (`AI_INSTRUCTIONS.md`) |

### 1 Model definition: Relationships

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-115 | Active | copyOf and hasCopy: a general link from a copy to its original. | W-124 |
| REG-116 | Active | hasPart/partOf is for Objects only; hasChild/childOf carries every other nesting. Nesting connectors add no notes or links of their own. | W-149,W-151 |
| REG-117 | Active | Generalization connectors become subtypeOf on the source (specific) note, supertypeOf generated. | W-152 |
| REG-118 | Partly superseded / check | Plain Connector connectors become the symmetric interfaces field; BindingConnector becomes equals. One link per note pair; every distinct name kept. Every connector is an interface; no assembly context line. | W-153,W-154,W-155 |
| REG-119 | Partly superseded / check | Aggregation: composite Object pairs are hasPart, everything else hasChild; an existing link wins. Realisation: a requirement applies to an Object (appliesTo), a Function realizes a Use Case. | W-159,W-160 |
| REG-120 | Partly superseded / check | Dependency mapping by stereotype: satisfy (Function or Design satisfies a requirement), deriveReqt (derivedFrom), refine (refines, drives), trace (describes, affects, appliesTo, references), verify (verifies), unstereotyped (dependsOn). | W-163,W-164,W-165,W-166,W-167,W-168,W-169 |
| REG-121 | Partly superseded / check | Abstraction allocate: an Object performs a Function and has a Design. UseCase extend is optionOf, include is hasChild. Association: participants written only on the Use Case. Usage: a Function or Design realizes a Use Case. | W-170,W-171,W-172,W-173 |
| REG-122 | Active | ControlFlow and StateFlow become precedes/follows. Flow elements stay modelCheck notes; StateFlow carries trigger, guard and effect lines. | W-174,W-175 |
| REG-123 | Active | appliesTo/applies stays a pair and supertypeOf stays generated. Long inverse lists are judged after the import. | W-179 |
| REG-124 | Active | Relationship review removed 54 unused fields in seven groups (carries/flowsOn, instanceOf, connects, start/end state, operatingState, hasBehavior, subject, hasContext, hasParticipant, 28 verification and failure fields). conflictsWith kept. | W-184,W-186,W-187,W-188,W-189,W-190,W-192 |
| REG-125 | Active | Reviewed or endpoint-invalid connectors are evidence-only and never written as canonical relationships. Review - Semantic and Connectors.csv must match exactly what was withheld. | W-376,W-388 |
| REG-126 | Active | Only relationships defined in `relationships.yaml` are used. A relationship with no endpoint rule is not restricted, and `tracesTo` is provisional until replaced. | R-3.1 (`AI_INSTRUCTIONS.md` (W-272, W-277, W-288)) |
| REG-127 | Active | Author the forward relationship only. Inverses are generated and must match. Where they disagree, the forward field wins. | R-3.2 (1.23 §4, `AI_INSTRUCTIONS.md` (W-275)) |
| REG-128 | Stale | State ownership: `hasState` runs from Object or Condition to Condition. `stateOf` is the generated inverse. | R-3.3 (`relationships.yaml` 1.36) |
| REG-129 | Stale | Requirement scope uses `appliesTo`. Verification uses `verifies`. Which classes may `satisfies` a Requirement must be re-read from `relationships.yaml` 1.36. | R-3.4 (1.23 §7 (W-327)) |
| REG-130 | Stale | Behavior controlled by the modeled product is distinct from externally controlled behavior (Use Case). Human or external steps are not product behavior. | R-3.5 (1.23 §5) |
| REG-131 | Active | Folder placement is navigation only. It creates no semantic relationship. | R-3.6 (1.23 §1, §9) |
| REG-132 | Active | A repeated identical semantic relationship is not used to express quantity. Quantity is Local Model `multiplicity`. | R-3.7 (1.23 §15.7) |

### 2 Importer: EA to notes: EA field and tag dispositions

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-133 | Active | An external document is one note per document edition with an anchor per clause. Clauses with no relationships fold into the document note; connected clauses become their own notes. | W-16 |
| REG-134 | Active | Sequence-style EA ids (id tag, SysML1.4::id) are dropped. Clause identity comes from the element name or the Stakeholder ID tag. | W-26 |
| REG-135 | Partly superseded / check | 69 of 121 EA tagged values are dropped (never have a value, or only a placeholder). Dispositions recorded in ea-tag-dispositions.yaml. | W-29 |
| REG-136 | Active | Every EA element type is mapped one at a time in ea-element-mapping.yaml. Nothing counts as mapped until approved. | W-32 |
| REG-137 | Active | Every source field and tag ends in one of five dispositions: property, body, structure, archive, drop. | W-33 |
| REG-138 | Active | Author and CreatedDate are structure. ModifiedDate, Version, Phase, Complexity, Effort, Status are dropped. ea_guid becomes the EA GUID line. | W-39 |
| REG-139 | Active | 21 element fields with no real value in the extract are dropped. | W-40 |
| REG-140 | Active | Nine presentation, code-generation and display-style element fields are dropped. | W-41 |
| REG-141 | Partly superseded / check | Note, Alias and Multiplicity are body fields with two placements: main text, or source section. | W-42 |
| REG-142 | Active | Part quantities go on the assembly note, one line per Part. Unlinked Parts become Object notes. | W-43 |
| REG-143 | Active | The block a Part represents comes from PDATA1. | W-44 |
| REG-144 | Active | PDATA2, PDATA3, PDATA4 and NType are archive (kept only in the source export). | W-45 |
| REG-145 | Active | Join keys (Object_ID, ParentID, Package_ID, Connector_ID, Diagram_ID, ea_guid and similar) are structure: the translator uses them and does not copy them into notes. Package_ID, Name and Parent_ID build the folder tree that follows the EA package structure. | W-46,W-57,W-65,W-70,W-72 |
| REG-146 | Active | Object_Type and Stereotype are properties feeding the temporary eaType. MDSE type and subtype come from the element mapping. | W-47 |
| REG-147 | Active | Name is structure: it becomes the note title and file name. Where the file name must differ, the original is kept as a Name line in the source section. | W-48 |
| REG-148 | Active | Source fields or tables with no real value, or one constant value on every row, are dropped (elements, connectors, packages, diagrams, subordinate tables, connector tags). The export keeps every column, and a fresh import can reopen a field. | W-49,W-50,W-60,W-63,W-68,W-74,W-85 |
| REG-149 | Active | Connector Direction and DestIsAggregate are structure. Ten connectors point the wrong way if Direction is ignored. | W-51 |
| REG-150 | Active | Connector style, label, and diagram display-setting fields are archive: kept only in the original export. | W-52,W-53,W-69 |
| REG-151 | Active | Connector SourceCard is written as the quantity line on the assembly note. DestCard is archive. | W-54 |
| REG-152 | Active | Connectors are imported where drawn. Block-level flow connectors are flagged and fixed after import. | W-55 |
| REG-153 | Active | Connector Name and Notes are body lines: on both end notes for Connector and InformationFlow, on the owner-side note for other types. SourceRole is archive. | W-56 |
| REG-154 | Active | Ten connector layout and style fields are dropped. Real layout is per diagram. | W-59 |
| REG-155 | Active | Sequence connector SeqNo and DiagramID are structure. PDATA1 to PDATA3 on sequence/state-flow connectors are body. | W-61 |
| REG-156 | Active | Administrative package fields are dropped. Package Notes is body (main text). Package CreatedDate is structure. Diagram tables are added to the worklist. | W-64,W-66,W-67 |
| REG-157 | Active | Linked documents (ModelDocument, ExtDoc) come in as attachment files in the owning note's folder, named "<note file name> asset <n>". RTF text documents are attached unchanged. Licensing of third-party standards is decided after the import. | W-75,W-76,W-77,W-78 |
| REG-158 | Active | t_xref decisions: Stereotypes archive; MOFProps relationship rows (conveyed, trigger, target, entry, doActivity, effect, represents) are structure; remaining CustomProperties dropped or archived. | W-79,W-83,W-84 |
| REG-159 | Active | Every Requirement element (13,988) is imported as its own note. Folding into document notes is a stage 2 task. Replaces the fold rule of W-16 for the import. | W-81 |
| REG-160 | Active | t_operation rows become body lines on the State note: Entry action, Do action, Exit action. | W-86 |
| REG-161 | Active | Tags Status, Object Type, Applicability Status, Priority, Abstraction Layer, Domain and Origin are dropped. A new analysis follows the import. | W-87,W-89,W-90,W-109 |
| REG-162 | Active | Comment, knowledge, part identity, procurement, electrical and FMEA tags are body lines, real values only. | W-91,W-92,W-94,W-95 |
| REG-163 | Active | Body lines from tags use the exact EA tag name (- <EA tag name>: <value>) during the import period. Renaming happens after. | W-93 |
| REG-164 | Active | Classifier, Classifier_guid and PDATA1 on element types other than Part were set aside until the element mapping existed; W-180 settles them. | W-96,W-180 |
| REG-165 | Active | The text and SysML1.4::text tags are kept as normal text below the Note. Reverses W-29 for these two tags. | W-102 |
| REG-166 | Active | One Name line format for connectors of every type: - Connector name: <name> (to [[other end]]). | W-158 |
| REG-167 | Active | NoteLink: a note linked to one element is written into that element's body under an EA notes label; a note linked to several stays an Info note with describes. | W-161,W-162 |
| REG-168 | Active | The four unmapped t_xref kinds (12 rows) are body lines on both ends. State action lines from t_operation and t_xref are written as defined, no merge. | W-194,W-195 |

### 2 Importer: EA to notes: EA to SysML v2 mapping

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-289 | Active | Element family mapping (60 exact EA type/stereotype families = 40 native definition + 7 local usage/behavior + 13 non-native): Requirement variants to RequirementDefinition; Activity variants to ActionDefinition; UseCase to UseCaseDefinition; State to StateDefinition; Class variants (Hardware/Physical/Software Component, block, Module, Platform, Business Line, unstereotyped) to PartDefinition; System Partner and Actor to external PartDefinition; Object to PartDefinition (valid prior classifier becomes specialization, not typing); interface Classes to InterfaceDefinition; Generic Physical Interface to PortDefinition; Logical/Physical Signal to ItemDefinition; Software Parameter to AttributeDefinition; testCase to VerificationCaseDefinition; Constraint to ConstraintDefinition; Event to OccurrenceDefinition; Physical Context to PartDefinition (composite) or external PartDefinition (single). | V2-30 (60-family reconciliation) |
| REG-290 | Active | Local usages: Action, Part and Port become owned usages (untyped allowed with UNRESOLVED_ACTION_TYPE, UNRESOLVED_PART_TYPE, UNRESOLVED_PORT_TYPE); Part:FlowProperty becomes an ItemUsage owned by the port; StateNode becomes a StateUsage; Synchronization becomes fork/join from actual control-flow evidence; Trigger becomes a transition trigger. | V2-31 (60-family reconciliation) |
| REG-291 | Active | Non-native: Package = folder only; InformationItem, Note, Issue, Change, Decision, Text = MDSE notes with YAML links (no inferred executable branching); Artifact:Image and Artifact:Document = attachments referenced in element YAML; Sequence = reference-only workflow view; ProxyConnector = reference to the original connection; Boundary = aggregate evidence note (STEP-00 2 revises the earlier removal). | V2-32 (60-family reconciliation) |
| REG-292 | Active | Connector family mapping (26 families, 14,688 connectors): Generalization to specialization; Abstraction:allocate to allocation; Aggregation to owned PartUsage where physical containment is evidenced, else review; Dependency:satisfy to satisfy; Realisation to perform/allocate by endpoint kinds, else review; refine to Dependency + Refinement metadata; Association to ConnectionUsage only if connectivity is proven; UseCase:extend to optional case usage; UseCase:include to required nested case usage; ControlFlow to Succession with guards; StateFlow to transition; Nesting to approved nested usage else organizational; NoteLink to YAML links only; Sequence reference-only; Usage to generic Dependency; Dependency:verify to verification; Connector to port-to-port ConnectionUsage; Realisation:deriveReqt takes precedence over generic Realisation. Eligibility is per connector, never per family. | V2-33 (26-family audit) |
| REG-293 | Active | Exact-family exceptions override wildcard selectors: shared/composite aggregation = owned typed usage (a non-owning ref part only for an existing occurrence); untyped Part/Action/Port allowed with review flags; InformationItem = MDSE note, not ItemDefinition; Physical Context needs composition evidence; Object classifier = specialization, not typing; Copy alias only with proven identity; Binding only for compatible equal features, else flagLink; include = required nested usage, extend = optional conditional usage; Event = OccurrenceDefinition; quantities and units need explicit source evidence (never infer unit from name); requirement nesting is not derivation or folder hierarchy; unresolved connectors get a persistent per-source flagLink. The approved-version resolver refuses wildcard fallback. | V2-48 (Exception audit EXC-01..12) |

### 2 Importer: EA to notes: Flags

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-294 | Partly superseded / check | Dispositions: native; MDSE descriptive note; flagLink (one traceable record per unresolved connector with endpoints, direction, family, GUID, roles, multiplicity, aggregation, reason code and a note-body entry; implies no hierarchy or connection); flagNote (unresolved element/note: keep original content, identity and provenance, intended links, review action). The user's convention adds flagImport (import issues) and flagConflict (merge conflicts). | V2-44 (Flag-and-Continue Policy) |
| REG-295 | Active | A flag is an Obsidian callout whose type names the issue. Types: `flagImport`, `flagConflict`, `flagLink`, `flagNote`. New types are added to this section before use. | R-5.1 (MDSE definition) |
| REG-296 | Active | The importer and AI processes add flags. Only an engineer removes a flag, after the issue is resolved. | R-5.2 (MDSE definition) |

### 2 Importer: EA to notes: Importer

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-169 | Active | Import runs in two stages. Stage 1 copies EA faithfully with approved deterministic rules only. Stage 2 applies meaning as separate reviewed changes, each a person-approved git commit. | W-30 |
| REG-170 | Active | Source reference is a ledger (one row per source element and connector: disposition, rule, resulting uid) plus a run manifest. Values are not copied. | W-35 |
| REG-171 | Active | Every review item must be resolvable from the vault alone. The tool writes review tables keyed by GUID in 99_System/11_Import. | W-156,W-157 |
| REG-172 | Active | Ledger.csv and the run manifest are generated on every run into 99_System/11_Import, sorted by GUID. Ledger outcomes include note, folded, link, and others. | W-215 |
| REG-173 | Partly superseded / check | Review tables are read-only evidence in 99_System/11_Import with shared first columns: Block-Level Flow Connectors, Added Ports, Nesting Direction, Equals Direction. | W-216,W-217,W-218,W-219,W-220 |
| REG-174 | Active | The tool opens the .qeax read-only, numbers every note from the whole model, and writes only the selected packages (selected by path). Links leaving a slice are written as in a full run. A fold follows the note that receives it. | W-252,W-253,W-254,W-255 |
| REG-175 | Active | Source-count check: the tool compares whole-model source counts (table rows, elements by type, connectors by type, diagrams by type) with the counts in the file on every run. Any difference fails the check and discards the run. | W-257,W-268 |
| REG-176 | Active | Package paths for the slice filter are written Name > Name > Name, matched on the EA package name after trimming spaces. | W-266 |
| REG-177 | Active | The importer resets stale browser state when the source is re-analyzed and rejects the translator workspace as an import target. | W-290 |
| REG-178 | Partly superseded / check | Source Map is the rerun identity authority. Identity conflicts are hard errors. EA-owned translated fields may refresh on rerun; MDSE identity, filename/path, MDSE-only relationships and human content are preserved; overwritten human edits are logged. | W-317 |
| REG-179 | Active | Linked-document payloads are ZIP-wrapped; the importer unwraps up to two levels, verifies CRC and size, and fails explicitly on encrypted, ZIP64, unsupported or ambiguous entries. | W-323 |
| REG-180 | Active | Import writes use a persistent transaction: Import State.json is IMPORT_IN_PROGRESS before the first write; a destination with an import-state file is not a clean base and is rejected for another semantic import. A partial vault is never authoritative. CONFLICT: a second import into a vault with prior state is rejected, which blocks Phase 2 additive import (C-11 family). | W-371 |
| REG-181 | Active | Import status is multi-dimensional: SOURCE_PASS/WARN, PLAN_PASS, WRITE_PASS/FAIL/IN_PROGRESS, SEMANTIC_CLEAR/REVIEW_REQUIRED, ACCEPTANCE_PENDING. No single PASS implies acceptance. | W-372 |
| REG-182 | Active | A QEA/QEAX in SQLite WAL mode is a blocking failure (SQLITE_WAL_MODE); the importer does not read the WAL; the user closes or checkpoints EA first. | W-373,W-390 |
| REG-183 | Active | Every viable QEAX is SHA-256 fingerprinted (bounded chunk reads) and the digest is copied into preflight, Import State and Run Manifest. Accepted EA8647 snapshot is 186,036,224 bytes. | W-375,W-392 |
| REG-184 | Active | Import transaction failure behavior is tested in CI: write IMPORT_IN_PROGRESS first; on failure persist IMPORT_FAILED / WRITE_FAIL; Import State is strict JSON. Completion is a mechanical state, never semantic acceptance. | W-387,W-389 |
| REG-185 | Active | EA source shape is governed by a versioned machine-readable source profile (Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json, schema mdse-ea-source-profile/1), synced into the single-file importer. Every one of 100 SQLite tables has a disposition: 12 imported, 34 ignored non-empty approved, 54 ignored must-be-empty. | W-393,W-394 |
| REG-186 | Active | Generated Markdown uses LF line endings before write. | W-395 |
| REG-187 | Active | Translator Definition checks 2 to 5 are approved: no two notes share an id, uid or file name; every link written resolves to a note or attachment in the run; every YAML/JSON file parses and every relationship field written is in relationships.yaml; run-manifest counts match the file counts or differences are listed (check 5 does not fit a slice run; open). | W-256 |
| REG-188 | Active | Source ledger: every object and connector gets exactly one row with one disposition from native, alias_merged, evidence_only, deferred_review, excluded_by_policy, error. excluded_by_policy needs a traceable reason. No silent drops. Fields: source_system, fixture_hash, source_table, source_pk, ea_guid, ea_type, ea_stereotype, source_package_id, rule_id, rule_version, disposition, target_semantic_kind, target_stable_id, target_file, evidence, diagnostic_code, confidence, operator_action. | V2-34 (Phase 1 controls) |
| REG-189 | Active | Guardrails: no unsupported custom SysML relationships; shared physical part = one definition with parent-owned typed usages and BOM quantity/unit separate; Copy becomes an alias only when identity equivalence is independently established; redefinition, subsetting and variation are not inferred from EA or BOM; do not derive satisfy or verify from generic Realization; trace, refine, Realisation and Association need explicit buckets with no generic fallthrough. | V2-35 (Phase 1 controls) |
| REG-190 | Active | Vault write contract: preflight (read-only fingerprint, schema, pinned ruleset and SysML v2.0 library manifest; no write on mismatch); build a typed semantic graph; stage a complete manifest of additions, changes and deletions in a disposable directory; validate and preview the diff before atomic publish; failed validation leaves the approved vault untouched; canonical semantic files stay separate from view/layout metadata and reports; record a run manifest (fixture hash, timestamps, tool/rule/library versions, disposition totals, validation results, exceptions, file hashes, changeset, rollback reference). | V2-36 (Phase 1 controls 1 to 4, 8, 10) |
| REG-191 | Active | Merge by field ownership: EA owns source semantics, BOM owns versioned BOM evidence, MDSE owns canonical IDs, placement and derived projections, users own local annotations. Never silently overwrite manually edited semantic content. Reimport reconciles by (source system, source GUID, semantic role) to a stable target ID with a three-way comparison against the last-generated baseline, detecting source-changed, user-changed and concurrent change separately. Removal or relocation only through a tombstone/redirect plan. | V2-37 (Phase 1 controls 5, 6) |
| REG-192 | Active | Failure levels: Fatal stop (unreadable/corrupt QEAX, source/profile/hash mismatch, unusable identities, evidence or provenance loss, ledger/count corruption, no coherent navigable vault, unexpected diagram access, unsafe overwrite, unparseable core model, untraceable drops). Localized semantic problems flag and continue. Warnings (missing optional multiplicity or metadata, formatting) log and continue. One parser rejection never poisons a batch: isolate it, write an MDSE fallback, revalidate, proceed. | V2-45 (Flag-and-Continue Policy) |
| REG-193 | Active | Zero-silent-loss: every source record reconciles exactly once into native, alias_merged, evidence_only, deferred_review, excluded_by_policy or error. Unrecoverable omission, unauthorized deletion, silent deduplication, failed note-link resolution and conflicting-edit overwrite are export blockers. BOM reader preserves rejected rows (position and value), never rounds decimals, infers units, or omits formulas, revisions or effectivity. | V2-49 (Data Retention Holds) |
| REG-194 | Active | The importer is one self-contained HTML file (21_Importer/mdse_v2_importer.html): double-click, offline, no network request, no dependency. Two modes: New vault (writes a ZIP) and Add to existing vault (writes into a chosen folder and never deletes). The page is built by build_importer_html.mjs from src/ files; CI --check fails on a stale page. Python and Java are development and CI tools only; users never run them. | V2-50 (ADR-V2-07) |
| REG-195 | Partly superseded / check | Add-onto-existing table (Ruleset 1.23 §16.4): match by uid; user zone kept; id/uid never change; status, tags and other keys kept; subtype, eaType, sourceRole and primarySymbol refreshed from EA (change logged); ## Source: EA and ## SysML v2 replaced; same uid with different type is a conflict (nothing written); identical input is unchanged and byte-identical; a note with no managed footer gets one appended. The refresh/replace rows conflict with C-4, C-5. | V2-51 (ADR-V2-07) |
| REG-196 | Active | Browser support: writing into an existing folder needs the File System Access API (Chrome, Edge); Firefox and Safari can only build ZIPs and run the read-only check. | V2-52 (ADR-V2-07) |
| REG-199 | Proposed | Note ownership: unknown user-defined YAML keys are retained; all non-SysML Markdown, attachments and engineer notes are preserved byte-for-byte unless the engineer edits them; an import write plan lists created, unchanged, updated, conflicted, deferred, rejected and moved, with a preview before commit; an identical repeat import yields no changes; no deletion in pilot imports (missing source records are reported); writes are atomic (snapshot, staged files, integrity checks, apply or rollback, audit trail); unsupported native relationships stay in the review ledger, never shown as SysML relations. | V2-59 (Shared Note and Release Contract) |

### 2 Importer: EA to notes: Merge, rerun and conflicts

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-200 | Active | Review changes are recorded as a git diff against the baseline import commit, with reasons in Review Changes Log.md. An AI turns them into rule changes. | W-38 |
| REG-201 | Active | Import is mechanical. The importer applies the Ruleset and does not interpret. | R-4.1 (MDSE definition) |
| REG-202 | Active | Every change to an existing file is listed in one dated changelog per import run. Each entry links the changed file, describes the change, and flags any conflict. | R-4.10 (MDSE definition) |
| REG-203 | Active | Importing the same input again produces no changes and no changelog entries. | R-4.11 (MDSE definition; 1.23 §15.6 (completion)) |
| REG-204 | Active | A run is complete only when every planned entity reaches an explicit terminal state: written, intentionally suppressed by rule, or explicitly failed. There is no unexplained remainder. | R-4.14 (1.23 §15.6) |

### 2 Importer: EA to notes: Naming and folders

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-205 | Active | The folder tree starts at the ten packages under IPC !. Model and IPC ! are not folders. 00 Product Abstract is a folder only. Mapping is decided by element type, not package walk, except Requirements. | W-117,W-118,W-119 |
| REG-206 | Active | Unsafe characters are only those the system does not allow (Windows set). Replacement order: / becomes -, : becomes space-dash, ? and * removed, quote becomes two apostrophes, and so on. | W-196,W-197 |
| REG-207 | Active | The characters [ ] # ^ are also replaced in file names (to ( ), no., removed) because they cannot be used inside a link. | W-205 |
| REG-208 | Active | Every attachment is named <owning note's final file name> asset <n>, counted in RTF picture order, including a single file. | W-210 |
| REG-209 | Partly superseded / check | Import filenames are human-oriented. Port filenames are i<owner> - <port name>. Supersedes the id-suffix part of W-198 and W-199. | W-289 |
| REG-210 | Active | A regulatory folder that duplicates its directly contained element's title collapses to the section number; the note keeps the full title. | W-309 |
| REG-211 | Partly superseded / check | Duplicate files/folders use ~2, ~3. Forced filesystem alteration uses ~a, ~b (Excel-column sequence); combined form ~a~2. Numeric markers go to duplicate-name review. | W-318 |
| REG-212 | Active | No length-driven shortening in the importer; hard stop at 400 characters; links go to file name or uid; Shorten paths becomes a post-import task. Replaces the 212-character limit of W-318 and Ruleset 1.23 section 15.4. | W-324 |
| REG-213 | Active | No importer-defined total path or file-count limits and no folder_N mechanical subdivisions. Only the physical filesystem component limit remains. Supersedes W-324 400-character stop, the 75-file folder rule and AI_INSTRUCTIONS line 56 (stale, C-12). | W-382 |
| REG-214 | Active | Preserve source package placement. An emitted element with emitted children is written inside its own folder (Parent/Parent.md, Parent/Child.md). URL, $inet, path and query-string source names are not valid filenames. | W-383 |
| REG-215 | Active | Use the shortest human-readable name that stays unambiguous in context. | R-7.1 (1.23 §15.1) |
| REG-216 | Active | UID is the stable machine identity. The filename is a locator and may carry context for uniqueness. The visible heading is the engineering name. | R-7.2 (1.23 §15.1) |
| REG-217 | Active | Default to EA Name. EA Alias is used only when Name is unsuitable for people. The original Name is kept in provenance. | R-7.3 (1.23 §15.1) |
| REG-218 | Active | Ports use the filename form `i<owner> - <Port Name>.md`. The `i` convention is for Ports only. | R-7.4 (1.23 §15.1) |
| REG-219 | Active | Duplicate names take `~2`, `~3`. Forced alterations take `~a`, `~b`. Numeric markers are duplicate-review items. Alphabetic markers are altered-name review items. | R-7.5 (1.23 §16.3) |
| REG-220 | Active | Note filenames are unique across the vault, case-insensitive. Links use the filename: `[[File name]]`. | R-7.6 (1.23 §15.4a (W-382)) |
| REG-221 | Active | There is no total path-length limit. A single file or folder name the filesystem cannot create is shortened or blocked deterministically. | R-7.7 (1.23 §15.4 (W-382)) |
| REG-222 | Active | Folder structure follows the model's package nesting. A nested element's folder is named for its parent. | R-7.8 (1.23 §9) |
| REG-223 | Active | Do not create mechanical `folder_N` subdivisions. | R-7.9 (1.23 §9 (W-347 era)) |
| REG-224 | Active | Automatic navigation files (`README`, `BASE_local`, `BASE_all`, `CANVAS`) are created only for the primary top-level domain folders. | R-7.10 (1.23 §9.1) |
| REG-225 | Active | Imported filenames must not collide with reserved infrastructure names (`Template - `, `Rule - `, `README_`, `BASE_`, `CANVAS_`). A collision with an engineering note is blocking. | R-7.11 (1.23 §15.2) |

### 3 SysML text and parser: Importer

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-197 | Active | Parser gate: the pinned official SysML v2 parser (Java) runs in CI and on a maintainer's machine, not in the page. The ZIP carries a parser-check report (parser version, per-note result, date). Workbench marks it stale whenever a SysML block changes afterward and never presents unchecked SysML as verified. | V2-53 (ADR-V2-07) |

### 3 SysML text and parser: SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-270 | Active | SysML v2 text is authoritative for formal structure and relationships. Standard OMG SysML v1-to-v2 transformation is the default; documented, evidence-backed MDSE rules may override it. Do not manufacture custom native v2 relationships. Unsupported or ambiguous EA semantics become explicit flagLink evidence and are never silently dropped or asserted. | V2-02 (Architecture Decisions; Baseline 1) |
| REG-271 | Active | One MDSE note per reusable defined element. Usages are declared in the owning note, never duplicated as definition notes. Packages organize folders and imply no formal composition. Folder placement never defines SysML ownership or namespace. | V2-03 (Baseline 2) |
| REG-272 | Active | The last ## SysML v2 section (fenced sysml block) is the authoritative text. Free Markdown above it is preserved. Workbench structure and visuals are derived from the text and rebuilt from it. Edits update native text atomically and are parser-validated. The mid-note ## SysML source layout is NOT approved. | V2-04 (Baseline 3; Source Ownership) |
| REG-273 | Active | Governed YAML keeps MDSE type/subtype, EA source type/stereotype, deterministic UID, source identity/provenance and flagLink evidence. YAML-only source labels are not native SysML assertions. | V2-05 (Baseline 4) |
| REG-274 | Active | Mapping fixed by category: physical Objects become part def; context-owned part usages; specialization distinct from containment; actual source multiplicity on usages; nested states and actions; requirements and verification; constraints; namespaces; causation distinct from temporal succession. | V2-06 (Baseline 5) |
| REG-275 | Active | Keep ProxyPort/FullPort distinction (FullPort may need a part usage, ProxyPort a port usage, Binding Port stays distinct). Preserve contextual endpoints, boundary/exposure, flows, messages, conjugation, binding/equality. A graphical edge never proves a native relationship. | V2-07 (Baseline 6; STEP-00 5) |
| REG-276 | Active | One common EA source graph with separate V1/V2 mapping profiles. No automatic folder-to-containment mapping. All EA States are SysML v2 States. Stereotyped Function activities stay Functions wherever they sit in EA. Generalization orientation requires source-proven direction and native eligibility. | V2-08 (Baseline 7) |
| REG-278 | Active | Identity: note UID is independent of filename, path and label. A qualified SysML name is an address, not permanent identity. Source EA GUID and BOM keys live in an audit ledger. A symbol rename needs reference-update analysis. Derived indexes (symbol, usage, relationship, reverse usage, source ledger) are rebuilt and never hand-edited. Extraction is byte-for-byte deterministic against a pinned compiler/spec baseline. | V2-13 (Source Ownership) |
| REG-279 | Active | Copies that represent one definition merge into one canonical note with native alias memberships; distinct usages and connectors never collapse. | V2-14 (STEP-00 1) |
| REG-280 | Active | Boundaries are kept in one aggregate Boundary note (disposition boundary_grouped), as MDSE descriptive evidence and never as a native SysML Boundary relationship. | V2-15 (STEP-00 2) |
| REG-281 | Active | EA Packages become organizational folders; no Package notes and no preservation of incidental package metadata. | V2-16 (STEP-00 3) |
| REG-282 | Active | Attachments are not definition notes. The owning engineering notes hold the links; no orphan attachment references (GAP-DOC-01). | V2-18 (STEP-00 6) |
| REG-283 | Active | Unresolved links use flagLink, one source connector stays identifiable, and one explanatory line in the owning note body states what was replaced and why. Counts, percentages and concentration by mapping family are monitored; the alert threshold comes from the actual import report. Untyped Part/Action/Port usages import with nonblocking review markers; no definition is invented. | V2-19 (STEP-00 7, 8) |
| REG-284 | Active | Original EA and BOM sources stay external; no second source archive. Importers reconcile updates deterministically with stable identity, source revision/fingerprint checks, repeat import, difference preview and an explicit conflict/merge action. (This is the V2 statement that matches the user's additive/changelog rules.) | V2-21 (STEP-00 11) |
| REG-285 | Active | Change handling: unchanged inputs produce zero edits; repeated runs are idempotent; full rebuild is recovery only. Stage edits, validate, report conflicts, then write only changed files while keeping unrelated notes and human content. Imported deletions get a tombstone/review and never silently erase manually edited notes or unmodeled attachments. Keep an undo manifest of pre-change hashes. Updates are staged for diff/PR approval and never overwrite another contributor's work. | V2-26 (Functional Parity) |
| REG-286 | Active | Derived state (Obsidian links, Canvas JSON, indexes, Excel exports, HTML previews) is rebuildable and never a competing source of truth. | V2-27 (Functional Parity) |
| REG-287 | Proposed | The `## SysML v2` section is the sole authoritative native text. It is read and changed through the shared parser and validator with an optimistic version check. | R-9.1 (`MDSE_V2_0_SHARED_NOTE_AND_RELEASE_CONTRACT`) |
| REG-288 | Active | The parser gate is run in CI and on a maintainer's machine. The ZIP carries a parser-check report. Workbench marks the report stale after any SysML change. | R-9.2 (ADR-V2-07 (owner accepted 2026-10-19)) |

### 4 Base vault and Bootstrap: Base vault, Bootstrap, release

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-240 | Partly superseded / check | Cross-vault plugins archived. MDSE Bootstrap auto-installs pinned plugins for team rollout. Obsidian Git pinned at 2.40.0. | W-05 |
| REG-241 | Active | MDSE Bootstrap registers each person at install: asks for a name, derives the author code, saves it locally, and adds the person to authors.yaml. | W-24 |
| REG-242 | Active | The import goes into a fresh vault with MDSE Bootstrap and plugins installed. A script builds a clean base vault; the translator fills a copy of it and does not create the vault, Obsidian settings or plugins. Base vault contents are approved as listed. | W-248,W-249,W-250 |
| REG-243 | Active | Controlled plugin release: all runtime plugins ship inside the Base Vault, pinned and hashed in plugin-lock.yaml. Bootstrap does release check and author registration; after the user trusts the author it may safely repair activation (enable locked plugins, disable prohibited core plugins) only if version and hashes match. Governed data.json is hash-locked. Bootstrap does not download or update binaries. Startup verification is staged. | W-322,W-325,W-330,W-331,W-333,W-347 |
| REG-244 | Active | The EA importer is external to the operational engineering vault; it writes into a fresh Base Vault but is not shipped inside it. | W-332 |
| REG-245 | Active | A clean Base Vault build is deterministic with .vault.yaml UNINITIALIZED and no Git; a candidate model repository is made from a copy. Pre-release validation warns on candidate tooling. Initialize-Vault.sh must pass sh -n. OS metadata (.DS_Store, Thumbs.db) is never governed content. | W-334,W-335,W-336,W-338 |
| REG-246 | Active | Bootstrap full verification waits for a 5 s quiet window with a 60 s maximum deferral; delayed Bootstrap work is lifecycle-safe and full verification is single-flight. | W-363,W-366 |
| REG-247 | Active | Semantic import needs an initialized vault identity. A base with vault_uid UNINITIALIZED is a valid fresh base; the importer initializes it with a vault name and a 13-character author code, rewriting only .vault.yaml. | W-374,W-381,W-391 |
| REG-248 | Active | Each issued importer is paired with one base vault using the same semantic release version. The importer checks it before writing. | R-10.1 (1.23 §15.8) |
| REG-249 | Active | Relationship and element schemas keep their own version numbers. | R-10.2 (1.23 §15.8) |
| REG-250 | Active | The Run Manifest records importer release, base release, relationship-schema version, and element-schema version. | R-10.3 (1.23 §15.8) |
| REG-251 | Active | The runtime base carries `mdse_release` in `.vault.yaml`. Methodology material is not copied into engineering vaults. | R-10.4 (1.23 §15.9 (W-321)) |

### 5 Read-only Workbench: Workbench

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-252 | Active | A controlled Workbench user guide ships in every Base Vault and is cross-repo checked. | W-341 |
| REG-253 | Active | Workbench performance and cache architecture: one disposable semantic cache bound to vault_uid and schema versions; A/B commit slots; authored-link evidence for reconciliation; revision-scoped shared assurance service; ctime+mtime+size fingerprinting; path-hash buckets; core readiness before Local Model hydration; metadata-settled link re-resolution; bounded runtime history; a read failure is a scoped finding and never poisons the cache. | W-343,W-344,W-345,W-346,W-348,W-349,W-350,W-351,W-352,W-353,W-355,W-356 |
| REG-254 | Active | (duplicate IDs in log) Workbench exposes one lightweight clickable runtime-health surface that never runs expensive work; live editor and metadata events are coalesced per path in a 250 ms quiet window. | W-351b,W-352b |
| REG-255 | Active | Workbench runtime staging: bounded parallel shard reads; core model usable before Local Model hydration; heavy work staggered into non-overlapping lanes; elapsed-time work slices (12 ms) not fixed counts; background hydration is activity-aware, preemptible and promotable on demand; subsystems fail independently with separate health evidence; time-to-core-ready measured separately; cache persistence is single-flight and never starts hydration; views declare needsLocalOccurrences; no model I/O in onload or layout-ready. | W-353b,W-354b,W-355b,W-356b,W-357,W-358,W-359,W-360,W-362,W-364b,W-365,W-367,W-369 |

### 6 Acceptance on real QEAX: Importer

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-198 | Proposed | Milestones: M2 QEAX to notes in JS (approved-family resolver, typed relationship gates, uid/id allocation continuing from the highest id per prefix; output equals the Python oracle; add-onto run twice is a no-op); M3 canonical graph to SysML v2 text plus parser-check report; M4 package Bootstrap and Workbench into the new-vault ZIP; M5 run the reduced QEAX, then the full one. | V2-54 (ADR-V2-07 milestones) |

### 6 Acceptance on real QEAX: SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-277 | Active | Gates: A semantics (no ambiguous basic structural ownership), B synthetic golden charger, C BOM (no double count or invented substitution), D Workbench edit without hand-writing SysML, E externally valid SysML and usable v2 vault. First-test order: source/ledger tests, native parser fixtures, one small real QEAX slice, then scale to all 11,447 elements and 14,688 connectors (reduced QEAX), then HTML importer plus disposable V2 base, then read-only Workbench and Bootstrap, then deterministic rerun and audit. | V2-12 (Baseline; Delivery Plan) |

### 6 Acceptance on real QEAX: Testing and acceptance

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-256 | Active | Acceptance gates: G0 source counts and fingerprint, 100% ledger coverage; G1 every type/stereotype pair has an entry or explicit review disposition; G2 stable definition/usage identity, no inferred non-native edges; G3 generated SysML parses and type-checks against the pinned official grammar and libraries; G4 no broken canonical links, complete where-used, no duplicate part definitions; G5 second identical import gives zero changes and BOM-before-EA equals EA-before-BOM where supported; G6 user annotations retained, divergent changes detected; G7 Workbench edit round-trips to the same typed graph; G8 release diff approved, rollback tested. | V2-38 (Phase 1 controls gates) |
| REG-257 | Active | Release acceptance targets R1 to R7: R1 read-only fingerprint/schema/ledger coverage; R2 deterministic canonical mapping with native/extension/deferred outcomes; R3 valid native SysML for eligible rows, separately parser-tested; R4 notes generated into a fresh disposable V2 Base; R5 read-only Workbench shows definition/usage distinction, navigation, provenance, diagnostics; R6 independent Windows/macOS/offline packaging with locked dependencies; R7 no golden claim until outcome and UI checks are complete. | V2-43 (Release Architecture) |
| REG-258 | Active | Functional acceptance gates on complete source accounting, preservation, navigability, stable identity, core native parser success, correct local fallback and zero silent losses, NOT on zero flags. Flags are stable across reimport with no duplicate active representations; promotion from flag to approved semantics keeps provenance. Report summary counts by family; review only high-impact recurring categories in a bounded queue. | V2-46 (Flag-and-Continue Policy) |
| REG-259 | Proposed | mdse_note_format.py validates order, identity, class/subtype, footer layout and that primarySymbol is declared in the block. CI runs it on golden and sample notes; importer output must pass it before a ZIP is called ready. The interim generator v2_step03s_generate_notes.py does not emit this format yet. | V2-57 (ADR-V2-06 enforcement) |
| REG-260 | Proposed | Release gates: QEAX and CSV adapters share one source graph schema; parser accepts positives and rejects negatives; repeat import no-op with modified engineer notes and attachments surviving and conflicts unable to disappear; Workbench navigates, edits, saves, undoes and reopens with unchanged semantics; Bootstrap installs, previews updates, preserves user state and rolls back; Windows and macOS Obsidian smoke acceptance. Deferred: automatic plugin updates, enterprise login, multiuser concurrent editing, advanced graphical design, V1 compatibility. | V2-60 (Shared Note and Release Contract) |
| REG-261 | Active | Before handoff: YAML parses, `id` and `uid` are unique, links resolve, inverses are synchronized, Functions have performers where applicable, and requirement basis, satisfaction, and verification gaps are visible. | R-11.1 (1.23 §14) |

## Phase 2: BOM import, merge and approval (28)


### BOM

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-311 | Proposed | One reusable note per normalized internal part number; revisions and occurrences never duplicate it. Parent assembly owns BOM usages with counts, quantities and applicability. Where Used is a reverse query and is never materialized in the child. Separate discrete multiplicity from measured quantity and unit; preserve raw values; never guess units or double count. | V2-22 (BOM Integration) |
| REG-312 | Proposed | One effective BOM per parent and configuration/revision. Competing simultaneous effective BOMs block automatic interpretation. Historical revisions stay in the source ledger. Family similarity is not automatically specialization, variation or substitutability. | V2-23 (BOM Integration) |
| REG-313 | Proposed | A row with blank internal Part Number and populated Manufacturing Part Number is an alternate of the preceding primary line in the same parent, revision, configuration and BOM group. Consecutive rows attach to the same primary. It is not a child usage and adds no quantity. With no unambiguous preceding primary it is review-only. Acceptance: the three-line example yields 2 required PC-100 occurrences. | V2-24 (BOM-ALT-001) |
| REG-314 | Active | BOM-before-EA and EA-before-BOM imports must converge where supported (G5). | V2-39 (Phase 1 controls) |
| REG-315 | Proposed | Proposals folder holds BOM-A14-VARIANTOF (one-way variantOf from Object to Object, max one forward target, no cycles, no self link, no implicit subtypeOf/partOf/substitutability, derived read-only reverse query) and bom-local-model-06-readonly.yaml. Not active; relationships.yaml 1.36 stays authoritative. | V2-67 (Schema proposals) |
| REG-316 | Active | The vault holds the latest revision of each product in scope. Superseded revisions are not imported. | R-6.1 (ADR-V2-08) |
| REG-317 | Active | One note per PartNumber. A part's properties come from its latest revision. | R-6.2 (ADR-V2-08, MDSE definition) |
| REG-318 | Active | A usage records the child revision pinned by the parent. Parent PN and line number identify a usage. | R-6.3 (ADR-V2-08) |
| REG-319 | Active | A PN whose latest revision cannot be determined is reported and not imported. | R-6.4 (ADR-V2-08) |
| REG-320 | Active | Revision strings are stored as exported, not normalized. | R-6.5 (ADR-V2-08) |
| REG-321 | Active | A child part's body lists each assembly that uses an older revision of it, with that usage. | R-6.6 (MDSE definition) |
| REG-322 | Active | A parent that pins a child revision different from the child's latest revision is flagged with `flagConflict`. | R-6.7 (MDSE definition) |
| REG-323 | Active | Alternate-part rows with a blank PN attach to the PN above them. They are not parts. | R-6.8 (ADR-V2-08) |
| REG-324 | Active | Drawing-only lines are recorded as document references and excluded from quantities. | R-6.9 (ADR-V2-08) |

### Merge, rerun and conflicts

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-297 | Active | Import is additive. An import never deletes existing content. | R-4.2 (MDSE definition) |
| REG-298 | Active | An empty YAML property may be filled by an import. | R-4.3 (MDSE definition) |
| REG-299 | Active | Content that does not match existing body content is added to the body. | R-4.4 (MDSE definition) |
| REG-300 | Active | A change to any existing value requires approval, including EA-owned fields. Approval is given before the run (pre-approval, by field selection in the Start step) or after the run (review approval). | R-4.5 (MDSE definition; supersedes 1.23 §16.4 (see section 14)) |
| REG-301 | Active | Pre-approval applies to all notes in the run. | R-4.6 (MDSE definition) |
| REG-302 | Active | A conflict is content that contradicts existing YAML, v2, or body content and is not approved for change. It is not applied. It is listed in the body with a `flagConflict` callout for engineer review. | R-4.7 (MDSE definition) |
| REG-303 | Active | An engineer resolves a conflict by approving a change or by selecting the correct data by hand. | R-4.8 (MDSE definition) |
| REG-304 | Active | A source record that disappears is reported with a `flagImport` callout. It is not deleted. This applies to EA-owned relationships. | R-4.9 (MDSE definition; supersedes 1.23 §16.4 removal rule (see section 14)) |
| REG-305 | Active | A content change made by an engineer is not changed by an import unless approved. | R-4.12 (MDSE definition; 1.23 §16.4) |
| REG-306 | Active | Add-onto-existing matches a note by `uid`, not by path. | R-4.13 (ADR-V2-07) |

### Open decisions

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-307 | Open | Standards content in the vault: whether third-party standards content may stay (Post-Import Tasks Task 2); second edition of a standard; STD and STK prefixes in element-types.yaml; the Stakeholder ID tag holds clause numbers, not stakeholder IDs. | OPEN-06 |
| REG-308 | Open | Only Object_Type and Stereotype are decided as frontmatter; 38 EA tags are Source: EA body lines (PN, MFG PN, Brand, Quantity, Piece Cost, Current Max). Which become frontmatter or SysML attributes? Recommendation: promote the Identity group (id, SysML1.4::id, PN, MFG PN, Brand). | OPEN-V2-Q3 (ADR-V2-06) |

### SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-309 | Active | Preserve approved EA identity allocation; BOM deterministic UID allocation uses a 2020 baseline, separately. One part-number definition note. BOM parent owns usages, quantities and UOM. Manufacturing alternates are non-additive. Effectivity and revisions are handled separately. Never invent variant or generalization from similar builds. | V2-09 (Baseline 8) |
| REG-310 | Active | Changes to the `## SysML v2` section by import require approval (R-4.5). | R-9.3 (MDSE definition) |

## Phase 3: Workbench editing (3)


### SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-326 | Active | Workbench has distinct structural and visual representations. A child usage is edited by locating its owner and changing the owning source region. Edits show a preview and semantic diff, check source hash for staleness, save atomically (or journal and recover) and re-index. Moving or renaming notes never changes structure. | V2-10 (Baseline 9; Source Ownership) |
| REG-327 | Active | Graph staleness: edits are validated at commit. A graph opened against a newer model revision freezes interaction and prompts Reset/Refresh. Never overwrite the model from a stale graph or mutate SysML merely by opening a view. | V2-20 (STEP-00 10) |

### Workbench

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-325 | Active | Workbench is an editor, not only a viewer, for Local Model context and reusable definitions through separate surfaces. Internal Structure view is a presentation of one Local Model context; Canvas geometry is never model semantics. | W-339,W-340 |

## Later (19)


### Classes and types

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-329 | Active | Diagram class (prefix DIA) holds the companion note of each diagram, subtype the EA diagram type. The note has a Canvas link line, written only when the canvas exists. A folded EA note drawn on a diagram becomes a canvas text card. | W-212,W-213,W-214 |

### EA field and tag dispositions

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-330 | Active | Diagram Name, Author, CreatedDate, ModifiedDate and Notes dispositions. Duplicate diagram names need a duplicate rule. | W-71 |
| REG-331 | Active | Each diagram is an Obsidian canvas file plus a companion note (uid, id, description, source lines). Sequence diagrams get a separate rule. | W-73 |
| REG-332 | Active | Sequence messages are an ordered list on the diagram's companion note, not relationships. | W-176 |

### Governance and documents

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-335 | Proposed | Two trees: the toolchain repo (Test_Vault_) and the generated model vault (SharePoint first). Four-phase tidy in place: 99System into 26_Definitions/decisions; split 26_Definitions into adr/steps/registers/audits/concepts/generated; split 25_Testing into unit/gates/fixtures and 24_Workbench/docs into decisions/design; move 100_Archive out. Replace 51 workflows with one suite-manifest-driven workflow. Generate catalogs and censuses in CI. Needs user approval per phase. | V2-47 (File Organization Proposal) |
| REG-336 | Blocked | The staging branch chore/v2-folder-separation-20261018 (1,433 moves) is BLOCKED: do not merge until zero executable stale references (120 flagged), V2 Base/Importer/Bootstrap have their own buildable copies (active V2 never depends on archived V1 runtime), manifest and ruleset hashes are pinned, parser/ledger/note-writer smoke gates pass at the exact SHA, source and archive blob SHAs are compared, and the PR is merged by review only (no auto-merge, no history or branch deletion). | V2-68 (Migration Merge Gates) |

### Importer

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-333 | Active | Diagrams-only run: adds diagram files to an existing vault, never creates or edits element notes, resolves references through the ledger uid, and is deterministic. A narrow exception to W-36 and W-37. | W-62 |
| REG-334 | Active | v0.8.0 is a complete model-and-attachment import. EA diagrams are deferred to a selectable, idempotent post-import pass chosen by EA diagram type. Every source diagram is reconciled as intentionally deferred. | W-300,W-301 |

### Note format and templates

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-328 | Active | An element with a default diagram gets a Default diagram line, written only if the diagram canvas is created. | W-80 |

### Open decisions

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-337 | Open | relationships.yaml still carries a crossVault guidance entry (W-263/W-265). | OPEN-02 |
| REG-338 | Open | Diagram handling: how Ports are drawn, selection beyond type, drawn objects with no note, reading the Review Changes Log (W-62, W-73). | OPEN-03 |
| REG-339 | Open | Which note keeps its id when a sweep finds duplicates; whether original EA modified dates are kept; which status values mean a person must still review AI-created notes; whether a stamping script computes uid and id mechanically; backfilling uid and id on existing notes. | OPEN-04 |
| REG-340 | Open | Post-import tasks (Tasks 1 to 8 in Post-Import Tasks.md): flow-connector moves, containment specificity, directional pair replacing equals, properties from body lines, multi-line tag values, relationship field order and empty-field writing (W-126). | OPEN-07 |
| REG-341 | Open | Handoff package EA_Native_Translator_Handoff_2026-09-28 is to be reviewed one topic at a time; nothing adopted yet. Methodology notes (rules, decisions, canvases, bases) and 99 canvas nodes pointing at non-existent paths await a decision. | OPEN-08 |
| REG-342 | Open | Freestyle.md template: whether to add a uid line; Port.md default subtype; modelCheck and legacy folder values in element-types.yaml versus W-04; unused types.json properties (18). | OPEN-10 |

### SysML v2 authority

| Reg ID | Status | Rule | Source IDs |
|---|---|---|---|
| REG-343 | Active | EA sequences produce a workflow note (participants, messages, ordering, guards) using native Message/EventOccurrence/Succession only with explicit source evidence. All EA diagram work, including Canvas seeding, is deferred until the toolchain and golden import are accepted. | V2-17 (STEP-00 4; ADR-V2-05) |
| REG-344 | Active | V1 function baseline to carry forward: Bootstrap, Workbench element management and views, importer behavior, test/release, and export to SysML source, Markdown, model tables and Excel (BOM, interfaces, requirements, where-used, mapping). Parity needs comparison of actual code and tests, not a checklist. | V2-28 (Functional Parity) |
| REG-345 | Active | Fixture coverage targets: every element and relationship kind including invalid edge cases and non-happy paths (damaged source, partial update, stale hashes, conflicts, interrupted update, new user fields, attachment preservation). | V2-29 (Functional Parity) |
| REG-346 | Active | All EA diagrams (tables, layout, Canvas generation, diagram-based normalization, fidelity checks) are out of scope for all active V2 tools and golden import tests. Reopen only after the golden import is accepted, all planned tools are complete and the user approves a diagram phase. | V2-41 (ADR-V2-05; Release Architecture) |

## Conflicts between sources

| ID | Tool | Conflict | Sources | Proposed resolution | Blocks |
|---|---|---|---|---|---|
| C-1 | Importer | EA-owned fields replaced on rerun | 1.23 §16.4, W-317 vs R-4.5 (your rule: change needs approval) | Your rule replaces it. Amend 1.23 §16.4 and note W-317 as partly superseded. | P1 |
| C-2 | Importer | Removed EA relationships are removed on rerun | 1.23 §16.4 vs R-4.9 (flagImport, never delete) | Your rule replaces it. Amend 1.23 §16.4. | P2 |
| C-3 | Importer | Same uid with different type: reported, nothing written | ADR-V2-07 vs R-4.7 (flagConflict in body) | Content conflicts use flagConflict. Identity conflicts: see C-13. | P2 |
| C-4 | Importer | subtype, eaType, sourceRole, primarySymbol refreshed from EA | ADR-V2-07, ADR-V2-06 vs R-4.5 | Approval only. Amend both ADRs. | P2 |
| C-5 | Importer | ## SysML v2 and ## Source: EA replaced on each rerun | ADR-V2-07, ADR-V2-06 vs R-4.5, R-9.3 | Approval only. Amend both ADRs. | P2 |
| C-6 | BOM | Superseded revisions not imported; mismatch reported as conflict | ADR-V2-08 vs R-6.6, R-6.7 | Parent is flagged, child body lists the older-revision usage. Close the ADR-V2-08 open question. | P2 |
| C-7 | Model rules | Template keeps all properties vs empty non-template fields not written | AI_INSTRUCTIONS.md step 1 vs R-2.3 | Confirm R-2.2 and R-2.3 scope (imported notes only, or hand-made notes too). | P1 |
| C-8 | Governance | Translator Definition §10 is cited but the file is not in the repo | 1.23 §14 | Create it or remove the citation. The 100 table dispositions live in the source profile (W-393, W-394). | P1 |
| C-9 | Model rules | Stable tokens for usages once Local Model is gone | ADR-V2-06 Q1 vs R-8.5 | Open. Needs a pinned-parser test of SysML short names. | P1 |
| C-10 | Model rules | Ruleset 1.23 is behind the Decision Log (W-320 to W-398) | 1.23 §3–§7, §15.7 vs W-384, W-398, current schemas | Re-derive class, relationship and Local Model rules from the schemas, not 1.23. | P1 |
| C-11 | Importer | "Never run over an existing vault / never re-import" vs add-onto and BOM import | W-36, W-37, W-62 vs ADR-V2-07, R-4.2 | Record a new W-decision that names W-36, W-37 and W-62 as superseded. | P2 |
| C-12 | Importer | Path length: 212, then 400 hard stop, then none, then 400 report-only | W-318, W-324, W-382, ADR-V2-06 Q5 | W-382 is the latest accepted (no limit). Confirm whether to add a 400-character report for SharePoint. | P1 |
| C-13 | Importer | Identity conflicts are hard errors vs flagConflict | W-317 vs R-4.7 | Keep hard error for identity; flagConflict for content. Confirm. | P2 |
| C-14 | Base and Bootstrap | Dataview removed in W-370 but still named in older docs | W-370 vs project notes, older docs | W-370 governs. Search templates and AI_INSTRUCTIONS for Dataview dependencies. | P1 |
| C-15 | Importer | A destination that already holds Import State.json is rejected for another semantic import | W-371 (and W-389) vs add-onto import (ADR-V2-07, Phase 2 BOM) | Needs a decision: how Import State records an add-onto run. Blocks Phase 2 unless amended. | P2 |
| C-16 | Governance | Where Workbench source is authoritative | W-328 (MDSE_Workbench repo) vs Tool Definitions page (Test_Vault_ 55_Workbench, provisional) vs 24_Workbench in this repo | Owner to name one location. | P1 |
| C-17 | Model rules | AI_INSTRUCTIONS line 56 keeps folders at or below 75 files and allows folder_N | AI_INSTRUCTIONS.md vs W-382 (no file-count limits, no folder_N) | AI_INSTRUCTIONS.md is stale. Amend. | P1 |
| C-18 | Importer | Boundary: removed from the model vs one aggregate Boundary note vs per-element modelCheck/Boundary | 60-family reconciliation, STEP-00 2, element-types.yaml modelCheck | STEP-00 2 (aggregate note) is latest. Update the mapping docs and the modelCheck subtype list. | P1 |
| C-19 | Model rules | Frontmatter relationship fields: derived mirror or dropped | ADR-V2-06 Q2 vs relationships.yaml 1.36 (authored forward fields) | Owner decision. It decides whether Rovo can query relationships without parsing SysML. | P1 |

## Open decisions (owner)

| ID | Phase | Question |
|---|---|---|
| REG-239 | P1 | Local Model usages are SysML usages in v2. Stable tokens for v2 usages are an open question (ADR-V2-06 Q1). |
| REG-262 | P1 | Inverse-field regenerate script: language, location, when it runs; whether Nodian is removed (W-275, W-287). |
| REG-263 | P1 | Bootstrap must implement author registration: the first-use popup saves a code locally but does not create the person note; install-time name entry should create .obsidian/author-code.txt by the same rule as the snippet; where the Bootstrap source lives. |
| REG-264 | P1 | What makes a vault ready for finishing touches (golden definition). |
| REG-265 | P1 | Where do the stable 30-character tokens for usages live in SysML text? Recommendation: SysML short names, part <'2026...'> controller : Controller; must be accepted by the pinned parser first (not verified). |
| REG-266 | P1 | Keep frontmatter relationship fields as a derived mirror of the SysML block (written only by Workbench in the same transaction) or drop them? Recommendation: keep, so "what satisfies REQ-x" can be queried without parsing SysML. Directly affects Rovo queryability. |
| REG-267 | P1 | Adopt sourceRole and primarySymbol as governed v2 property names? Recommendation: yes. |
| REG-268 | P1 | Reinstate a blocking path-length report (never shortening) for SharePoint, and at what limit? Recommendation: 400 decoded characters plus a sync-root budget. (C-12) |
| REG-269 | P1 | How will Rovo read the model? The Atlassian SharePoint connector lists Word, Excel, PowerPoint, PDF and web pages, not Markdown. Confirm with Atlassian; if .md is not indexed, generate a Rovo-readable projection. |
| REG-307 | P2 | Standards content in the vault: whether third-party standards content may stay (Post-Import Tasks Task 2); second edition of a standard; STD and STK prefixes in element-types.yaml; the Stakeholder ID tag holds clause numbers, not stakeholder IDs. |
| REG-308 | P2 | Only Object_Type and Stereotype are decided as frontmatter; 38 EA tags are Source: EA body lines (PN, MFG PN, Brand, Quantity, Piece Cost, Current Max). Which become frontmatter or SysML attributes? Recommendation: promote the Identity group (id, SysML1.4::id, PN, MFG PN, Brand). |
| REG-337 | Later | relationships.yaml still carries a crossVault guidance entry (W-263/W-265). |
| REG-338 | Later | Diagram handling: how Ports are drawn, selection beyond type, drawn objects with no note, reading the Review Changes Log (W-62, W-73). |
| REG-339 | Later | Which note keeps its id when a sweep finds duplicates; whether original EA modified dates are kept; which status values mean a person must still review AI-created notes; whether a stamping script computes uid and id mechanically; backfilling uid and id on existing notes. |
| REG-340 | Later | Post-import tasks (Tasks 1 to 8 in Post-Import Tasks.md): flow-connector moves, containment specificity, directional pair replacing equals, properties from body lines, multi-line tag values, relationship field order and empty-field writing (W-126). |
| REG-341 | Later | Handoff package EA_Native_Translator_Handoff_2026-09-28 is to be reviewed one topic at a time; nothing adopted yet. Methodology notes (rules, decisions, canvases, bases) and 99 canvas nodes pointing at non-existent paths await a decision. |
| REG-342 | Later | Freestyle.md template: whether to add a uid line; Port.md default subtype; modelCheck and legacy folder values in element-types.yaml versus W-04; unused types.json properties (18). |
| DEC-1 | P1 | Amend 1.23 §16.4, ADR-V2-06/07/08 and AI_INSTRUCTIONS.md now, or after the baseline run? |
| DEC-2 | P2 | BOM list and GSE charger BOM timing |
| DEC-3 | P1 | Where private real-data evidence is stored |
| DEC-4 | P1 | Commit MDSE_Definition.md into Test_Vault_ and where |
| DEC-5 | P1 | Scope of the empty-field rule (imported notes only, or hand-made notes too) |

## Retired (superseded or historical, no build effort)

| Reg ID | Rule | Source IDs |
|---|---|---|
| REG-347 | Parts that represent a Class fold into the assembly as a hasPart entry; Parts pointing at Activity, State or Signal become hasPart entries; Parts with no usable block become Object notes with subtype part. | W-136,W-137,W-138 |
| REG-348 | Activity becomes Function (or Verification for a test case). | W-141 |
| REG-349 | State in the Design package becomes Design; elsewhere State. | W-142 |
| REG-350 | transmits, receives and exchanges on a Port point at the Item Flow notes for the data it carries. | W-177 |
| REG-351 | Fix by changing the tool and importing fresh. Never run over an existing vault. Import must be deterministic. | W-36 |
| REG-352 | Import and review loop: fresh import, review, then finishing touches or a fresh re-import with improved rules. A released vault is never re-imported. | W-37 |
| REG-353 | The native importer is a local offline HTML tool that reads the .qeax through browser File.slice(). v0.1 was a read-only preflight. | W-271 |
| REG-354 | Designator parse rules for Regulatory and Webasto Requirements; designators keep / in the id. | W-201,W-202 |
| REG-355 | Canonical identity for a merged added-Port group is the earliest-created source Port. | W-276 |
| REG-356 | Applied the property set and order (W-97, W-88) to the 26 templates, schemas, snippets and instructions. | W-112 |
| REG-357 | V1 Port rules: interface Classes become Port notes, instance Ports merge into block Ports, redefinition becomes subtypeOf, hasPort/portOf, Port and pin naming, proxy and full subtypes, review lines. | W-113,W-114,W-120,W-121,W-122,W-123,W-125,W-127,W-128,W-129,W-130,W-134 |
| REG-358 | Removed State Machine pairs hasStateMachine, hasState, hasTransition. | W-185 |
| REG-359 | Correction: the connector worklist was missing 13 export columns; added. | W-58 |
| REG-360 | Line format for values kept on a merged Port. | W-211 |
| REG-361 | Source reference keyed by EA GUID, copied values. | W-34 |
| REG-362 | Vault sweep confirmed every field and tag column is covered by a disposition. | W-108 |
| REG-363 | Dry run, vault review, and consistency checks of the element and connector mapping (each element lands in one outcome; every connector lands in exactly one rule). | W-148,W-150,W-178,W-183 |
| REG-364 | Work order: import blockers come before the templates. | W-193 |
| REG-365 | Open-list clean-up and full workspace review for clashes and old material. | W-221,W-245 |
| REG-366 | No package filter: every test run is a full run. | W-251 |
| REG-367 | Importer v0.4 and the base vault synchronized to relationship schema 1.32. | W-287 |
| REG-368 | Occurrence model validated through the real importer (v0.6); cross-repository audit sets v0.5.2/schema 1.35 as the merge-forward baseline. | W-295,W-296 |
| REG-369 | Duplicate names take the note's id as suffix. | W-198,W-199,W-200 |
| REG-370 | Remediate 88 over-260-character Industrial connector paths by semantic placement and removing repeated parent wording. | W-307,W-308 |
| REG-371 | The base vault gets a fresh .vault.yaml (UNINITIALIZED) and is passed as a ZIP. | W-269,W-270 |
| REG-372 | Workspace clean-up: mapping files aligned to W-237 to W-239, Ruleset 1.22 issued, README and stale governance documents replaced, old translator folder archived and Rulesets 1.19 to 1.21 removed. | W-258,W-260,W-261,W-264 |
| REG-373 | Pause the next integration vault until Workbench and importer are aligned; use one fresh integrated vault. | W-337 |
| REG-374 | First test slice was 02 Product Context. | W-267 |
| REG-375 | The actual QEAX (EA_2026_09_06_endgame.qeax) matched the verified source counts; v0.2 whole-model planning passed (35,969 elements, 21,822 connectors, 1,387 packages, 2,924 diagrams, 42,052 xref rows). Source values truncated at 255 characters are source truncation. | W-273,W-274 |
