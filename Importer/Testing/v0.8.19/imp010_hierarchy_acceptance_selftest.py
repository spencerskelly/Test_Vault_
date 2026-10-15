#!/usr/bin/env python3
"""Synthetic regression for IMP-010A/B hierarchy acceptance."""
from __future__ import annotations
import csv, json, sqlite3, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
VALIDATOR = HERE / "imp010_hierarchy_acceptance.py"

def guid(n: int) -> str:
    return "{%08X-0000-0000-0000-%012X}" % (n, n)

def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        db = root / "fixture.qeax"
        vault = root / "vault"
        imp = vault / "99_System/11_Import"
        imp.mkdir(parents=True)
        con = sqlite3.connect(db)
        con.execute("create table t_package(Package_ID integer, Parent_ID integer, Name text)")
        con.executemany("insert into t_package values(?,?,?)", [(1,0,"Model"),(2,1,"04 Product Function"),(3,1,"05 Product Design")])
        con.execute("create table t_object(Object_ID integer,Object_Type text,Stereotype text,Name text,ParentID integer,PDATA1 text,PDATA2 text,Classifier integer,Classifier_guid text,ea_guid text,Package_ID integer)")
        rows=[]; carriers=[]; oid=1
        first=None
        for i in range(141):
            o,t,p=oid,oid+1,oid+2; oid+=3
            rows += [(o,"Activity","System Function",f"AOwner{i}",0,None,None,0,None,guid(o),2),(t,"Activity","Hardware Function",f"ATarget{i}",0,None,None,0,None,guid(t),2),(p,"Part",None,None,o,guid(t),None,0,None,guid(p),2)]
            carriers.append((p,o,t,"hasChild","childOf")); first=first or (o,t)
        o,t=first; p=oid; oid+=1
        rows.append((p,"Part",None,None,o,guid(t),None,0,None,guid(p),2)); carriers.append((p,o,t,"hasChild","childOf"))
        for i in range(60):
            o,t,p=oid,oid+1,oid+2; oid+=3
            rows += [(o,"State","System State",f"SOwner{i}",0,None,None,0,None,guid(o),3),(t,"State","System State",f"STarget{i}",0,None,None,0,None,guid(t),3),(p,"Part",None,None,o,guid(t),None,0,None,guid(p),3)]
            carriers.append((p,o,t,"hasChild","childOf"))
        o,t,p=oid,oid+1,oid+2
        rows += [(o,"Class","Hardware Component","ObjectOwner",0,None,None,0,None,guid(o),1),(t,"State","System State","DesignTarget",0,None,None,0,None,guid(t),3),(p,"Part",None,None,o,guid(t),None,0,None,guid(p),1)]
        carriers.append((p,o,t,"hasDesign","designOf"))
        con.executemany("insert into t_object values(?,?,?,?,?,?,?,?,?,?,?)", rows)
        con.commit(); con.close()
        byid={r[0]:r for r in rows}
        with (imp/"Ledger.csv").open("w",newline="",encoding="utf-8") as f:
            w=csv.writer(f); w.writerow(["ea_guid","source_kind","ea_type","ea_name","outcome","rule","uid","id","folded_into_uid"])
            for r in rows:
                obj_id,typ,st,name,parent,pd1,pd2,cl,cg,eg,pkg=r; uid=f"u{obj_id:06d}"
                if typ=="Part":
                    target=next(x for x in rows if x[9]==pd1); tuid=f"u{target[0]:06d}"
                    w.writerow([eg,"element","Part","","folded","W-137/W-149",tuid,"X",tuid])
                else:
                    w.writerow([eg,"element",typ,name,"note","W",uid,"X",""])
        with (imp/"Local Model Source Map.csv").open("w",newline="",encoding="utf-8") as f:
            csv.writer(f).writerow(["source_model_id","source_key","owner_uid","local_id","local_kind","ea_guid","ea_source_kind","ea_owner_guid"])

        # Base templates legitimately repeat an unexpanded Templater uid expression.
        # The real acceptance must ignore those source-template placeholders rather
        # than misdiagnose them as duplicate generated model identities.
        templates = vault/"99_System/05_Templates"
        templates.mkdir(parents=True, exist_ok=True)
        placeholder = '---\nuid: <% tp.file.include("[[Snippet - uid]]") %>\n---\n'
        (templates/"Plan.md").write_text(placeholder, encoding="utf-8")
        (templates/"Document.md").write_text(placeholder, encoding="utf-8")

        rels={}
        for _,o,t,fw,inv in carriers:
            rels.setdefault(o,{}).setdefault(fw,set()).add(t)
            rels.setdefault(t,{}).setdefault(inv,set()).add(o)
        for r in rows:
            if r[1]=="Part":
                continue
            obj_id,_,_,name,*_=r
            lines=["---",f"uid: {json.dumps(f'u{obj_id:06d}')}"]
            for field,targets in rels.get(obj_id,{}).items():
                lines.append(field+":")
                for target_id in sorted(targets):
                    lines.append("  - "+json.dumps(f"[[{byid[target_id][3]}]]"))
            lines += ["---","",f"# {name}",""]
            (vault/f"{name}.md").write_text("\n".join(lines),encoding="utf-8")
        good=subprocess.run([sys.executable,str(VALIDATOR),str(db),str(vault)],capture_output=True,text=True)
        if good.returncode or "RESULT: PASS" not in good.stdout:
            print(good.stdout); print(good.stderr,file=sys.stderr)
            raise SystemExit("valid IMP-010 fixture did not pass")
        victim=vault/"AOwner0.md"
        victim.write_text(victim.read_text(encoding="utf-8").replace('  - "[[ATarget0]]"\n',''),encoding="utf-8")
        bad=subprocess.run([sys.executable,str(VALIDATOR),str(db),str(vault)],capture_output=True,text=True)
        if bad.returncode==0 or "missing hasChild link" not in bad.stdout:
            print(bad.stdout); print(bad.stderr,file=sys.stderr)
            raise SystemExit("missing hierarchy link was not rejected")
    print("v0.8.19 IMP-010A/B hierarchy validator synthetic self-test: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
