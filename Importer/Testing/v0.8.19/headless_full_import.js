#!/usr/bin/env node
"use strict";

const fs = require("fs");
const fsp = fs.promises;
const path = require("path");
const vm = require("vm");
const { performance } = require("perf_hooks");
const { webcrypto } = require("crypto");

if (process.argv.length < 5) {
  console.error("Usage: node headless_full_import.js IMPORTER_HTML SOURCE_QEAX OUTPUT_BASE");
  process.exit(2);
}
const importerPath = path.resolve(process.argv[2]);
const sourcePath = path.resolve(process.argv[3]);
const outputPath = path.resolve(process.argv[4]);
const secondOutputPath = process.argv[5] ? path.resolve(process.argv[5]) : null;
const benchmarkPath = path.join(path.dirname(__filename), "attachment_benchmark.json");
const benchmarkObject = fs.existsSync(benchmarkPath) ? JSON.parse(fs.readFileSync(benchmarkPath, "utf8")) : null;

class DiskSlice {
  constructor(filePath, start, end) { this.filePath=filePath; this.start=start; this.end=end; }
  async arrayBuffer() {
    const len=Math.max(0,this.end-this.start);
    const fh=await fsp.open(this.filePath,"r");
    try{
      const b=Buffer.allocUnsafe(len);
      let off=0;
      while(off<len){
        const r=await fh.read(b,off,len-off,this.start+off);
        if(!r.bytesRead)break;
        off+=r.bytesRead;
      }
      const out=b.subarray(0,off);
      return out.buffer.slice(out.byteOffset,out.byteOffset+out.byteLength);
    }finally{await fh.close();}
  }
  async text(){return Buffer.from(await this.arrayBuffer()).toString("utf8");}
}
class DiskFile {
  constructor(filePath){
    this.filePath=filePath;
    const st=fs.statSync(filePath);
    this.size=st.size; this.name=path.basename(filePath); this.lastModified=st.mtimeMs;
    this.type="";
  }
  slice(start=0,end=this.size){
    start=Math.max(0,Number(start)||0); end=Math.min(this.size,end==null?this.size:Number(end));
    return new DiskSlice(this.filePath,start,end);
  }
  async arrayBuffer(){return this.slice(0,this.size).arrayBuffer();}
  async text(){return fsp.readFile(this.filePath,"utf8");}
}
class WritableHandle {
  constructor(filePath){this.filePath=filePath;this.closed=false;}
  async write(data){
    await fsp.mkdir(path.dirname(this.filePath),{recursive:true});
    if(typeof data==="string")return fsp.writeFile(this.filePath,data,"utf8");
    if(data instanceof Uint8Array||Buffer.isBuffer(data))return fsp.writeFile(this.filePath,Buffer.from(data));
    if(data instanceof ArrayBuffer)return fsp.writeFile(this.filePath,Buffer.from(data));
    if(data&&typeof data.arrayBuffer==="function")return fsp.writeFile(this.filePath,Buffer.from(await data.arrayBuffer()));
    throw new Error("Unsupported write payload for "+this.filePath);
  }
  async close(){this.closed=true;}
  async abort(){this.closed=true;try{await fsp.unlink(this.filePath);}catch(_){}}
}
class FileHandle {
  constructor(filePath){this.filePath=filePath;this.name=path.basename(filePath);this.kind="file";}
  async getFile(){return new DiskFile(this.filePath);}
  async createWritable(){return new WritableHandle(this.filePath);}
}
class DirectoryHandle {
  constructor(dirPath){this.dirPath=dirPath;this.name=path.basename(dirPath);this.kind="directory";}
  async getDirectoryHandle(name,opt={}){
    const p=path.join(this.dirPath,name);
    if(opt.create)await fsp.mkdir(p,{recursive:true});
    else if(!(await existsDir(p))){const e=new Error("Directory not found: "+p);e.name="NotFoundError";throw e;}
    return new DirectoryHandle(p);
  }
  async getFileHandle(name,opt={}){
    const p=path.join(this.dirPath,name);
    if(opt.create){await fsp.mkdir(path.dirname(p),{recursive:true});if(!fs.existsSync(p))await fsp.writeFile(p,"");}
    else if(!(await existsFile(p))){const e=new Error("File not found: "+p);e.name="NotFoundError";throw e;}
    return new FileHandle(p);
  }
  async *entries(){
    const list=await fsp.readdir(this.dirPath,{withFileTypes:true});
    list.sort((a,b)=>a.name.localeCompare(b.name));
    for(const d of list)yield [d.name,d.isDirectory()?new DirectoryHandle(path.join(this.dirPath,d.name)):new FileHandle(path.join(this.dirPath,d.name))];
  }
}
async function existsFile(p){try{return (await fsp.stat(p)).isFile();}catch(_){return false;}}
async function existsDir(p){try{return (await fsp.stat(p)).isDirectory();}catch(_){return false;}}

