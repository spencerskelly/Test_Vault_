#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.12/EA_to_MDSE_Native_Importer_v0.8.12.html");
const src=fs.readFileSync(importer,"utf8");
const fn=src.indexOf("function applyConnectorRelations");
const skip=src.indexOf("if(p.review){",fn);
const write=src.indexOf('if(ct==="Connector"){',fn);
if(skip<0||write<0||skip>write)throw new Error("reviewed connector is not skipped before canonical relation writing");
if(!src.includes("function suppressEndpointFindings"))throw new Error("endpoint suppression helper missing");
const suppress=src.indexOf("suppressEndpointFindings(graph,endpointFindings);");
const validate=src.indexOf("for(const [k,fm] of graph.entries())",suppress);
if(suppress<0||validate<suppress)throw new Error("off-rule relationships are not suppressed before validation");
for(const t of [
  "review-only source connector; not written to canonical YAML;",
  "off-rule graph relationship suppressed from canonical YAML",
  "Review-only connector mappings withheld from canonical YAML",
  "Off-rule graph relationships suppressed before write"
])if(!src.includes(t))throw new Error("missing review evidence text: "+t);
console.log("v0.8.12 canonical relationship boundary checks: PASS");
