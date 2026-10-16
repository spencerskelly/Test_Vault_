# Base Vault

Development area for the controlled MDSE engineering-vault release.

## Folder intent
- **Definition/** — release manifest and human-readable runtime definition.
- **Tools/** — versioned build/config/lock tooling for the base release.
- **Runtime/** — vendored plugin payloads and other generated runtime material used to assemble a base.
- **Testing/** — release consistency checks and test artifacts.
- **Initialization/** — scripts delivered or mapped into a clean generated vault for one-time vault initialization.

`build-base.py` first produces a deterministic uninitialized, non-Git build artifact. The release owner validates it, initializes the vault identity, and turns a copy into the candidate/model Git repository. The Base Vault tooling ultimately assembles the product delivered to an engineer. Tool-development material itself is not copied into the released engineering vault unless the release manifest explicitly maps it there. The Importer is external to the operational vault: it targets a fresh generated base during model creation but is not shipped in the resulting engineer vault.


## Current candidate checkpoint — 2026-10-03

The r2 builder successfully produced a Bootstrap-0.3.1 candidate base and `check-release.py --base` completed with **0 fail / 4 expected pre-release warnings**. The initializer is syntax-gated under `sh -n` (W-336). A new integration vault is intentionally deferred until Workbench WB-106 and importer v0.8.6 are aligned (W-337). OS metadata is excluded from governed copy trees (W-338).
