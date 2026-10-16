# EA to MDSE Native Importer v0.8.3

v0.8.3 preserves v0.8.2 unchanged.

Changes:
- keeps the 212-character path limit;
- reserves at least 8 readable filename characters plus .md;
- preserves normalized engineering folders first;
- if the folder hierarchy is still too long, replaces the longest contributing non-root folder with a deterministic sibling label such as folder_3;
- applies that replacement consistently to the entire subtree;
- repeats only as needed;
- keeps the original source folder and final output path in review evidence.

Reason for change: the real EA8647 v0.8.2 run passed preflight and whole-model planning, then found a path whose folder hierarchy remained too long even after redundant note/folder collapse.

Retained fixes:
- v0.8.2 redundant note-named folder collapse;
- v0.8.1 Local Model Object-only part occurrence rule;
- v0.8.1 base-vault selection hardening;
- 75-file folder capacity with deterministic folder_1, folder_2, etc. subdivision.
