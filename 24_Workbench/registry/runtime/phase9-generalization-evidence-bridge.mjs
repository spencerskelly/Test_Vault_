// Phase 8 → Phase 9 review-only bridge.
// This function accepts an independently verified direction record ONLY for structural review.
// It cannot authenticate its caller, attest a QEAX, or authorize native emission.
import {validateGraph} from './canonical-model.mjs';
export function reviewGeneralizationFromEvidence(graph,evidence){
 const diagnostics=[];
 const fail=code=>diagnostics.push({code,detail:'source-evidence-boundary'});
 if(evidence?.schema!=='mdse-phase9-generalization-direction/1')fail('INVALID_DIRECTION_EVIDENCE_SCHEMA');
 if(evidence?.reconciliationVerified!==true)fail('RECONCILIATION_NOT_VERIFIED');
 if(evidence?.sourceFamily!=='Generalization')fail('NOT_SOURCE_GENERALIZATION');
 if(evidence?.sourceDirection!=='Source -> Destination')fail('SOURCE_DIRECTION_UNVERIFIED');
 if(!evidence?.connectorRef||typeof evidence.connectorRef!=='string'||!evidence.connectorRef.trim())fail('CONNECTOR_PROVENANCE_MISSING');
 if(!evidence?.sourceNodeId||!evidence?.targetNodeId)fail('SOURCE_ENDPOINTS_MISSING');
 if(!evidence?.snapshotSha256||!(/^[a-f0-9]{64}$/).test(evidence.snapshotSha256))fail('SNAPSHOT_HASH_MISSING');
 if(diagnostics.length)return {status:'review',diagnostics,graphValidated:false,nativeCertified:false};
 const proposed={kind:'specialization',fromId:evidence.sourceNodeId,toId:evidence.targetNodeId,sourceRef:evidence.connectorRef,direction:'subtype-to-supertype'};
 const trial={...graph,relationships:[...(graph?.relationships||[]),proposed]};
 const validated=validateGraph(trial);
 return {status:validated.valid?'reviewable':'review',diagnostics:validated.diagnostics,graphValidated:validated.valid,proposedEdge:validated.valid?proposed:null,nativeCertified:false};
}
