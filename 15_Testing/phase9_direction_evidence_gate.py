"""Review-only local source direction evidence; never approves emission."""
import csv,pathlib,sqlite3
def check(qeax,ledger,connector_id):
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+'?mode=ro',uri=True) as db:
  rows=db.execute('SELECT ea_guid,Connector_Type,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_ID=?',(connector_id,)).fetchall()
 with open(ledger,newline='',encoding='utf-8') as f:
  matches=[r for r in csv.DictReader(f) if r.get('source_pk')==str(connector_id)]
 if len(rows)!=1 or len(matches)!=1:return {'status':'review','reason':'SOURCE_CARDINALITY','nativeCertified':False}
 guid,kind,direction,source,target=rows[0];row=matches[0]
 expected=(str(guid or ''),str(source),str(target),direction)
 actual=tuple(row.get(k) for k in ('source_guid','raw_from','raw_to','source_direction'))
 if kind!='Generalization' or direction!='Source -> Destination':return {'status':'review','reason':'UNVERIFIED_SOURCE_DIRECTION','nativeCertified':False}
 if actual!=expected or tuple(row.get(k) for k in ('normalized_from','normalized_to'))!=(str(source),str(target)):return {'status':'review','reason':'LEDGER_MISMATCH','nativeCertified':False}
 if row.get('status')!='orientation_normalized' or row.get('family')!='Generalization':return {'status':'review','reason':'LEDGER_NOT_QUALIFIED','nativeCertified':False}
 return {'status':'direction_candidate','direction':'subtype-to-supertype','nativeCertified':False}
