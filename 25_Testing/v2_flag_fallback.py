#!/usr/bin/env python3
"""MDSE v2 local-only flag fallback adapter. No native emission or diagrams."""
import argparse,csv,json
from collections import Counter
from pathlib import Path
FLAG_LINK_STATES={'flaglink_candidate','semantic_role_review','workflow_context_review','non_native_context_review','direction_evidence_review','conditional_usage_review'}
REQUIRED={'source_pk','source_guid','family','disposition','reason','raw_from','raw_to','source_direction'}
def build(dispositions,element_exceptions=()):
    flags=[];seen=set();statuses=Counter()
    for row in dispositions:
        if not REQUIRED.issubset(row):raise ValueError('MISSING_DISPOSITION_COLUMNS')
        key=row['source_guid']
        if not key or not row['source_pk'] or key in seen:raise ValueError('DUPLICATE_OR_MISSING_CONNECTOR_IDENTITY')
        seen.add(key);statuses[row['disposition']]+=1
        if row['disposition'] not in FLAG_LINK_STATES:continue
        if not row['raw_from'] or not row['raw_to']:raise ValueError('MISSING_FLAGLINK_ENDPOINT')
        flags.append({'type':'flagLink','identity':'ea-connector:'+key,'sourceConnectorId':row['source_pk'],'sourceConnectorGUID':key,'sourceElementId':row['raw_from'],'targetElementId':row['raw_to'],'sourceFamily':row['family'],'sourceDirection':row['source_direction'],'reason':row['disposition'],'explanation':row['reason'],'reviewStatus':'open','nativeSyntax':False})
    seen_elements=set()
    for e in element_exceptions:
        key=e.get('sourceElementGUID') or ('ea-element-id:'+str(e.get('sourceElementId','')))
        if not e.get('sourceElementId') or key in seen_elements or not e.get('reason'):raise ValueError('INVALID_FLAGNOTE_IDENTITY_OR_REASON')
        seen_elements.add(key)
        flags.append({'type':'flagNote','identity':'ea-element:'+key,'sourceElementId':e['sourceElementId'],'sourceElementGUID':e.get('sourceElementGUID',''),'sourceFamily':e.get('sourceFamily',''),'reason':e['reason'],'explanation':e.get('explanation',e['reason']),'originalContent':e.get('originalContent',''),'reviewStatus':'open','nativeSyntax':False})
    return flags,dict(sorted(statuses.items()))
def run(input_path,output_path,element_path=None):
    input_path=Path(input_path).resolve();output_path=Path(output_path).resolve()
    if output_path.exists():raise ValueError('OUTPUT_ALREADY_EXISTS')
    if output_path==input_path:raise ValueError('OVERWRITE_SOURCE_FORBIDDEN')
    with input_path.open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        if not REQUIRED.issubset(reader.fieldnames or []):raise ValueError('MISSING_DISPOSITION_COLUMNS')
        rows=list(reader)
    elements=json.loads(Path(element_path).read_text()) if element_path else []
    if not isinstance(elements,list):raise ValueError('ELEMENT_EXCEPTIONS_MUST_BE_ARRAY')
    flags,statuses=build(rows,elements)
    output={'schema':'mdse-v2-local-flag-fallback/1','nativeEmissionAuthorized':False,'eaDiagramsProcessed':0,'sourceConnectorRows':len(rows),'dispositions':statuses,'flags':flags,'flagLinkCount':sum(x['type']=='flagLink' for x in flags),'flagNoteCount':sum(x['type']=='flagNote' for x in flags)}
    output_path.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return {k:v for k,v in output.items() if k!='flags'}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--dispositions',required=True);parser.add_argument('--out',required=True);parser.add_argument('--element-exceptions')
    args=parser.parse_args();print(json.dumps(run(args.dispositions,args.out,args.element_exceptions),indent=2))
