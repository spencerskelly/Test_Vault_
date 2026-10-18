"""Read-only fail-closed Local Model 0.5 topology index, Flow-safe v3."""
from pathlib import Path
import re

BLOCK = re.compile(r"^\^(ep|conn)-(\d{17}[a-z-]{13})$")
REF = re.compile(r"#\^(ep|conn)-(\d{17}[a-z-]{13})\b")
START = "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END = "<!-- MDSE:LOCAL-MODEL END -->"

def parse_index(vault: Path):
    owners, boundaries, connections, equality, errors = {}, set(), {}, set(), []
    for path in sorted(vault.rglob("*.md")):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        rel = path.relative_to(vault).as_posix()
        active, section, record = False, "", []

        def flush():
            if not record:
                return
            matches = [BLOCK.fullmatch(line.strip()) for line in record]
            ids = [m for m in matches if m]
            if len(ids) != 1:
                errors.append(f"{rel}: expected exactly one record block ID")
                return
            key = "-".join(ids[0].groups())
            fields = {}
            current = None
            for line in record:
                m = re.match(r"^- ([A-Za-z][A-Za-z0-9]*):\s*(.*)$", line)
                if m:
                    current = m.group(1)
                    if current in fields:
                        errors.append(f"{rel}: duplicate field {current} in {key}")
                        current = None
                    else:
                        fields[current] = m.group(2)
                elif current and re.match(r"^\s+-\s+", line):
                    fields[current] += " " + line.strip()
                elif line.strip() and not line.startswith(" "):
                    current = None
            def refs(field, kind="ep"):
                return ["-".join(m) for m in REF.findall(fields.get(field, "")) if m[0] == kind]
            if section == "Interfaces":
                if key in owners:
                    errors.append(f"duplicate endpoint {key}")
                owners[key] = rel
                if "part" not in fields and "parent" not in fields:
                    boundaries.add(key)
                for dst in refs("equals"):
                    equality.add((key, dst))
            elif section == "Connections":
                if key in connections:
                    errors.append(f"duplicate connection {key}")
                endpoints = []
                for field in ("endpointA", "endpointB"):
                    found = refs(field)
                    if len(found) != 1:
                        errors.append(f"{rel}: {key} invalid {field}")
                    endpoints.append(found[0] if len(found) == 1 else None)
                connections[key] = {"owner": rel, "endpoints": tuple(endpoints), "exposes": refs("exposes")}
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() == START:
                if active:
                    errors.append(f"{rel}: nested Local Model region")
                active, section, record = True, "", []
            elif active and line.strip() == END:
                flush()
                active, section, record = False, "", []
            elif active and line.startswith("### ") and not line.startswith("#### "):
                flush()
                section, record = line[4:].strip(), []
            elif active and line.startswith("##### "):
                # Flow belongs to its Connection but has its own endpoint role fields.
                flush()
                record = []
            elif active and line.startswith("#### "):
                flush()
                record = [line]
            elif active and record:
                record.append(line)
        if active:
            flush()
            errors.append(f"{rel}: unclosed Local Model region")
    return {"owners": owners, "boundaries": boundaries, "connections": connections,
            "equality": equality, "errors": errors}
