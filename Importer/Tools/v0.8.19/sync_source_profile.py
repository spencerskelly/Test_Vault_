#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROFILE = ROOT / "Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json"
IMPORTER = ROOT / "Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html"
OPEN = '<script id="mdse-source-profile" type="application/json">\n'
CLOSE = '\n</script>'

def load_profile():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    if data.get("schema") != "mdse-ea-source-profile/1":
        raise SystemExit("unsupported source profile schema")
    if not isinstance(data.get("profileId"), str) or not data["profileId"].strip():
        raise SystemExit("profileId is required")
    if not isinstance(data.get("sourceModelId"), str) or not data["sourceModelId"].strip():
        raise SystemExit("sourceModelId is required")
    expected = data.get("expected")
    if not isinstance(expected, dict):
        raise SystemExit("expected object is required")
    for section in ("tables", "elementTypes", "connectorTypes", "diagramTypes"):
        values = expected.get(section)
        if not isinstance(values, dict) or not values:
            raise SystemExit(f"expected.{section} must be a non-empty object")
        for key, value in values.items():
            if not isinstance(key, str) or not key or not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise SystemExit(f"invalid expected.{section} entry: {key!r}={value!r}")
    for required in ("t_object", "t_connector", "t_package", "t_diagram"):
        if required not in expected["tables"]:
            raise SystemExit(f"missing required table count: {required}")
    return data

def embedded_range(text):
    start = text.find(OPEN)
    if start < 0:
        raise SystemExit("importer embedded source-profile block is missing")
    body_start = start + len(OPEN)
    end = text.find(CLOSE, body_start)
    if end < 0:
        raise SystemExit("importer embedded source-profile block is unterminated")
    return body_start, end

def canonical(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def main():
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = ap.parse_args()

    data = load_profile()
    text = IMPORTER.read_text(encoding="utf-8")
    start, end = embedded_range(text)
    wanted = canonical(data)

    if args.check:
        embedded = text[start:end]
        try:
            embedded_data = json.loads(embedded)
        except Exception as exc:
            raise SystemExit(f"embedded source profile is invalid JSON: {exc}")
        if embedded_data != data:
            raise SystemExit("embedded source profile does not equal external authority")
        if embedded != wanted:
            raise SystemExit("embedded source profile is not canonical JSON; run --write")
        if 'const EXPECTED_TABLES = {' in text or 'const SOURCE_MODEL_ID="EA8647"' in text:
            raise SystemExit("legacy compiled EA8647 source contract remains in importer engine")
        for token in (
            "const SOURCE_PROFILE=loadSourceProfile();",
            "const SOURCE_MODEL_ID=SOURCE_PROFILE.sourceModelId;",
            "const EXPECTED_TABLES=SOURCE_PROFILE.expected.tables;",
            "const EXPECTED_ELEMENT_TYPES=SOURCE_PROFILE.expected.elementTypes;",
            "const EXPECTED_CONNECTOR_TYPES=SOURCE_PROFILE.expected.connectorTypes;",
            "const EXPECTED_DIAGRAM_TYPES=SOURCE_PROFILE.expected.diagramTypes;",
        ):
            if token not in text:
                raise SystemExit(f"generic source-profile loader token missing: {token}")
        print(f"source profile sync: PASS ({data['profileId']})")
        return

    IMPORTER.write_text(text[:start] + wanted + text[end:], encoding="utf-8")
    print(f"embedded source profile updated from {PROFILE.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
