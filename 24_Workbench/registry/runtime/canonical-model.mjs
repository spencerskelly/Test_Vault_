import { evaluate, createWorkbenchMenu } from './eligibility-engine.mjs';
export const DEFINITION_KINDS = Object.freeze(['PartDefinition','ActionDefinition','StateDefinition','RequirementDefinition','ItemDefinition','PortDefinition','InterfaceDefinition','ConstraintDefinition','AttributeDefinition','CalculationDefinition','VerificationCaseDefinition','UseCaseDefinition','OccurrenceDefinition']);
const defKinds=new Set(DEFINITION_KINDS);
const usageToDef={PartUsage:'PartDefinition',ActionUsage:'ActionDefinition',StateUsage:'StateDefinition',RequirementUsage:'RequirementDefinition',ItemUsage:'ItemDefinition',PortUsage:'PortDefinition',InterfaceUsage:'InterfaceDefinition',ConstraintUsage:'ConstraintDefinition',AttributeUsage:'AttributeDefinition',CalculationUsage:'CalculationDefinition',VerificationCaseUsage:'VerificationCaseDefinition',UseCaseUsage:'UseCaseDefinition',IncludeUseCaseUsage:'UseCaseDefinition',OccurrenceUsage:'OccurrenceDefinition',EventOccurrenceUsage:'OccurrenceDefinition'};
const issue=(code,detail)=>({code,detail});
export function validateGraph(graph){
 const errors=[],reviewFlags=[],nodes=new Map();
 for(const n of graph?.nodes||[]){
  if(!n?.id||!n.kind||nodes.has(n.id)){errors.push(issue('INVALID_ID','Missing/duplicate node ID'));continue;}
  nodes.set(n.id,n);
 }
 for(const n of nodes.values()){
  if(n.definitionId){
   const d=nodes.get(n.definitionId);
   if(!usageToDef[n.kind])errors.push(issue('DEFINITION_LINK_ON_NON_USAGE',n.id));
   else if(!d)errors.push(issue('MISSING_DEFINITION',n.id));
   else if(d.kind!==usageToDef[n.kind])errors.push(issue('INCOMPATIBLE_DEFINITION',n.id));
  }
  if(usageToDef[n.kind]&&!n.definitionId){
   const allowed={PartUsage:'UNRESOLVED_PART_TYPE',ActionUsage:'UNRESOLVED_ACTION_TYPE',PortUsage:'UNRESOLVED_PORT_TYPE'};
   if(allowed[n.kind])reviewFlags.push({...issue(allowed[n.kind],n.id),status:'review_required',sourceRef:n.sourceRef??null});
   else errors.push(issue('UNTYPED_USAGE',n.id));
  }
  if(n.ownerId&&!nodes.has(n.ownerId))errors.push(issue('MISSING_OWNER',n.id));
  if(n.kind==='PortUsage'&&n.ownerId&&nodes.has(n.ownerId)&&!['PartDefinition','PartUsage'].includes(nodes.get(n.ownerId).kind))errors.push(issue('INVALID_PORT_OWNER',n.id));
  if(n.multiplicity!==undefined){
   const m=n.multiplicity;
   if(!Array.isArray(m)||m.length!==2||!Number.isInteger(m[0])||m[0]<0||!(m[1]==='*'||(Number.isInteger(m[1])&&m[1]>=m[0])))errors.push(issue('INVALID_MULTIPLICITY',n.id));
  }
  if(n.sourceRef!==undefined&&(typeof n.sourceRef!=='string'||!n.sourceRef.trim()))errors.push(issue('INVALID_PROVENANCE',n.id));
  if(n.ownerId===n.id)errors.push(issue('OWNERSHIP_CYCLE',n.id));
  if(n.ownerId&&defKinds.has(n.kind)&&n.definitionId)errors.push(issue('INVALID_DEFINITION_IDENTITY',n.id));
 }
 for(const n of nodes.values()){
  const visited=new Set();let current=n;
  while(current?.ownerId){if(visited.has(current.id)){errors.push(issue('OWNERSHIP_CYCLE',n.id));break;}visited.add(current.id);current=nodes.get(current.ownerId);}
 }
 errors.push(...validateCanonicalRelationships(graph,nodes));
 return {valid:errors.length===0,diagnostics:errors.sort((a,b)=>a.code.localeCompare(b.code)||a.detail.localeCompare(b.detail)),reviewRequired:reviewFlags.length>0,reviewFlags:reviewFlags.sort((a,b)=>a.code.localeCompare(b.code)||a.detail.localeCompare(b.detail)),nodes};
}
export function normalizeEA(input){
 const {family,sourceId,targetId,roles,evidence={},connectorId}=input||{};
 const reject=(code)=>({ok:false,diagnostics:[issue(code,connectorId||'unknown')]});
 if(!family||!sourceId||!targetId)return reject('INCOMPLETE_SOURCE_CONNECTOR');
 if(!roles||!['source-to-target','target-to-source'].includes(roles.orientation))return reject('UNVERIFIED_SOURCE_DIRECTION');
 let fromId=roles.orientation==='source-to-target'?sourceId:targetId;
 let toId=roles.orientation==='source-to-target'?targetId:sourceId;
 if(family==='Generalization'&&roles.meaning!=='subtype-to-supertype')return reject('UNVERIFIED_GENERALIZATION_DIRECTION');
 if(family==='Abstraction:allocate'&&!['performer-to-action','exhibitor-to-state','allocation-source-to-target'].includes(roles.meaning))return reject('UNVERIFIED_ALLOCATION_ROLE');
 if(family==='Dependency:satisfy'&&roles.meaning!=='subject-to-requirement')return reject('UNVERIFIED_SATISFY_ROLE');
 if(family==='Realisation'&&roles.meaning!=='implementation-to-specification'&&roles.meaning!=='requirement-to-implementation')return reject('UNVERIFIED_REALISATION_ROLE');
 if(family==='Realisation'&&roles.meaning==='implementation-to-specification'&&roles.normalizedMeaning==='requirement-to-implementation') [fromId,toId]=[toId,fromId];
 return {ok:true,family,fromId,toId,originalDirection:roles.orientation,evidence:{...evidence,direction:roles.orientation},provenance:{connectorId,sourceId,targetId,roles}};
}
export function evaluateOnGraph(registry,graph,input){
 const validation=validateGraph(graph);
 if(!validation.valid)return {status:'rejected',mutation:false,options:[],diagnostics:validation.diagnostics};
 const n=normalizeEA(input);
 if(!n.ok)return {status:'rejected',mutation:false,options:[],diagnostics:n.diagnostics};
 const from=validation.nodes.get(n.fromId),to=validation.nodes.get(n.toId);
 if(!from||!to)return {status:'rejected',mutation:false,options:[],diagnostics:[issue('UNKNOWN_ENDPOINT','Connector refers to unknown canonical node')]};
 const ownerId=input.ownerId||null;
 if(ownerId&&(!validation.nodes.has(ownerId)))return {status:'rejected',mutation:false,options:[],diagnostics:[issue('UNKNOWN_OWNER',ownerId)]};
 if(ownerId&&ownerId===to.id&&input.family==='Aggregation')return {status:'rejected',mutation:false,options:[],diagnostics:[issue('OWNERSHIP_CYCLE','Child cannot own its proposed parent')]};
 if(input.family==='Aggregation'&&ownerId===from.id){
  let cursor=from,seen=new Set();
  while(cursor?.ownerId&&!seen.has(cursor.id)){seen.add(cursor.id);if(cursor.ownerId===to.id)return {status:'rejected',mutation:false,options:[],diagnostics:[issue('OWNERSHIP_CYCLE','Proposed edge closes a cycle')]};cursor=validation.nodes.get(cursor.ownerId);}
 }
 const result=evaluate(registry,{family:n.family,from,to,ownerId,originalDirection:n.originalDirection,evidence:n.evidence});
 return {...result,reviewFlags:validation.reviewFlags,reviewRequired:validation.reviewRequired,normalization:n.provenance,canonical:{fromId:n.fromId,toId:n.toId},graphVersion:graph.version||null};
}
export function menuOnGraph(registry,graph,input){
 const result=evaluateOnGraph(registry,graph,input);
 if(!result.canonical)return {status:result.status,items:[],diagnostics:result.diagnostics};
 const selection={family:input.family,from:{id:result.canonical.fromId,kind:graph.nodes.find(n=>n.id===result.canonical.fromId).kind},to:{id:result.canonical.toId,kind:graph.nodes.find(n=>n.id===result.canonical.toId).kind},ownerId:input.ownerId,originalDirection:input.roles.orientation,evidence:{...input.evidence,direction:input.roles.orientation}};
 const menu=createWorkbenchMenu(registry,selection);
 return {...menu,normalization:result.normalization};
}

