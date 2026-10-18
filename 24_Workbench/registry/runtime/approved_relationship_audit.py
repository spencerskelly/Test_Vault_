#!/usr/bin/env python3
"""Read-only EA relationship-family audit. Never write model rows into methods repo."""
import argparse, collections, csv, hashlib, json, pathlib, sqlite3
POLICIES={
'Generalization':'specialization','Abstraction:allocate':'allocation','Aggregation':'owned_part_usage_review',
'Dependency:satisfy':'satisfy','Realisation':'realisation_typed_review','Dependency:refine':'refinement',
'Dependency':'dependency','Dependency:trace':'trace_dependency','Association':'connection_review',
'UseCase:extend':'optional_case_usage','ControlFlow':'succession','Dependency:deriveReqt':'derivation',
'NoteLink':'mdse_yaml_link','UseCase:include':'required_case_usage','Sequence':'reference_view',
'StateFlow':'state_transition','Nesting':'nesting_review','Usage':'dependency',
'Dependency:verify':'verification','Dependency:RecoveryRequirement':'derivation','Connector':'port_connection_review',
'Abstraction:Derive':'derivation','Abstraction:trace':'trace_dependency','Usage:Responsibility':'allocation_review',
'Abstraction:Refine':'refinement','Realisation:deriveReqt':'derivation_review'}
REVIEW={v for v in POLICIES.values() if v.endswith('_review')}
NON_NATIVE={'mdse_yaml_link','reference_view'}
def family(r):
 return (r['Connector_Type'] or '')+(':'+r['Stereotype'] if r['Stereotype'] else '')
def kind(obj):
 if obj is None:return 'missing'
 t,s=obj
 if t=='Requirement':return 'requirement'
 if t=='Activity':return 'verification' if s=='testCase' else 'action'
 if t=='Action':return 'action'
 if t=='UseCase':return 'usecase'
 if t in ('State','StateNode'):return 'state'
 if t=='Port':return 'port'
 if t=='Part':return 'flowproperty' if s=='FlowProperty' else 'partusage'
 if t=='Signal':return 'attribute' if s=='Software Parameter' else 'item'
 if t in ('Class','Object','Actor'):return 'part'
 return 'other'
def evaluate(row,objs):
 f=family(row);p=POLICIES.get(f);a=kind(objs.get(row['Start_Object_ID']));b=kind(objs.get(row['End_Object_ID']));issues=[]
 if p is None:return 'error','UNMAPPED_FAMILY',['UNMAPPED_FAMILY'],a,b
 if a=='missing' or b=='missing':issues.append('MISSING_ENDPOINT')
 if not row['Direction'] or row['Direction'].strip().lower()=='unspecified':issues.append('SOURCE_DIRECTION_UNATTESTED')
 if p in NON_NATIVE:return 'evidence_only',p,issues,a,b
 if p in REVIEW:issues.append('SEMANTIC_EVIDENCE_REQUIRED')
 if p=='specialization' and (a not in ('part','requirement','action','state','item','usecase') or a!=b):issues.append('SPECIALIZATION_KIND_REVIEW')
 if p=='derivation' and (a!='requirement' or b!='requirement'):issues.append('REQUIREMENT_ENDPOINT_REVIEW')
 if p=='verification' and {a,b}!={'verification','requirement'}:issues.append('VERIFY_ENDPOINT_REVIEW')
 if p in ('required_case_usage','optional_case_usage') and (a!='usecase' or b!='usecase'):issues.append('CASE_ENDPOINT_REVIEW')
 if p=='state_transition' and (a!='state' or b!='state'):issues.append('STATE_ENDPOINT_REVIEW')
 if p=='port_connection_review' and (a!='port' or b!='port'):issues.append('PORT_ENDPOINT_REVIEW')
 if p=='succession' and (a!='action' or b!='action'):issues.append('ACTION_ENDPOINT_REVIEW')
 return ('deferred_review' if issues else 'candidate_only'),p,issues,a,b
def run(src,out):
 src=pathlib.Path(src);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect('file:'+str(src.resolve())+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
 objs={r['Object_ID']:(r['Object_Type'],r['Stereotype'] or '') for r in c.execute('select Object_ID,Object_Type,Stereotype from t_object')}
 counts=collections.Counter();families=collections.Counter();diagnostics=collections.Counter()
 with (out/'PRIVATE_connector_reconciliation.csv').open('w',newline='') as f:
  cols=['source_pk','source_guid','source_family','native_candidate','start_kind','end_kind','raw_direction','disposition','diagnostics']
  w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
  for r in c.execute('select Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID from t_connector order by Connector_ID'):
   disposition,policy,issues,a,b=evaluate(r,objs);counts[disposition]+=1;families[family(r)]+=1;diagnostics.update(issues)
   w.writerow(dict(source_pk=r['Connector_ID'],source_guid=r['ea_guid'],source_family=family(r),native_candidate=policy,start_kind=a,end_kind=b,raw_direction=r['Direction'],disposition=disposition,diagnostics=';'.join(issues)))
 total=sum(counts.values());assert total==c.execute('select count(*) from t_connector').fetchone()[0]
 summary=dict(fixture_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),connectors=total,families=len(families),unmapped_families=sorted(set(families)-set(POLICIES)),dispositions=dict(counts),diagnostics=dict(diagnostics),native_accepted=0,note='Candidate-only is not native acceptance; trusted role evidence and parser pending.')
 (out/'aggregate_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 return summary
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qeax',required=True);p.add_argument('--out',required=True);a=p.parse_args();print(json.dumps(run(a.qeax,a.out),indent=2))
