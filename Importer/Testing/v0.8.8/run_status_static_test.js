#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.8/EA_to_MDSE_Native_Importer_v0.8.8.html");
const src=fs.readFileSync(importer,"utf8");
const required=[
  'version: "0.8.8"',
  '"- Source status: "+sourceStatus',
  '"- Plan status: "+planStatus',
  '"- Write status: WRITE_PASS',
  '"- Semantic status: "+semanticStatus',
  '"- Acceptance status: "+acceptanceStatus',
  'result:"WRITE_PASS"',
  'write:status==="IMPORT_COMPLETE"?"WRITE_PASS":(status==="IMPORT_FAILED"?"WRITE_FAIL":"WRITE_IN_PROGRESS")'
];
for(const s of required)if(!src.includes(s))throw new Error("missing status contract: "+s);
if(src.includes('"- Result: PASS (implementation candidate'))throw new Error("generic PASS manifest line still present");
console.log("v0.8.8 run-status static checks: PASS");
