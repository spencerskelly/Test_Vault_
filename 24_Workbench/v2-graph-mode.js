/* MDSE v2 STEP-02Y: local read-only graph panel in existing Workbench. */
(()=>{"use strict";
const el=(t,parent,text)=>{const x=document.createElement(t);x.textContent=text||"";parent.append(x);return x};
const bar=el("section",document.body);bar.style.cssText="padding:16px;background:#142238;color:#dce8f4;border-top:2px solid #567";
el("h2",bar,"MDSE graph navigation (STEP-02W)");
const files=el("input",bar);files.type="file";files.accept=".jsonl";files.multiple=true;
const search=el("input",bar);search.placeholder="Search UID, path or kind";search.setAttribute("aria-label","Search graph");
const status=el("p",bar,"Load local nodes.jsonl and edges.jsonl. Existing SysML preview is unaffected.");
const list=el("div",bar),detail=el("div",bar);
list.style.cssText="max-height:300px;overflow:auto";detail.style.cssText="max-height:350px;overflow:auto";
let nodes=new Map(),edges=[],adj=new Map(),selected=null;
const button=(parent,text,fn)=>{const b=el("button",parent,text);b.style.margin="3px";b.onclick=fn;return b};
function render(){
 list.replaceChildren();detail.replaceChildren();const q=search.value.toLowerCase();let matches=0;
 for(const n of nodes.values()){if(!(n.id+" "+n.uid+" "+n.path+" "+n.kind).toLowerCase().includes(q))continue;matches++;if(matches<=100)button(list,n.uid||n.path||n.id,()=>{selected=n.id;render()})}
 status.textContent=nodes.size+" nodes · "+edges.length+" edges · "+matches+" matching nodes (first 100 shown)";
 const n=nodes.get(selected);if(!n)return;el("h3",detail,n.uid||n.path||n.id);el("pre",detail,JSON.stringify(n,null,2));
 for(const e of (adj.get(n.id)||[]).slice(0,80)){const other=e.source===n.id?e.target:e.source;button(detail,(e.disposition||"relation")+" · "+(e.family||"")+" → "+other,()=>{selected=other;render()});const p=el("pre",detail,JSON.stringify(e,null,2));p.style.whiteSpace="pre-wrap"}
}
async function read(f,accept){let i=0;for(const line of (await f.text()).split(/\r?\n/)){if(!line.trim())continue;i++;let val;try{val=JSON.parse(line)}catch{throw Error(f.name+" JSON row "+i)}accept(val)}}
files.onchange=async()=>{try{
 const filesByName=new Map([...files.files].map(f=>[f.name,f]));
 if(!filesByName.has("nodes.jsonl")||!filesByName.has("edges.jsonl"))throw Error("Select both graph files");
 const n=new Map(),e=[],a=new Map(),seen=new Set();
 await read(filesByName.get("nodes.jsonl"),x=>{if(!x.id||n.has(x.id))throw Error("Duplicate node");n.set(x.id,x);a.set(x.id,[])});
 await read(filesByName.get("edges.jsonl"),x=>{if(!x.id||seen.has(x.id))throw Error("Duplicate connector");if(!n.has(x.source)||!n.has(x.target))throw Error("Missing endpoint");seen.add(x.id);e.push(x);a.get(x.source).push(x);if(x.source!==x.target)a.get(x.target).push(x)});
 nodes=n;edges=e;adj=a;selected=n.keys().next().value||null;render()
 }catch(err){status.textContent="Graph rejected: "+err.message}files.value=""};
search.oninput=render;
})();