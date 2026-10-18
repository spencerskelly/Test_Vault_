"""Typed EA endpoint and aggregation-owner candidates; source evidence only."""
import collections
import json
import pathlib
import sqlite3

PART_LIKE={"PartDefinition","PartUsage"}
def normalize_kind(typ,stereo):
    if typ=="Class" and stereo=="block":return "PartDefinition"
    if typ in ("Object","Part"):return "PartUsage"
    if typ=="Port":return "PORT_CLASSIFICATION_REVIEW"
    if typ=="Class" and stereo and "Interface" in stereo:return "INTERFACE_CLASSIFICATION_REVIEW"
    return None

def classify(row,objects):
    src=objects.get(row["Start_Object_ID"])
    dst=objects.get(row["End_Object_ID"])
    if src is None or dst is None:return "missing_endpoint"
    if row["Start_Object_ID"]==row["End_Object_ID"]:return "self_reference_review"
    if row["Connector_Type"]!="Aggregation":return "not_aggregation"
    s_kind=normalize_kind(*src)
    d_kind=normalize_kind(*dst)
    if "REVIEW" in (s_kind or "") or "REVIEW" in (d_kind or ""):
        return "port_interface_review"
    if s_kind not in PART_LIKE or d_kind not in PART_LIKE:
        return "incompatible_endpoint_kinds"
    src_flag,dst_flag=row["SourceIsAggregate"],row["DestIsAggregate"]
    if (src_flag,dst_flag) not in ((2,0),(0,2)):
        return "shared_or_ambiguous_ownership"
    if row["Direction"]!="Source -> Destination":
        return "ownership_direction_review"
    # Identified composite end is evidence; no native part usage is created.
    return "typed_composite_owner_candidate"

def audit(path):
    c=sqlite3.connect("file:"+str(pathlib.Path(path).resolve())+"?mode=ro",uri=True)
    c.row_factory=sqlite3.Row
    try:
        objects={r["Object_ID"]:(r["Object_Type"],r["Stereotype"] or "")
                 for r in c.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        counts=collections.Counter()
        query="""SELECT Connector_Type,Start_Object_ID,End_Object_ID,Direction,
                        SourceIsAggregate,DestIsAggregate FROM t_connector"""
        for row in c.execute(query):
            counts[classify(row,objects)]+=1
        total=sum(counts.values())
        return {"schema":"mdse-ea-typed-owner-evidence/1","totalConnectors":total,
                "categories":dict(sorted(counts.items())),
                "nativeCertified":0,"status":"EVIDENCE_ONLY"}
    finally:c.close()
