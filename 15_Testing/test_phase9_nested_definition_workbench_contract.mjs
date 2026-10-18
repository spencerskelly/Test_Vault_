import assert from 'node:assert/strict';
import {test} from 'node:test';
import {validateGraph} from '../14_Workbench/registry/runtime/canonical-model.mjs';
// Canonical graph keeps lexical owner and semantic generalization separate.
// This is a Workbench contract fixture, not a SysML-native emitter.
const graph=()=>({version:'phase9-synthetic',nodes:[
 {id:'parent',kind:'PartDefinition',sourceRef:'synthetic-parent'},
 {id:'child',kind:'PartDefinition',ownerId:'parent',sourceRef:'synthetic-child'}
],relationships:[
 {kind:'lexicalContainment',fromId:'parent',toId:'child'},
 {kind:'specialization',fromId:'child',toId:'parent',sourceRef:'synthetic-generalization'}
]});
test('nested definitions remain distinct canonical nodes',()=>{
 const x=graph();assert.equal(validateGraph(x).valid,true);
 assert.equal(x.nodes[1].ownerId,'parent');
});
test('lexical containment and specialization remain separate',()=>{
 const x=graph();assert.equal(x.relationships.length,2);
 assert.deepEqual(x.relationships.map(e=>e.kind),['lexicalContainment','specialization']);
});
test('no part usage is manufactured',()=>assert.equal(graph().nodes.some(n=>n.kind==='PartUsage'),false));
test('specialization retains source provenance',()=>assert.equal(graph().relationships[1].sourceRef,'synthetic-generalization'));
test('owner recursion is rejected by existing canonical validator',()=>{
 const x=graph();x.nodes[0].ownerId='child';
 assert.ok(validateGraph(x).diagnostics.some(e=>e.code==='OWNERSHIP_CYCLE'));
});
