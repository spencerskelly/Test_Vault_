"""Read-only approved EA family resolver. No native text emission or diagram access.

Exact 60 element and 26 connector families are the decision baseline; the old
provisional selector registry remains untouched for historical comparison.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json"
VALID_DISPOSITIONS = {
    "native_candidate", "conditional_review", "folder_only", "mdse_note",
    "attachment_link", "reference_only", "aggregate_boundary_note",
}
OUTLIER = "OUTLIER_UNAPPROVED_OR_UNMATCHED_FAMILY"


def family_key(ea_type, stereotype=""):
    if not isinstance(ea_type, str) or not isinstance(stereotype, str):
        raise ValueError("SOURCE_KIND_MUST_BE_STRING")
    if not ea_type or ea_type != ea_type.strip() or stereotype != stereotype.strip():
        raise ValueError("SOURCE_KIND_REQUIRES_EXACT_NORMALIZED_INPUT")
    return ea_type + (":" + stereotype if stereotype else "")


def load_registry(path=DEFAULT_REGISTRY):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema") != "mdse-v2-approved-family-resolver/0.1":
        raise ValueError("APPROVED_REGISTRY_SCHEMA_MISMATCH")
    if data.get("automatic_native_emission") is not False or data.get("ea_diagrams_enabled") is not False:
        raise ValueError("UNSAFE_NATIVE_OR_DIAGRAM_AUTHORIZATION")
    if data.get("source_data_tables") != ["t_object", "t_connector", "t_package"]:
        raise ValueError("SOURCE_TABLE_SCOPE_DRIFT")
    element_rules = data.get("elements", [])
    connector_rules = data.get("relationships", [])
    if len(element_rules) != 60 or len(connector_rules) != 26:
        raise ValueError("APPROVED_FAMILY_COVERAGE_INCOMPLETE")
    elements = {r["family"]: r for r in element_rules}
    connectors = {r["family"]: r for r in connector_rules}
    if len(elements) != len(element_rules) or len(connectors) != len(connector_rules):
        raise ValueError("DUPLICATE_EXACT_FAMILY")
    if not all(r["disposition"] in VALID_DISPOSITIONS and r["emission_enabled"] is False
               and r["parser_accepted"] is False for r in element_rules):
        raise ValueError("UNAUTHORIZED_ELEMENT_EMISSION")
    if not all(r["disposition"] in ("conditional_native_candidate", "reference_only")
               and r["emission_enabled"] is False and r["parser_accepted"] is False for r in connector_rules):
        raise ValueError("UNAUTHORIZED_CONNECTOR_EMISSION")
    if sum(r["source_count"] for r in connector_rules) != 14688:
        raise ValueError("SOURCE_CONNECTOR_FAMILY_COUNTS_DRIFT")
    return {"elements": elements, "relationships": connectors, "metadata": {
        "schema": data["schema"], "automatic_native_emission": False, "ea_diagrams_enabled": False,
    }}


def resolve_element(ea_type, stereotype="", *, registry=None):
    index = registry if registry is not None else load_registry()
    key = family_key(ea_type, stereotype)
    rule = index["elements"].get(key)
    if rule is None:
        return {"family": key, "status": "review_required", "reason": OUTLIER,
                "native_kind": None, "emission_authorized": False}
    return {"family": key, "status": "approved_group", "disposition": rule["disposition"],
            "native_kind": rule["native_kind"], "evidence_to_review": rule["conditional_evidence"],
            "review_notes": rule["review_notes"], "emission_authorized": False,
            "requires_row_validation": rule["disposition"] in {"native_candidate", "conditional_review"}}


def resolve_connector(ea_type, stereotype="", *, registry=None):
    index = registry if registry is not None else load_registry()
    key = family_key(ea_type, stereotype)
    rule = index["relationships"].get(key)
    if rule is None:
        return {"family": key, "status": "review_required", "reason": OUTLIER,
                "native_operation": None, "emission_authorized": False}
    return {"family": key, "status": "approved_group", "disposition": rule["disposition"],
            "native_operation": rule["native_operation"],
            "evidence_to_review": rule["required_evidence"],
            "emission_authorized": False,
            "requires_row_validation": rule["disposition"] == "conditional_native_candidate"}
