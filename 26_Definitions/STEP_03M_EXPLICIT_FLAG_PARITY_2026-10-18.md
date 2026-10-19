# STEP-03M Flag Parity (2026-10-18)

Changes committed to main:
- STEP-03B gate now recognizes explicit connector flagLink arrays and supports optional expected link count.
- Workbench flag-review panel counts explicit flagLink entries.
- Five regression tests added under 25_Testing.

Mac verification:

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03m_explicit_flag_parity.py' -v
python3 25_Testing/v2_step03b_graph_flag_gate.py "$HOME/Documents/MDSE_Local_STEP03K/annotated/nodes.jsonl" "$HOME/Documents/MDSE_Local_STEP03K/annotated/edges.jsonl" --expected-flag-notes 0 --expected-flag-links 0
```

Zero expectations apply only to family annotation output, not attachment or semantic review flags. Source-identified attachment ownership and browser acceptance remain open. Do not invent historical missing flag identities. Exclude diagrams and private QEAX data from GitHub.
