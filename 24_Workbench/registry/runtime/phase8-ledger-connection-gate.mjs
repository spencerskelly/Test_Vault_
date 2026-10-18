import {validateConnectionEvidence} from './canonical-model.mjs';
// An explicit local, independently reconciled ledger row is required.
// Caller booleans alone never attest EA semantics or authorize native emission.
export function evaluateLedgerConnection(graph,row,attestation){
 const diagnostics=[];
 const fail=code=>diagnostics.push({code,detail:'local-evidence-gate'});
 if(attestation?.schema!=='mdse-phase8-local-ledger-attestation/1'||attestation?.verified!==true||attestation?.native_certified!==0)fail('LEDGER_ATTESTATION_REQUIRED');
 if(!row||!String(row.source_guid||'').trim()||!String(row.source_pk||'').trim())fail('SOURCE_CONNECTOR_ID_REQUIRED');
 if(!row||!String(row.normalized_from||'').trim()||!String(row.normalized_to||'').trim())fail('NORMALIZED_ENDPOINTS_REQUIRED');
 if(row?.source_direction!=='Source -> Destination')fail('SOURCE_DIRECTION_NOT_EXPLICIT');
 if(row?.diagnostics||!['role_normalized','orientation_normalized','owner_endpoint_identified','family_candidate'].includes(row?.status))fail('UNRESOLVED_SOURCE_DIAGNOSTICS');
 if(row?.family!=='Association'&&row?.family!=='Connector')fail('CONNECTION_FAMILY_NOT_CONFIRMED');
 if(!['source-owns-destination','destination-owns-source','explicit-connection-owner'].includes(row?.role))fail('CONNECTION_OWNER_ROLE_UNVERIFIED');
 if(diagnostics.length)return {valid:false,diagnostics,nativeCertified:false};
 // Even a schema-valid row is only eligible for structural review, not native certification.
 const connection={id:String(row.source_pk),sourceRef:String(row.source_guid),
   ownerId:String(row.connection_owner_id||''),fromId:String(row.normalized_from),
   toId:String(row.normalized_to),direction:'source-to-target',directionEvidence:true};
 const checked=validateConnectionEvidence(graph,connection);
 return {...checked,reviewOnly:true,nativeCertified:false};
}
