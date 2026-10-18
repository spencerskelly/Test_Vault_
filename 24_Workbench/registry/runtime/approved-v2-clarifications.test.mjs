import test from 'node:test';
import assert from 'node:assert/strict';
import {validateGraph,DEFINITION_KINDS} from './canonical-model.mjs';
import {evaluate} from './eligibility-engine.mjs';

test('UseCase and Occurrence reusable definitions with context usages',()=>{
  assert.ok(DEFINITION_KINDS.includes('UseCaseDefinition'));
  assert.ok(DEFINITION_KINDS.includes('OccurrenceDefinition'));
  const g={nodes:[
    {id:'owner',kind:'PartDefinition'},
    {id:'caseD',kind:'UseCaseDefinition'},
    {id:'occD',kind:'OccurrenceDefinition'},
    {id:'caseU',kind:'UseCaseUsage',ownerId:'owner',definitionId:'caseD'},
    {id:'inclU',kind:'IncludeUseCaseUsage',ownerId:'caseU',definitionId:'caseD'},
    {id:'occU',kind:'OccurrenceUsage',ownerId:'owner',definitionId:'occD'},
    {id:'eventU',kind:'EventOccurrenceUsage',ownerId:'owner',definitionId:'occD'}]};
  assert.equal(validateGraph(g).valid,true);
  assert.equal(validateGraph({nodes:[{id:'u',kind:'UseCaseUsage',definitionId:'missing'}]}).valid,false);
});

test('Part Action Port without definition are allowed but require review, not structural rejection',()=>{
  const g={nodes:[{id:'p',kind:'PartDefinition'},...[
    ['part','PartUsage','UNRESOLVED_PART_TYPE'],
    ['action','ActionUsage','UNRESOLVED_ACTION_TYPE'],
    ['port','PortUsage','UNRESOLVED_PORT_TYPE']
  ].map(([id,kind])=>({id,kind,ownerId:'p',sourceRef:'EA-SYNTHETIC-'+id}))]};
  const r=validateGraph(g);
  assert.equal(r.valid,true);
  assert.equal(r.reviewRequired,true);
  assert.deepEqual(r.reviewFlags.map(x=>x.code).sort(),[
    'UNRESOLVED_ACTION_TYPE','UNRESOLVED_PART_TYPE','UNRESOLVED_PORT_TYPE']);
  assert.equal(r.reviewFlags.length,3);
  assert.ok(r.reviewFlags.every(x=>x.status==='review_required'&&x.sourceRef));
  const bad=validateGraph({nodes:[{id:'part',kind:'PartUsage',ownerId:'MISSING'}]});
  assert.equal(bad.valid,false);
  assert.ok(bad.diagnostics.some(x=>x.code==='MISSING_OWNER'));
});

test('Shared and composite remain review-only candidate owned usages; unknown rejected',()=>{
  const rule={id:'AGG-OWNED',ea:['Aggregation'],native:'PartUsage',gate:'review',
    source:['EA aggregation/composition flags','direction','classifier identity','multiplicity and containment evidence'],
    eligible:{from:['PartDefinition'],to:['PartDefinition'],requires_owner:true},
    workbench:{structural:'usage',visual:'owned feature',navigation:'where-used'}};
  const reg={policy:'deny_by_default',rules:[rule]};
  const base={family:'Aggregation',from:{id:'owner',kind:'PartDefinition'},to:{id:'child',kind:'PartDefinition'},
    ownerId:'owner',originalDirection:'source-to-target',
    evidence:{direction:'source-to-target',aggregationKind:'shared',classifierId:'child',multiplicity:'1',ownerId:'owner'}};
  for(const kind of ['shared','composite',1,2]){
    const r=evaluate(reg,{...base,evidence:{...base.evidence,aggregationKind:kind}});
    assert.equal(r.status,'review_required');
    assert.ok(!r.options[0].diagnostics.some(x=>x.code==='AGGREGATION_UNPROVEN'));
    assert.equal(r.mutation,false);
  }
  assert.ok(evaluate(reg,{...base,evidence:{...base.evidence,aggregationKind:'unknown'}}).options[0].diagnostics.some(x=>x.code==='AGGREGATION_UNPROVEN'));
  assert.ok(evaluate(reg,{...base,ownerId:null}).options[0].diagnostics.some(x=>x.code==='MISSING_OWNER'));
});
