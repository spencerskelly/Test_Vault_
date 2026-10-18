// Pinned SysML v2 candidate registry guard for translator / Workbench previews.
// This module deliberately never emits SysML v2 or authorizes a write.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {resolve} from 'node:path';
import {evaluate} from './eligibility-engine.mjs';

const files=[
 '24_Workbench/registry/family_disposition_registry.v0.2.json',
 '24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json',
 '24_Workbench/registry/sysml_v2_semantic_decisions.v0.1.json'
];
export function loadPinnedV2(root){
 const pins=JSON.parse(readFileSync(resolve(root,'24_Workbench/registry/sysml_v2_registry_pins.v0.1.json')));
 if(pins.schema!=='mdse-v2-registry-pins/1'||Object.keys(pins.files||{}).sort().join('|')!==[...files].sort().join('|'))throw Error('INVALID_PIN_MANIFEST');
 const data={};
 for(const rel of files){
  const bytes=readFileSync(resolve(root,rel));
  if(createHash('sha256').update(bytes).digest('hex')!==pins.files[rel])throw Error('REGISTRY_HASH_MISMATCH: '+rel);
  data[rel]=JSON.parse(bytes.toString('utf8'));
 }
 const source=data[files[0]],target=data[files[1]],decisions=data[files[2]];
 if(source.schema_version!=='0.2.0'||target.version!=='0.2.0'||decisions.version!=='0.1.0')throw Error('REGISTRY_VERSION_MISMATCH');
 const sourceFamilies=source.families.map(x=>x.family).sort();
 const targetFamilies=target.relationshipRules.map(x=>x.family).sort();
 if(sourceFamilies.length!==26||new Set(sourceFamilies).size!==26||JSON.stringify(sourceFamilies)!==JSON.stringify(targetFamilies))throw Error('REGISTRY_FAMILY_DRIFT');
 const expected=target.relationshipRules.filter(x=>x.existingCandidateDifference).map(x=>x.family).sort();
 const registered=decisions.records.map(x=>x.family).sort();
 if(expected.length!==11||JSON.stringify(expected)!==JSON.stringify(registered))throw Error('DECISION_DRIFT');
 if(target.automaticNativeEmission!==false||target.defaultDisposition!=='deferred_review'||target.relationshipRules.some(x=>x.emission!=='deferred_pending_evidence_and_parser')||decisions.records.some(x=>x.nativeEmissionAuthorized!==false))throw Error('NATIVE_EMISSION_UNSAFE');
 return Object.freeze({source,target,decisions});
}
export function evaluatePinnedV2(root,phase3Registry,request){
 const pinned=loadPinnedV2(root);
 if(!pinned.target.relationshipRules.some(x=>x.family===request?.family))return {status:'rejected',mutation:false,nativeEmission:false,reason:'UNKNOWN_CANDIDATE_FAMILY'};
 const result=evaluate(phase3Registry,request);
 return {...result,mutation:false,nativeEmission:false,semanticGate:'DEFERRED_PENDING_PARSER_AND_EVIDENCE'};
}
