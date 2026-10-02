# 09_Tools — Current status

This folder contains native importer history and vault initialization helpers.

## Current v0.8 direction

There is **no release-conformant v0.8 importer file yet**.

Use these as code/history references only:
- v0.5.2 — accepted safety/base-validation lineage;
- v0.7 — occurrence/QEAX assessment and merge evidence.

Do not use v0.7 to generate a model intended to keep.

The next issued importer is:

`EA_to_MDSE_Native_Importer_v0.8.0.html`

and it must follow:
1. `../10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`
2. `../10_Docs/Translator Definition.md`
3. Workspace Decision Log through W-319
4. relationships 1.35
5. element-types 1.17
6. local-model 0.2

The matched clean base must declare `mdse_release: "0.8.0"`. v0.8 is a clean import; do not migrate/patch a v0.7-generated vault in place.

## Important current rules

- source lineage: EA8647;
- one global 30-character identity-token namespace;
- Local Model Source Map authoritative on rerun;
- duplicate name marker `~2`;
- forced alteration marker `~a`;
- maximum generated repository-relative path 212;
- attachment failures non-blocking but reconciled;
- all source diagrams must reconcile although initial diagram creation is deferred.

See `MDSE v0.8 Toolchain Review - 2026-10-02.md` for the code-gap audit.
