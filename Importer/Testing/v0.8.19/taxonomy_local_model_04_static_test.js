#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}

need('version: "0.8.19"',"version");
need('const REL_SCHEMA_VERSION="1.36";',"relationship schema");
need('const ELEMENT_SCHEMA_VERSION="1.18";',"element schema");
need('const LOCAL_MODEL_SCHEMA_VERSION="0.4";',"local schema");
need('const LOCAL_BODY_SCHEMA="0.4";',"rendered local schema");

need('if(stereotypeIncludes(raw,"function")||pkg.vaultNames(raw.Package_ID).includes("04 Product Function"))return "function";',
  "Activity function precedence");
need('else{p.mdseType="Behavior";p.subtype=behaviorSubtype(raw,pkg);p.rule="W-384";}',
  "Activity -> Behavior");
need('p.outcome="note";p.mdseType="Behavior";p.subtype="action";p.rule="W-384";',
  "Action -> Behavior/action");
need('p.outcome="note";p.mdseType="Behavior";p.subtype="step";p.rule="W-384";',
  "Step -> Behavior/step");
need('p.outcome="note";p.mdseType="Condition";p.subtype=conditionSubtype(raw,pkg);p.rule="W-384";',
  "State -> Condition");
need('p.outcome="note";p.mdseType="Condition";p.subtype="state machine";p.rule="W-384";',
  "StateMachine -> Condition/state machine");
need('} else if(t==="Mode"){\n      p.outcome="note";p.mdseType="Condition";p.subtype="mode";p.rule="W-384";',
  "Mode -> Condition/mode as its own source type");
forbid('if(stereotypeIncludes(raw,"mode"))return "mode";',
  "EA State stereotype must not silently become Mode");

need('if(INTERFACE_CLASS_STEREOTYPES.has(st)){p.subtype="interface";p.rule="W-384";}',
  "Interface Class -> Object/interface");
need('else{p.outcome="local endpoint";p.mdseType="";p.subtype="";p.rule="W-384";p.targetKey=q.resolvedKey||"";}',
  "EA Port -> local endpoint only");
forbid('p.mdseType="Port"',"Port note classification removed");
forbid('p.mdseType="Function"',"Function class removed");
forbid('p.mdseType="State"',"State class removed");
forbid('p.mdseType="Design"',"Design class removed");
forbid('p.mdseType="State Machine"',"State Machine class removed");

need('if(pt==="Class"){\n      ownerKey=firstClassKeyForRaw(parent.Object_ID);parentPath=[];',
  "Class-owned Ports become boundary Interfaces");
need('lines.push("### Parts","");',"0.4 Parts heading");
need('lines.push("### Interfaces","");',"0.4 Interfaces heading");
forbid('lines.push("### Part Occurrences","");',"0.3 Parts heading not written by 0.4");
forbid('lines.push("### Local Interfaces","");',"0.3 Interface heading not written by 0.4");

need('if(conn.exposesRefs&&conn.exposesRefs.length)lines.push("- exposes: "+conn.exposesRefs.map(x=>localRefLink(localModel,x,e)).join(", "));',
  "Connection owns exposes");
need('resolved as Connection exposes -> boundary Interface',"binding exposure resolution");
need('definition is not Object / interface',"Interface occurrence definition validator");
need('exposes target is not an assembly-boundary Interface',"Connection exposes boundary validator");
need('conn.sourceIds.includes(n2(bc.Connector_ID))',"BindingConnector provenance carried into exposed Connection");
need('could not be deterministically resolved to one internal Connection exposure; temporary equals/review evidence retained.',
  "ambiguous binding remains review evidence");

need('W-384: EA Ports are Local Model Interface occurrences only. No note-level Port ownership,',
  "note-level Port graph removed");
forbid('addForwardRel(graph,ownerKey,"hasPort"', "hasPort graph write removed");
forbid('base.field="interfaces";base.rule="W-153/W-155"', "Port interfaces relationship removed");

const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 taxonomy/Local Model 0.4 regression: PASS");
