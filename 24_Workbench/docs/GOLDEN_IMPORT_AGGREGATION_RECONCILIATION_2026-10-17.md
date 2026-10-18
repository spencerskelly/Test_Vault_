# Golden Import — Aggregation reconciliation (candidate pass)

Read-only analysis of reduced QEAX on 2026-10-17. All 2,267 Aggregation connectors were classified by trusted source/aggregate-end orientation and source element families, applying approved decisions.

Candidate dispositions: PartUsage 1959; ActionUsage 148; StateUsage 76; UseCaseUsage 10; ItemUsage 6; MDSE-only Change hierarchy 12; unresolved MDSE flagLink 56. Total 2267. No native parser acceptance claimed.

flagLink reasons: Part to Business Line 24; Business Line to Part 11; interface subtype pending verification 11; State to Activity 5; InformationItem to Part 3; Part to Interface 1; State to Part 1. Each flagLink must be retained in the affected note YAML with a human-readable explanation in its body. Do not infer containment for flagged links. The 11 interface cases may become approved port/interface usages after subtype review.

Each individual EA connector remains distinct. Preserve role, connector GUID, orientation, aggregate flag and explicit child-end cardinality; leave missing multiplicity unspecified. The detailed reconciliation ledger and model names/IDs are kept local, not in the methods repository.

Remaining: implement YAML and body-note emitters, stable cross-reimport naming, source semantic validation and SysML v2 parser tests. Counts are provisional semantic candidates.
