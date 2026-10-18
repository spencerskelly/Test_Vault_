import {validateGraph} from './canonical-model.mjs';
// Review-only. Attestation flags are caller claims, not authentication.
export function proposeGeneralization(graph,row,evidence){
 const errors=[];
 const fail=x=>errors.push({code:x,detail:'source-handoff'});
 if(evidence?.schema!=='mdse-phase8-reconciled-local-manifest/1'||evidence?.verified!==true||evidence?.native_certified!==0)fail('BUNDLE_CHECK_REQUIRED');
 if(evidence?.semantic_direction_verified!==true)fail('SOURCE_SEMANTICS_UNVERIFIED');
 if(row?.family!=='Generalization'||row?.role!=='source-subtype-to-destination-supertype')fail('ROLE_UNVERIFIED');
 if(row?.source_direction!=='Source -> Destination')fail('DIRECTION_UNVERIFIED');
 if(String(row?.normalized_from)!==String(row?.raw_from)||String(row?.normalized_to)!==String(row?.raw_to))fail('ORIENTATION_MISMATCH');
 if(!row?.source_guid||!row?.source_pk)fail('MISSING_PROVENANCE');
 if(errors.length)return {status:'review',diagnostics:errors,nativeCertified:false,mutation:false};
 const edge={kind:'specialization',fromId:String(row.normalized_from),toId:String(row.normalized_to),sourceRef:String(row.source_guid),direction:'subtype-to-supertype'};
 const result=validateGraph({...graph,relationships:[...(graph?.relationships||[]),edge]});
 return {status:result.valid?'candidate':'review',diagnostics:result.diagnostics,proposedEdge:result.valid?edge:null,nativeCertified:false,mutation:false};
}