class StubElement {
  constructor(id=""){
    this.id=id;this.textContent="";this.innerHTML="";this.disabled=false;this.className="";
    this.value="";this.checked=false;this.files=[];this.style={};this.children=[];
  }
  addEventListener(){}
  appendChild(x){this.children.push(x);return x;}
  remove(){}
  click(){}
  setAttribute(){}
  getAttribute(){return null;}
}
const elements=new Map();
function getEl(id){if(!elements.has(id))elements.set(id,new StubElement(id));return elements.get(id);}
getEl("wholeModel").checked=true;

const documentStub={
  getElementById:getEl,
  createElement:(tag)=>new StubElement(tag),
  body:new StubElement("body"),
  querySelector:()=>null,
  querySelectorAll:()=>[],
};
class MutationObserverStub { constructor(cb){this.cb=cb;} observe(){} disconnect(){} }

const context={
  console, performance, TextDecoder, TextEncoder, Uint8Array, Uint16Array, Uint32Array, ArrayBuffer,
  DataView, BigInt, Map, Set, Date, Math, JSON, RegExp, String, Number, Boolean, Error, TypeError,
  Promise, Object, Array, parseInt, parseFloat, isFinite, encodeURIComponent, decodeURIComponent,
  Blob:globalThis.Blob, Response:globalThis.Response, DecompressionStream:globalThis.DecompressionStream,
  CompressionStream:globalThis.CompressionStream, crypto:webcrypto, document:documentStub,
  MutationObserver:MutationObserverStub, URL:globalThis.URL,
  setTimeout, clearTimeout, queueMicrotask,
};
context.__attachmentBenchmarkObject=benchmarkObject;
context.window=context;
context.globalThis=context;
context.navigator={userAgent:"node-headless-mdse"};
context.alert=()=>{};
context.confirm=()=>true;

