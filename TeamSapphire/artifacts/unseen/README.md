# The unseen incident

**Status: awaiting release.** A fresh slice of the same universe with new planted
anomalies is released to all teams simultaneously in the final hours. This folder
is the bundle for it.

Everything here is produced by the same command that produced the artifacts for
the main dataset — no separate path, no manual assembly:

```bash
./investigate.sh /path/to/unseen-data-dir
.venv/bin/python scripts/build_artifacts.py out/diagnosis.json artifacts/unseen/
.venv/bin/python scripts/export_trace.py    out/diagnosis.json artifacts/unseen/traces/
```

When filled, this folder will contain:

| | |
|---|---|
| `diagnoses/` | The plain-language diagnosis, the responsible segment(s) — or the finding that none is responsible — and the full ruled-out ledger |
| `queries.md` | Every query behind every cited number, with rows read and timing |
| `compound-segments.md` | Two-dimension findings, if any |
| `traces/` | The exported Langfuse trace that proves our system generated the diagnosis |

**Built for this, not for the anomalies we found during the build.** The harness
runs cold and unattended, exits non-zero if any narrated number cannot be traced
back to computed evidence, and was rehearsed twice against a sealed slice before
the release.
