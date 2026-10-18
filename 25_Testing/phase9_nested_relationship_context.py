"""Read-only nested EA generalization relationship audit. Aggregate-only output."""
import argparse,collections,json,pathlib,sqlite3
STYLES={'Hardware Component','Physical Component','Module','Logical Signal'}
def analyze(path):
 counts=collections.Counter();categories=collections.Counter()
 with sqlite3.connect(pathlib.Path(path).resolve().as_uri()+'?mode=ro',uri=True) as db:
  objects={r[0]:(r[1],r[2] or '',r[3] or 0) for r in db.execute('SELECT Object_ID,Object_Type,Stereotype,ParentID FROM t_object')}
  nested=set()
  for a,b in db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
   x,y=objects.get(a),objects.get(b)
   if not x or not y or x[:2]!=y[:2] or x[1] not in STYLES or x[0] not in ('Class','Signal'):continue
   for n,o in ((a,x),(b,y)):
    if o[2]:nested.add(n)
  counts['unique_nested_elements']=len(nested)
  for n in nested:
   parent=objects[n][2]
   counts['parent_present' if parent in objects else 'parent_missing']+=1
   counts['parent_hardware_component' if parent in objects and objects[parent][:2]==('Class','Hardware Component') else 'parent_other']+=1
  for kind,a,b in db.execute('SELECT Connector_Type,Start_Object_ID,End_Object_ID FROM t_connector'):
   if a not in nested and b not in nested:continue
   counts['incident_connector_appearances']+=1
   role='nested_to_parent' if a in nested and b==objects[a][2] else 'parent_to_nested' if b in nested and a==objects[b][2] else 'other'
   categories[(kind,role)]+=1
 return {'schema':'mdse-phase9-nested-relationship-context/1','counts':dict(sorted(counts.items())),'connector_categories':[{'type':k,'relationship_to_parent':r,'count':v} for (k,r),v in sorted(categories.items())],'native_certified':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qeax',required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error('QEAX file not found')
 print(json.dumps(analyze(a.qeax),indent=2))
