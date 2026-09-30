<%*
const PREFIX = {"Object":"OBJ","Port":"PORT","Item Flow":"IFLOW","Function":"FUNC","Functional Flow":"FFLOW","State":"STATE","State Machine":"SM","Requirement":"REQ","Design":"DES","Use Case":"UC","Actor":"ACT","Failure Mode":"FM","Issue":"ISS","Info":"INFO","Step":"STEP","Verification":"VER","Procedure":"PROC","Setup":"SETUP","Plan":"PLAN","Result":"RES","Document":"DOC","Artifact":"ART","Diagram":"DIA","modelCheck":"MC","Property Definition":"INFO","Person":"INFO"};
const templateName = tp.config.template_file ? tp.config.template_file.basename : "";
const prefix = PREFIX[templateName.split(" - ")[0]];
if (prefix) {
  const re = new RegExp(`^${prefix}-(\\d+)$`);
  let max = 0;
  const line = new RegExp(`^\\s*[-*]\\s*${prefix}-(\\d+)\\b`);
  for (const f of tp.app.vault.getMarkdownFiles()) {
    const cache = tp.app.metadataCache.getFileCache(f);
    const m = String(cache?.frontmatter?.id ?? "").match(re);
    if (m) max = Math.max(max, Number(m[1]));
    // earlier ids: bullets under a "Former ids" heading (W-207); only notes that have the heading are read
    const h = (cache?.headings ?? []).find(x => x.level === 2 && x.heading.trim() === "Former ids");
    if (h) {
      const text = await tp.app.vault.cachedRead(f);
      for (const l of text.slice(h.position.end.offset).split("\n").slice(1)) {
        if (/^#/.test(l)) break;
        const q = l.match(line);
        if (q) max = Math.max(max, Number(q[1]));
      }
    }
  }
  tR += `${prefix}-${String(max + 1).padStart(5, "0")}`;
}
%>