import {validateGraph} from './canonical-model.mjs';
// The caller must supply a projection from a *locally reconciled* EA record.
// No supplied flags grant trust or native emission. All results remain review-only.
export function reviewEAGeneralization(graph,record){
 const diagnostics=[];
 const fail=code=>diagnostics.push({code,detail:'generalization-evidence'});
 const nonempty=x=>typeof x==='string'&&x.trim().length>0;
 if(record?.family!=='Generalization')fail('NOT_GENERALIZATION');
 if(!nonempty(record?.sourceRef))fail('MISSING_SOURCE_PROVENANCE');
 if(!nonempty(record?.rawFrom)||!nonempty(record?.rawTo))fail('MISSING_RAW_ENDPOINTS');
 if(record?.sourceDirection!=='Source -> Destination')fail('UNVERIFIED_EA_DIRECTION');
 if(record?.role!=='source-subtype-to-destination-supertype')fail('UNVERIFIED_EA_ROLE');
 if(record?.normalizedFrom!==record?.rawFrom||record?.normalizedTo!==record?.rawTo)fail('NORMALIZATION_ENDPOINT_MISMATCH');
 const candidate={kind:'specialization',fromId:record?.normalizedFrom,toId:record?.normalizedTo,
    direction:'subtype-to-supertype',sourceRef:record?.sourceRef};
 const checked=validateGraph({...graph,relationships:[...(graph?.relationships||[]),candidate]});
 if(!checked.valid)diagnostics.push(...checked.diagnostics);
 return {status:diagnostics.length?'rejected':'review',diagnostics,candidate:diagnostics.length?null:candidate,
    trustedSourceVerified:false,nativeCertified:false,mutation:false};
}
