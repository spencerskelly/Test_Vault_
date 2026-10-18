"""Read-only EA GUID and parent chain integrity; aggregate-only result."""
import sqlite3
from pathlib import Path

SOURCES=(("element","t_object","Object_ID","ParentID"),
         ("package","t_package","Package_ID","Parent_ID"),
         ("connector","t_connector","Connector_ID",None))

def parent_audit(pairs):
    parents=dict(pairs)
    missing=sum(p not in parents for p in parents.values() if p not in (None,0))
    self_links=sum(n==p for n,p in parents.items())
    complete=set()
    cycles=set()
    for origin in parents:
        path={}
        n=origin
        while n in parents and n not in complete and n not in path:
            path[n]=len(path)
            n=parents[n]
        if n in path:
            cycle=list(path)[path[n]:]
            cycles.add(tuple(sorted(cycle)))
        complete.update(path)
    return {"unresolvedParents":missing,"selfParentLinks":self_links,
            "parentCycles":len(cycles)}

def audit(db):
    con=sqlite3.connect("file:"+str(Path(db).resolve())+"?mode=ro",uri=True)
    try:
        results={}
        for kind,table,primary,parent in SOURCES:
            count,missing_guids=con.execute(
                f"SELECT COUNT(*), SUM(CASE WHEN ea_guid IS NULL OR TRIM(ea_guid)='' THEN 1 ELSE 0 END) FROM {table}").fetchone()
            duplicates=con.execute(
                f"SELECT COUNT(*) FROM (SELECT ea_guid FROM {table} WHERE ea_guid IS NOT NULL AND TRIM(ea_guid)<>'' GROUP BY ea_guid HAVING COUNT(*)>1)").fetchone()[0]
            item={"total":count,"blankGuids":missing_guids or 0,"duplicateGuidGroups":duplicates}
            if parent:
                item.update(parent_audit(con.execute(f"SELECT {primary},{parent} FROM {table}")))
            results[kind]=item
        violations=sum(v for record in results.values() for k,v in record.items() if k!="total")
        return {"schema":"mdse-ea-identity-containment-audit/1",
                "status":"PASS" if violations==0 else "REVIEW_REQUIRED",
                "categories":results,"violationCount":violations,"nativeCertified":0}
    finally:con.close()
