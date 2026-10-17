"""Local-only aggregate source-family audit; never writes model rows."""
import argparse,csv,json,collections,pathlib
def reconcile(registry,path):
    mapping={r['family']:r for r in registry['families']}
    if len(mapping)!=len(registry['families']):raise ValueError('Duplicate family')
    totals=collections.Counter();unknown=set()
    with open(path,newline='') as fh:
        for row in csv.DictReader(fh):
            key=row['connector_type']+':'+row['connector_stereotype']
            disposition=mapping[key]['disposition'] if key in mapping else 'unknown_family'
            totals[(disposition,'patterns')]+=1;totals[(disposition,'connectors')]+=int(row['count'])
            if key not in mapping:unknown.add(key)
    result={'total_patterns':sum(n for (d,k),n in totals.items() if k=='patterns'),'total_connectors':sum(n for (d,k),n in totals.items() if k=='connectors'),'by_disposition':{d:{'patterns':totals[d,'patterns'],'connectors':totals[d,'connectors']} for d in sorted({x for x,y in totals})},'unknown_families':sorted(unknown),'note':'Family recognition only; not typed or native-conformance acceptance'}
    return result
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--registry',required=True);a.add_argument('--shapes',required=True);a.add_argument('--output',required=True);v=a.parse_args()
    result=reconcile(json.load(open(v.registry)),v.shapes)
    p=pathlib.Path(v.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
    if result['unknown_families']:raise SystemExit(2)
