# Running it

One command, cold start to diagnosis. No prompts, no interactive steps.

## Prerequisites

- Python 3.11+
- A ClickHouse Cloud service (or any ClickHouse endpoint)
- An Anthropic API key — **only** for the narration stage. Everything else runs without it, and the structured diagnosis is complete without narration.

## 1. Install

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

`clickhouse-connect[async]` is not optional — plain `clickhouse-connect` installs and imports fine, then throws `ImportError: Async support requires aiohttp` at API startup. The extra is pinned in `requirements.txt`.

## 2. Configure

```bash
cp .env.example .env
```

| Variable | What it is | Required |
|---|---|---|
| `CLICKHOUSE_HOST` | e.g. `abc123.ap-south-1.aws.clickhouse.cloud` — host only, no scheme | yes |
| `CLICKHOUSE_PORT` | `8443` for Cloud (HTTPS) | yes |
| `CLICKHOUSE_SECURE` | `true` for Cloud | yes |
| `CLICKHOUSE_DATABASE` | `inmobi` | yes |
| `CLICKHOUSE_USER` / `CLICKHOUSE_PASSWORD` | needs `CREATE`/`INSERT` for setup; `SELECT` + `dictGet` to investigate | yes |
| `ANTHROPIC_API_KEY` | narration only — omit it and use `--no-narrate` | no |
| `LANGFUSE_HOST` / `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | stage tracing. Absent → tracer is a no-op, run proceeds | no |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | ClickStack/HyperDX collector for API traces | no |
| `API_PORT` / `CORS_ORIGINS` | defaults `8010` / `http://localhost:3100` | no |

**`.env` is gitignored and is not in this repo.** Nothing is hardcoded — one `.env` change moves the whole system between ClickHouse Cloud and a local server.

## 3. Create the schema

Order matters: dictionaries first (the rollup views resolve dimensions through them at insert time), then the rollups.

```bash
.venv/bin/python scripts/ch.py run-file sql/01_dictionaries.sql
.venv/bin/python scripts/ch.py run-file sql/02_rollups.sql
```

Materialized views are **insert triggers** — they only see rows inserted *after* creation. Creating them before loading means new data (including the unseen incident) rolls up automatically.

## 4. Load the dataset

```bash
.venv/bin/python scripts/load.py /path/to/dataset-dir
```

The loader validates the shape and **refuses to ingest a window that overlaps data already present** — double-counted hours would silently corrupt every baseline.

If the raw table was populated before the views existed, backfill the rollups once:

```bash
.venv/bin/python scripts/backfill.py --verify
```

`--verify` checks that the rollups agree with `ad_events` to the digit, and that all nine dimensions sum to the same total. The backfill is **not idempotent** — it is guarded, but do not run it twice.

## 5. Investigate — the one command

```bash
./investigate.sh
```

That is the whole thing. It detects, decomposes, localizes, characterizes, scans compounds, records what was ruled out, narrates once, and writes `out/diagnosis.md`, `out/diagnosis.json` and a trace URL.

```bash
./investigate.sh /path/to/new-data-dir              # load that slice first, then investigate
./investigate.sh --start "2026-06-08 00:00:00" \
                 --end   "2026-07-03 00:00:00"      # explicit window
./investigate.sh --watch 60                          # same engine, on a loop
./investigate.sh --no-narrate                        # skip the LLM entirely
```

**Exit code 0 means every narrated number was traced back to computed evidence.** A non-zero exit means one could not be — never ship that output.

**Window inference:** without `--start`/`--end` the window is inferred from the newest data present, and deliberately **stops one hour short of it**. Under continuous ingestion the newest hour is always partial — run at 14:30 and hour 14 holds thirty minutes of traffic, which against a full-hour baseline reads as a ~50% collapse on every run forever. Pass `--include-partial-hour` to override; an explicit `--end` is always honoured as given.

## 6. Generate the artifacts

```bash
.venv/bin/python scripts/build_artifacts.py out/diagnosis.json artifacts/
```

Renders the diagnoses, the full query appendix and the compound findings from the run itself.

## 7. API and UI (optional)

```bash
./dev.sh                # API on :8010, incident view on :3100
./dev.sh status
./dev.sh stop
```

The API reads `out/diagnosis.json` **once at startup** — after a fresh investigation, restart it (`./dev.sh restart api`) or the UI will keep serving the previous run.

## The OSS stack — and why there are no credentials here

**No credentials appear anywhere in this repository, and none will be added.** It is public, and a PR to a public upstream: anything committed lives in git history permanently, and the services below front a ClickHouse Cloud account and an LLM API key. `.env` is gitignored; `.env.example` lists variable *names* only.

The stack runs on a GCP VM (`n2-standard-8`, `asia-south1`) reachable **only over Tailscale**. Nothing is internet-facing.

| Service | Role | Port |
|---|---|---|
| **ClickHouse Cloud** (`ap-south-1`) | The only analytical store — raw table, 2 rollups, 3 dictionaries | 8443 |
| **Langfuse** | Traces every investigation stage, including the ruled-out branches | 3000 |
| **LibreChat** | The *InMobi Analytics* agent, over the ClickHouse MCP server | 3080 |
| **ClickStack / HyperDX** | OTel traces of the API + dashboards charting the rollups | 8080 |
| **ClickHouse MCP** | Read-only bridge from the agent to ClickHouse (`mcp_agent`, verified unable to write) | — |

### How to read the traces without access to our network

This is the point that matters for grading. Langfuse's own share links are unauthenticated URLs **on the same private host**, so they do not help a reader outside our tailnet.

So every trace is **exported and committed**:

```
artifacts/traces/<trace-id>.json    full export — every span, input, output, timing
artifacts/traces/<trace-id>.md      readable stage-by-stage summary
```

That is the same object the Langfuse UI renders. Regenerate with:

```bash
.venv/bin/python scripts/export_trace.py out/diagnosis.json artifacts/traces/
```

### Reproducing on your own infrastructure

Everything is env-driven — point `.env` at your own ClickHouse and the pipeline runs unchanged. Langfuse and OTel are optional: absent their variables, the tracer degrades to a no-op and the investigation proceeds normally. The agent layer is the reference compose from [ClickHouse/agentic-data-stack](https://github.com/ClickHouse/agentic-data-stack), with the ClickHouse MCP server pointed at a read-only user.

## Tests

```bash
.venv/bin/python -m pytest tests/ -v
```

15 integration tests against the real database. They skip cleanly if it is unreachable, so the suite never fails for the wrong reason.

## Inspecting a single stage

Each stage has a standalone runner, which is how the pipeline was built and debugged:

```bash
.venv/bin/python scripts/try_detect.py
.venv/bin/python scripts/try_decompose.py
.venv/bin/python scripts/try_localize.py
.venv/bin/python scripts/try_characterize.py
.venv/bin/python scripts/try_segments.py
.venv/bin/python scripts/try_narrate.py
```

## Ad-hoc SQL

```bash
.venv/bin/python scripts/ch.py query "SELECT count() FROM inmobi.ad_events"
```

Dependency-free — it runs from any interpreter, without the venv.
