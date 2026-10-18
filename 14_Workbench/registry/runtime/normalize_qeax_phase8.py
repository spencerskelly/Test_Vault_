"""Read-only Phase 8 EA normalization. Local ledger only; no SysML emitter."""
import sqlite3,csv,json,collections,pathlib,argparse,os,tempfile,shutil
K={'Class':'PartDefinition','Object':'PartUsage','Part':'PartUsage','Activity':'ActionDefinition','Action':'ActionUsage','State':'StateDefinition','Requirement':'RequirementDefinition','UseCase':'UseCaseDefinition','Signal':'ItemDefinition','InformationItem':'ItemDefinition','Port':'PortUsage'}
def kind(t,s):
 if t in ('Note','Boundary','Text','Decision','Synchronization','StateNode','Issue','Change','Artifact','Trigger') or (t=='Class' and s=='Business Line'):return None
 if t=='Activity' and s=='testCase':return 'VerificationCaseDefinition'
 if t=='Class' and 'Interface' in (s or ''):return 'InterfaceDefinition'
 return K.get(t)
def decide(row,a,b,registered):
 t,s=row['Connector_Type'],row['Stereotype'] or ''
 fam=t+(':'+s if s else '')
 ak=kind(*a) if a else None;bk=kind(*b) if b else None
 start,end=row['Start_Object_ID'],row['End_Object_ID']
 rule=None;role='unknown';status='deferred_review';diag=[]
 if not ak or not bk:diag.append('UNRESOLVED_ENDPOINT_KIND')
 if row['Direction']!='Source -> Destination':diag.append('DIRECTION_NOT_EXPLICIT')
 if fam=='Generalization':
  rule='GENERALIZE';role='source-subtype-to-destination-supertype'
  if ak and bk and ak==bk and ak.endswith('Definition') and row['Direction']=='Source -> Destination':status='orientation_normalized'
  else:diag.append('SPECIALIZATION_REQUIRES_REVIEW')
 elif fam=='Aggregation':
  rule='AGG-OWNED';src,dst=row['SourceIsAggregate'],row['DestIsAggregate']
  if (src,dst)==(0,2):start,end=end,start;role='destination-owns-source';status='owner_endpoint_identified'
  elif (src,dst)==(2,0):role='source-owns-destination';status='owner_endpoint_identified'
  elif (src,dst) in ((0,1),(1,0)):diag.append('SHARED_NOT_COMPOSITE')
  else:diag.append('AGGREGATION_FLAGS_UNKNOWN')
  if ak not in ('PartDefinition','PartUsage') or bk not in ('PartDefinition','PartUsage'):status='deferred_review';diag.append('NON_PART_AGGREGATION')
 elif fam=='Abstraction:allocate':
  if ak in ('ActionDefinition','ActionUsage') and bk in ('PartDefinition','PartUsage'):
   rule='ALLOC-PERFORM';start,end=end,start;role='object-performs-action';status='role_normalized'
  elif ak in ('StateDefinition','StateUsage') and bk in ('PartDefinition','PartUsage'):
   rule='ALLOC-EXHIBIT';start,end=end,start;role='object-exhibits-state';status='role_normalized'
  else:rule='ALLOC-GENERIC';diag.append('ALLOCATION_ROLE_REVIEW')
 elif fam=='Realisation':
  if bk=='RequirementDefinition' and ak in ('PartDefinition','PartUsage','ActionDefinition','ActionUsage'):
   rule='REAL-REQ';start,end=end,start;role='requirement-to-implementation';status='role_normalized'
  else:rule='REAL-OBJECT';diag.append('REALISATION_ROLE_REVIEW')
 elif fam=='Dependency':rule='DEPENDENCY';status='family_candidate'
 elif fam=='Dependency:satisfy':rule='SATISFY';diag.append('SATISFY_DIRECTION_REVIEW')
 elif fam in registered:diag.append('REGISTRY_REVIEW_OR_EVIDENCE_ONLY')
 else:diag.append('UNKNOWN_FAMILY')
 if status!='deferred_review':diag.append('NATIVE_PARSER_AND_EVIDENCE_PENDING')
 return dict(family=fam,rule=rule or '',role=role,status=status,normalized_from=start,normalized_to=end,source_kind=ak or '',target_kind=bk or '',diagnostics=sorted(set(diag)))