// Strict, opt-in candidate guard. No native emission authorization.
export function validateConnectionEvidence(graph,connection){
 const diagnostics=[];
 const indexed=new Map((graph?.nodes||[]).map(n=>[n.id,n]));
 const fail=(code)=>diagnostics.push(issue(code,connection?.id||'unknown'));
 if(!connection?.id||!connection?.sourceRef?.trim?.())fail('MISSING_CONNECTOR_PROVENANCE');
 const owner=indexed.get(connection?.ownerId);
 if(!owner||!['PartDefinition','PartUsage'].includes(owner.kind))fail('INVALID_CONNECTION_OWNER');
 const endpoints=[indexed.get(connection?.fromId),indexed.get(connection?.toId)];
 if(endpoints.some(n=>!n))fail('UNRESOLVED_CONNECTION_ENDPOINT');
 else {
  for(const n of endpoints){
   if(!['PartUsage','PortUsage'].includes(n.kind))fail('INVALID_CONNECTION_ENDPOINT_KIND');
   // Only direct child endpoints are provisionally supported; wider traversal remains deferred.
   if(n.ownerId!==connection.ownerId)fail('CONNECTION_ENDPOINT_SCOPE_UNVERIFIED');
  }
 }
 if(!['source-to-target','target-to-source','bidirectional','undirected'].includes(connection?.direction))fail('UNVERIFIED_CONNECTION_DIRECTION');
 if(connection?.directionEvidence!==true)fail('UNATTESTED_DIRECTION');
 return {valid:diagnostics.length===0,diagnostics,nativeCertified:false};
}

 // Relationship checks are deliberately limited to two modeled edge kinds.
 // Other families remain in their own eligibility gates; no emitter authorization.
