#!/usr/bin/env node
"use strict";

const fs=require("fs");
const path=require("path");
const vm=require("vm");

const root=path.resolve(__dirname,"../../..");
const profile=JSON.parse(fs.readFileSync(path.join(root,"Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json"),"utf8"));
const html=fs.readFileSync(path.join(root,"Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html"),"utf8");

const dispositions=profile.tableDispositions;
if(!dispositions||Object.keys(dispositions).length!==100)throw new Error("expected complete 100-table EA8647 disposition inventory");
if(dispositions.t_operationparams!=="imported"||profile.expected.tables.t_operationparams!==0)throw new Error("empty importer-used t_operationparams is not governed");
const allowed=new Set(["imported","ignored_nonempty_approved","ignored_must_be_empty"]);
for(const [name,disposition] of Object.entries(dispositions)){
  if(!allowed.has(disposition))throw new Error("unknown disposition "+name+"="+disposition);
}
for(const name of Object.keys(profile.expected.tables)){
  if(dispositions[name]!=="imported")throw new Error("count-gated table is not imported: "+name);
}

function extractFunction(name){
  const marker="function "+name+"(";
  const start=html.indexOf(marker);
  if(start<0)throw new Error("runtime function missing: "+name);
  const brace=html.indexOf("{",start);
  let depth=0,quote=null,escaped=false;
  for(let i=brace;i<html.length;i++){
    const ch=html[i];
    if(quote){
      if(escaped){escaped=false;continue;}
      if(ch==="\\"){escaped=true;continue;}
      if(ch===quote)quote=null;
      continue;
    }
    if(ch==='"'||ch==="'"||ch==="`"){quote=ch;continue;}
    if(ch==="{")depth++;
    else if(ch==="}"&&--depth===0)return html.slice(start,i+1);
  }
  throw new Error("unterminated function "+name);
}

const ctx={TABLE_DISPOSITIONS:dispositions,EXPECTED_TABLES:profile.expected.tables,Map,Object,String};
vm.createContext(ctx);
vm.runInContext(extractFunction("applyTableDispositionPolicy")+"\nthis.__apply=applyTableDispositionPolicy;",ctx);

function baseline(){
  const tables=new Map();
  const diagnostics={};
  for(const [name,disposition] of Object.entries(dispositions)){
    tables.set(name.toLowerCase(),{name});
    diagnostics[name]={
      name,
      present:true,
      rows:disposition==="imported"?profile.expected.tables[name]:(disposition==="ignored_must_be_empty"?0:1)
    };
  }
  return {reader:{tables},diagnostics};
}
function run(setup){
  const b=baseline();
  if(setup)setup(b);
  const issues=[];
  ctx.__apply(b.reader,b.diagnostics,issues);
  return issues;
}
function expectCode(code,setup){
  const issues=run(setup);
  if(!issues.some(i=>i.code===code))throw new Error("expected "+code+" but got "+JSON.stringify(issues));
}

if(run().length)throw new Error("accepted disposition inventory unexpectedly fails");
expectCode("TABLE_DISPOSITION_MISSING",b=>b.reader.tables.set("__new_table",{name:"__new_table"}));

const emptyName=Object.keys(dispositions).find(n=>dispositions[n]==="ignored_must_be_empty");
expectCode("TABLE_DISPOSITION_NONEMPTY",b=>{b.diagnostics[emptyName].rows=1;});

const missingName=Object.keys(dispositions)[0];
expectCode("TABLE_DISPOSITION_TABLE_MISSING",b=>{b.reader.tables.delete(missingName.toLowerCase());b.diagnostics[missingName]={name:missingName,present:false,rows:0};});

const importedName=Object.keys(profile.expected.tables)[0];
expectCode("TABLE_COUNT_DIFF",b=>{b.diagnostics[importedName].rows=profile.expected.tables[importedName]+1;});

const approvedName=Object.keys(dispositions).find(n=>dispositions[n]==="ignored_nonempty_approved");
const approvedIssues=run(b=>{b.diagnostics[approvedName].rows=999999;});
if(approvedIssues.length)throw new Error("explicitly approved ignored nonempty table should not be exact-count gated");

for(const token of [
  'code:"TABLE_DISPOSITION_MISSING"',
  'code:"TABLE_DISPOSITION_TABLE_MISSING"',
  'code:"TABLE_DISPOSITION_NONEMPTY"',
  'tableDispositions:TABLE_DISPOSITIONS'
]){
  if(!html.includes(token))throw new Error("runtime IMP-008 token missing: "+token);
}

console.log("IMP-008 table disposition regression: PASS");
