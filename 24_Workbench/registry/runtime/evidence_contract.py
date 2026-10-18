"""Strict EA source evidence envelope; no source records stored."""
REQUIRED={'family','connectorId','sourceId','targetId','roles','evidence'}
OPTIONAL={'ownerId'}
ROLES={'orientation','meaning','normalizedMeaning'}
EVIDENCE={'direction','aggregationKind','multiplicity','classifierId','semanticJustification','sourceFlags','sourceTags','operatorDecisionId'}
def validate(row):
    errors=[]
    if not isinstance(row,dict):return ['INVALID_RECORD']
    for k in sorted(REQUIRED-set(row)):errors.append('MISSING_'+k.upper())
    for k in sorted(set(row)-REQUIRED-OPTIONAL):errors.append('UNKNOWN_'+k.upper())
    for k in sorted((REQUIRED-{'roles','evidence'}) & set(row)):
        if not isinstance(row[k],str) or not row[k].strip():errors.append('INVALID_'+k.upper())
    if 'ownerId' in row and row['ownerId'] is not None and (not isinstance(row['ownerId'],str) or not row['ownerId'].strip()):errors.append('INVALID_OWNERID')
    roles=row.get('roles')
    if not isinstance(roles,dict):errors.append('INVALID_ROLES')
    else:
        for k in sorted(set(roles)-ROLES):errors.append('UNKNOWN_ROLE_'+k.upper())
        if roles.get('orientation') not in ('source-to-target','target-to-source'):errors.append('INVALID_ORIENTATION')
        if not isinstance(roles.get('meaning'),str) or not roles['meaning'].strip():errors.append('INVALID_ROLE_MEANING')
        if 'normalizedMeaning' in roles and not isinstance(roles['normalizedMeaning'],str):errors.append('INVALID_NORMALIZED_MEANING')
    evidence=row.get('evidence')
    if not isinstance(evidence,dict):errors.append('INVALID_EVIDENCE')
    else:
        for k in sorted(set(evidence)-EVIDENCE):errors.append('UNKNOWN_EVIDENCE_'+k.upper())
        for k,v in evidence.items():
            if k in ('sourceFlags','sourceTags'):
                if not isinstance(v,dict) or not all(isinstance(a,str) and isinstance(b,(str,bool,int,float)) for a,b in v.items()):errors.append('INVALID_EVIDENCE_'+k.upper())
            elif not isinstance(v,str):errors.append('INVALID_EVIDENCE_'+k.upper())
        if isinstance(roles,dict) and evidence.get('direction') and evidence['direction']!=roles.get('orientation'):errors.append('DIRECTION_CONFLICT')
    return sorted(set(errors))
