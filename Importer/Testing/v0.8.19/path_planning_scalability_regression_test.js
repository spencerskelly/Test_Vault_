#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
need("const hasChildrenKeys=new Set();","precomputed child-owner set");
need("for(const x of entities.values())if(x.parentEntityKey)hasChildrenKeys.add(x.parentEntityKey);","single whole-model child scan");
need("pathPlanForEntity(e,folderMap,entities,hasChildrenKeys)","production path planner uses precomputed child set");
need("hasChildrenKeys?hasChildrenKeys.has(e.key):false","constant-time child lookup");
const planStart=src.indexOf("function planOutputPaths");
const planEnd=src.indexOf("\nasync function generateSlice",planStart);
if(planStart<0||planEnd<0)throw new Error("planOutputPaths region missing");
const plan=src.slice(planStart,planEnd);
if((plan.match(/pathPlanForEntity\(/g)||[]).length!==1)throw new Error("unexpected path planner call count in planOutputPaths");
const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 path-planning scalability regression: PASS");
