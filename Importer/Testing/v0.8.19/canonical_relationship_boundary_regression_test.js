#!/usr/bin/env node
"use strict";

const fs=require("fs");
const path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");

const fn=src.indexOf("function applyConnectorRelations");
const reviewSkip=src.indexOf("if(p.review){",fn);
const firstConnectorWrite=src.indexOf('if(ct==="Connector"){',fn);
if(fn<0||reviewSkip<0||firstConnectorWrite<0||reviewSkip>firstConnectorWrite){
  throw new Error("reviewed connector is not skipped before canonical relation writing");
}

const collect=src.indexOf("const endpointFindings=collectEndpointFindings(graph,entities);");
const suppress=src.indexOf("suppressEndpointFindings(graph,endpointFindings);",collect);
const validate=src.indexOf("for(const [k,fm] of graph.entries())",suppress);
if(collect<0||suppress<0||validate<0||!(collect<suppress&&suppress<validate)){
  throw new Error("off-rule/provisional graph findings are not suppressed before canonical validation/render");
}

for(const token of [
  "review-only source connector; not written to canonical YAML;",
  "off-rule graph relationship suppressed from canonical YAML",
  "Review-only connector mappings withheld from canonical YAML",
  "Off-rule graph relationships suppressed before write"
]){
  if(!src.includes(token))throw new Error("missing governed relationship-boundary evidence token: "+token);
}

console.log("IMP-002 canonical relationship boundary regression: PASS");
