# MDSE Impact-Focused Remaining Work — 2026-10-05

**Status: current execution filter.** This document does not replace [[MDSE Plan - Path to a Golden Model]] or any `W-n` / `WB-n` authority. It narrows the remaining work to items that materially improve engineering usefulness, data safety, release confidence, or team usability.

## 1. Value test

Continue a task only when it materially improves at least one of these:

1. **Model integrity** — prevents wrong, stale, duplicated, orphaned, or corrupted engineering data.
2. **Engineering usability** — lets an engineer inspect or change the model safely without raw Markdown or specialist knowledge.
3. **Release confidence** — proves the importer, Workbench, Bootstrap, and Base operate together on the real model.
4. **Performance at real scale** — measurably improves startup, indexing, editing, validation, or recovery on the production-size vault.
5. **Adoption / operability** — removes a blocker for normal Mac/Windows users or for controlled Git-based collaboration.

Work that only produces more internal neatness, duplicate documentation, speculative abstraction, or micro-optimization without a measured bottleneck is deferred.

## 2. What is already good enough

- The numbered Workbench performance/stability roadmap is complete through Step 60. Do not create more numbered stability steps unless a changed candidate invalidates an accepted gate.
- Startup/readiness staging, warm-cache behavior, recovery paths, repeated restart acceptance, and the major runtime architecture have already received substantial validation.
- The methodology/base/importer governance structure is mature enough to support the next integrated release gate.
- The current high-value Workbench safety work is the bounded completion of stale-identity protection across mutation paths. WB-125 and WB-126 materially reduce the risk of writing through stale index state; finish this boundary, then stop expanding it unless testing exposes another real failure.

## 3. Critical points

### C1 — Finish the write-safety boundary, then stop hardening in isolation

The highest remaining corruption risk is a writer mutating a note or local record after its source identity has changed. Complete the same fresh-source identity protection for the remaining ordinary property/body mutation paths and prove failure is atomic; after that, move on to engineering workflow capability rather than continuing open-ended defensive work.

### C2 — Complete the minimum usable structured editor

The system does not become materially useful to the engineering team until representative note, relationship, part, endpoint, connection, and flow edits can be made through Workbench without raw Markdown. W4/W5 therefore carry more value than additional standalone runtime tuning.

### C3 — Prove the toolchain on one fresh, real integration vault

Importer v0.8.6, Workbench, Bootstrap 0.3.1, and the 0.8.0 Base remain candidates until they operate together on the real QEAX and real vault scale. One controlled integration run is the strongest remaining risk-reduction activity.

### C4 — Make correctness measurable and repeatable

Determinism, headless validation, broken-link/identity/inverse checks, and run-to-run diffing convert review from manual trust into evidence. These are release-enabling controls, not polish.

### C5 — Validate actual engineer workflows before expanding features

After integration, exercise a small number of real engineering tasks end-to-end: navigate an assembly, inspect context vs definition, change a property, add/remove a relationship, reconnect structure, undo, restart, and confirm the result persists. Feature expansion should follow observed friction from these workflows.

## 4. Remaining work — granular impact sequence

### Phase A — Close the active Workbench safety boundary

**A1 — Inventory remaining mutation entry points.**  
List every legacy or structured writer that can change note frontmatter, ordinary body content, relationships, or Local Model records. Mark which already perform a fresh-source UID/owner-identity check and which do not.

**A2 — Guard ordinary property writes.**  
Before a property mutation is applied, verify the current file's UID still matches the indexed target. Fail closed without changing the file when identity is stale or missing.

**A3 — Guard ordinary body writes.**  
Apply the same fresh-source identity check to body-edit paths, while preserving the governed Local Model region boundary. A stale source must produce no partial write.

**A4 — Verify Local Model owner identity coverage.**  
Confirm patch/create/delete operations on local parts, endpoints, connections, and flows validate the current owning note identity immediately before mutation. Consolidate duplicate guards into the shared transaction layer where possible.

**A5 — Prove atomic failure behavior.**  
Add regression cases for stale UID, missing UID, renamed/replaced file, stale local owner, and interrupted write preparation. The expected result is always zero model mutation when validation fails.

**A6 — Declare the identity-safety boundary complete.**  
Record the covered writer paths and stop adding defensive identity work unless a real test exposes a new unsafe mutation route. This is the deliberate exit from open-ended hardening.

### Phase B — Deliver the minimum engineering editor

**B1 — Edit a normal note property through Workbench.**  
Support one representative schema-governed property edit with validation, preview of the semantic change, Apply/Cancel, and undo/redo.

**B2 — Add and remove a first-class relationship.**  
Use the schema to restrict legal source/target combinations, update the inverse consistently, and show the impact before Apply.

**B3 — Edit a Local Model occurrence.**  
Allow a user to change a representative part or endpoint record in context without opening raw Markdown, while keeping reusable-definition editing separate.

**B4 — Create a Local Model occurrence.**  
Create a part or endpoint through the governed identity allocator and Local Model 0.2 writer, then confirm it appears in Structure/Internal views immediately.

**B5 — Create and remove a local connection.**  
Stage connection endpoint selection, validate ownership/boundary rules, Apply atomically, and make undo restore the exact prior model.

**B6 — Attach a flow to a connection.**  
Create/edit a connection-owned flow and confirm interface-centric views derive it rather than duplicating flow truth elsewhere.

**B7 — Exercise one structural transaction.**  
Move or reconnect a representative occurrence using Review/Apply/Cancel, including a temporarily invalid intermediate state that cannot be committed until valid.

