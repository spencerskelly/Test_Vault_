import {validateGraph} from './canonical-model.mjs';
// Untrusted transport contract for locally reconciled EA generalizations.
// This is not a cryptographic issuer or a native-emission eligibility decision.
export function reviewEAGeneralizationEvidence(graph, evidence) {
 const codes=[];
 const fail=c=>codes.push({code:c,detail:'generalization-evidence'});
 if(evidence?.schema!=='mdse-ea-generalization-handoff/1')fail('HANDOFF_SCHEMA_INVALID');
 if(evidence?.family!=='Generalization')fail('NOT_GENERALIZATION');
 if(evidence?.rawDirection!=='Source -> Destination')fail('EA_SOURCE_DIRECTION_NOT_EXPLICIT');
 if(evidence?.role!=='source-subtype-to-destination-supertype')fail('EA_ROLE_UNCONFIRMED');
 if(typeof evidence?.sourceConnectorRef!=='string'||!evidence.sourceConnectorRef.trim())fail('CONNECTOR_PROVENANCE_MISSING');
 if(typeof evidence?.sourceSnapshotSha256!=='string'||!/^[0-9a-f]{64}$/i.test(evidence.sourceSnapshotSha256))fail('SOURCE_SNAPSHOT_HASH_MISSING');
 if(typeof evidence?.ledgerSha256!=='string'||!/^[0-9a-f]{64}$/i.test(evidence.ledgerSha256))fail('LEDGER_HASH_MISSING');
 const sourceId=evidence?.sourceId,targetId=evidence?.targetId;
 const v=validateGraph(graph);
 if(!v.valid)fail('CANONICAL_GRAPH_INVALID');
 const from=v.nodes.get(sourceId),to=v.nodes.get(targetId);
 if(!from||!to)fail('CANONICAL_ENDPOINT_MISSING');
 else if(!from.kind.endsWith('Definition')||from.kind!==to.kind)fail('GENERALIZATION_KINDS_UNVERIFIED');
 if(sourceId===targetId)fail('SELF_GENERALIZATION');
 if(evidence?.normalizedFrom!==sourceId||evidence?.normalizedTo!==targetId)fail('NORMALIZED_DIRECTION_MISMATCH');
 if(evidence?.sourceStatus!=='orientation_normalized')fail('SOURCE_DISPOSITION_NOT_QUALIFIED');
 // Do not claim the caller-supplied hashes or sourceStatus are independently authenticated.
 return {reviewable:codes.length===0,diagnostics:codes,
   candidate:codes.length===0?{kind:'specialization',fromId:sourceId,toId:targetId,sourceRef:evidence.sourceConnectorRef,direction:'subtype-to-supertype'}:null,
   sourceAuthenticated:false,nativeCertified:false,mayEmitNative:false};
}
