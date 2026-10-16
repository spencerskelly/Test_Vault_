# EA to MDSE Native Importer v0.8.9

v0.8.9 builds on v0.8.8 and implements W-373 / IMP-004.

## Change

SQLite WAL mode is now a **blocking preflight failure** rather than a warning.

The importer intentionally reads only the selected `.qea/.qeax` file. If the SQLite header indicates WAL mode, the source may depend on uncheckpointed companion WAL content, so planning and writing are not allowed.

The operator must close/checkpoint the EA project and use a clean snapshot.

## Validation

- Embedded JavaScript syntax parse: PASS.
- Static assertion confirms `SQLITE_WAL_MODE` is emitted with severity `fail`.
- Static assertion confirms the old warning form is absent.

## Next hardening item

IMP-005: require the destination base to have an initialized vault identity before it can be selected for import.
