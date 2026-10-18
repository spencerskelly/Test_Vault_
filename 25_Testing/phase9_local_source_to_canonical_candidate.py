"""Local-only bridge from a read-only QEAX source connector + Phase 8 row to canonical review.
Never issues attestation, native certification, or an emitter permission.
"""
def candidate(source, ledger, endpoint_map):
    diagnostics=[]
    required=("Connector_ID","ea_guid","Connector_Type","Stereotype","Direction","Start_Object_ID","End_Object_ID")
    if any(k not in source for k in required):diagnostics.append("SOURCE_FIELDS_MISSING")
    if source.get("Connector_Type")!="Generalization" or (source.get("Stereotype") or "").strip():
        diagnostics.append("GENERALIZATION_SOURCE_KIND_UNVERIFIED")
    if source.get("Direction")!="Source -> Destination":diagnostics.append("EA_DIRECTION_NOT_EXPLICIT")
    if str(source.get("Connector_ID",""))!=str(ledger.get("source_pk","")) or str(source.get("ea_guid",""))!=str(ledger.get("source_guid","")):
        diagnostics.append("SOURCE_LEDGER_IDENTITY_MISMATCH")
    start=str(source.get("Start_Object_ID",""));end=str(source.get("End_Object_ID",""))
    if (start,end)!=(str(ledger.get("raw_from","")),str(ledger.get("raw_to",""))):
        diagnostics.append("RAW_ENDPOINT_MISMATCH")
    if (start,end)!=(str(ledger.get("normalized_from","")),str(ledger.get("normalized_to",""))):
        diagnostics.append("LEDGER_DIRECTION_MISMATCH")
    if ledger.get("role")!="source-subtype-to-destination-supertype" or ledger.get("status")!="orientation_normalized":
        diagnostics.append("ROLE_NOT_NORMALIZED")
    if ledger.get("diagnostics") not in ("","NATIVE_PARSER_AND_EVIDENCE_PENDING"):
        diagnostics.append("UNRESOLVED_LEDGER_DIAGNOSTICS")
    frm=endpoint_map.get(start);to=endpoint_map.get(end)
    if not frm or not to:diagnostics.append("UNRESOLVED_CANONICAL_ENDPOINT")
    elif not frm.get("id") or not to.get("id") or frm.get("kind")!=to.get("kind") or not frm["kind"].endswith("Definition"):
        diagnostics.append("INCOMPATIBLE_CANONICAL_DEFINITION")
    if not str(source.get("ea_guid") or "").strip():diagnostics.append("MISSING_SOURCE_GUID")
    if diagnostics:return {"status":"review","diagnostics":sorted(set(diagnostics)),"relationship":None,"native_certified":False}
    return {"status":"candidate","diagnostics":[],"relationship":{
        "kind":"specialization","fromId":frm["id"],"toId":to["id"],
        "direction":"subtype-to-supertype","sourceRef":source["ea_guid"]
    },"native_certified":False}
