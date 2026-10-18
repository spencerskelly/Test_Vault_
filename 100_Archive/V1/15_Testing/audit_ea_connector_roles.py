"""Read-only EA connector orientation and ownership evidence audit."""
import collections
import pathlib
import sqlite3

def audit(path):
    c=sqlite3.connect('file:'+str(pathlib.Path(path).resolve())+'?mode=ro',uri=True)
    c.row_factory=sqlite3.Row
    try:
        counts=collections.Counter()
        kinds=collections.Counter()
        query="""SELECT Connector_Type,Direction,Start_Object_ID,End_Object_ID,
        SourceIsAggregate,DestIsAggregate,SourceRole,DestRole,SourceCard,DestCard
        FROM t_connector ORDER BY Connector_ID"""
        for row in c.execute(query):
            r=dict(row)
            t=r["Connector_Type"] or "<missing>"
            kinds[t]+=1
            direction=r["Direction"] or "<missing>"
            if direction!="Source -> Destination": counts["direction_not_explicit"]+=1
            if r["Start_Object_ID"]==r["End_Object_ID"]:counts["self_endpoint"]+=1
            if t=="Generalization" and direction!="Source -> Destination":
                counts["generalization_direction_unattested"]+=1
            if t=="Aggregation":
                ends=(r["SourceIsAggregate"],r["DestIsAggregate"])
                if ends==(0,2):counts["aggregation_composite_dest"]+=1
                elif ends==(2,0):counts["aggregation_composite_source"]+=1
                elif ends in ((0,1),(1,0)):counts["aggregation_shared"]+=1
                else:counts["aggregation_flags_ambiguous"]+=1
                if not (r["SourceRole"] or r["DestRole"]):
                    counts["aggregation_no_explicit_roles"]+=1
                if not (r["SourceCard"] or r["DestCard"]):
                    counts["aggregation_no_explicit_cardinality"]+=1
        return {"schema":"mdse-ea-connector-role-audit/1","connectors":sum(kinds.values()),
            "byType":dict(sorted(kinds.items())),"diagnostics":dict(sorted(counts.items())),
            "nativeCertified":0,"status":"EVIDENCE_ONLY"}
    finally:c.close()
