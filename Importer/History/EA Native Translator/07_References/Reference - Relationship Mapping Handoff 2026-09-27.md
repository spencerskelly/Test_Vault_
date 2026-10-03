---
uid:
type: Info
status: Working
workspace: EA Native Translator
---
# Relationship Mapping Handoff — 2026-09-27

The current native-translator relationship review uses this handoff as the latest working relationship authority represented by the notes in this workspace.

## Strategy carried into the vault

1. Translate directly when EA relationship + endpoint semantics have an approved MDSE meaning.
2. Preserve unresolved relationships as directional `map*Out / map*In` evidence.
3. Suppress only relationships intentionally determined to have no useful MDSE meaning, recording that action in translator diagnostics/transformation logs.
4. For mapped relationships, write the approved MDSE semantic direction even when it differs from EA source direction.
5. Trend a mature imported vault toward zero unresolved `map*` properties.

See [[Translator Open Decisions]] for the continuation sequence.
