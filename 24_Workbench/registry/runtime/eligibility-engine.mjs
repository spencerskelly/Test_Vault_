// Phase 4 relationship eligibility engine. No writes, parser or automatic normalization.
const definitionKinds=new Set(['PartDefinition','ActionDefinition','StateDefinition','RequirementDefinition','ItemDefinition','PortDefinition','InterfaceDefinition','ConstraintDefinition','AttributeDefinition','CalculationDefinition','VerificationCaseDefinition','UseCaseDefinition','OccurrenceDefinition']);
const matches=(actual,expected)=>expected==='Element'?!!actual&&/^[A-Za-z][A-Za-z0-9]*$/.test(actual):expected==='Definition'?definitionKinds.has(actual):actual===expected;
const diagnostic=(code,detail)=>({code,detail});
const evidenceKey=s=>/direction|orientation/i.test(s)?'direction':/multiplicity|cardinality/i.test(s)?'multiplicity':/flag|composition/i.test(s)?'aggregationKind':/classifier/i.test(s)?'classifierId':/containment|parent\/child|owner/i.test(s)?'ownerId':/mapping|meaning|justification|classification|intended/i.test(s)?'semanticJustification':null;
export function evaluate(registry,request){
 if(registry?.policy!=='deny_by_default'||!Array.isArray(registry.rules))throw Error('INVALID_REGISTRY');
 if(typeof request?.family!=='string')return {status:'rejected',mutation:false,options:[],diagnostics:[diagnostic('INVALID_REQUEST','Missing family')]};
 const rules=registry.rules.filter(r=>r.ea.includes(request.family));
 if(!rules.length)return {status:'rejected',mutation:false,options:[],diagnostics:[diagnostic('UNKNOWN_FAMILY',request.family)]};
 const options=rules.map(rule=>{
  const errors=[],from=request.from,to=request.to;
  if(!from?.id||!to?.id||!from?.kind||!to?.kind)errors.push(diagnostic('MISSING_ENDPOINT','Both typed endpoint identities required'));
  if(!rule.eligible.from.some(k=>matches(from?.kind,k))||!rule.eligible.to.some(k=>matches(to?.kind,k)))errors.push(diagnostic('ENDPOINT_MISMATCH',`${from?.kind||'?'} -> ${to?.kind||'?'}`));
  if(!request.originalDirection)errors.push(diagnostic('MISSING_DIRECTION','Normalize EA connector orientation explicitly'));
  if(rule.eligible.requires_owner&&!request.ownerId)errors.push(diagnostic('MISSING_OWNER','Owning context required'));
  if(rule.eligible.requires_owner&&request.ownerId&&request.ownerId!==from?.id)errors.push(diagnostic('OWNER_MISMATCH','Owner must be normalized from endpoint'));
  if(from?.id&&from.id===to?.id)errors.push(diagnostic('SELF_RELATIONSHIP','Identical endpoints'));
  const missing=[...new Set(rule.source.map(evidenceKey).filter(Boolean))].filter(k=>request.evidence?.[k]===undefined||request.evidence?.[k]===null||request.evidence?.[k]==='');
  if(missing.length)errors.push(diagnostic('MISSING_EVIDENCE',missing.sort().join(',')));
  if(rule.id==='AGG-OWNED'&&!['shared','composite','1','2',1,2].includes(request.evidence?.aggregationKind))errors.push(diagnostic('AGGREGATION_UNPROVEN','Explicit shared/composite EA flag and independently verified ownership required'));
  if(rule.id==='GENERALIZE'&&from?.kind!==to?.kind)errors.push(diagnostic('INCOMPATIBLE_SPECIALIZATION','Definition kinds differ; formal type system pending'));
  if(rule.gate==='review')errors.push(diagnostic('REVIEW_REQUIRED','Operator decision and provenance required'));
  if(rule.native===null)errors.push(diagnostic('NO_NATIVE_MAPPING','Evidence-only exception'));
  return {ruleId:rule.id,native:rule.native,gate:rule.gate,eligible:errors.length===0,diagnostics:errors.sort((a,b)=>a.code.localeCompare(b.code)),workbench:rule.workbench,ownership:rule.ownership};
 });
 const priority=registry.precedence||[];
 options.sort((a,b)=>(priority.indexOf(a.ruleId)<0?999:priority.indexOf(a.ruleId))-(priority.indexOf(b.ruleId)<0?999:priority.indexOf(b.ruleId))||a.ruleId.localeCompare(b.ruleId));
 const specific=options.find(o=>['ALLOC-PERFORM','ALLOC-EXHIBIT'].includes(o.ruleId)&&!o.diagnostics.some(d=>d.code==='ENDPOINT_MISMATCH'));
 if(specific)for(const o of options)if(o.ruleId==='ALLOC-GENERIC'){o.eligible=false;o.diagnostics.push(diagnostic('SPECIALIZED_RULE_PRECEDENCE','No generic fallback for Perform/Exhibit endpoint patterns'));o.diagnostics.sort((a,b)=>a.code.localeCompare(b.code));}
 const viable=options.filter(o=>o.eligible);
 const status=viable.length?'preview_available':options.some(o=>o.diagnostics.some(d=>d.code==='REVIEW_REQUIRED'))?'review_required':'rejected';
 const codes=[...new Set(options.flatMap(o=>o.diagnostics.map(d=>d.code)))].sort();
 return {status,mutation:false,options,diagnostics:viable.length?[]:codes.map(c=>diagnostic(c,'See option diagnostics'))};
}
export function createWorkbenchMenu(registry,selection){
 const result=evaluate(registry,selection);
 return {status:result.status,items:result.options.map(o=>({id:o.ruleId,label:o.native||'Preserve source evidence',enabled:o.eligible,reasonCodes:o.diagnostics.map(d=>d.code),preview:{operation:o.ruleId,fromId:selection.from?.id??null,toId:selection.to?.id??null,ownerId:selection.ownerId??null},structure:o.workbench.structural,visual:o.workbench.visual,navigation:o.workbench.navigation})),diagnostics:result.diagnostics};
}
