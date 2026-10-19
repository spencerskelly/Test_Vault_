#!/usr/bin/env python3
"""Read-only QEAX source-row adapter for STEP-04. Writes only to local private output."""
import argparse, sqlite3, json, hashlib, pathlib, collections
import importlib.util

def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def run(qeax,out):
    gate_path=pathlib.Path(__file__).with_name('v2_step04_ledger_gate.py')
    spec=importlib.util.spec_from_file_location('step04gate',gate_path)
    gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
    qeax=pathlib.Path(qeax).resolve();out=pathlib.Path(out).resolve()
    if out==qeax or out.is_relative_to(qeax.parent/'.git'):
        raise ValueError('Unsafe destination')
    out.mkdir(parents=True,exist_ok=True)
    sha=digest(qeax)
    db=sqlite3.connect(qeax.as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
    families=set()
    dest=out/'source_disposition.jsonl'
    with dest.open('w',encoding='utf8') as f:
        for table,pk,typ in [('t_object','Object_ID','Object_Type'),('t_connector','Connector_ID','Connector_Type')]:
            cols={x[1] for x in db.execute('pragma table_info('+table+')')}
            if not {pk,typ,'Stereotype','ea_guid'}<=cols:raise ValueError('QEAX schema mismatch: '+table)
            q=f'SELECT {pk} AS id, ea_guid AS guid,{typ} AS kind,Stereotype AS stereo FROM {table} ORDER BY {pk}'
            for r in db.execute(q):
                kind=(r['kind'] or '').strip();st=(r['stereo'] or '').strip()
                families.add((table,kind,st))
                if table=='t_object' and kind=='Boundary':
                    disp,reason='evidence_only','BOUNDARY_GROUPED_PENDING_TARGET'
                elif table=='t_object' and kind=='Package':
                    disp,reason='excluded_by_policy','FOLDER_ORGANIZATION_PENDING'
                elif table=='t_connector' and kind in {'NoteLink','Connector'}:
                    disp,reason='evidence_only','NON_SEMANTIC_LINK_PENDING_TARGET'
                else:
                    disp,reason='deferred_review','SEMANTIC_TARGET_NOT_EMITTED'
                row=dict(source_system='EA',fixture_hash=sha,source_table=table,
                         source_pk=r['id'],ea_guid=r['guid'],ea_type=kind,
                         ea_stereotype=st,rule_id='STEP04B-CONSERVATIVE',
                         rule_version='1',disposition=disp,evidence='QEAX_SOURCE_ROW',
                         diagnostic_code=reason,
                         operator_action='Resolve through approved mapping and output crosswalk')
                f.write(json.dumps(row,sort_keys=True)+'\n')
    expected={t:db.execute(f'SELECT count(*) FROM {t}').fetchone()[0] for t in ('t_object','t_connector')}
    with dest.open(encoding='utf8') as f:
        report=gate.audit((json.loads(line) for line in f),expected)
    public=dict(source_sha256=sha,ledger_passed=report['passed'],source_counts=expected,
                disposition_counts={k:v for k,v in report['counts'].items() if k.startswith('disposition:')},
                family_counts=len(families),failure_count=len(report['failures']),
                caveat='Accounting only. No native semantic output accepted.')
    (out/'aggregate_summary.json').write_text(json.dumps(public,indent=2)+'\n')
    db.close()
    return public

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--qeax',required=True);p.add_argument('--out',required=True)
    a=p.parse_args();print(json.dumps(run(a.qeax,a.out),indent=2))
