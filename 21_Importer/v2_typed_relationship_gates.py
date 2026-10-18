"""Classify typed EA relationship evidence without emitting SysML."""
import collections
import json
import pathlib
import sqlite3

def assess(source, registry, limit=100):
    if not 1 <= limit <= 1000:
        raise ValueError("INVALID_LIMIT")
    rules=json.loads(pathlib.Path(registry).read_text())
    if rules.get("automaticNativeEmission") is not False:
        raise ValueError("UNSAFE_REGISTRY")
    entries=rules["relationshipRules"]
    if any(r.get("emission")!="deferred_pending_evidence_and_parser" for r in entries):
        raise ValueError("UNSAFE_RULE")
    mapping={r["family"]:r for r in entries}
    if len(mapping)!=len(entries):
        raise ValueError("DUPLICATE_RULE")
    result=collections.Counter()
    with sqlite3.connect(pathlib.Path(source).resolve().as_uri()+"?mode=ro",uri=True) as db:
        objects={i:(t or "",s or "") for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        connectors=db.execute("SELECT Connector_Type,Stereotype,Start_Object_ID,End_Object_ID FROM t_connector ORDER BY Connector_ID LIMIT ?",(limit,)).fetchall()
    for kind,stereo,src,dst in connectors:
        if src not in objects or dst not in objects:
            gate="missing_endpoint"
        else:
            family=(kind or "")+":"+(stereo or "")
            rule=mapping.get(family)
            a,b=objects[src],objects[dst]
            if rule is None: gate="unmatched_family"
            elif family=="Generalization:": gate="direction_unverified"
            elif family=="Aggregation:": gate="ownership_and_multiplicity_unverified"
            elif family=="Dependency:deriveReqt":
                gate="derivation_roles_unverified" if a[0]==b[0]=="Requirement" else "invalid_derivation_endpoints"
            elif family=="Dependency:satisfy":
                gate="satisfy_roles_unverified" if (a[0]=="Requirement") != (b[0]=="Requirement") else "invalid_satisfy_endpoints"
            elif family=="Dependency:verify":
                gate="verify_roles_unverified" if (a[0]=="Requirement" and b[0] in ("Activity","UseCase")) or (b[0]=="Requirement" and a[0] in ("Activity","UseCase")) else "invalid_verify_endpoints"
            elif "Port" in (a[0],b[0]):
                gate="port_classifier_and_ownership_unverified"
            else: gate="registry_gate:"+str(rule.get("gate","unspecified"))
        result[gate]+=1
    return {"schema":"mdse-v2-typed-relationship-gates/1","reviewed":len(connectors),
            "gates":dict(sorted(result.items())),"deferred":len(connectors),
            "native_emission":0,"ea_direction_unmodified":True}
