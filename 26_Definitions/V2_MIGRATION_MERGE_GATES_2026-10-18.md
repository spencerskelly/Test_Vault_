# V2 migration review gate — 2026-10-18

**Status: BLOCKED — do not merge staging branch into main.**

The automated staging branch `chore/v2-folder-separation-20261018` includes 1,433 file moves: 1,165 archived and 268 classified active V2. It is reversible through Git history, but **physical relocation is not the same as executable migration**.

## Review findings
- Active V2 references: 120 stale paths flagged in `26_Definitions/V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json`. All runnable V2 imports/tests must resolve against the new paths, not archived V1 files.
- Active `14_Workbench/registry` has been moved to `24_Workbench/registry`, and selected V2 tests from `15_Testing` to `25_Testing`. Runtime imports and CI commands require coordinated repair.
- Archive classification moved **all** `13_Bootstrap` sources and most `10_Base Vault`/ `11_Importer` sources into `100_Archive/V1`. These components remain available for reference, but the V2 Base/Importer/Bootstrap still need separately versioned, buildable copies or validated new implementation. Do not make an active V2 release depend on archive runtime code.
- V2 concept documents in `26_Definitions` and pass history in `29_SysMLv2_Translator_Workbench` remain active. Some older 2026-10-15 proposal labels are superseded by approved 2026-10-17/18 decisions, not evidence to reopen the ontology.
- Main workflow paths, tests and active files outside legacy directories also require post-move audit. An automatic `git mv` cannot guarantee these references.

## Required exit gates
1. All active V2 code/docs under 20–29; archive reference-only. Copy or independently implement reusable Bootstrap/Base/Importer library pieces into 20/21/23 with new v2 version ownership (do not relabel archived V1 binary).
2. Rewrite imports, registry lookup paths, parser tests and CI workflows on staging branch; run audit and obtain **zero executable stale references**. Historical references explicitly marked historical may remain.
3. Pin V2-only manifest and ruleset hashes, with no modification to approved element/relationship semantics.
4. Run V2 official parser positive/negative fixtures, canonical graph and ledger regression, and synthetic note writer/small-import smoke gates from the exact staging SHA.
5. Independently compare source and archived file blob SHAs for every moved path, detect collisions and missing content, publish aggregate-only findings.
6. Review and merge staging by PR only after CI passes. Do not permit automatic PR merge and do not delete history, branches or test data.

**Decision:** V1 completed and archived for reference; V2 is sole active development authority. This is a packaging/migration task, not a translation rule review.
