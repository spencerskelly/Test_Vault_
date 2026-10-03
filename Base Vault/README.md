# Base Vault

Development area for the controlled MDSE engineering-vault release.

## Folder intent
- **Definition/** — release manifest and human-readable runtime definition.
- **Tools/** — versioned build/config/lock tooling for the base release.
- **Runtime/** — vendored plugin payloads and other generated runtime material used to assemble a base.
- **Testing/** — release consistency checks and test artifacts.
- **Initialization/** — scripts delivered or mapped into a clean generated vault for one-time vault initialization.

`build-base.py` first produces a deterministic uninitialized, non-Git build artifact. The release owner validates it, initializes the vault identity, and turns a copy into the candidate/model Git repository. The Base Vault tooling ultimately assembles the product delivered to an engineer. Tool-development material itself is not copied into the released engineering vault unless the release manifest explicitly maps it there. The Importer is external to the operational vault: it targets a fresh generated base during model creation but is not shipped in the resulting engineer vault.