const html=fs.readFileSync(importerPath,"utf8");
const s1=html.indexOf("<script>"),s2=html.lastIndexOf("</script>");
if(s1<0||s2<s1)throw new Error("Importer embedded script missing");
const source=html.slice(s1+8,s2)+`
globalThis.__imp002Capture={endpointFindings:[],entityCtx:null,finalGraph:[]};
const __imp002OriginalSuppress=suppressEndpointFindings;
suppressEndpointFindings=function(graph,findings){
  globalThis.__imp002Capture.endpointFindings=(findings||[]).map(x=>Object.assign({},x));
  const out=__imp002OriginalSuppress(graph,findings);
  globalThis.__imp002Capture.finalGraph=Array.from(graph.entries()).map(([owner,fm])=>[
    owner,Array.from(fm.entries()).map(([field,targets])=>[field,Array.from(targets)])
  ]);
  return out;
};
const __imp002OriginalRender=renderEntityMarkdown;
renderEntityMarkdown=function(e,graph,entityCtx,...rest){
  globalThis.__imp002Capture.entityCtx=entityCtx;
  return __imp002OriginalRender(e,graph,entityCtx,...rest);
};
globalThis.__mdseImp002Audit=function(){
  const cap=globalThis.__imp002Capture||{};
  if(!lastPlannerContext||!cap.entityCtx)throw new Error("IMP-002 audit requires a completed real plan and entity context.");
  const reviewed=(lastPlannerContext.connectorPlans||[]).filter(p=>p.review&&p.field);
  const rawGuidSet=new Set((lastPlannerContext.connectors||[]).map(x=>normGuid(x.ea_guid||x.ConnectorGUID||x.Connector_GUID||"")).filter(Boolean));
  const reviewEvidenceExpected=reviewed.map(p=>{
    const from=cap.entityCtx.entities.get(p.sourceKey),to=cap.entityCtx.entities.get(p.targetKey);
    return {
      source_guid:p.eaGuid||"",
      category:p.field==="tracesTo"?"provisional":"connector review",
      relationship:p.field||"",
      from_type:p.sourceType||"",
      from_name:from?(from.fileName||from.naturalName||from.key):(p.sourceKey||""),
      to_type:p.targetType||"",
      to_name:to?(to.fileName||to.naturalName||to.key):(p.targetKey||""),
      detail:"review-only source connector; not written to canonical YAML; "+(p.rule||"")+(p.detail?"; "+p.detail:"")
    };
  });
  const reviewedMissingRaw=reviewed.filter(p=>!rawGuidSet.has(normGuid(p.eaGuid||""))).map(p=>p.eaGuid||p.sourceId||"");

  let currentPlan=null;
  const writerCalls=[];
  const plans=Array.from(lastPlannerContext.connectorPlans||[]);
  const replayCtx=Object.create(lastPlannerContext);
  replayCtx.connectorPlans={
    [Symbol.iterator]:function(){
      let i=0;
      return {next:function(){
        if(i>=plans.length){currentPlan=null;return {done:true};}
        currentPlan=plans[i++];
        return {value:currentPlan,done:false};
      }};
    }
  };
  const originalAddForwardRel=addForwardRel;
  addForwardRel=function(graph,ownerKey,field,targetKey,allowDuplicate){
    writerCalls.push({
      source_guid:currentPlan&&currentPlan.eaGuid||"",
      review:!!(currentPlan&&currentPlan.review),
      planned_field:currentPlan&&currentPlan.field||"",
      written_field:field,
      ownerKey,targetKey
    });
    return originalAddForwardRel(graph,ownerKey,field,targetKey,allowDuplicate);
  };
  try{
    applyConnectorRelations(new Map(),replayCtx,cap.entityCtx,new Set());
  }finally{
    addForwardRel=originalAddForwardRel;
  }

  const graph=new Map((cap.finalGraph||[]).map(([owner,fields])=>[
    owner,new Map(fields.map(([field,targets])=>[field,Array.from(targets)]))
  ]));
  const hasEdge=(owner,field,target)=>!!(graph.get(owner)&&graph.get(owner).get(field)&&graph.get(owner).get(field).includes(target));
  const endpointFindings=(cap.endpointFindings||[]).map(x=>{
    const owner=cap.entityCtx.entities.get(x.ownerKey),target=cap.entityCtx.entities.get(x.targetKey);
    const inverse=REL_PAIRS[x.field]||(REL_SYMMETRIC.has(x.field)?x.field:"");
    return Object.assign({},x,{
      inverseField:inverse,
      ownerPath:owner&&owner.outputPath||"",
      ownerLink:owner&&(owner.linkTarget||owner.fileName)||"",
      targetPath:target&&target.outputPath||"",
      targetLink:target&&(target.linkTarget||target.fileName)||""
    });
  });
  const remainingSuppressedEdges=[];
  for(const x of endpointFindings){
    if(hasEdge(x.ownerKey,x.field,x.targetKey))remainingSuppressedEdges.push(x.ownerKey+"|"+x.field+"|"+x.targetKey);
    if(x.inverseField&&hasEdge(x.targetKey,x.inverseField,x.ownerKey))remainingSuppressedEdges.push(x.targetKey+"|"+x.inverseField+"|"+x.ownerKey);
  }
  const provisionalGraphEdges=[];
  for(const [owner,fm] of graph.entries()){
    for(const field of ["tracesTo","tracesFrom"]){
      for(const target of (fm.get(field)||[]))provisionalGraphEdges.push(owner+"|"+field+"|"+target);
    }
  }
  const endpointEvidenceExpected=endpointFindings.map(x=>({
    source_guid:"",
    category:x.reason,
    relationship:x.field,
    from_type:x.fromType,
    from_name:x.ownerName,
    to_type:x.toType,
    to_name:x.targetName,
    detail:"off-rule graph relationship suppressed from canonical YAML"
  }));
  return {
    reviewedPlanCount:reviewed.length,
    reviewedWriterCalls:writerCalls.filter(x=>x.review),
    reviewedMissingRaw,
    reviewEvidenceExpected,
    endpointFindingCount:endpointFindings.length,
    endpointFindings,
    endpointEvidenceExpected,
    remainingSuppressedEdges,
    provisionalGraphEdges
  };
};
globalThis.__mdseHeadlessRun = async function(sourceFile, outputHandle){
  attachmentBenchmark=globalThis.__attachmentBenchmarkObject||null;
  selectedFile=sourceFile;
  lastReport=null;lastPlan=null;lastPlannerContext=null;lastSliceReport=null;outputDirHandle=null;
  await analyze();
  const preflight=lastReport?JSON.parse(JSON.stringify(lastReport)):null;
  if(!lastReport||lastReport.result==="FAIL")return {phase:"preflight",preflight,plan:null,slice:null,uiLog:el("log").textContent};
  await buildTranslationPlan();
  const plan=lastPlan?JSON.parse(JSON.stringify(lastPlan)):null;
  if(!lastPlan||lastPlan.result!=="PASS")return {phase:"plan",preflight,plan,slice:null,uiLog:el("log").textContent};
  outputDirHandle=outputHandle;
  el("wholeModel").checked=true;
  el("slicePath").value="";
  await generateSlice();
  const slice=lastSliceReport?JSON.parse(JSON.stringify(lastSliceReport)):null;
  const imp002Audit=slice?globalThis.__mdseImp002Audit():null;
  return {phase:slice?"complete":"write",preflight,plan,slice,imp002Audit,uiLog:el("log").textContent,sliceStatus:el("sliceStatus").textContent};
};
globalThis.__mdseHeadlessRegenerate = async function(outputHandle){
  lastSliceReport=null;
  outputDirHandle=outputHandle;
  el("wholeModel").checked=true;
  el("slicePath").value="";
  await generateSlice();
  const slice=lastSliceReport?JSON.parse(JSON.stringify(lastSliceReport)):null;
  return {phase:slice?"complete":"write",slice,uiLog:el("log").textContent,sliceStatus:el("sliceStatus").textContent};
};
`;

