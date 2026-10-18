#!/usr/bin/env python3
"""Read-only QEAX connector reconciliation; writes local-only source ledger."""
import argparse,sqlite3,csv,json,hashlib,collections,pathlib
KIND={'Requirement':'RequirementDefinition','Activity':'ActionDefinition','Action':'ActionUsage','State':'StateDefinition','Class':'PartDefinition','Part':'PartUsage','UseCase':'UseCaseDefinition','Signal':'ItemDefinition','InformationItem':'ItemDefinition','Actor':'PartDefinition','Object':'PartUsage','Port':'PortUsage','Constraint':'ConstraintDefinition'}
EXCEPT={'Note','Text','Boundary','Decision','Synchronization','StateNode','Issue','Change','Artifact','Package','Trigger','Sequence'}
BASE={'Generalization','Abstraction:allocate','Aggregation','Dependency:satisfy','Realisation','Dependency:refine','Dependency','Dependency:trace','Abstraction:trace','Abstraction:Refine'}
REVIEW={'Association','UseCase:extend','ControlFlow','Dependency:deriveReqt','UseCase:include','Sequence','StateFlow','Nesting','Usage','Dependency:verify','Dependency:RecoveryRequirement','Abstraction:Derive','Usage:Responsibility','Realisation:deriveReqt'}
EVIDENCE={'NoteLink','Connector'}
def family(t,s):return t+(':'+s if s else '')
def classify(o):
 if not o:return None
 t,s=o
 if t in EXCEPT or (t=='Class' and s=='Business Line'):return None
 if t=='Activity' and s=='testCase':return 'VerificationCaseDefinition'
 if t=='Class' and 'Interface' in (s or ''):return 'InterfaceDefinition'
 return KIND.get(t)
def disposition(c,a,b):
 t,s,direction,srcagg,dstagg,sc,dc=c
 key=family(t,s);kt,ku=classify(a),classify(b);reasons=[]
 if not kt or not ku:reasons.append('UNRESOLVED_ENDPOINT_KIND')
 if not direction or direction.strip() in ('','Unspecified'):reasons.append('UNVERIFIED_DIRECTION')
 if key in EVIDENCE:return 'evidence_only',['NON_SEMANTIC_CONNECTOR']+reasons,None
 if key in REVIEW:return 'deferred_review',['SEMANTIC_REVIEW_REQUIRED']+reasons,None
 if key not in BASE:return 'deferred_review',['UNKNOWN_FAMILY']+reasons,None
 if key in {'Dependency:refine','Dependency:trace','Abstraction:trace','Abstraction:Refine'}:return 'deferred_review',['TRACE_REFINE_REVIEW']+reasons,'DEPENDENCY-TRACE-REFINE'
 if key in {'Aggregation','Realisation'}:return 'deferred_review',['OWNERSHIP_OR_REALISATION_REVIEW']+reasons,'AGG-OWNED' if key=='Aggregation' else 'REAL-REQ_OR_OBJECT'
 if key=='Generalization':
  if not (kt and ku and kt.endswith('Definition') and ku.endswith('Definition')):reasons.append('ENDPOINT_MISMATCH')
  reasons.append('EA_GENERALIZATION_ORIENTATION_NOT_ATTESTED')
  return 'deferred_review',reasons,'GENERALIZE'
 if key=='Abstraction:allocate':
  if {kt,ku}&{'ActionDefinition','ActionUsage'}:rule='ALLOC-PERFORM'
  elif {kt,ku}&{'StateDefinition','StateUsage'}:rule='ALLOC-EXHIBIT'
  else:rule='ALLOC-GENERIC'
  return 'deferred_review',['ALLOCATION_ROLE_UNATTESTED']+reasons,rule
 if key=='Dependency:satisfy':return 'deferred_review',['SATISFY_DIRECTION_UNATTESTED']+reasons,'SATISFY'
 if key=='Dependency':return ('deferred_review' if reasons else 'candidate_only'),reasons+['NATIVE_PARSER_NOT_VERIFIED'],'DEPENDENCY'
 return 'deferred_review',['MISSING_RULE']+reasons,None
def run(src,out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 con=sqlite3.connect('file:'+str(pathlib.Path(src).resolve())+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
 objects={r['Object_ID']:(r['Object_Type'],r['Stereotype'] or '') for r in con.execute('SELECT Object_ID,Object_Type,Stereotype FROM t_object')}
 summary=collections.Counter();diagnostics=collections.Counter();families=collections.Counter()
 headers=['source_pk','source_guid','source_family','source_type','target_type','source_kind','target_kind','raw_direction','disposition','rule_id','diagnostics']
 with (out/'connector_disposition_ledger.csv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=headers);wr.writeheader()
  q='SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate,SourceCard,DestCard FROM t_connector ORDER BY Connector_ID'
  for r in con.execute(q):
   a=objects.get(r['Start_Object_ID']);b=objects.get(r['End_Object_ID']);fam=family(r['Connector_Type'] or '',r['Stereotype'] or '')
   disp,issues,rule=disposition((r['Connector_Type'],r['Stereotype'] or '',r['Direction'],r['SourceIsAggregate'],r['DestIsAggregate'],r['SourceCard'],r['DestCard']),a,b)
   issues=sorted(set(issues));summary[disp]+=1;families[fam]+=1;diagnostics.update(issues)
   wr.writerow(dict(source_pk=r['Connector_ID'],source_guid=r['ea_guid'],source_family=fam,source_type=family(*(a or ('MISSING',''))),target_type=family(*(b or ('MISSING',''))),source_kind=classify(a) or '',target_kind=classify(b) or '',raw_direction=r['Direction'],disposition=disp,rule_id=rule or '',diagnostics=';'.join(issues)))
 totals={'fixture_sha256':hashlib.sha256(pathlib.Path(src).read_bytes()).hexdigest(),'connector_count':sum(summary.values()),'object_count':len(objects),'dispositions':dict(summary),'diagnostics':dict(diagnostics),'family_counts':dict(families),'native_accepted':0,'caution':'Candidate only is not native acceptance. EA direction and semantic role attestation, ownership and parser remain gated.'}
 (out/'aggregate_summary.json').write_text(json.dumps(totals,indent=2)+'\n')
 assert totals['connector_count']==con.execute('select count(*) from t_connector').fetchone()[0]
 return totals
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qeax',required=True);p.add_argument('--out',required=True);a=p.parse_args();t=run(a.qeax,a.out);print(json.dumps({k:v for k,v in t.items() if k!='family_counts'},indent=2))
