> [!WARNING] ARCHIVED 2026-10-03 (W-326). SUPERSEDED by [[MDSE Plan - Path to a Golden Model]]
> This proposal's open points and roadmap are carried into the plan (sections 9 and 11). Evidence only.

# MDSE Platform Roadmap and Critical Points — 2026-10-02

> [!NOTE]
> **PROPOSAL, not a decision.** Nothing here changes a rule. Items become decisions only when logged as `W-n` or `WB-n`. Current state and authority: [[00 - Current State]].

## Part 1. Critical points before building the v0.8 tools

Found in the 2026-10-02 review. Checked: Workbench typecheck, 31 tests and build run clean; the importer v0.7 JavaScript parses; schema constants match. Not checked: the importer against the real QEAX, Workbench inside Obsidian, the 60,000-note benchmark.

1. **Importer has no automated tests.** One HTML file, 123 functions. v0.8 adds identity allocation, Source Map, Local Model writer and the 212-character planner. Proposal: a pure core (no DOM, no file handles) with Node tests, the HTML as a thin shell, and golden fixtures from a small QEAX slice (the "Connector ASM - Anderson" subtree has long paths, URL-named and "- Copy" notes).
2. **Two copies of the rules.** The importer embeds the relationship fields; Workbench reads `relationships.yaml`. Found in this review: Workbench test fixtures had drifted from the authority schemas. Fixed by W-320 (fixtures synced, drift check added). Proposal: one shared `mdse-core` package (schema loader, endpoint rules, ModelRef, Local Model parser, ID allocator, inverse regeneration CLI) used by both tools.
3. **Identity and Source Map cannot be repaired afterwards.** Test determinism (two runs byte-identical), collisions (1 ms rule, GUID ordering across notes and local records) and keep the Source Map in the vault under git.
4. **Local Model regions versus hand editing.** Workbench 0.1.15 blocks body edits on governed notes. WB-106 needs region-aware editing; add a health check for broken START/END markers, also as a pre-commit or CI check.
5. **Runtime plugin deployment.** Resolved by W-322: plugins ship inside the base, pinned and hashed, and MDSE Bootstrap 0.3.0 checks the release. Open: run the Base First-Open Test Sheet in Obsidian; the final issued base must pin a WB-106-capable Workbench. CI/release workflows remain inactive until separately enabled.
6. **Review volume.** Every `tracesTo` and 252 nesting-direction items are findings; batch preview and batch resolve (M3) are not built. Estimate the finding count from the acceptance sample before accepting a whole import.
7. **Obsidian performance at 30,000+ notes is unmeasured on the team's hardware** (Dataview, Breadcrumbs, Nodian, Fileclass). Open the 60k synthetic vault on the weakest machine before rollout.
8. **Documentation volume.** The Decision Log is about 437 KB. Addressed in part by [[00 - Current State]], the manifest and the checker; further step: archive old decisions into a dated file and keep short structured entries.
9. **Persisted inverse fields** mean one edit touches two notes; branches can diverge. Run inverse regenerate-and-verify in CI once the shared core exists.

Suggested order: items 1, 2 and runtime plugin deployment first; then the v0.8 importer against the slice fixtures, with WB-106 in parallel once the shared Local Model parser exists; issue the final base only after both are release-ready; measure items 6 and 7 before pilot gate R1.

## Part 2. Roadmap (direction, not commitment)

Principle: Markdown and YAML stay the authority; every surface (Obsidian, Canvas, future web or CLI) is replaceable.

1. **Keep and pilot (R1).** Accepted whole-model import on the matched 0.8.0 pair; WB-106; Create (M2); batch review; pilot with 2 to 3 engineers.
2. **Team daily driver.** Change control through branches and pull requests with semantic diffs; baselines as git tags; CI validation gate; Canvas Model Edit; variants per W-314 (read `abstract` and `usage`, derive candidates, read-only variation UI, session configuration, later named configurations).
3. **Headless platform.** CLI and MCP server on the shared core so AI agents query the model and propose changes as pull requests; impact analysis; AI-suggested trace links arriving as review findings.
4. **Outputs the business uses.** Generated traceability matrices, interface control documents, requirement specifications (docx, XLSX, ReqIF), FMEA tables, compliance coverage dashboards (the regulatory requirement set is the first candidate).
5. **Digital thread.** Links to Jira and Confluence, test results as verification evidence, BOM and PLM data, derived artifacts (CAN signal tables, communication interface documents, parameter tables), SysML v2 import and export to avoid lock-in.
6. **Productize across product lines.** Shared libraries across MHE, GSE, EVSE and PCE with controlled reuse; federated models; decide then whether Obsidian remains the front end.
