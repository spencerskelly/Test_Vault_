"""Stream a private EA evidence manifest atomically. No model rows in stdout."""
import argparse, collections, hashlib, json, os, pathlib, sqlite3, tempfile

TABLES={"element":("t_object","Object_ID"),"connector":("t_connector","Connector_ID"),
        "package":("t_package","Package_ID"),"tag":("t_objectproperties","PropertyID")}
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,default=str)

def write_manifest(db,snapshot,destination):
    db=pathlib.Path(db).resolve()
    destination=pathlib.Path(destination).resolve()
    if not snapshot:raise ValueError("MISSING_SNAPSHOT_ID")
    if destination.exists():raise ValueError("DESTINATION_EXISTS")
    if not destination.parent.is_dir():raise ValueError("PARENT_MISSING")
    conn=sqlite3.connect("file:"+str(db)+"?mode=ro",uri=True)
    conn.row_factory=sqlite3.Row
    fd,path=tempfile.mkstemp(prefix=".source-manifest-",suffix=".tmp",dir=destination.parent)
    counts=collections.Counter()
    seen=set()
    try:
        with os.fdopen(fd,"w",encoding="utf-8") as output:
            for kind,(table,primary) in TABLES.items():
                for row in conn.execute(f"SELECT * FROM {table} ORDER BY {primary}"):
                    raw=dict(row)
                    key=raw[primary]
                    if key is None or (kind,key) in seen:raise ValueError("INVALID_OR_DUPLICATE_ID")
                    seen.add((kind,key))
                    fingerprint=hashlib.sha256(canonical(raw).encode()).hexdigest()
                    record={"schema":"mdse-source-manifest-entry/1","sourceKind":"EA",
                            "snapshotId":snapshot,"recordKind":kind,"sourceKey":str(key),
                            "fingerprint":fingerprint,"disposition":"uninterpreted",
                            "reason":"SOURCE_INGESTED_NOT_TRANSLATED"}
                    output.write(canonical(record)+"\n")
                    counts[kind]+=1
            output.flush()
            os.fsync(output.fileno())
        os.rename(path,destination)
    finally:
        conn.close()
        if os.path.exists(path):os.unlink(path)
    return {"schema":"mdse-source-manifest-aggregate/1","sourceKind":"EA",
            "total":sum(counts.values()),"byKind":dict(sorted(counts.items())),
            "duplicateSourceIdentities":0,"nativeCertified":0}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("db")
    p.add_argument("--snapshot",required=True)
    p.add_argument("--out",required=True)
    a=p.parse_args()
    print(json.dumps(write_manifest(a.db,a.snapshot,a.out),indent=2))
