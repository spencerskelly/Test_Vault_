#!/usr/bin/env python3
"""Read-only source-faithful EA object/connector graph baseline; NOT SysML translation."""
import argparse, hashlib, json, sqlite3
from pathlib import Path

def export(qeax, destination):
    src=Path(qeax).resolve(); out=Path(destination).resolve()
    if out == src or src in out.parents: raise ValueError('Output must be separate from QEAX')
    if out.exists() and any(out.iterdir()): raise ValueError('Output directory must be empty or absent')
    out.mkdir(parents=True,exist_ok=True)
    db=sqlite3.connect(src.as_uri()+'?mode=ro',uri=True)
    try:
        if db.execute('PRAGMA quick_check').fetchone()[0]!='ok': raise ValueError('QEAX integrity check failed')
        obj_cols=[r[1] for r in db.execute('PRAGMA table_info(t_object)')]
        con_cols=[r[1] for r in db.execute('PRAGMA table_info(t_connector)')]
        objects=db.execute('SELECT * FROM t_object ORDER BY Object_ID')
        ids=set(); node_count=0
        with (out/'nodes.jsonl').open('w',encoding='utf8') as f:
            for row in objects:
                raw=dict(zip(obj_cols,row)); oid=raw['Object_ID']; guid=raw['ea_guid']
                if oid in ids or oid is None or not guid: raise ValueError('Invalid or duplicate EA object identity')
                ids.add(oid); node_count+=1
                node={'id':str(oid),'eaObjectID':oid,'eaGUID':guid,'name':raw.get('Name'),'type':raw.get('Object_Type'),'stereotype':raw.get('Stereotype'),'source':{'table':'t_object','row':raw}}
                f.write(json.dumps(node,ensure_ascii=False,default=str)+'\n')
        seen=set(); edge_count=0
        with (out/'edges.jsonl').open('w',encoding='utf8') as f:
            for row in db.execute('SELECT * FROM t_connector ORDER BY Connector_ID'):
                raw=dict(zip(con_cols,row)); cid=raw['Connector_ID']; a=raw['Start_Object_ID']; b=raw['End_Object_ID']
                if cid is None or cid in seen: raise ValueError('Invalid or duplicate connector identity')
                if a not in ids or b not in ids: raise ValueError('Broken connector endpoint')
                seen.add(cid); edge_count+=1
                edge={'id':str(cid),'source':str(a),'target':str(b),'eaGUID':raw['ea_guid'],'type':raw.get('Connector_Type'),'stereotype':raw.get('Stereotype'),'sourceData':{'table':'t_connector','row':raw}}
                f.write(json.dumps(edge,ensure_ascii=False,default=str)+'\n')
        with src.open('rb') as source_file:
            source_hash=hashlib.file_digest(source_file,'sha256').hexdigest()
        summary={'status':'source_faithful_baseline_only','source_objects':node_count,'source_connectors':edge_count,'diagram_imported':False,'semantics_translated':False,'review_flags_applied':False,'qeax_sha256':source_hash}
        (out/'export_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
        return summary
    finally: db.close()

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('qeax');p.add_argument('output_dir');a=p.parse_args()
    print(json.dumps(export(a.qeax,a.output_dir),indent=2))
