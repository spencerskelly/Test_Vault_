# EA to MDSE Native Importer v0.8.4

v0.8.4 preserves v0.8.3 unchanged.

## Why this version exists

The real EA8647 v0.8.3 whole-model run completed semantic generation successfully:
- 30,298 notes
- 2,030 Local Model parts
- 2,484 endpoints
- 460 connections
- 53 flows

However, all 376 approved linked documents failed attachment extraction. The governed source baseline expects:
- 247 ModelDocument rows
- 129 ExtDoc rows
- 376 approved linked documents total
- 390 attachment files total when extraction succeeds

## Changes from v0.8.3

- Decodes raw EA linked-document ZIP payloads from t_document BinContent before applying RTF/image extraction.
- Supports stored and deflate-compressed ZIP entries.
- Accepts generic ArrayBuffer views in blobBytes().
- Preserves existing direct raw-image/raw-RTF handling when content is not zipped.
- Uses BUILD.version in the success UI/log instead of hard-coded v0.8.0 text.
- Success logging now reports linked documents written, attachment files written, and reconciled failures.

## Acceptance target

A successful EA8647 attachment run should approach the governed baseline of 376 linked documents producing 390 files, with any residual failures explicitly listed in Attachment Reconciliation.csv.

All semantic/path fixes from v0.8.1 through v0.8.3 remain in place.
