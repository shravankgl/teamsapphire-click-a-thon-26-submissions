# Team Sapphire

## Track

InMobi — *"From alert to answer: the automated root-cause analyst."*

## Project

**From alert to answer** — your alert says revenue moved. This says *why*, which segment, and what it ruled out.

## Team Members

- Shravan (@shravankgl)

## What it does

Every data-driven team watches a handful of numbers — revenue, fill rate, eCPM, CTR. When one moves, an alert reports *what* happened. The expensive question is *why*, and today an analyst answers it by drilling through dashboards for hours.

This does the drilling. Point it at a window and in about a minute it returns a diagnosis with the arithmetic attached:

- **Detects** deviations against a *like-for-like* baseline — same weekday, same hour-of-day, median over trailing weeks — so a Sunday-night trough is not an incident
- **Decomposes** the movement through the exact revenue identity to name the responsible *factor*: volume, fill, render, or price
- **Localizes** the responsible *segment* by excess over what each segment's own size explains, across nine dimensions independently
- **Finds compound segments** — `iOS 18.1 × APAC` — that no single-dimension scan can see
- **Reads the shape** of the transition: step vs. gradual, day-boundary aligned, what held steady. This is where "why" lives
- **Records what it ruled out**, with numbers. On a uniform drop the correct answer is *"no segment is responsible"*, and saying so is a finding
- **Narrates once** with an LLM over computed numbers only — then verifies every figure in the prose against the computed evidence and **exits non-zero if one cannot be traced**

**The analysis is SQL. The LLM writes the sentence.** Delete the narration stage and the structured diagnosis is unchanged.

## Hosted Demo

**https://shravankgl.github.io/teamsapphire-click-a-thon-26-submissions/TeamSapphire/demo/**

The incident view showing all five detected events, the responsible segments, the ruled-out ledger for every dimension, the compound findings, and the query-latency envelope.

It fetches the live API first and falls back to a committed snapshot of a real `./investigate.sh` run — so the hosted version shows genuine engine output with no backend, and says so in a banner rather than passing a cached run off as live. That snapshot is regenerated from the harness, never hand-authored: this system's whole claim is that every number was computed from the data, so a plausible-looking hand-written fixture would be the one thing capable of putting a fabricated figure in front of a judge.

## Demo Video

*[to be added — 2–3 minutes]*

## Architecture

See **[ARCHITECTURE.md](ARCHITECTURE.md)** for the full 2-pager: how detection, drill-down and diagnosis fit together, where the analysis actually runs, the attribution approach, the OSS integrations, and the LLM provider rationale.

In one diagram:

```
ad_events (raw MergeTree, 9,000,000 rows)
   │  3 dictionaries resolve 9 dimensions via dictGet() at insert time — no JOIN
   │  2 materialized views fire on every INSERT
   ├── events_hourly          hourly platform totals            840 rows
   └── events_hourly_by_dim   (hour, dim_name, dim_value)     53,760 rows
                │
   1  DETECT       like-for-like baseline, global AND per segment      SQL
   2  CONSOLIDATE  group flagged hours into distinct events         Python
   3  DECOMPOSE    which factor moved — exact identity, log space      SQL
   4  LOCALIZE     which segment — or that none is responsible         SQL
   4b CHARACTERIZE the shape of the transition                         SQL
   4c INTERSECT    compound segments invisible to one dimension        SQL
   5  RULE OUT     everything checked and cleared, with numbers        SQL
                │
   6  NARRATE     one LLM call over computed numbers      ← the only LLM
```

## Artifacts

**[`artifacts/`](artifacts/)** — the graded outputs.

| | |
|---|---|
| [`diagnoses/`](artifacts/diagnoses/) | One file per detected incident: plain-language diagnosis, the factor decomposition, the segment named (or that none is), the transition shape, and the full ruled-out ledger |
| [`queries.md`](artifacts/queries.md) | **All 111 queries**, with the exact SQL, rows read and timing. Every number in every diagnosis comes from one of these |
| [`compound-segments.md`](artifacts/compound-segments.md) | The 27 two-dimension findings, each with both parents' movement for comparison |
| [`unseen/`](artifacts/unseen/) | The unseen-incident bundle — diagnosis, numbers, and trace |

These are generated from the run itself by [`scripts/build_artifacts.py`](scripts/build_artifacts.py), not written by hand.

## What it found

On the provided dataset, unassisted:

| | When | Shape | Diagnosis |
|---|---|---|---|
| 1 | 2026-06-21, 24h | global, uniform across all 9 dimensions | requests **−43.5%**; fill, render and eCPM normal → traffic arrival, and **no segment is responsible** |
| 2 | 06-23 → 06-25, 72h | localized to `os_version = Android 15` | fill rate **0.785 → 0.433**; requests normal |
| 3 | 06-28 → 06-30, 3 days | **compound** — `iOS 18.1 × APAC` | fill rate **−50.6%** |

Incident 3 is the one that matters. On 2026-06-28: global **−1.0%**, APAC alone **−2.3%**, iOS 18.1 alone **−12.3%**, and `iOS 18.1 × APAC` **−50.6%**. No single-dimension scan can see it — it is the problem statement's own worked example.

Incident 2 shows why shape matters: **96% of its total change landed inside one hour**, exactly on a day boundary, reversing just as sharply after exactly three days while requests, render rate and eCPM held steady. That is consistent with a scheduled, demand-side change with an end date — not a degradation. We state it as what the evidence is consistent with, never as an established mechanism.

