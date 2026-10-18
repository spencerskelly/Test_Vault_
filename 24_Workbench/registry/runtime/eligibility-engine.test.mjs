import test from 'node:test';
import assert from 'node:assert/strict';
import {evaluate,createWorkbenchMenu} from './eligibility-engine.mjs';
const mk=(id,ea,native,gate,source,from,to,owner=false)=>({id,ea:[ea],native,gate,source,eligible:{from,to,requires_owner:owner},workbench:{structural:'tree',visual:'projection',navigation:'inverse'}});
const r={policy:'deny_by_default',precedence:['ALLOC-PERFORM','ALLOC-EXHIBIT','ALLOC-GENERIC'],rules:[
mk('ALLOC-PERFORM','Abstraction:allocate','PerformActionUsage','conditional',['direction'],['PartDefinition'],['ActionDefinition'],true),
mk('ALLOC-GENERIC','Abstraction:allocate','AllocationUsage','conditional',['allocation meaning'],['PartDefinition','ActionDefinition'],['PartDefinition','ActionDefinition']),
mk('GENERALIZE','Generalization','Specialization','conditional',['orientation'],['Definition'],['Definition']),
mk('TRACE','Dependency:trace',null,'review',['meaning'],['Element'],['Element'])
]};
const input={family:'Abstraction:allocate',from:{id:'p',kind:'PartDefinition'},to:{id:'a',kind:'ActionDefinition'},ownerId:'p',originalDirection:'normalized',evidence:{direction:'p-a',semanticJustification:'performs'}};
test('perform precedence',()=>{const x=evaluate(r,input);assert.equal(x.status,'preview_available');assert.equal(x.options[0].ruleId,'ALLOC-PERFORM');assert.equal(x.options.find(o=>o.ruleId==='ALLOC-GENERIC').eligible,false)});
test('missing owner rejects and does not fall back',()=>assert.equal(evaluate(r,{...input,ownerId:null}).status,'rejected'));
test('invalid endpoints',()=>assert.equal(evaluate(r,{...input,from:{id:'x',kind:'RequirementDefinition'}}).status,'rejected'));
test('missing direction',()=>assert.equal(evaluate(r,{...input,originalDirection:null}).status,'rejected'));
test('unknown family',()=>assert.equal(evaluate(r,{family:'unknown'}).diagnostics[0].code,'UNKNOWN_FAMILY'));
test('trace remains evidence only',()=>assert.equal(evaluate(r,{family:'Dependency:trace',from:input.from,to:input.to,originalDirection:'normalized',evidence:{semanticJustification:'trace'}}).status,'review_required'));
test('generalization incompatible definitions',()=>assert.ok(evaluate(r,{family:'Generalization',from:input.from,to:input.to,originalDirection:'normalized',evidence:{direction:'p-a'}}).diagnostics.some(x=>x.code==='INCOMPATIBLE_SPECIALIZATION')));
test('menu preview cannot write',()=>{const x=createWorkbenchMenu(r,input);assert.equal(x.items[0].enabled,true);assert.equal(x.items[0].preview.operation,'ALLOC-PERFORM')});
test('input unchanged',()=>{const before=JSON.stringify(input);evaluate(r,input);assert.equal(JSON.stringify(input),before)});