export function validateCanonicalRelationships(graph,index=null){
 const nodes=index||new Map((graph?.nodes||[]).map(n=>[n.id,n]));
 const errors=[],seen=new Set(),specialization=new Map();
 for(const edge of graph?.relationships||[]){
  const key=[edge?.kind,edge?.fromId,edge?.toId].join('|');
  if(!edge?.kind||!edge?.fromId||!edge?.toId){errors.push(issue('INVALID_RELATIONSHIP','missing field'));continue;}
  if(seen.has(key))errors.push(issue('DUPLICATE_RELATIONSHIP',key));
  seen.add(key);
  const from=nodes.get(edge.fromId),to=nodes.get(edge.toId);
  if(!from||!to){errors.push(issue('RELATIONSHIP_ENDPOINT_MISSING',key));continue;}
  if(edge.kind==='lexicalContainment'){
   if(to.ownerId!==from.id)errors.push(issue('LEXICAL_OWNER_MISMATCH',key));
  }else if(edge.kind==='specialization'){
   if(!defKinds.has(from.kind)||from.kind!==to.kind)errors.push(issue('INVALID_SPECIALIZATION_KINDS',key));
   if(from.id===to.id)errors.push(issue('SPECIALIZATION_CYCLE',key));
   if(typeof edge.sourceRef!=='string'||!edge.sourceRef.trim())errors.push(issue('SPECIALIZATION_PROVENANCE_REQUIRED',key));
   if(edge.direction!=='subtype-to-supertype')errors.push(issue('SPECIALIZATION_DIRECTION_UNVERIFIED',key));
   if(!specialization.has(from.id))specialization.set(from.id,[]);
   specialization.get(from.id).push(to.id);
  }else errors.push(issue('UNSUPPORTED_CANONICAL_RELATIONSHIP',key));
 }
 // Iterative DFS detects cycles without recursive call-stack risk.
 const color=new Map();
 for(const start of specialization.keys()){
  if(color.get(start))continue;
  const stack=[[start,0]];color.set(start,1);
  while(stack.length){
   const top=stack[stack.length-1],neighbors=specialization.get(top[0])||[];
   if(top[1]>=neighbors.length){color.set(top[0],2);stack.pop();continue;}
   const next=neighbors[top[1]++];
   if(color.get(next)===1)errors.push(issue('SPECIALIZATION_CYCLE',top[0]));
   else if(!color.has(next)){color.set(next,1);stack.push([next,0]);}
  }
 }
 return errors;
}
