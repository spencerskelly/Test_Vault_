# STEP-03T — Approved family classification without premature note renaming

2026-10-18 — committed: `21_Importer/v2_step03t_placement_manifest.py` and three tests.

The generator output from STEP-03S is source-faithful but uses provisional `EA-<Object_ID>.md` identities. Renaming or moving files prematurely would break links and risk conflict with MDSE UID, folder hierarchy, and package metadata rules. STEP-03T therefore creates a **local-only per-note manifest**, using the approved 60-family resolver. It preserves `eaGUID`, `eaObjectID`, source note, exact approved family, disposition, candidate native kind and a proposed *classification group*. Group names are NOT approved final vault paths; `placementAuthorized`, `noteRenameAuthorized`, and `sysmlV2Certified` remain false. Package is `folder_only` in the approved registry, but the existing interim Package notes remain until relationships and directory mapping have a verified replacement.

### Local validation

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03t_placement_manifest.py' -v
python3 21_Importer/v2_step03t_placement_manifest.py \
 "$HOME/Documents/MDSE_Local_STEP03S/Generated_Vault" \
 "$HOME/Documents/MDSE_Local_STEP03S/placement_manifest.private.jsonl"
```

Expected total: 11,303 classified interim element notes. Manifest must not already exist. No diagram data is accessed or generated. Do not upload this per-note manifest to public GitHub.

Next: validate approved MDSE folder and UID governance from V2 definitions, build lossless ID-to-path crosswalk with all relationships (and folder-only package references) accounted for, apply moves atomically to a new output vault, and run navigation parity. Do not invent placement semantics from source package hierarchy.
