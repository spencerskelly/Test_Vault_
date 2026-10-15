"""Resolve IMP-011 owner references only by exact, unique known note paths.

Do not accept suffix, basename, case-insensitive or guessed matches.
"""
from pathlib import PurePosixPath

def resolve_owner(owner_note: str, known_paths: set[str], aliases: dict[str, str] | None = None) -> str:
    value = owner_note.strip().replace("\\", "/")
    if not value or value.startswith("/") or ".." in PurePosixPath(value).parts:
        raise ValueError("unsafe or empty owner reference")
    if value in known_paths:
        return value
    if aliases and value in aliases and aliases[value] in known_paths:
        target = aliases[value]
        if sum(1 for candidate in known_paths if candidate == target) != 1:
            raise ValueError("ambiguous mapped owner")
        return target
    raise ValueError(f"unresolved owner reference: {value}")

