/* STEP-02Z: add a read-only flag review overview to existing Workbench. */
(() => {
  "use strict";
  const section = document.createElement("section");
  section.style.cssText = "padding:12px 16px;border-top:1px solid #526984;background:#142238;color:#dce8f4";
  section.innerHTML = "<h2>Unresolved review queue (local, read-only)</h2>";
  const input = document.createElement("input");
  input.type = "file"; input.multiple = true; input.accept = ".jsonl";
  input.setAttribute("aria-label", "Load STEP-02W graph files for flagged review");
  const info = document.createElement("p");
  info.textContent = "Select nodes.jsonl and edges.jsonl to inspect unresolved items.";
  const result = document.createElement("div");
  section.append(input, info, result);
  document.body.append(section);
  function flags(value) {
    if (Array.isArray(value)) return value.length;
    return value ? 1 : 0;
  }
  async function eachLine(file, visit) {
    let lineNo = 0;
    for (const raw of (await file.text()).split(/\r?\n/)) {
      if (!raw.trim()) continue;
      lineNo++;
      let record;
      try { record = JSON.parse(raw); }
      catch { throw new Error(file.name + " has malformed JSON at line " + lineNo); }
      visit(record);
    }
  }
  input.addEventListener("change", async () => {
    try {
      const byName = new Map([...input.files].map(f => [f.name, f]));
      if (!byName.has("nodes.jsonl") || !byName.has("edges.jsonl")) throw new Error("Both graph files are required");
      let nodes = 0, edges = 0, noteFlags = 0, linkFlags = 0;
      const nodeIds = new Set(), edgeIds = new Set(), targets = [];
      const flagged = [];
      await eachLine(byName.get("nodes.jsonl"), n => {
        if (!n.id || nodeIds.has(n.id)) throw new Error("Duplicate or missing node ID");
        nodeIds.add(n.id); nodes++;
        const count = flags(n.flagNote);
        noteFlags += count;
        if (count) flagged.push({type:"flagNote", id:n.id, detail:n.flagNote});
      });
      await eachLine(byName.get("edges.jsonl"), e => {
        if (!e.id || edgeIds.has(e.id)) throw new Error("Duplicate or missing connector ID");
        edgeIds.add(e.id); edges++;
        targets.push([e.source,e.target]);
        if (flags(e.flagLink) || /flaglink|unresolved|review/i.test(String(e.disposition || "")) || e.type === "flagLink") {
          linkFlags += flags(e.flagLink) || 1; flagged.push({type:"flagLink", id:e.id, detail:e});
        }
      });
      if (targets.some(([a,b]) => !nodeIds.has(a) || !nodeIds.has(b))) throw new Error("Broken graph endpoint");
      result.replaceChildren();
      const summary = document.createElement("p");
      summary.textContent = nodes + " nodes · " + edges + " edges · " + linkFlags + " flagged links · " + noteFlags + " flagged notes";
      result.append(summary);
      const query = document.createElement("input");
      query.placeholder = "Filter unresolved records";
      result.append(query);
      const records = document.createElement("div");
      records.style.cssText = "max-height:280px;overflow:auto";
      result.append(records);
      const draw = () => {
        records.replaceChildren();
        const q = query.value.toLowerCase();
        let matched=0;
        for (const item of flagged) {
          if (!(item.id+" "+item.type).toLowerCase().includes(q)) continue;
          matched++;
          if (matched > 100) continue;
          const disclosure=document.createElement("details");
          const title=document.createElement("summary");
          title.textContent=item.type+" — "+item.id;
          disclosure.append(title);
          const evidence=document.createElement("pre");
          evidence.textContent=JSON.stringify(item.detail,null,2);
          disclosure.append(evidence);records.append(disclosure);
        }
      };
      query.oninput=draw; draw();
      info.textContent = "Local evidence loaded. Review is read-only; no resolutions are saved.";
    } catch (error) {
      result.replaceChildren();
      info.textContent="Review import rejected: "+error.message;
    } finally { input.value=""; }
  });
})();