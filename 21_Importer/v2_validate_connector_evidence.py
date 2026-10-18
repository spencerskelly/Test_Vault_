"""Read-only validation of bounded EA connector-end evidence."""
import collections,json,pathlib,re,sqlite3
CARD=re.compile(r"^(?:0|[1-9][0-9]*)(?:\.\.(?:\*|0|[1-9][0-9]*))?$|^\*$")
def multiplicity(value):
    if value is None or not str(value).strip():return "absent"
    s=str(value).strip()
    if not CARD.fullmatch(s):return "invalid"
    if ".." in s:
        a,b=s.split("..")
        if b!="*" and int(a)>int(b):return "invalid"
    return "valid"
def audit(source,limit=1000):
    if not 1<=limit<=20000:raise ValueError("INVALID_LIMIT")
    p=pathlib.Path(source).resolve()
    if not p.is_file():raise ValueError("SOURCE_NOT_FOUND")
    counts=collections.Counter()
    with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True) as db:
        oc={r[1] for r in db.execute("PRAGMA table_info(t_object)")}
        cc={r[1] for r in db.execute("PRAGMA table_info(t_connector)")}
        if not {"Object_ID","Object_Type","Stereotype","Classifier","Classifier_guid"}.issubset(oc) or not {"Connector_ID","Connector_Type","SourceCard","DestCard","SourceIsAggregate","DestIsAggregate","Start_Object_ID","End_Object_ID"}.issubset(cc):
            raise ValueError("UNSUPPORTED_SOURCE_SCHEMA")
        objects={r[0]:r[1:] for r in db.execute("SELECT Object_ID,Object_Type,Stereotype,Classifier,Classifier_guid FROM t_object")}
        rows=db.execute("SELECT Connector_Type,SourceCard,DestCard,SourceIsAggregate,DestIsAggregate,Start_Object_ID,End_Object_ID FROM t_connector ORDER BY Connector_ID LIMIT ?",(limit,)).fetchall()
    for kind,sc,dc,sa,da,start,end in rows:
        if start not in objects or end not in objects:counts["missing_endpoint"]+=1
        for side,v in (("source",sc),("destination",dc)):
            counts["multiplicity_"+side+"_"+multiplicity(v)]+=1
        if kind=="Aggregation":
            if sa in (1,2) and da in (1,2):counts["aggregation_both_ends_marked_review"]+=1
            elif sa in (1,2) or da in (1,2):counts["aggregation_single_end_flag_"+str(sa if sa in (1,2) else da)]+=1
            else:counts["aggregation_no_end_flag_review"]+=1
        for eid in (start,end):
            obj=objects.get(eid)
            if obj and obj[0]=="Port":
                _,st,cls,guid=obj
                if not (st or "").strip():counts["port_stereotype_absent"]+=1
                if not cls and not (guid or "").strip():counts["port_classifier_absent"]+=1
    return {"schema":"mdse-v2-evidence-validity/1","selected_connectors":len(rows),"counts":dict(sorted(counts.items())),"aggregation_semantics":"unverified","port_kind":"unverified","native_relationships_emitted":0,"source_modified":False}
