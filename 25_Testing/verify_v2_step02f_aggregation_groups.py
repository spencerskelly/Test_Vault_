#!/usr/bin/env python3
"""Read-only aggregate verification for approved STEP-02F aggregation groups.
Uses only t_object and t_connector; no source rows or diagram data are emitted.
"""
import argparse,collections,json,pathlib,sqlite3
EXPECTED={'PartUsageCandidate':1959,'ActionUsageCandidate':148,'StateUsageCandidate':76,'UseCaseUsageCandidate':10,'ItemUsageCandidate':6,'MDSEChangeHierarchy':12,'flagLinkCandidate':56}
def analyze(path):
    db=sqlite3.connect(pathlib.Path(path).resolve().as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
    objects={r['Object_ID']:(r['Object_Type'],r['Stereotype'] or '') for r in db.execute('SELECT Object_ID,Object_Type,Stereotype FROM t_object')}
    counts=collections.Counter();reasons=collections.Counter();flags=collections.Counter()
    for r in db.execute("SELECT Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate FROM t_connector WHERE Connector_Type='Aggregation'"):
        v=(r['SourceIsAggregate'],r['DestIsAggregate']);flags[str(v)]+=1
        if v[0] in (1,2) and v[1]==0: owner,child=objects[r['Start_Object_ID']],objects[r['End_Object_ID']]
        elif v[1] in (1,2) and v[0]==0: owner,child=objects[r['End_Object_ID']],objects[r['Start_Object_ID']]
        else: raise ValueError('AMBIGUOUS_AGGREGATION_OWNERSHIP')
        types=(owner[0],child[0])
        if types==('Change','Change'): group='MDSEChangeHierarchy'
        elif types==('Activity','Activity'): group='ActionUsageCandidate'
        elif types==('State','State'): group='StateUsageCandidate'
        elif types==('UseCase','UseCase'): group='UseCaseUsageCandidate'
        elif types==('Signal','Signal'): group='ItemUsageCandidate'
        elif all(t in ('Class','Object','Actor') for t in types):
            if 'Business Line' in (owner[1],child[1]): group='flagLinkCandidate';reasons['BusinessLineEndpoint']+=1
            elif any('Interface' in s for s in (owner[1],child[1])): group='flagLinkCandidate';reasons['InterfaceEndpoint']+=1
            else: group='PartUsageCandidate'
        else: group='flagLinkCandidate';reasons['MixedEndpointKinds']+=1
        counts[group]+=1
    return {'schema':'mdse-v2-step02f-aggregation-audit/1','status':'MATCHED_PRIOR_APPROVED_AGGREGATE' if dict(counts)==EXPECTED else 'REVIEW_REQUIRED','groups':dict(sorted(counts.items())),'flag_reason_counts':dict(sorted(reasons.items())),'aggregation_flags':dict(sorted(flags.items())),'total':sum(counts.values()),'native_certified':0,'ea_diagrams_processed':0,'source_rows_exported':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('qeax');a=p.parse_args();result=analyze(a.qeax)
    print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='MATCHED_PRIOR_APPROVED_AGGREGATE' else 1)
