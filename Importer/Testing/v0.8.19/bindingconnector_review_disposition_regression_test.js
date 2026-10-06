#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");

function extract(name){
  const start=src.indexOf("function "+name+"(");
  if(start<0)throw new Error("missing "+name);
  const next=src.indexOf("\nfunction ",start+10);
  if(next<0)throw new Error("missing boundary after "+name);
  return src.slice(start,next).trim();
}
function n2(v){const n=Number(v);return Number.isFinite(n)?Math.trunc(n):0;}
const code=[extract("prefixPath"),extract("bindingReviewDisposition"),"return {bindingReviewDisposition};"].join("\n");
const api=new Function("n2",code)(n2);

function ep(sourceId,ownerKey,path,parentPath){
  return {kind:"endpoint",sourceId,ownerKey,path,parentPath,localId:"ep-"+sourceId,anchor:"^ep-"+sourceId,equalsRefs:[]};
}
function local(endpoints,connections){
  return {endpointBySource:new Map(endpoints.map(x=>[x.sourceId,x])),connectionsByOwner:new Map(connections||[])};
}
function con(id,a,b){return {Connector_ID:id,Start_Object_ID:a,End_Object_ID:b};}
function expect(actual,expected,label){if(actual!==expected)throw new Error(label+": expected "+expected+", got "+actual);}

const outer=ep(1,"owner",["J1"],[]);
const inner=ep(2,"owner",["P1","J1"],["P1"]);
const c0=con(100,1,2);
let lm=local([outer,inner],[["owner",[]]]);
const outerKey="local:"+outer.ownerKey+":"+outer.path.join("/");
const innerKey="local:"+inner.ownerKey+":"+inner.path.join("/");
outer.equalsRefs=[{refKey:innerKey}];inner.equalsRefs=[{refKey:outerKey}];
let d=api.bindingReviewDisposition(c0,lm);
expect(d.category,"temporary local equals - no internal Connection","zero-candidate equals category");
expect(d.actualRelation,"Interface.equals (temporary)","zero-candidate equals relation");
expect(d.candidateConnections.length,0,"zero-candidate count");

outer.equalsRefs=[];inner.equalsRefs=[];
const realConn={localId:"conn-1",ownerKey:"owner",sourceIds:[200,100],
  endpointA:{kind:"endpoint",refKey:innerKey},
  endpointB:{kind:"endpoint",refKey:"local:owner:P1/J2"},
  exposesRefs:[{kind:"endpoint",refKey:outerKey}]};
lm=local([outer,inner],[["owner",[realConn]]]);
d=api.bindingReviewDisposition(c0,lm);
expect(d.category,"resolved Connection.exposes","exposure category");
expect(d.actualRelation,"Connection.exposes","exposure relation");
expect(d.connection.localId,"conn-1","exposure connection");
expect(d.exposes.localId,outer.localId,"exposure endpoint occurrence");
expect(d.candidateConnections.length,1,"exposure candidate count");

const deep=ep(4,"owner",["P1","P2","J1"],["P1","P2"]);
lm=local([inner,deep],[["owner",[]]]);
d=api.bindingReviewDisposition(con(101,2,4),lm);
expect(d.category,"same-owner nested internal binding","nested category");
expect(d.actualRelation,"","nested writes no relation");

const sib=ep(5,"owner",["P2","J1"],["P2"]);
lm=local([inner,sib],[["owner",[]]]);
d=api.bindingReviewDisposition(con(102,2,5),lm);
expect(d.category,"same-owner sibling/non-hierarchical binding","sibling category");

const other=ep(6,"other",["J1"],[]);
lm=local([outer,other],[["owner",[]],["other",[]]]);
d=api.bindingReviewDisposition(con(103,1,6),lm);
expect(d.category,"cross-owner binding","cross-owner category");

if(src.includes('sameOwner?"temporary local equals":"unresolved contextual owner/endpoints"'))
  throw new Error("legacy owner-geometry category logic remains");
for(const h of ["actual_relation","root_cause","connection_local","candidate_connection_count"]){
  if(!src.includes('"'+h+'"'))throw new Error("review CSV missing "+h);
}
console.log("v0.8.19 BindingConnector review disposition regression: PASS");
