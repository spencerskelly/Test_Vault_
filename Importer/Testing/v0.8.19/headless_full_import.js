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
context.window=context;
context.globalThis=context;
context.navigator={userAgent:"node-headless-mdse"};
context.alert=()=>{};
context.confirm=()=>true;

const html=fs.readFileSync(importerPath,"utf8");
const s1=html.indexOf("<script>"),s2=html.lastIndexOf("</script>");
if(s1<0||s2<s1)throw new Error("Importer embedded script missing");
const source=html.slice(s1+8,s2)+`
globalThis.__mdseHeadlessRun = async function(sourceFile, outputHandle){
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
  return {phase:slice?"complete":"write",preflight,plan,slice,uiLog:el("log").textContent,sliceStatus:el("sliceStatus").textContent};
};
`;

vm.createContext(context);
vm.runInContext(source,context,{filename:importerPath,timeout:120000});

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
    sliceStatus:result.sliceStatus,
    uiLog:result.uiLog
  };
  console.log("HEADLESS_RESULT_BEGIN");
  console.log(JSON.stringify(summary,null,2));
  console.log("HEADLESS_RESULT_END");
  if(result.phase!=="complete"||!result.slice||result.slice.result!=="WRITE_PASS")process.exitCode=1;
})().catch(err=>{console.error(err&&err.stack?err.stack:err);process.exitCode=1;});
