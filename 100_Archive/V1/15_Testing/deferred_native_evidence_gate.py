"""Fail-closed evidence eligibility for deferred EA native alternatives.

Approval evidence is necessary, never sufficient for emitting native syntax.
"""
import json
from pathlib import Path

def load(path):
    doc=json.loads(Path(path).read_text(encoding="utf-8"))
    if doc.get("schema")!="mdse-deferred-native-evidence-gates/1" or doc.get("nativeEmissionAuthorized") is not False:
        raise ValueError("UNSAFE_GATE_REGISTRY")
    return doc

def assess(registry,category,evidence):
    rule=registry["categories"].get(category)
    if rule is None:return {"status":"deferred_review","missing":["UNKNOWN_CATEGORY"],"nativeCertified":False}
    required=list(registry["requiredCommon"])+rule["required"]
    missing=sorted(k for k in required if evidence.get(k) is None or evidence.get(k)=="")
    native=evidence.get("candidate_native_construct")
    if not rule["nativeCandidates"] or native not in rule["nativeCandidates"]:
        missing.append("UNSUPPORTED_NATIVE_CANDIDATE")
    if evidence.get("reviewer_decision")!=registry["acceptedReviewDecision"]:
        missing.append("REVIEW_NOT_APPROVED")
    if evidence.get("parser_result")!=registry["acceptedParserResult"]:
        missing.append("PARSER_NOT_PASSED")
    # This gate is evidence coverage only; central registry and native parser
    # remain separately authoritative. Never certify an emitted relationship.
    return {"status":"evidence_complete_not_certified" if not missing else "deferred_review",
            "missing":sorted(set(missing)),"nativeCertified":False}
