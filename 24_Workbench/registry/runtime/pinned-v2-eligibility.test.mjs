import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,mkdirSync,writeFileSync,rmSync,readFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join,dirname,resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {loadPinnedV2,evaluatePinnedV2} from './pinned-v2-eligibility.mjs';

const root=resolve(dirname(fileURLToPath(import.meta.url)),'../../../');
test('pins load and prevent native emission',()=>{
 const pinned=loadPinnedV2(root);
 assert.equal(pinned.target.relationshipRules.length,26);
 const r=evaluatePinnedV2(root,{policy:'deny_by_default',rules:[]},{family:'Generalization:'});
 assert.equal(r.nativeEmission,false);
 assert.equal(r.mutation,false);
});
test('unknown candidate family rejected before evaluation',()=>{
 const r=evaluatePinnedV2(root,{policy:'deny_by_default',rules:[]},{family:'NotReal:'});
 assert.equal(r.status,'rejected');
 assert.equal(r.reason,'UNKNOWN_CANDIDATE_FAMILY');
});
test('tampered registry hash is rejected',()=>{
 const temp=mkdtempSync(join(tmpdir(),'v2-pin-test-'));
 try{
  const files=['14_Workbench/registry/sysml_v2_registry_pins.v0.1.json',
   '14_Workbench/registry/family_disposition_registry.v0.2.json',
   '14_Workbench/registry/sysml_v2_semantic_rules.v0.2.json',
   '14_Workbench/registry/sysml_v2_semantic_decisions.v0.1.json'];
  for(const f of files){mkdirSync(dirname(join(temp,f)),{recursive:true});writeFileSync(join(temp,f),readFileSync(join(root,f)));}
  writeFileSync(join(temp,files[2]),'{}');
  assert.throws(()=>loadPinnedV2(temp),/REGISTRY_HASH_MISMATCH/);
 }finally{rmSync(temp,{recursive:true,force:true});}
});
