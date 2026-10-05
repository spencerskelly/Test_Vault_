#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.17/EA_to_MDSE_Native_Importer_v0.8.17.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
need('version: "0.8.17"',"version");
need('function transientFsStateError(e)',"transient filesystem classifier");
need('const maxAttempts=4;',"bounded write retry");
need('await fsRetryPause(attempt);',"retry yield");
need('w.fsTransient=transientFsStateError(e);',"error type preserved");
need('const parts=path.split("/"),name=parts.pop(),d=await dirFor(root,parts,true);',"directory reacquired per attempt");
need('err.fsTransient||err.name==="InvalidStateError"', "outer transaction recognizes filesystem state failure");
const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.17 filesystem resilience regression: PASS");
