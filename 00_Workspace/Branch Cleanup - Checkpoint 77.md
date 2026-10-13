# Branch Cleanup — Checkpoint BR-77: Base Initialization Safety Contracts

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Frozen source SHA: 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: STATIC SOURCE REVIEW ONLY; no Base build, initialization or GUI test performed.

## Files inspected

- `Base Vault/Initialization/Initialize-Vault.sh`, blob `ff5ae878fb7086193a7546e73efc9d7541bcd98a`.
- `Base Vault/Initialization/Initialize-Vault.ps1`, blob `6009a25193ab81e44085f1540923dc4de4e631dc`.
- `Base Vault/Tools/v0.8.0-r2/build-base.py`, blob `67af4b69ea76a22b97db8851bd54ddc560b15784`.

## Confirmed behavior

- Base builder writes fresh `.vault.yaml` containing `vault_uid: UNINITIALIZED` and `mdse_release` from the controlled release manifest.
- Both initializers require a 13-character `[a-z-]` author code and an existing `.vault.yaml`. They generate 17-digit UTC timestamp plus author code, so a 30-character vault UID.
- Both preserve the extracted `mdse_release` value and write `default_branch: main` and user-provided display name.
- Both refuse initialization if no `UNINITIALIZED` substring is found and if release identifier cannot be extracted.
- Builder and both initializer scripts were inspected, but no commands were executed.

## New safety gaps to address in a separately reviewed engineering PR

**B77-01 — Exact field validation (P1):** Shell uses `grep -q UNINITIALIZED .vault.yaml`, PowerShell uses `$existing -match "UNINITIALIZED"`. Both accept the substring *anywhere* in file rather than parsing `vault_uid` and requiring an exact scalar value. A previously initialized vault containing that word in some other field/comment can pass the current guard. Fix by parsing strict approved YAML fields, validating UID state and rejecting duplicate keys.

**B77-02 — Safe serialization of display name (P1):** Both scripts interpolate user-supplied vault display name into plain YAML `name: <input>` without YAML quoting/escaping. Colons, comments, embedded newlines or other YAML syntax can corrupt metadata or create additional keys. Use one controlled YAML serializer or a limited validated input format and atomic output; test names with quotes, colon+space, hashes and newlines.

**B77-03 — Atomic write / preserve original on failure (P1):** Both scripts overwrite `.vault.yaml` directly, with no temp-file-plus-rename boundary. Interruption can leave an incomplete file. Ensure temp file is validated and atomically renamed with existing permissions; never automatically overwrite an initialized vault.

**B77-04 — Source release equivalence (P1):** Both scripts check only that `mdse_release` is nonempty; they do not independently prove it equals the controlled release or the generated plugin lock. The release/Bootstrap checker is the intended separate qualification step, but initialization should avoid representing an arbitrary file as matching. Add a preflight that does not silently mutate the release value; keep security/model release approvals separate.

## Recommended negative tests (not implemented)

1. `vault_uid: <valid initialized ID>` with `UNINITIALIZED` in comment or `name` -> refusal and unchanged bytes.
2. Duplicate `vault_uid` keys / missing UID / malformed scalar -> refusal.
3. Display names containing `A: B`, `#`, quote and newline -> valid roundtrip or explicit safe rejection; no unexpected YAML fields.
4. Simulate failure before replacement -> unchanged source `.vault.yaml`; no partial success announcement.
5. Valid clean Base UID `UNINITIALIZED` with controlled release -> exactly one valid UID and unchanged `mdse_release`.
6. Run on actual macOS and Windows PowerShell supported versions; verify encoding and reader compatibility.

## Limitations and release boundary

The static weakness does not prove exploitation or actual vault corruption. Existing Bootstrap and release validation may detect invalid artifacts later but do not replace safety at initialization. BR-76 disposable Base generation/validation remains NOT EXECUTED.

NEXT BR-78: Evaluate exact `.vault.yaml` parsing and validation already present in MDSE Bootstrap before deciding how to implement new initializer guards, and avoid duplicating controls unnecessarily.

No code/manifest/plugin file changed, PR approved/merged/closed, branch deleted, repository archived, model/QEAX accessed or release issued.
