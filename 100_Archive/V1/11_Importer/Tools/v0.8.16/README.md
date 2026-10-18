# EA to MDSE Native Importer v0.8.16

v0.8.16 builds on v0.8.15 and implements W-382. It changes output placement and naming only; semantic mappings, relationship classification, Local Model 0.3 behavior, identity allocation and source evidence rules are unchanged.

## Output changes

- No importer-defined total generated-path-length limit.
- No generated-file-count limit per folder.
- No mechanical `folder_N` capacity subdivisions.
- The physical filesystem component limit remains enforced.
- A nested emitted element is written under a folder named for its emitted parent element: `Parent.md` beside `Parent/Child.md`, recursively for deeper nesting.
- Imported note filenames are globally unique case-insensitively across the vault namespace.
- Existing base/system note basenames are reserved before imported names are assigned.
- Collision resolution follows the governed naming order: explicit type-specific discriminator where defined (for example Requirement `_r`), then the shortest useful emitted-parent/source-package context, then deterministic `~2`, `~3`, ... only as the fallback.
- Imported-note links use filename-only targets because imported filenames are globally unique.
- `Review - Long Paths.csv` is no longer generated.

These changes deliberately affect the generated vault result, not the EA semantic interpretation.
