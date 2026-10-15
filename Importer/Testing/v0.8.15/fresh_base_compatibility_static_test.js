#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.15/EA_to_MDSE_Native_Importer_v0.8.15.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
need('version: "0.8.15"',"version");
need('const LOCAL_MODEL_SCHEMA_VERSION="0.3";',"Local Model 0.3");
need('async function requireBaseVault(root,allowUninitialized=false)',"fresh-base inspection path");
need('const initialized=!!vaultUid&&vaultUid.toUpperCase()!=="UNINITIALIZED";',"uninitialized detection");
need('const base=await requireBaseVault(candidate,true);',"uninitialized base selectable");
need('id="initializeOutput"',"explicit initialization control");
need('async function initializeSelectedBase()',"initializer implementation");
need('/^[a-z-]{13}$/.test(author)',"governed author-code validation");
need('await writeTextPath(outputDirHandle,".vault.yaml",text);',"vault identity write");
need('const verified=await requireBaseVault(outputDirHandle,false);',"strict revalidation");
need('el("generateSlice").disabled=true;',"write remains blockable");
need('Fresh base — initialization required',"fresh-base UX status");
forbid('Run the governed vault initializer before selecting this destination.',"old false incompatibility instruction");
forbid('Local Model 0.2 records',"stale Local Model UI text");
const scripts=[...src.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
if(scripts.length!==1)throw new Error("expected one embedded script");
new Function(scripts[0]);
console.log("v0.8.15 fresh-base compatibility regression: PASS");
