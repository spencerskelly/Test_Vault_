# STEP-03B — Serialized graph flag parity gate (2026-10-18)

Status: **regression gate committed; permanent exporter correction and full Workbench/browser acceptance pending**.

The STEP-03A local audit established 11,445 graph nodes, 14,688 edges, 408 flagged connectors and 159 expected flagNotes. The initial export had only 15 node-resident notes; 144 attachment catalog flags existed in a review index but not their corresponding graph nodes. Local repair reached 159 node-resident flags, without QEAX mutation.

## Committed guard

`25_Testing/v2_step03b_graph_flag_gate.py` checks uniqueness of node and connector IDs, endpoint existence, and **node-resident** flagNote counts against an independently supplied expected count. It reports aggregate counts only. Example, using local-only graph files:

```bash
python3 25_Testing/v2_step03b_graph_flag_gate.py \
  /local/private/nodes.jsonl /local/private/edges.jsonl \
  --expected-flag-notes 159
```

Exit status 0 means the expected node-resident flag count matches and graph identities/endpoints pass. Do not reuse 159 for different inputs: derive the expected count independently from that import's review/aggregate ledger. The check is a parity gate, not proof of semantic correctness or exact flag ownership; also verify the attachment IDs against the review index. A locally tested equivalent implementation passed five synthetic tests covering catalog flags, missing flags, duplicate nodes, duplicate edges and broken endpoints. Committed script requires independent checkout execution/CI wiring.

## Next implementation step

Integrate attachment catalog flagNote serialization into the **canonical STEP-02W exporter**. A review-index-only flag must not be counted as graph-resident. Match each attachment by stable canonical identity, write the associated flagNote into the existing corresponding node, preserve its provenance, and fail on unmatched/ambiguous identity rather than quietly inventing or merging another node. Re-export and require this gate to pass from a fresh run, including deterministic rerun and edge-accounting checks.

Then open the corrected private graph in the committed Workbench and verify search/navigation, all visible flags, no source loss, and acceptable responsiveness. The native SysML parser and Obsidian acceptance remain separate gates. **EA diagrams stay excluded**; source QEAX and private ledgers stay local. Unresolved flags may remain in a functional model; **missing flags or broken endpoints may not**.

No claim of golden-import acceptance or permanent exporter fix is made.