**B8 — Verify curated Internal Structure survives refresh.**  
Change a representative assembly, refresh/rebuild the view, and prove semantic updates do not destroy manual presentation geometry.

**B9 — Run the editor workflow regression.**  
Execute property edit, relationship edit, occurrence edit, connection/flow edit, undo/redo, plugin reload, and full restart. Treat failures in persistence or semantic identity as release blockers.

### Phase C — Promote a Workbench candidate for integration

**C1 — Run the affected stability scope once on the new candidate.**  
Because editor/safety changes create a new candidate after the Step-60 freeze, rerun only the acceptance scope affected by those changes rather than reopening the entire historical roadmap.

**C2 — Build and freeze the integration candidate artifact.**  
Record commit and artifact hashes for the editor-capable Workbench candidate after tests/build/performance gates pass.

**C3 — Vendor the candidate into the controlled Base.**  
Update the runtime payload, plugin lock, and release manifest; set `wb106Version` only when the expanded WB-106 editor gate is genuinely satisfied.

**C4 — Run release checks before integration.**  
`check-release.py --workbench` and the Base checks must pass with no unexplained failures before spending time on a fresh integration vault.

### Phase D — Execute the one high-value integrated run

**D1 — Build a fresh Base artifact.**  
Generate the Base from controlled source and verify it before initialization. Do not reuse a previously edited candidate vault.

**D2 — Initialize the candidate repository once.**  
Run the initializer, establish vault identity and Git, and commit the clean initialized baseline before importing model content.

**D3 — Pass Bootstrap first-open behavior on the Mac.**  
Test enable/disable persistence, damaged-plugin handling, governed settings drift, and author registration in the same integration vault.

**D4 — Run importer v0.8.6 decode-only acceptance.**  
Require the known attachment benchmark to pass at 376 documents / 390 files / zero residual before a whole-model write.

**D5 — Run the full real-QEAX import.**  
Generate the complete candidate model once into the fresh Base and retain the full evidence package.

**D6 — Rebuild Workbench and run model checks.**  
Capture Local Model findings, Review counts, index duration, and any broken-reference/identity/inverse/off-rule findings.

**D7 — Run the minimum engineer workflow on the imported model.**  
Use real imported assemblies and relationships to repeat the Phase-B edit workflows. This is the point where the editor proves value against the actual engineering model rather than fixtures.

**D8 — Restart and verify persistence/recovery.**  
Perform plugin reload and full Obsidian restart, then confirm model edits, semantic cache behavior, views, and Review state remain correct.

### Phase E — Turn the integrated result into release evidence

**E1 — Add run-to-run diff evidence.**  
Generate a comparison between equivalent imports so added/removed/renamed/changed model content is explicit instead of manually inferred.

**E2 — Prove deterministic import behavior.**  
Run the same QEAX into a second fresh Base and require no semantic differences except permitted run metadata.

**E3 — Run a headless model validator.**  
Check YAML, links, unique UID/ID/path, inverse consistency, Local Model validity, and identity collisions without requiring Obsidian. A failed validator must fail the run.

**E4 — Decide the remaining rule-level post-import groups.**  
Resolve only importer-fixable issues that materially affect correctness or large-scale usability before freezing the model; avoid note-by-note cleanup that can be generated correctly.

**E5 — Decide the Windows path limit and apply rules by pattern.**  
Use the real target vault location and Windows test machine to set the limit, then correct dominant path patterns rather than manually renaming hundreds of notes.

**E6 — Execute the keep/freeze decision.**  
If importer, Base, Bootstrap, Workbench, determinism, and validation gates pass, keep the run. After this point, stop treating the vault as disposable and move remaining work to reviewed model changes.

### Phase F — Validate usefulness before broad rollout

**F1 — Sample the imported model against EA.**  
Use risk-based/random samples by major element class and compare name, type, text, properties, and relationships. Correct systemic findings before broad use.

**F2 — Measure on the slowest practical team machine.**  
Record vault open, Workbench ready/index, Local Model check, key view load, and representative edit latency. Optimize only measured bottlenecks.

**F3 — Run a two- or three-engineer pilot.**  
Have engineers perform a small set of normal modeling tasks and collect friction, errors, and missing affordances. This pilot should drive the next feature list.

**F4 — Close only adoption blockers.**  
Fix issues that prevent safe everyday use, understandable navigation, review, or collaboration. Defer convenience features and broader visualization until the pilot proves they matter.

**F5 — Baseline and protect the golden model.**  
Tag the accepted model, archive the source QEAX/checksum, enable repository protections/CI, and define the normal branch/review workflow.

## 5. Explicitly defer unless evidence changes

- New numbered performance/stability steps beyond the closed Step-60 roadmap.
- Additive EA diagram generation before the semantic model is accepted.
- Cross-vault infrastructure during the golden-model push.
- Broad Canvas gesture/features beyond the minimum structural editor.
- General vault-size pruning without a measured size/performance problem.
- Rerun-over-kept-vault ownership machinery while the clean-import/freeze rule remains valid.
- Cosmetic documentation cleanup that does not remove user confusion or release ambiguity.
- Additional plugin replacement/removal without measured startup, correctness, or maintenance benefit.

## 6. Practical execution order

The shortest path to material value is:

**A1–A6 → B1–B9 → C1–C4 → D1–D8 → E1–E6 → F1–F5**

The first major milestone is **D8**: a fresh, real imported vault in which an engineer can safely inspect and modify the model through Workbench and restart without losing correctness. The second is **E6**: a keepable, evidence-backed model. The third is **F5**: a protected golden model ready for normal engineering use.
