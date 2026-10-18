#!/usr/bin/env python3
"""Compare every table in a local QEAX against existing EA table disposition policy.

Read-only. Report aggregate diagnostics only, no proprietary rows or source GUIDs.
Historical full-model counts are deliberately NOT applied to reduced QEAX.
"""
import argparse, collections, json, pathlib, sqlite3, sys

def reconcile(db, policy):
    dispositions=policy["tableDispositions"]
    imported=set(policy["expected"]["tables"])
    connection=sqlite3.connect("file:"+str(pathlib.Path(db).resolve())+"?mode=ro",uri=True)
    try:
        if connection.execute("PRAGMA quick_check").fetchone()[0]!="ok":
            raise ValueError("sqlite quick_check failed")
        tables=[n for (n,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        counts={}
        for table in tables:
            quoted='"'+table.replace('"','""')+'"'
            counts[table]=connection.execute("SELECT COUNT(*) FROM "+quoted).fetchone()[0]
    finally:
        connection.close()
    issues=[]
    for table,count in sorted(counts.items()):
        policy_kind=dispositions.get(table)
        if policy_kind is None:
            issues.append({"category":"UNCLASSIFIED_TABLE","table":table,"count":count})
        elif policy_kind=="ignored_must_be_empty" and count:
            issues.append({"category":"FORBIDDEN_NONEMPTY","table":table,"count":count})
        elif policy_kind=="imported" and table not in imported:
            issues.append({"category":"IMPORTED_UNCOUNTED","table":table,"count":count})
    for table in dispositions:
        if table not in counts:
            issues.append({"category":"EXPECTED_TABLE_MISSING","table":table})
    return {
        "schema":"mdse-ea-table-disposition-audit/1",
        "tableCount":len(counts),
        "nonemptyTables":sum(v>0 for v in counts.values()),
        "dispositions":dict(sorted(collections.Counter(dispositions[t] for t in counts if t in dispositions).items())),
        "issueCount":len(issues),"issues":issues,
        "status":"PASS" if not issues else "BLOCKED"
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("qeax",type=pathlib.Path)
    parser.add_argument("policy",type=pathlib.Path)
    parser.add_argument("--out",type=pathlib.Path,help="Optional local JSON report; do not commit source-specific evidence")
    args=parser.parse_args()
    p=json.loads(args.policy.read_text(encoding="utf-8"))
    report=reconcile(args.qeax,p)
    result=json.dumps(report,indent=2)+"\n"
    if args.out:
        args.out.write_text(result,encoding="utf-8")
    print(result,end="")
    return 0 if report["status"]=="PASS" else 1

if __name__=="__main__": sys.exit(main())
