"""Read-only bounded EA end-role, multiplicity and port-classifier evidence."""
import argparse,collections,json,pathlib,sqlite3
C=("Connector_ID","Connector_Type","Stereotype","Direction","Start_Object_ID","End_Object_ID","SourceRole","DestRole","SourceCard","DestCard","SourceContainment","DestContainment","SourceIsAggregate","DestIsAggregate","SourceRoleType","DestRoleType")
O=("Object_ID","Object_Type","Stereotype","Classifier","Classifier_guid","Multiplicity")
def audit(source,limit=100):
    if not 1<=limit<=1000:raise ValueError("INVALID_LIMIT")
    p=pathlib.Path(source).resolve()
    if not p.is_file():raise ValueError("SOURCE_NOT_FOUND")
    with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True) as db:
        for table,cols in (("t_object",O),("t_connector",C)):
            if not set(cols).issubset({r[1] for r in db.execute("PRAGMA table_info("+table+")")}):
                raise ValueError("UNSUPPORTED_SCHEMA:"+table)
        objects={r[0]:r[1:] for r in db.execute("SELECT "+",".join(O)+" FROM t_object")}
        rows=db.execute("SELECT "+",".join(C)+" FROM t_connector ORDER BY Connector_ID LIMIT ?",(limit,)).fetchall()
    counts=collections.Counter()
    for row in rows:
        _,kind,stereo,direction,start,end,srole,drole,scard,dcard,scontain,dcontain,sagg,dagg,srole_type,drole_type=row
        if start not in objects or end not in objects:
            counts["missing_endpoint"]+=1
            continue
        counts["linked_endpoints"]+=1
        for prefix,eid,role,card,contain,aggregate,role_type in (
            ("source",start,srole,scard,scontain,sagg,srole_type),
            ("destination",end,drole,dcard,dcontain,dagg,drole_type)):
            typ,stereotype,classifier,classifier_guid,multiplicity=objects[eid]
            if str(card or "").strip():counts[prefix+"_cardinality_present"]+=1
            if str(role or "").strip():counts[prefix+"_role_present"]+=1
            if str(contain or "").strip().casefold() not in ("","unspecified"):counts[prefix+"_containment_specified"]+=1
            if aggregate in (1,2,"1","2"):counts[prefix+"_aggregation_indicator_present"]+=1
            if str(role_type or "").strip():counts[prefix+"_role_type_present"]+=1
            if typ=="Port":
                counts["port_endpoints"]+=1
                counts["port_stereotype_present" if str(stereotype or "").strip() else "port_stereotype_missing"]+=1
                counts["port_classifier_reference_present" if classifier not in (None,"",0,"0") or str(classifier_guid or "").strip() else "port_classifier_reference_missing"]+=1
                if str(multiplicity or "").strip():counts["port_multiplicity_present"]+=1
        counts["connector_direction_recorded" if str(direction or "").strip() else "connector_direction_missing"]+=1
    return {"schema":"mdse-v2-connector-end-evidence/1","selected_connectors":len(rows),"evidence_counts":dict(sorted(counts.items())),"source_direction":"preserved_uninterpreted","interpretation":"presence_only_not_semantic_validity","native_relationships_emitted":0,"source_modified":False}
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("qeax");ap.add_argument("--limit",type=int,default=100)
    a=ap.parse_args();print(json.dumps(audit(a.qeax,a.limit),indent=2))
