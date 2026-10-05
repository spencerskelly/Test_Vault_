#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.18/EA_to_MDSE_Native_Importer_v0.8.18.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
need('version: "0.8.18"',"version");
need('function machineNoiseName(v)',"machine-noise classifier");
need('function safeHumanAlias(v)',"safe alias preference");
need('return context+" - external reference";',"context-derived fallback");
need('if(rawName&&machineNoiseName(rawName))name=alias||fallbackReferenceName(e);',"machine-noise naming rule");
need('if(hasChildren){outSegs.push(e.fileName);changed=true;}',"parent note inside parent folder");
need('for(const p of parents){outSegs.push(p.fileName);changed=true;}',"nested parent folders");
forbid('folderRepeatsFile',"source-folder removal heuristic");
const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.18 naming/placement regression: PASS");
