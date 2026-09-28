<%*
const PREFIX = {"Object":"OBJ","Interface":"INT","Item Flow":"IFLOW","Context":"CTX","Function":"FUNC","Functional Flow":"FFLOW","State":"STATE","State Machine":"SM","Transition":"TRANS","Requirement":"REQ","Design":"DES","Use Case":"UC","Actor":"ACT","Failure Mode":"FM","Issue":"ISS","Info":"INFO","Step":"STEP","Verification":"VER","Procedure":"PROC","Setup":"SETUP","Plan":"PLAN","Result":"RES","Document":"DOC","Artifact":"ART","Property Definition":"INFO","Person":"INFO"};
const templateName = tp.config.template_file ? tp.config.template_file.basename : "";
const prefix = PREFIX[templateName.split(" - ")[0]];
if (prefix) {
  const re = new RegExp(`^${prefix}-(\\d+)$`);
  let max = 0;
  for (const f of tp.app.vault.getMarkdownFiles()) {
    const fm = tp.app.metadataCache.getFileCache(f)?.frontmatter;
    for (const c of [fm?.id, ...(Array.isArray(fm?.formerIds) ? fm.formerIds : [])]) {
      const m = String(c ?? "").match(re);
      if (m) max = Math.max(max, Number(m[1]));
    }
  }
  tR += `${prefix}-${String(max + 1).padStart(5, "0")}`;
}
%>