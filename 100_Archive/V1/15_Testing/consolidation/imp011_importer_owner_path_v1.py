"""Resolve v0.8.19 owner.pathTarget against exact generated note paths."""
from pathlib import PurePosixPath

def resolve_importer_owner(owner_note: str, known_paths: set[str]) -> str:
    value = owner_note.strip()
    if not value or "\\" in value or value.startswith("/"):
        raise ValueError("invalid importer owner path")
    if any(p in (".", "..", "") for p in value.split("/")):
        raise ValueError("unsafe importer owner path")
    # Importer assigns pathTarget = outputPath with terminal '.md' removed.
    candidate = value if value.endswith(".md") else value + ".md"
    if candidate in known_paths:
        return candidate
    raise ValueError("owner pathTarget not found exactly in generated vault")
