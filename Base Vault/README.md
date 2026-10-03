# Base Vault

Development area for the controlled MDSE engineering-vault release.

## Folder intent
- **Definition/** — release manifest and human-readable runtime definition.
- **Tools/** — versioned build/config/lock tooling for the base release.
- **Runtime/** — vendored plugin payloads and other generated runtime material used to assemble a base.
- **Testing/** — release consistency checks and test artifacts.
- **Initialization/** — scripts delivered or mapped into a clean generated vault for one-time vault initialization.

The Base Vault tooling assembles the product delivered to an engineer. Tool-development material itself is not copied into the released engineering vault unless the release manifest explicitly maps it there.
