"""Evaluate EA stereotype candidates without native acceptance."""
import collections,json,pathlib,sqlite3
def classify(typ,stereo,rules):
    exact=[r for r in rules if r["type"]==typ and r["stereotype"]==(stereo or "")]
    broad=[r for r in rules if r["type"]==typ and r["stereotype"]=="*"]
    return (exact or broad or [None])[0]
def audit(db,registry):
    config=json.loads(pathlib.Path(registry).read_text())
    if config["nativeEmissionAuthorized"] is not False:raise ValueError("UNSAFE_TAXONOMY")
    c=sqlite3.connect("file:"+str(pathlib.Path(db).resolve())+"?mode=ro",uri=True)
    try:
        objects={i:(t,s or "") for i,t,s in c.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        counts=collections.Counter()
        for st,en,sflag,dflag,direction,ctype in c.execute(
            "SELECT Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate,Direction,Connector_Type FROM t_connector"):
            if ctype!="Aggregation":continue
            a=classify(*objects[st],config["rules"]) if st in objects else None
            b=classify(*objects[en],config["rules"]) if en in objects else None
            if st==en:category="self_reference_review"
            elif not a or not b:category="unclassified_endpoint"
            elif a["status"]=="separate_behavior_review" or b["status"]=="separate_behavior_review":category="behavior_nesting_review"
            elif "port" in a["status"] or "interface" in a["status"] or "port" in b["status"] or "interface" in b["status"]:category="port_interface_review"
            elif a["kind"] not in ("PartDefinition","PartUsage") or b["kind"] not in ("PartDefinition","PartUsage"):category="other_endpoint_review"
            elif (sflag,dflag) not in ((0,2),(2,0)):category="shared_or_ambiguous_ownership"
            elif direction!="Source -> Destination":category="direction_review"
            else:category="expanded_part_ownership_candidate"
            counts[category]+=1
        return {"schema":"mdse-ea-stereotype-ownership-aggregate/1","totalAggregations":sum(counts.values()),
                "categories":dict(sorted(counts.items())),"nativeCertified":0}
    finally:c.close()