vm.createContext(context);
vm.runInContext(source,context,{filename:importerPath,timeout:120000});

function parseCsv(text){
  const rows=[];let row=[],field="",quoted=false;
  for(let i=0;i<text.length;i++){
    const ch=text[i];
    if(quoted){
      if(ch==='"'&&text[i+1]==='"'){field+='"';i++;continue;}
      if(ch==='"'){quoted=false;continue;}
      field+=ch;continue;
    }
    if(ch==='"'){quoted=true;continue;}
    if(ch===","){row.push(field);field="";continue;}
    if(ch==="\n"){
      row.push(field);field="";
      if(row.length>1||row[0]!=="")rows.push(row);
      row=[];continue;
    }
    if(ch==="\r")continue;
    field+=ch;
  }
  if(field||row.length){row.push(field);rows.push(row);}
  if(!rows.length)return [];
  const header=rows[0];
  return rows.slice(1).map(vals=>Object.fromEntries(header.map((h,i)=>[h,vals[i]||""])));
}
function evidenceKey(r){
  return JSON.stringify([
    r.source_guid||"",r.category||"",r.relationship||"",r.from_type||"",
    r.from_name||"",r.to_type||"",r.to_name||"",r.detail||""
  ]);
}
function multiset(values){
  const m=new Map();
  for(const v of values)m.set(v,(m.get(v)||0)+1);
  return m;
}
function sameMultiset(a,b){
  const ma=multiset(a),mb=multiset(b);
  if(ma.size!==mb.size)return false;
  for(const [k,n] of ma)if(mb.get(k)!==n)return false;
  return true;
}
function frontmatter(text){
  if(!text.startsWith("---\n")&&!text.startsWith("---\r\n"))return "";
  const normalized=text.replace(/\r\n/g,"\n");
  const end=normalized.indexOf("\n---\n",4);
  return end<0?"":normalized.slice(4,end);
}
function relationValues(text,field){
  const fm=frontmatter(text), lines=fm.split("\n"),out=[];
  for(let i=0;i<lines.length;i++){
    if(lines[i]!==field+":")continue;
    for(let j=i+1;j<lines.length&&/^  - /.test(lines[j]);j++){
      const raw=lines[j].slice(4);
      try{out.push(JSON.parse(raw));}catch(_){out.push(raw);}
    }
  }
  return out;
}
function allMarkdownFiles(root){
  const out=[],stack=[root];
  while(stack.length){
    const dir=stack.pop();
    for(const ent of fs.readdirSync(dir,{withFileTypes:true})){
      if(ent.name===".git")continue;
      const p=path.join(dir,ent.name);
      if(ent.isDirectory())stack.push(p);
      else if(ent.isFile()&&ent.name.toLowerCase().endsWith(".md"))out.push(p);
    }
  }
  return out;
}
function manifestNumber(text,label){
  const prefix="- "+label+":";
  const line=String(text||"").replace(/\r\n/g,"\n").split("\n").find(x=>x.startsWith(prefix));
  if(!line)return null;
  const n=Number(line.slice(prefix.length).trim());
  return Number.isFinite(n)?n:null;
}
function validateImp002(result,root){
  const audit=result&&result.imp002Audit;
  if(!audit)throw new Error("IMP-002 audit missing from completed import");

  if(audit.reviewedWriterCalls.length){
    throw new Error("IMP-002: "+audit.reviewedWriterCalls.length+" reviewed connector plan(s) invoked the canonical relationship writer");
  }
  if(audit.reviewedMissingRaw.length){
    throw new Error("IMP-002: "+audit.reviewedMissingRaw.length+" reviewed connector GUID(s) do not resolve to raw t_connector rows");
  }
  if(audit.remainingSuppressedEdges.length){
    throw new Error("IMP-002: "+audit.remainingSuppressedEdges.length+" off-rule/provisional graph edge(s) remain after suppression");
  }
  if(audit.provisionalGraphEdges.length){
    throw new Error("IMP-002: "+audit.provisionalGraphEdges.length+" provisional tracesTo/tracesFrom graph edge(s) remain");
  }

  const evidencePath=path.join(root,"99_System/11_Import/Review - Semantic and Connectors.csv");
  const manifestPath=path.join(root,"99_System/11_Import/Run Manifest.md");
  const rows=parseCsv(fs.readFileSync(evidencePath,"utf8"));
  const manifest=fs.readFileSync(manifestPath,"utf8");
  const reviewRows=rows.filter(r=>(r.detail||"").startsWith("review-only source connector; not written to canonical YAML;"));
  const suppressedRows=rows.filter(r=>(r.detail||"")==="off-rule graph relationship suppressed from canonical YAML");

  if(!sameMultiset(reviewRows.map(evidenceKey),audit.reviewEvidenceExpected.map(evidenceKey))){
    throw new Error("IMP-002: review-only connector evidence does not exactly match the real planner review set");
  }
  if(!sameMultiset(suppressedRows.map(evidenceKey),audit.endpointEvidenceExpected.map(evidenceKey))){
    throw new Error("IMP-002: suppressed endpoint evidence does not exactly match the real endpoint finding set");
  }

  const manifestReviewed=manifestNumber(manifest,"Review-only connector mappings withheld from canonical YAML");
  const manifestSuppressed=manifestNumber(manifest,"Off-rule graph relationships suppressed before write");
  if(manifestReviewed!==audit.reviewedPlanCount||reviewRows.length!==audit.reviewedPlanCount){
    throw new Error("IMP-002: manifest/review evidence reviewed-connector counts disagree");
  }
  if(manifestSuppressed!==audit.endpointFindingCount||suppressedRows.length!==audit.endpointFindingCount){
    throw new Error("IMP-002: manifest/review evidence suppressed-edge counts disagree");
  }

  let yamlSuppressedHits=0;
  for(const x of audit.endpointFindings){
    if(!x.ownerPath||!x.targetPath)throw new Error("IMP-002: suppressed finding lacks emitted owner/target path");
    const ownerText=fs.readFileSync(path.join(root,x.ownerPath),"utf8");
    const targetLink="[["+(x.targetLink||"")+"]]";
    if(relationValues(ownerText,x.field).includes(targetLink))yamlSuppressedHits++;
    if(x.inverseField){
      const targetText=fs.readFileSync(path.join(root,x.targetPath),"utf8");
      const ownerLink="[["+(x.ownerLink||"")+"]]";
      if(relationValues(targetText,x.inverseField).includes(ownerLink))yamlSuppressedHits++;
    }
  }
  if(yamlSuppressedHits)throw new Error("IMP-002: "+yamlSuppressedHits+" suppressed relationship value(s) are still present in written YAML");

  let provisionalYamlValues=0;
  for(const p of allMarkdownFiles(root)){
    const text=fs.readFileSync(p,"utf8");
    provisionalYamlValues+=relationValues(text,"tracesTo").length;
    provisionalYamlValues+=relationValues(text,"tracesFrom").length;
  }
  if(provisionalYamlValues)throw new Error("IMP-002: "+provisionalYamlValues+" provisional tracesTo/tracesFrom value(s) exist in written YAML");

  return {
    reviewedConnectorPlans:audit.reviewedPlanCount,
    reviewedConnectorEvidence:reviewRows.length,
    reviewedWriterCalls:0,
    suppressedEndpointFindings:audit.endpointFindingCount,
    suppressedEndpointEvidence:suppressedRows.length,
    suppressedYamlValues:0,
    provisionalYamlValues:0
  };
}

