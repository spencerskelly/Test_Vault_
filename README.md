# Ampure Vault Base

Reusable starter for GitHub-backed Obsidian vaults.

This base combines:

- the current engineering MDSE structure and relationship model;
- the company-vault authority and cross-vault rules maintained in `Ampure_Data`;
- Git-safe Obsidian configuration;
- vault identity via `.vault.yaml`;
- a clean test surface for vault-to-vault linking.

## First use

1. Copy/unzip this package into a **new folder**.
2. Initialize `.vault.yaml` using `99_System/09_Tools/Initialize-Vault.sh` on macOS/Linux or `Initialize-Vault.ps1` on Windows.
3. Open the folder as an Obsidian vault.
4. Install/enable the plugins listed in `99_System/01_Admin/Enabled Plugin Stack.md`.
5. Create the GitHub repository and publish this folder.
6. Open `00_Home/Cross-Vault Link Test.md`.

Do not reuse a populated `.vault.yaml` from another vault.

## Authority

- `Ampure_Data` is the common company vault and owns enterprise-wide shared identities.
- Engineering/product-line vaults own detailed technical definitions.
- Shared information is referenced, not copied, unless there is a specific approved reason.
