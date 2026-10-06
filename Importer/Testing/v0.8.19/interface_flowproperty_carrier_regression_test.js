#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const importer = path.resolve(__dirname, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

function need(text,label){if(!src.includes(text))throw new Error(label+": missing "+text);}
function forbid(text,label){if(src.includes(text))throw new Error(label+": forbidden "+text);}

need('function exactInterfaceFlowCopyTarget(raw,byId,byGuidNorm)', "exact-copy classifier");
need('p.outcome="folded";p.rule="W-397";p.targetKey=planKey("object",flowCopy.Object_ID);', "copy folds to FlowProperty definition");
need('owner.type==="Object"&&owner.plan&&owner.plan.subtype==="interface"&&child.type==="Item Flow"', "interface FlowProperty ownership guard");
need('addForwardRel(graph,owner.key,"hasChild",child.key,false);', "current generic ownership");
need('definitionEntity.mdseType==="Item Flow"&&p.rule==="W-397"', "no structural Local Model Part for exact flow copy");
need('partBySource.set(id,null);', "handled/rejected Part caching");
need('const partBySource=new Map(), endpointBySource=new Map(), warnings=[], warningKeys=new Set()', "warning dedupe key set");
need('parts:Array.from(partsByOwner.values()).reduce((n,a)=>n+a.length,0)', "Local Model Part stats count emitted records only");
forbid('parts:Array.from(partBySource.values()).length', "handled null cache entries must not inflate Local Model Part stats");
need('"Detection","direction"', "direction retained");
need('name==="direction"?"Direction":name', "human-facing direction label");
need('"- FlowProperty type: "', "FlowProperty type source evidence");
forbid('hasFlow:{', "do not revive obsolete Port-note hasFlow schema");

const badCall='ownerField(owner.type,child.type,child.plan&&child.plan.subtype)';
if(src.includes(badCall))throw new Error("W-396 folded Part ownerField argument-order regression returned");

const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 IMP-010C Interface FlowProperty regression: PASS");
