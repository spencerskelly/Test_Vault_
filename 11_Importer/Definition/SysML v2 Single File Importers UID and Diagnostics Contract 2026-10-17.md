# SysML v2 HTML importer — UID, BOM epoch, embedded rules and diagnostics

Date: 2026-10-17. Decision status: EA timestamp+author UID rule already governed; new BOM epoch and unified import interface are approved direction. Implementation gated by source and native SysML parser verification.

## Architecture
Use **one distributable, offline, self-contained HTML importer**, with selectable **EA/QEAX** and **BOM workbook** adapters and a common translation/output/validation engine. Two separate inputs/modes; no automatic EA/BOM note merge. Do not load libraries/rules from network at runtime. Preserve browser local-file selection, generate a *fresh* vault/staging directory or archive, never write over the live vault. Existing source-aware EA HTML SQLite loader should be reused, not replaced by lossy CSV conversion. If workbook parsing cannot be reliably embedded into a single HTML with offline library, keep a second *self-contained* BOM HTML sibling, both built from the exact same versioned embedded rules and model libraries. Report hash/version differences as build failures.

## UID — EA
Maintain current `16_Definitions/Properties/uid.md` normative 30-char scheme: 17-digit `yyyyMMddHHmmssSSS` **as source-local wall-clock fields, no UTC conversion**, plus 13-character lowercase ASCII author code (last name + first name, truncation/padding as governed). Use EA `CreatedDate` exactly as stored; milliseconds absent become `000`; EA `Author` for suffix, with existing governed fallback `skellyspencer`; missing CreatedDate obeys existing import-specific fallback and deterministic GUID order. Tied tokens increment milliseconds to keep global uniqueness among notes and local entity tokens. Stable source GUID→UID allocation ledger prevents rerun drift. **Do not start EA IDs at the BOM epoch**.

## UID — BOM: ALL_BOMs namespace
All newly imported BOM note UIDs use the **same 30-character standard**, but **allocate starting at local epoch `20200101000000000`**, beginning 2020-01-01 00:00:00.000, to place BOM-origin notes early in UID sorting. This is an **allocation convention, not a claim that the manufacturing parts were created then**. Store source created/revision dates separately in provenance/YAML. Suffix: use the governed named importer operator/creator author code (13 chars) chosen from the fresh vault's authors list; no invented manufacturer author. The same author suffix may be reused while incrementing timestamp by 1ms for each uniquely numbered note.

- Allocation order: deterministic normalized internal part-number sort, with source row immutable tie-break for missing/ambiguous numbers; **do not invent part numbers**. One BOM definition note per accepted normalized unique internal part number; different revisions do not create duplicate notes. Any supplemental family definitions get a deterministic secondary key and are recorded in manifest.
- Preserve previously allocated BOM UID for that part number on retry, using a durable local **source-key→UID manifest**. Do not reassign because row/order or file count changes.
- Check each candidate UID against **all existing notes and local-entity identity tokens** in destination/staging vault. On collision, increment millisecond by one and retry. Keep an allocation ledger and collision counter. Never modify an existing UID to satisfy a new import.
- Each EA note has its own UID, even if alias equals BOM internal part number; candidate overlap analysis happens after independent import only.
- Retain source catalog name `ALL_BOMs`, source file hashes and provenance. Source file name is not a semantic identity substitute when two independent BOM sets use identical part numbers.
- Validation: 30-char regex, 2020 epoch or later, author suffix normalization, timestamp rollover after 999ms, collision handling and stable rerun.

## Embedded translation rules
The standalone HTML must carry a **generated, immutable embedded snapshot** of approved versioned: 60 EA element-family mappings, 26 connector-family dispositions, follow-on aggregation rules, approved SysML v2 operation/definition/usage registry, source profiles and EA direction evidence; BOM part identity, source column aliases, effective BOM, revision/alternates, multiplicity/quantity/UOM; note section/template/YAML flagLink rules and UID policy. A build script hashes canonical source rules into the single HTML. On launch show rule/profile versions and hash; preflight fails on source schema mismatch, missing rules, unsupported library/parser, unknown fields requiring review or hash drift. Never maintain a second hand-edited mapping table within UI code.

## Structured analysis and error logging
Provide Import Analysis and Diagnostics tabs in each mode with:
1. Preflight: source kind, file digest, schema/table/workbook headers, counts, source/adapter version, embedded ruleset hash, rule coverage and permissions.
2. Source inventory: per-family element/connector/BOM row totals, owner direction, missing endpoints, names/alias, provenance and history.
3. Mapping ledger: **one disposition per source record**, stable source key/ID → note UID / usage token(s) / SysML representation, rule ID+version, evidence, confidence, unresolved reason and source line.
4. Diagnostics severity `INFO/WARNING/ERROR/BLOCKER`, stable error code, family, source identifier, stage, human-readable message, suggested repair, ruleset reference and related records. Catch parser failures, unsupported syntax, duplicate UIDs, dangling links, owner cycles, conflicting cardinality, duplicate effective BOMs, invalid units, malformed continuations, unresolved YAML flagLink and non-native constructs.
5. Summary: expected and produced counts, exclusive disposition reconciliation, unsupported/error by category, skipped/missing/no-op counts and timing. Never claim parser-conformant if not parsed.
6. Export separate offline `import-manifest.json`, `disposition-ledger.csv/json`, `errors.csv/json`, `summary.md` and deterministic native syntax/notes preview; redacted aggregate report for Test_Vault_ only. Do not send source model records to network.
7. **Dry-run default**. Block final export on BLOCKER (source-integrity, UID conflict, invalid serializer/native parser, loss of records or unsafe destination). Treat unresolved but properly preserved `flagLink` as reportable non-native fallback, not a reason to drop records. Warnings never silently converted.
8. Debug mode opt-in with stage timings, stack trace and details **only in local export**, not normal UI. Provide repeatable fixture runner using synthetic tests, check embedded rule hashes and compare dry-run ledgers across reruns.

## HTML user workflow
1. Open offline HTML; select EA/QEAX or BOM; choose source file using file picker.
2. Set author suffix, output fresh staging folder, package/assembly slice and mode (dry-run by default).
3. View preflight inventory and rule/profile hash.
4. Run analysis, inspect errors and filter flagged relations.
5. Generate model in fresh staging vault; save outputs, diagnostics, provenance and source manifest locally.
6. Import/open staging vault in Obsidian; inspect native syntax at note bottom and separate YAML fields; Workbench link/structure/behavior/requirements menus for inspection.
7. Re-run from same input twice and verify UID/usage stability and identical generated outputs. No implicit merge into any existing vault.

## Explicit stop gates
- Current rule documents are approved policy, **not** proof embedded v2 serializer/parser exists or the BOM column formats are settled.
- Production import and a fully native acceptance claim remain blocked until the native serializer, pinned parser, reconciler, diagnostics exporter, note template and staged output all pass synthetic and actual source tests.
- Generated output may keep unresolved links via MDSE YAML `flagLink` and written note explanation, with native syntax unaffected.
