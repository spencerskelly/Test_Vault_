#!/usr/bin/env node
"use strict";

const fs=require("fs"),fsp=require("fs/promises"),path=require("path"),vm=require("vm");

const importerPath=path.resolve(process.argv[2]||"");
const sourcePath=path.resolve(process.argv[3]||"");
const evidenceRoot=path.resolve(process.argv[4]||"");
const headlessLog=path.resolve(process.argv[5]||"");
if(!importerPath||!sourcePath||!evidenceRoot||!headlessLog){
  console.error("Usage: node source_fingerprint_real_acceptance.js <importer-html> <source-qeax> <evidence-root> <headless-log>");
  process.exit(2);
}

const src=fs.readFileSync(importerPath,"utf8");
const a=src.indexOf("function rotr32"),b=src.indexOf("class SQLiteReader",a);
if(a<0||b<a)throw new Error("current v0.8.19 streaming SHA-256 block not found");

const sandbox={Uint8Array,Uint32Array,BigInt,Number,Array,Math,tick:async()=>{}};
vm.createContext(sandbox);
vm.runInContext(src.slice(a,b)+";this.sha256FileHex=sha256FileHex;",sandbox,{filename:"v0819-sha256-production.js"});
const sha256FileHex=sandbox.sha256FileHex;

class DiskFile{
  constructor(filePath){
    this.filePath=filePath;
    this.name=path.basename(filePath);
    const st=fs.statSync(filePath);
    this.size=st.size;
    this.lastModified=st.mtimeMs;
  }
  slice(start=0,end=this.size){
    start=Math.max(0,Number(start)||0);
    end=Math.min(this.size,end==null?this.size:Number(end));
    const filePath=this.filePath;
    return {
      async arrayBuffer(){
        const len=Math.max(0,end-start);
        const fh=await fsp.open(filePath,"r");
        try{
          const buf=Buffer.allocUnsafe(len);
          if(len)await fh.read(buf,0,len,start);
          return buf.buffer.slice(buf.byteOffset,buf.byteOffset+buf.byteLength);
        }finally{await fh.close();}
      }
    };
  }
}

class ByteFlipDiskFile extends DiskFile{
  constructor(filePath,offset){super(filePath);this.offset=offset;this.name=path.basename(filePath).replace(/\.qeax?$/i,"")+"_one-byte-changed.qeax";}
  slice(start=0,end=this.size){
    start=Math.max(0,Number(start)||0);
    end=Math.min(this.size,end==null?this.size:Number(end));
    const base=super.slice(start,end),offset=this.offset;
    return {
      async arrayBuffer(){
        const ab=await base.arrayBuffer();
        const bytes=new Uint8Array(ab);
        if(offset>=start&&offset<end)bytes[offset-start]^=0x01;
        return bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength);
      }
    };
  }
}

function findFile(root,name){
  const stack=[root];
  while(stack.length){
    const dir=stack.pop();
    for(const ent of fs.readdirSync(dir,{withFileTypes:true})){
      const p=path.join(dir,ent.name);
      if(ent.isDirectory())stack.push(p);
      else if(ent.isFile()&&ent.name===name)return p;
    }
  }
  throw new Error("Evidence file not found: "+name);
}

function extractHeadlessPreflightDigest(text){
  const start=text.indexOf("HEADLESS_RESULT_BEGIN");
  const end=text.indexOf("HEADLESS_RESULT_END",start);
  if(start<0||end<0)throw new Error("HEADLESS_RESULT markers missing from log");
  const body=text.slice(start+"HEADLESS_RESULT_BEGIN".length,end).trim();
  const parsed=JSON.parse(body);
  const digest=parsed&&parsed.preflight&&parsed.preflight.source&&parsed.preflight.source.sha256;
  if(!/^[0-9a-f]{64}$/.test(String(digest||"")))throw new Error("preflight digest missing/invalid in headless log");
  return digest;
}

function manifestDigest(text){
  const m=/^- Source SHA-256:\s*([0-9a-f]{64})\s*$/mi.exec(text);
  if(!m)throw new Error("Run Manifest source SHA-256 missing");
  return m[1].toLowerCase();
}

(async()=>{
  const cleanFile=new DiskFile(sourcePath);
  const clean=String(await sha256FileHex(cleanFile)).toLowerCase();
  if(!/^[0-9a-f]{64}$/.test(clean))throw new Error("production clean SHA-256 is invalid");

  const flipOffset=Math.floor(cleanFile.size/2);
  const changed=String(await sha256FileHex(new ByteFlipDiskFile(sourcePath,flipOffset))).toLowerCase();
  if(!/^[0-9a-f]{64}$/.test(changed))throw new Error("production changed-byte SHA-256 is invalid");
  if(changed===clean)throw new Error("one-byte source mutation did not change SHA-256");

  const importStatePath=findFile(evidenceRoot,"Import State.json");
  const manifestPath=findFile(evidenceRoot,"Run Manifest.md");
  const state=JSON.parse(fs.readFileSync(importStatePath,"utf8"));
  const stateDigest=String(state&&state.source&&state.source.sha256||"").toLowerCase();
  const manifest=manifestDigest(fs.readFileSync(manifestPath,"utf8"));
  const preflight=extractHeadlessPreflightDigest(fs.readFileSync(headlessLog,"utf8")).toLowerCase();

  for(const [label,digest] of [["preflight",preflight],["transaction",stateDigest],["manifest",manifest]]){
    if(digest!==clean)throw new Error(label+" digest does not match production hash of exact source: "+digest+" != "+clean);
  }
  if(state.status!=="IMPORT_COMPLETE")throw new Error("evidence transaction is not IMPORT_COMPLETE");

  console.log("IMP006_SOURCE_FINGERPRINT_AUDIT "+JSON.stringify({
    source:path.basename(sourcePath),
    size:cleanFile.size,
    cleanSha256:clean,
    preflightSha256:preflight,
    transactionSha256:stateDigest,
    manifestSha256:manifest,
    changedByteOffset:flipOffset,
    changedSha256:changed,
    changedDigestDifferent:changed!==clean
  }));
})().catch(err=>{console.error(err&&err.stack?err.stack:err);process.exit(1);});