(async()=>{
  const result=await context.__mdseHeadlessRun(new DiskFile(sourcePath),new DirectoryHandle(outputPath));
  const summary={
    phase:result.phase,
    preflight:result.preflight&&{
      result:result.preflight.result,
      source:result.preflight.source,
      issues:result.preflight.issues,
      elementTypes:result.preflight.elementTypes,
      connectorTypes:result.preflight.connectorTypes
    },
    plan:result.plan&&{
      result:result.plan.result,
      counts:result.plan.counts,
      notes:result.plan.notes,
      portPlan:result.plan.portPlan,
      issues:result.plan.issues
    },
    slice:result.slice,
    imp002Audit:result.imp002Audit&&{
      reviewedPlanCount:result.imp002Audit.reviewedPlanCount,
      reviewedWriterCallCount:result.imp002Audit.reviewedWriterCalls.length,
      reviewedMissingRawCount:result.imp002Audit.reviewedMissingRaw.length,
      endpointFindingCount:result.imp002Audit.endpointFindingCount,
      remainingSuppressedEdgeCount:result.imp002Audit.remainingSuppressedEdges.length,
      provisionalGraphEdgeCount:result.imp002Audit.provisionalGraphEdges.length
    },
    sliceStatus:result.sliceStatus,
    uiLog:result.uiLog
  };
  console.log("HEADLESS_RESULT_BEGIN");
  console.log(JSON.stringify(summary,null,2));
  console.log("HEADLESS_RESULT_END");
  if(result.phase!=="complete"||!result.slice||result.slice.result!=="WRITE_PASS"){
    process.exitCode=1;
    return;
  }
  const imp002=validateImp002(result,outputPath);
  console.log("IMP002_AUDIT "+JSON.stringify(imp002));
  if(secondOutputPath){
    const second=await context.__mdseHeadlessRegenerate(new DirectoryHandle(secondOutputPath));
    console.log("HEADLESS_SECOND_RESULT_BEGIN");
    console.log(JSON.stringify(second,null,2));
    console.log("HEADLESS_SECOND_RESULT_END");
    if(second.phase!=="complete"||!second.slice||second.slice.result!=="WRITE_PASS")process.exitCode=1;
  }
})().catch(err=>{console.error(err&&err.stack?err.stack:err);process.exitCode=1;});