def reconcile(qeax,registry,output):
 con=sqlite3.connect('file:'+str(pathlib.Path(qeax).resolve())+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
 objs={r['Object_ID']:(r['Object_Type'],r['Stereotype'] or '') for r in con.execute('SELECT Object_ID,Object_Type,Stereotype FROM t_object')}
 families={x['family'] for x in json.loads(pathlib.Path(registry).read_text())['families']}
 output=pathlib.Path(output);output.mkdir(parents=True,exist_ok=True)
 status=collections.Counter();diagnostics=collections.Counter();rules=collections.Counter()
 with (output/'local_only_phase8_ledger.csv').open('w',newline='') as f:
  headers=['source_pk','source_guid','raw_from','raw_to','family','rule','role','status','normalized_from','normalized_to','source_kind','target_kind','diagnostics','source_direction','source_role','target_role','source_cardinality','target_cardinality','raw_source_type','raw_source_stereotype','raw_target_type','raw_target_stereotype','source_aggregation_flag','target_aggregation_flag']
  w=csv.DictWriter(f,fieldnames=headers);w.writeheader()
  q='SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate,SourceRole,DestRole,SourceCard,DestCard FROM t_connector ORDER BY Connector_ID'
  for r in con.execute(q):
   x=decide(r,objs.get(r['Start_Object_ID']),objs.get(r['End_Object_ID']),families)
   w.writerow(dict(source_pk=r['Connector_ID'],source_guid=r['ea_guid'],raw_from=r['Start_Object_ID'],raw_to=r['End_Object_ID'],source_direction=r['Direction'],source_role=r['SourceRole'],target_role=r['DestRole'],source_cardinality=r['SourceCard'],target_cardinality=r['DestCard'],raw_source_type=(objs.get(r['Start_Object_ID']) or ('',''))[0],raw_source_stereotype=(objs.get(r['Start_Object_ID']) or ('',''))[1],raw_target_type=(objs.get(r['End_Object_ID']) or ('',''))[0],raw_target_stereotype=(objs.get(r['End_Object_ID']) or ('',''))[1],source_aggregation_flag=r['SourceIsAggregate'],target_aggregation_flag=r['DestIsAggregate'],**{k:(';'.join(v) if isinstance(v,list) else v) for k,v in x.items()}))
   status[x['status']]+=1;rules[x['rule'] or '(none)']+=1;diagnostics.update(x['diagnostics'])
 summary={'total':sum(status.values()),'status':dict(status),'rule_candidates':dict(rules),'diagnostics':dict(diagnostics),'native_certified':0}
 assert summary['total']==con.execute('SELECT COUNT(*) FROM t_connector').fetchone()[0]
 (output/'aggregate_only.json').write_text(json.dumps(summary,indent=2)+'\n')
 return summary
def reconcile_atomic(qeax,registry,output):
 """Publish an all-or-nothing local result directory; never overwrite an existing run."""
 destination=pathlib.Path(output).resolve()
 if destination.exists():raise ValueError('OUTPUT_ALREADY_EXISTS')
 if not destination.parent.is_dir():raise ValueError('OUTPUT_PARENT_MISSING')
 stage=pathlib.Path(tempfile.mkdtemp(prefix='.phase8-incomplete-',dir=destination.parent))
 try:
  summary=reconcile(qeax,registry,stage)
  if summary['native_certified']!=0:raise ValueError('NATIVE_EMISSION_FORBIDDEN')
  os.rename(stage,destination)
  return summary
 finally:
  if stage.exists():shutil.rmtree(stage)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qeax',required=True);p.add_argument('--registry',required=True);p.add_argument('--out',required=True);v=p.parse_args();print(json.dumps(reconcile_atomic(v.qeax,v.registry,v.out),indent=2))
