"""Step 14 proposal-banner boundary: preserve every byte of earlier Workbench guidance.

This is a narrow audit helper for three specifically reviewed paths. It is NOT a
governance approval, and it never reads or modifies model/QEAX files.
"""
from __future__ import annotations

START = b"<!-- MDSE_STEP14_PROPOSAL_BANNER_START -->\n"
END = b"<!-- MDSE_STEP14_PROPOSAL_BANNER_END -->\n\n"
REVIEWED = {
    "00_Workspace/Workbench Performance and Stability Roadmap.md":
        "4f41a03020efe011260dbb884a4c279106814142",
    "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md":
        "0ff206b531c7659b4b46757554a7f1d6d4b1b53f",
    "55_Workbench/docs/README.md":
        "2dc82f816e4626982016ed9453c3c5fad8da3f32",
}


def original_historical_bytes(relative_path: str, raw: bytes) -> bytes:
    """Remove only the correctly positioned Step 14 proposal notice.

    The returned data must separately match the pinned pre-Step-14 Git blob.
    Missing/extra/misplaced banners on a reviewed source fail closed.
    """
    if relative_path not in REVIEWED:
        if START in raw or END in raw:
            raise ValueError("Step 14 banner on unexpected source")
        return raw
    if raw.count(START) != 1 or raw.count(END) != 1:
        raise ValueError("Expected one complete Step 14 banner")
    first_break = raw.find(b"\n\n")
    start = raw.find(START)
    if not raw.startswith(b"# ") or first_break < 0 or start != first_break + 2:
        raise ValueError("Step 14 banner is not directly after the original title")
    end = raw.find(END, start + len(START))
    if end < 0 or end == start:
        raise ValueError("Step 14 closing marker absent")
    banner = raw[start:end]
    for phrase in (
        b"PROPOSAL, NOT APPROVED",
        b"2026-10-10",
        b"1.36",
        b"1.18",
        b"0.5",
        b"0.1.18",
        b"55_Workbench/",
    ):
        if phrase not in banner:
            raise ValueError("Unreviewed or incomplete proposal banner")
    if b"<!-- MDSE_STEP14_PROPOSAL_BANNER_" in raw[end + len(END):]:
        raise ValueError("Nested/duplicated proposal marker")
    return raw[:start] + raw[end + len(END):]


def banner_body(relative_path: str, raw: bytes) -> bytes:
    """Get only the proposed visible notice after enforcing marker boundaries."""
    original_historical_bytes(relative_path, raw)
    return raw[raw.index(START) + len(START):raw.index(END)]