## How we built it

**ClickHouse** is the only analytical store. Raw `MergeTree`, two `SummingMergeTree` rollups maintained by materialized views, three dictionaries.

The schema is small on purpose, and the small schema is the design work. We built the obvious fully-crossed rollup first and measured it: **7,247,816 rows from 7.2M events** — nearly every event had its own dimension combination, so it compressed nothing and cost a second copy of the data. Across all nine dimensions there are only **62 distinct values in total**, so an *unpivoted* `(hour, dim_name, dim_value)` grain is **53,760 rows** — 167× smaller, and exactly the shape contribution ranking reads.

Rest of the stack: **Python** for orchestration and one division on already-aggregated rows · **FastAPI** with a `query_ms` / `rows_scanned` / `sql` envelope on every response · **Vite + React + shadcn/ui + ECharts** for the incident view · **Langfuse** tracing every stage including ruled-out branches · **LibreChat + ClickHouse MCP** for follow-ups · **ClickStack/HyperDX** for OTel traces and rollup charts.

**Testing:** 15 integration tests against the real database. Mocking ClickHouse would test our mocks; every failure this project actually had was in the interaction between SQL, real data and Python arithmetic.

## How to run it

Prerequisites: Python 3.11+, a ClickHouse endpoint, and an Anthropic API key — the key is needed **only** for narration; everything else runs without it and the structured diagnosis is complete either way.

**1. Install.** The `[async]` extra is not optional — plain `clickhouse-connect` imports fine and then throws at API startup.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

**2. Configure.** Copy the template and fill it in. Nothing is hardcoded, so one `.env` change moves the system between ClickHouse Cloud and a local server.

```bash
cp .env.example .env
```

| Variable | | Required |
|---|---|---|
| `CLICKHOUSE_HOST` | host only, no scheme | yes |
| `CLICKHOUSE_PORT` / `CLICKHOUSE_SECURE` | `8443` / `true` for Cloud | yes |
| `CLICKHOUSE_DATABASE` | `inmobi` | yes |
| `CLICKHOUSE_USER` / `CLICKHOUSE_PASSWORD` | `SELECT` + `dictGet` to investigate | yes |
| `CLICKHOUSE_ADMIN_USER` / `CLICKHOUSE_ADMIN_PASSWORD` | needed only to create schema and load | for setup |
| `ANTHROPIC_API_KEY` | narration only — omit and use `--no-narrate` | no |
| `LANGFUSE_HOST` / `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | stage tracing; absent → tracer is a no-op | no |

**3. Create the schema.** Order matters — the rollup views resolve dimensions through the dictionaries at insert time.

```bash
.venv/bin/python scripts/ch.py run-file sql/01_dictionaries.sql
.venv/bin/python scripts/ch.py run-file sql/02_rollups.sql
```

**4. Load a dataset.** The loader validates the shape and refuses a window that overlaps data already present, since double-counted hours corrupt every baseline.

```bash
.venv/bin/python scripts/load.py /path/to/dataset-dir
.venv/bin/python scripts/backfill.py --verify     # if raw was populated before the views existed
```

**5. Investigate — the one command.**

```bash
./investigate.sh                                    # the data already loaded
./investigate.sh /path/to/new-data-dir              # load that slice first, then investigate
./investigate.sh --start "2026-07-06 00:00:00" \
                 --end   "2026-07-10 22:00:00"      # an explicit window
./investigate.sh --watch 60                         # the same engine on a loop
./investigate.sh --no-narrate                       # skip the LLM entirely
```

Writes `out/diagnosis.md`, `out/diagnosis.json` and a trace URL. **Exit code 0 means every narrated number was traced back to computed evidence** — a non-zero exit means one could not be, and that output should never be shipped.

Without `--start`/`--end` the window is inferred from the newest data and deliberately stops one hour short of it: under continuous ingestion the newest hour is always partial, and against a full-hour baseline that reads as a ~50% collapse on every run.

**6. Artifacts and traces.**

```bash
.venv/bin/python scripts/build_artifacts.py out/diagnosis.json artifacts/
.venv/bin/python scripts/export_trace.py    out/diagnosis.json artifacts/traces/
```

**7. API and UI (optional).** The API reads `out/diagnosis.json` once at startup, so restart it after a fresh run.

```bash
./dev.sh          # API on :8010, incident view on :3100
```

**Tests:** `.venv/bin/python -m pytest tests/ -v` — 15 integration tests against the real database, skipping cleanly if it is unreachable.

[RUN.md](RUN.md) has the longer reference: per-stage runners, the OSS service map, and how to read the traces without access to our network.

## Honest limitations

- **Compound scanning is the bottleneck.** It reads raw `ad_events` and accounts for 99.6% of all rows read and 88% of query time. At 100× that is ~93 billion rows per run and not viable. The fix is a materialized pair rollup (~33,600 rows for `os_version × region`) — we did not build it.
- **Thresholds are judgment calls** anchored to measurements on one dataset. [`METHOD.md`](METHOD.md) §5 lists every one with what motivated it and how it fails. We ran no sensitivity sweep.
- **A correlated dimension can still be named responsible** — `region = EU` is flagged alongside Android 15 because Android 15 skews European. It is a reflection, not a second cause. The UI shows it with that caveat rather than hiding it.
- **Compound search is pairs, not triples.**
- **We see the shape of a change, not the system that caused it.** We say what the evidence is consistent with and name the specific thing a human should check.

## License

MIT — see [LICENSE](LICENSE).
