// Review-only normalization handoff. Caller-provided evidence is NOT independently trusted.
import {validateGraph} from './canonical-model.mjs';
export function reviewPhase8Generalization(graph, ledgerRow, rawConnector) {
 const errors=[];
 const fail=code=>errors.push(code);
 if(!ledgerRow||!rawConnector)return {reviewable:false,errors:['MISSING_SOURCE_EVIDENCE'],nativeCertified:false};
 const fields=[['source_pk','Connector_ID'],['source_guid','ea_guid'],['raw_from','Start_Object_ID'],['raw_to','End_Object_ID']];
 for(const [left,right] of fields){
  if(!String(ledgerRow[left]??'').trim()||String(ledgerRow[left])!==String(rawConnector[right]??''))fail('SOURCE_IDENTITY_MISMATCH');
 }
 if(rawConnector.Connector_Type!=='Generalization'||ledgerRow.family!=='Generalization')fail('WRONG_SOURCE_FAMILY');
 if(rawConnector.Direction!=='Source -> Destination'||ledgerRow.source_direction!==rawConnector.Direction)fail('RAW_DIRECTION_UNVERIFIED');
 if(ledgerRow.role!=='source-subtype-to-destination-supertype')fail('ROLE_UNVERIFIED');
 if(ledgerRow.normalized_from!==String(rawConnector.Start_Object_ID)||ledgerRow.normalized_to!==String(rawConnector.End_Object_ID))fail('NORMALIZED_DIRECTION_MISMATCH');
 if(ledgerRow.status!=='orientation_normalized')fail('STATUS_NOT_QUALIFIED');
 const v=validateGraph(graph);
 if(!v.valid)fail('INVALID_CANONICAL_GRAPH');
 const from=v.nodes.get(ledgerRow.normalized_from),to=v.nodes.get(ledgerRow.normalized_to);
 if(!from||!to)fail('CANONICAL_ENDPOINT_MISSING');
 else if(!from.kind.endsWith('Definition')||from.kind!==to.kind)fail('DEFINITION_KINDS_INCOMPATIBLE');
 return {reviewable:errors.length===0,errors:[...new Set(errors)].sort(),nativeCertified:false,
   evidenceLevel:'caller-supplied-local-crosscheck-only',mayEmitNative:false};
}
