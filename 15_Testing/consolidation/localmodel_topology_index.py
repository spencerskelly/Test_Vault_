"""Read-only Local Model 0.5 topology index.

Extract Interface ownership, boundary status, and Connection endpoints from
generated Markdown. Never mutates a vault; rejects ambiguous duplicate IDs.
"""
from pathlib import Path
import re

BLOCK = re.compile(r"^\^(?P<kind>ep|conn)-(?P<id>\d{17}[a-z-]{13})\s*$")
REF = re.compile(r"#\^(?P<kind>ep|conn)-(?P<id>\d{17}[a-z-]{13})\b")
START = "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END = "<!-- MDSE:LOCAL-MODEL END -->"


def parse_index(vault: Path):
    owners, boundaries, connections, equality, errors = {}, set(), {}, set(), []
    for path in vault.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        rel = path.relative_to(vault).as_posix()
        active, section, record = False, "", []

        def flush():
            if not record:
                return
            block = next((BLOCK.match(s.strip()) for s in record if BLOCK.match(s.strip())), None)
            if not block:
                errors.append(f"{rel}: record missing block ID")
                return
            key = f"{block['kind']}-{block['id']}"
            fields = {}
            for line in record:
                m = re.match(r"^- ([A-Za-z][A-Za-z0-9]*):\s*(.*)$", line)
                if m:
                    fields[m.group(1)] = m.group(2)
            if section == "Interfaces":
                if key in owners:
                    errors.append(f"duplicate endpoint {key}")
                owners[key] = rel
                if "part" not in fields and "parent" not in fields:
                    boundaries.add(key)
                for dst in REF.findall(fields.get("equals", "")):
                    if dst[0] == "ep":
                        equality.add((key, "-".join(dst)))
            elif section == "Connections":
                if key in connections:
                    errors.append(f"duplicate connection {key}")
                ends = []
                for k in ("endpointA", "endpointB"):
                    matches = REF.findall(fields.get(k, ""))
                    ends.append("-".join(matches[0]) if len(matches) == 1 and matches[0][0] == "ep" else None)
                exposure = ["-".join(m) for m in REF.findall(fields.get("exposes", "")) if m[0] == "ep"]
                connections[key] = {"owner": rel, "endpoints": tuple(ends), "exposes": exposure}
        for line in lines:
            if line.strip() == START:
                active, section, record = True, "", []
                continue
            if active and line.strip() == END:
                flush()
                active, section, record = False, "", []
                continue
            if not active:
                continue
            if line.startswith("### ") and not line.startswith("#### "):
                flush()
                record = []
                section = line[4:].strip()
            elif line.startswith("#### "):
                flush()
                record = [line]
            elif record:
                record.append(line)
        if active:
            errors.append(f"{rel}: unclosed Local Model region")
    return {"owners": owners, "boundaries": boundaries, "connections": connections,
            "equality": equality, "errors": errors}
