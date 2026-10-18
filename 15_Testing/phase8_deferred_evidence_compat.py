"""Adapt Phase 8 connector ledgers to deferred evidence *requirements*, never attest them.

The Phase 8 CSV contains normalized endpoints and source kinds but omits
several original EA inputs. Absent information must not be reconstructed.
"""
import csv
from collections import Counter

PHASE8_REQUIRED={"source_pk","source_guid","raw_from","raw_to","family",
 "rule","role","status","normalized_from","normalized_to","source_kind",
 "target_kind","diagnostics"}
UNATTESTED=("source_direction","source_role","target_role",
 "source_type","source_stereotype","source_semantic_assertion")

def adapt(row,snapshot_id):
    absent=sorted(PHASE8_REQUIRED-set(row))
    if absent:raise ValueError("INVALID_PHASE8_LEDGER_FIELDS: "+",".join(absent))
    if not snapshot_id:raise ValueError("MISSING_SNAPSHOT_ID")
    # This is metadata, not a filled evidence-gate record.
    return {"schema":"mdse-phase8-evidence-gap/1",
       "source_kind":"EA","source_snapshot":snapshot_id,
       "ea_connector_guid":row.get("source_guid") or None,
       "phase8_status":row["status"],
       "nativeCertified":False,
       "unattestedFields":list(UNATTESTED),
       "requiredManualEvidence":["reviewer_decision","reviewer_rationale",
         "candidate_native_construct","parser_fixture_id","parser_result",
         "workbench_structural","workbench_visual","workbench_navigation",
         "workbench_validation","roundtrip_provenance",
         "ea_element_guid"]}
def aggregate_compatibility(reader,snapshot_id):
    counts=Counter()
    for row in reader:
        status=adapt(row,snapshot_id)
        counts[(status["phase8_status"],tuple(status["unattestedFields"]))]+=1
    return {"schema":"mdse-phase8-evidence-compatibility-aggregate/1",
        "total":sum(counts.values()),
        "byPhase8Status":dict(sorted((s,sum(n for (status,_),n in counts.items()
                           if status==s)) for s,_ in counts)),
        "sourceEvidenceAutoApproved":0,"nativeCertified":0}

EXTENDED_RAW_FIELDS={"source_direction","source_role","target_role",
 "source_cardinality","target_cardinality","raw_source_type",
 "raw_source_stereotype","raw_target_type","raw_target_stereotype",
 "source_aggregation_flag","target_aggregation_flag"}

def raw_evidence_coverage(row):
    """Structural presence is not semantic truth or a parser pass."""
    absent=sorted(EXTENDED_RAW_FIELDS-set(row))
    if absent:return {"status":"schema_incomplete","missingColumns":absent,
                      "nativeCertified":False}
    return {"status":"raw_fields_retained","missingColumns":[],
            "nativeCertified":False}
