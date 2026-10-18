// Read-only boundary adapter. A caller's ledger fields do NOT constitute trusted attestation.
// No native emitter may consume this review projection as approved evidence.
export function reviewPhase8Generalization(row, source) {
 const diagnostics=[];
 const fail=c=>diagnostics.push({code:c});
 if(!row || !source) return {status:'review',diagnostics:[{code:'SOURCE_EVIDENCE_MISSING'}],nativeCertified:false,edge:null};
 const match=(a,b)=>String(a??'')===String(b??'');
 if(!match(row.source_pk,source.connectorId)||!match(row.source_guid,source.guid))fail('CONNECTOR_IDENTITY_MISMATCH');
 if(source.family!=='Generalization'||row.family!=='Generalization')fail('NOT_GENERALIZATION');
 if(source.direction!=='Source -> Destination'||row.source_direction!=='Source -> Destination')fail('EA_DIRECTION_NOT_EXPLICIT');
 if(!match(row.raw_from,source.startId)||!match(row.raw_to,source.endId))fail('SOURCE_ENDPOINT_MISMATCH');
 if(!match(row.normalized_from,source.startId)||!match(row.normalized_to,source.endId))fail('NORMALIZED_ENDPOINT_MISMATCH');
 if(row.role!=='source-subtype-to-destination-supertype')fail('ROLE_UNVERIFIED');
 if(row.status!=='orientation_normalized'||(row.diagnostics||'')!=='NATIVE_PARSER_AND_EVIDENCE_PENDING')fail('LEDGER_DISPOSITION_REVIEW');
 if(!source.definitionKindsVerified||source.fromKind!==source.toKind||!String(source.fromKind||'').endsWith('Definition'))fail('DEFINITION_KINDS_UNVERIFIED');
 if(!source.localSnapshotBound)fail('LOCAL_SNAPSHOT_ATTESTATION_MISSING');
 if(diagnostics.length)return {status:'review',diagnostics,nativeCertified:false,edge:null};
 return {status:'candidate_for_graph_review',diagnostics:[],nativeCertified:false,
  edge:{kind:'specialization',fromId:String(source.startId),toId:String(source.endId),direction:'subtype-to-supertype',sourceRef:String(source.guid)}};
}
