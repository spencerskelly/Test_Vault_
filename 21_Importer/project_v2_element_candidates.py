#!/usr/bin/env python3
"""Project a bounded EA/QEAX slice onto approved V2 candidate element rules.
Output is review evidence, not native SysML. No source identifiers printed.
"""
import argparse,collections,json,pathlib,sqlite3,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
RULES=ROOT/"24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json"
def select_rule(rules,ea_type,stereo):
    exact=[r for r in rules if r["eaType"]==ea_type and r["stereotype"].casefold()==stereo.casefold()]
    if len(exact)>1:raise ValueError("AMBIGUOUS_EXACT_RULE")
    if exact:return exact[0]
    wild=[r for r in rules if r["eaType"]==ea_type and r["stereotype"]=="*"]
    if len(wild)>1:raise ValueError("AMBIGUOUS_WILDCARD_RULE")
    return wild[0] if wild else None
def project(db_path,limit=20,registry_path=RULES):
    if not 1<=limit<=100:raise ValueError("INVALID_LIMIT")
    path=pathlib.Path(db_path).resolve()
    if not path.is_file():raise ValueError("SOURCE_NOT_FOUND")
    registry=json.loads(pathlib.Path(registry_path).read_text(encoding="utf-8"))
    if registry.get("schema")!="mdse-v2-semantic-rules/0.2" or registry.get("automaticNativeEmission") is not False:
        raise ValueError("INVALID_OR_UNSAFE_REGISTRY")
    rules=registry["elementRules"]
    if any(r.get("emission")!="deferred_pending_parser" for r in rules):raise ValueError("UNEXPECTED_EMISSION_AUTHORIZATION")
    with sqlite3.connect(path.as_uri()+"?mode=ro",uri=True) as db:
        cols={row[1] for row in db.execute("PRAGMA table_info(t_object)")}
        if not {"Object_ID","Object_Type","Stereotype"}.issubset(cols):
            raise ValueError("UNSUPPORTED_SOURCE_SCHEMA")
        rows=db.execute("SELECT Object_Type,Stereotype FROM t_object ORDER BY Object_ID LIMIT ?",(limit,)).fetchall()
    counts=collections.Counter()
    for ea_type,stereo in rows:
        rule=select_rule(rules,ea_type or "",stereo or "")
        counts["review:"+rule["target"] if rule else "review:UNMATCHED"]+=1
    return {"schema":"mdse-v2-element-candidate-review/1","source_rows":len(rows),
       "candidate_targets":dict(sorted(counts.items())),"deferred_rows":len(rows),
       "native_declarations_emitted":0,"approved_rules_modified":False}
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("qeax");ap.add_argument("--limit",type=int,default=20)
    args=ap.parse_args()
    try:print(json.dumps(project(args.qeax,args.limit),indent=2))
    except (ValueError,OSError,sqlite3.DatabaseError) as ex:
        print(json.dumps({"status":"BLOCKED","reason":str(ex)}),file=sys.stderr);sys.exit(1)
