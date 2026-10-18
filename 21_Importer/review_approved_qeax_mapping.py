#!/usr/bin/env python3
"""Summarize approved EA element/connector families from QEAX without diagrams.

No source IDs, names, original row values, or native declarations leave this tool.
Output is aggregate review evidence, NOT a golden import or approved native output.
"""
import argparse
import collections
import json
import pathlib
import sqlite3
import sys
from v2_approved_family_resolver import load_registry, resolve_element, resolve_connector


def _check_columns(db, table, required):
    try:
        found = {r[1] for r in db.execute("PRAGMA table_info(" + table + ")")}
    except sqlite3.DatabaseError as ex:
        raise ValueError("UNSUPPORTED_EA_SCHEMA") from ex
    if not set(required).issubset(found):
        raise ValueError("UNSUPPORTED_EA_SCHEMA: " + table)


def inspect(source, registry=None):
    path = pathlib.Path(source).resolve()
    if not path.is_file():
        raise ValueError("SOURCE_NOT_FOUND")
    rules = load_registry(registry) if registry is not None else load_registry()
    counts = collections.Counter()
    details = collections.Counter()
    exact = collections.Counter()
    try:
        with sqlite3.connect(path.as_uri()+"?mode=ro", uri=True) as db:
            _check_columns(db, "t_object", ("Object_Type", "Stereotype"))
            _check_columns(db, "t_connector", ("Connector_Type", "Stereotype"))
            _check_columns(db, "t_package", ("Package_ID",))
            for ea_type, stereotype in db.execute("SELECT Object_Type, Stereotype FROM t_object"):
                result = resolve_element(ea_type or "", stereotype or "", registry=rules)
                counts["elements"] += 1
                if result["status"] == "review_required":
                    counts["unknown_element_family_rows"] += 1
                else:
                    exact["element:" + result["family"]] += 1
                    details["element:" + result["disposition"]] += 1
            for ea_type, stereotype in db.execute("SELECT Connector_Type, Stereotype FROM t_connector"):
                result = resolve_connector(ea_type or "", stereotype or "", registry=rules)
                counts["connectors"] += 1
                if result["status"] == "review_required":
                    counts["unknown_connector_family_rows"] += 1
                else:
                    exact["connector:" + result["family"]] += 1
                    details["connector:" + result["disposition"]] += 1
            counts["organizational_packages"] = db.execute("SELECT COUNT(*) FROM t_package").fetchone()[0]
    except sqlite3.DatabaseError as ex:
        raise ValueError("NOT_VALID_QEAX_SQLITE") from ex
    return {
        "schema": "mdse-v2-approved-family-source-review/1",
        "source_scope": "ELEMENT_CONNECTOR_PACKAGE_ONLY",
        "ea_diagrams_processed": 0,
        "status": "OUTLIER_REVIEW_REQUIRED" if counts["unknown_element_family_rows"] or counts["unknown_connector_family_rows"]
            else "GROUPS_MATCHED_ROW_EVIDENCE_AND_PARSER_PENDING",
        "counts": dict(sorted(counts.items())),
        "approved_family_counts": dict(sorted(exact.items())),
        "dispositions": dict(sorted(details.items())),
        "native_declarations_emitted": 0,
        "source_rows_exported": 0,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax", type=pathlib.Path)
    args=ap.parse_args()
    try:
        print(json.dumps(inspect(args.qeax),indent=2))
    except (ValueError,OSError) as ex:
        print(json.dumps({"status":"BLOCKED","reason":str(ex)}),file=sys.stderr)
        return 1
    return 0

if __name__=="__main__":
    sys.exit(main())
