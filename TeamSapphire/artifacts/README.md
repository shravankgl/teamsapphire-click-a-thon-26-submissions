# Artifacts — the graded outputs

Generated from the run itself by [`../scripts/build_artifacts.py`](../scripts/build_artifacts.py)
and [`../scripts/export_trace.py`](../scripts/export_trace.py). Nothing here is
hand-written, so that any run reproduces the same set of artifacts from its own
output rather than depending on someone to assemble them correctly.

| | |
|---|---|
| [`diagnoses/`](diagnoses/) | One file per detected incident — plain-language diagnosis, factor decomposition, the segment named (or that none is), transition shape, and the full ruled-out ledger |
| [`queries.md`](queries.md) | **All 131 queries** with exact SQL, rows read and timing. Every number in every diagnosis comes from one of these |
| [`compound-segments.md`](compound-segments.md) | The 27 two-dimension findings, each with both parents' movement for comparison |
| [`traces/`](traces/) | Exported Langfuse traces — every stage in order with its inputs, verdict and timing, including the ruled-out branches. The SQL is in [`queries.md`](queries.md), not the trace |
| [`unseen/`](unseen/) | The unseen-incident bundle |

## The three anomalies found in the main dataset

| # | Window | Classification | Diagnosis |
|---|---|---|---|
| [1](diagnoses/02-2026-06-21-global.md) | 2026-06-21, 24h | `global` | requests **−43.5%**, uniform across all 9 dimensions — **no segment is responsible** |
| [2](diagnoses/01-2026-06-23-localized.md) | 06-23 → 06-25, 72h | `localized` | fill rate **0.785 → 0.433** on `os_version = Android 15` |
| [3](diagnoses/03-2026-06-28-unattributed.md) | 06-28 → 06-30, 68h | `compound` | `iOS 18.1 × APAC` fill rate **−50.6%** — see [compound-segments.md](compound-segments.md) |

Two further low-severity events (06-18 and 06-17) are included for completeness.
Both are small positive revenue movements that no dimension explains; we report
them rather than filtering them out, and label them `unattributed` rather than
inventing a cause.

## Why the ruled-out ledger is here

The problem statement's bonus criterion. Every dimension is tested with the same
arithmetic on every incident, and each diagnosis carries the full ledger:
`responsible + ruled_out = 9` in every case, so no dimension is silently dropped.

On the 06-21 incident the ledger *is* the answer — all three publisher tiers moved
within 0.2% of the global figure, all five ad formats within 0.4%, all seven
categories within 0.5%. Ranking segments by size of drop there names the largest
segment every time, confidently and wrongly. Reporting that no segment is
responsible is the correct finding.
