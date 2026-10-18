# MDSE v2.0 — Cross-tool contracts (pilot baseline)
Status: PROPOSED IMPLEMENTATION CONTRACT — not evidence of passing tests
Date: 2026-10-18
Companion: MDSE_V2_0_INTEGRATED_ENGINEERING_PILOT_PLAN_2026-10-18.md

## Update/version authority
- One coordinated release manifest defines compatible Base Vault, Importer, Bootstrap, Workbench and SysML rules/schema versions and hashes.
- Base Vault owns default assets and managed settings specification; Bootstrap owns installation and upgrades. Workbench owns interactive model writes; Importer owns import reconciliation. No tool unilaterally overwrites another tool's user-owned data.
- Bootstrap tracks installed manifest, vault ID and stable author ID; use verified releases, staged upgrade, preview and rollback. Author identity is provenance, not authentication. Credentials belong in OS or service credential stores, never in shared YAML.
- Controlled UX baseline: designated managed settings; explicit user-owned exceptions. Preserve user data/settings unless an approved migration explicitly and safely transforms them.

## Note ownership
- One permanent UID for note identity, independent of filename or folder. Source GUID maintained separately for provenance, not substituted for UID.
- YAML: managed IDs/source/evidence/revision metadata with a documented schema. Unknown user-defined keys retained.
- Section headed '## SysML v2': sole authoritative native SysML text. Read and change through a shared parser/validator plus optimistic version check. Do not blindly overwrite engineer-modified text.
- All other Markdown sections, attachments and engineer notes preserved byte-for-byte unless engineer explicitly edits them.
- Import write plan must include created, unchanged, updated, conflicted, deferred, rejected and moved; preview before commit; an identical repeat import yields no changes.
- No deletion during initial pilot imports. Missing source records are reported for review.
- Atomic transaction: snapshot/backup, staged files, integrity checks, rename/apply or rollback, and audit trail; interruption must never leave a silently partial model.
- Unsupported native relationships stay in review ledger and can appear in Workbench as unresolved evidence, never masquerading as SysML relations.

## Testing release gates
1. QEAX and CSV adapters share source graph schema; real source stays local.
2. Official SysML v2 parser validates positive and rejects negative fixtures.
3. Repeat import no-op; modified engineer note and attachment survive; conflicts cannot disappear.
4. Workbench can navigate, edit, save, undo and reopen model with unchanged semantics.
5. Bootstrap can install, preview update, preserve user state and roll back.
6. Windows/macOS Obsidian smoke acceptance; no stop-ship defects.

## Decisions intentionally deferred
Automatic plugin updates, enterprise login, multiuser concurrent editing, unverified native relationship emission, advanced graphical design and optional V1 compatibility. Work is based on already approved SysML v2 semantics.
