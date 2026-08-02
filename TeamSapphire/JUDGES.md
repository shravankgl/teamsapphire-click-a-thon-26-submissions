# Access for reviewers

Everything below is **read-only** and **time-boxed**. The stack is on a GCP VM that
is shut down at **14:00 IST, 2 August 2026**; every credential on this page is
retired at that point and is published on the understanding that it is disposable.
No write-capable or administrative credential appears here.

If you would rather not log into anything, the two artifacts that matter need no
account at all:

- **Hosted demo** — <https://shravankgl.github.io/teamsapphire-click-a-thon-26-submissions/TeamSapphire/demo/>
- **[`artifacts/`](artifacts/)** — every diagnosis, all the queries behind every
  number, and the exported traces, committed as files

---

## ClickHouse — verify any number yourself

This is the most direct way to check our work: re-run any query from
[`artifacts/queries.md`](artifacts/queries.md) and compare.

```
Host      x6fcqwjunt.ap-south-1.aws.clickhouse.cloud
Port      8443  (HTTPS, secure)
Database  inmobi
User      dashboard_ro
Password  a35b92256a9df1542e4bc356cf6b758081e57ba5Aa1!@#
```

`dashboard_ro` is `readonly = 1` — verified unable to `INSERT`, `ALTER` or `DROP`.

```bash
curl --user 'dashboard_ro:a35b92256a9df1542e4bc356cf6b758081e57ba5Aa1!@#' \
  'https://x6fcqwjunt.ap-south-1.aws.clickhouse.cloud:8443/?database=inmobi' \
  --data-binary 'SELECT count() FROM ad_events'
# 10500000
```

Note the schema carries **two dimension epochs**: events before `2026-07-06` are
joined to the original dimension tables (`geo_device_old`, `apps_old`,
`advertisers_old`) and events from `2026-07-06` to the regenerated ones. The unseen
dataset reuses the same IDs with different attributes, so a single dimension table
across both periods misattributes every segment — see
[`artifacts/unseen/README.md`](artifacts/unseen/README.md).

---

## Langfuse — the investigation traces

**<http://35.200.218.190:3000>** · `admin@clickathon.local` / `9880012f09e03ab8a94bb3faAa!`

Every stage of every run, in order, with its inputs, verdict and timing —
**including the branches that were ruled out**. Project: *clickathon-project*.

The traces are also **exported and committed** under `artifacts/*/traces/`, which is
the form to use after 14:00 or if you would rather not log in. That is the same
object the Langfuse UI renders.

---

## LibreChat — the conversational layer

**<http://35.200.218.190:3080>** · `judge@clickathon.io` / `Judge2026Review`

Open the **InMobi Analytics** agent. It queries the same ClickHouse tables through
the official ClickHouse MCP server, read-only.

Questions worth asking, with the answers we already know from the engine:

| Ask | Expected |
|---|---|
| *Which OS version had the lowest fill rate between June 23 and June 25?* | Android 15, **43.33%** — every other version sits in a 78.3–78.6% band |
| *Which segment caused the drop on 2026-06-21?* | **None.** The drop is uniform across all nine dimensions — the honest answer, and the one most systems get wrong by naming the largest segment |
| *Did fill rate drop for any specific combination of OS version and region?* | `iOS 18.1 × APAC`, −50.6% on 06-28, while APAC alone is −2.3% and iOS 18.1 alone −12.3% |

Registration is disabled, so this account is the only way in.

---

## ClickStack / HyperDX — pipeline traces and rollup charts

**<http://35.200.218.190:8080>** · `shravan@bytebeam.io` / `Admin@123456`

Dashboard: **Ad Metrics — Anomalies**. Charts the rollups directly, so the anomalies
are visible as raw shapes independent of anything our engine claims about them.

**Set the time range to 1 Jun – 6 Jul 2026.** The data ends 2026-07-05; a wider range
pads the empty tail and draws a false decay to zero.

---

## What is deliberately not here

- **No administrative or write-capable credential.** The ClickHouse account that owns
  the schema, the Anthropic API key, and the Langfuse secret key are not published and
  are not derivable from anything here.
- **ClickHouse's own internal instances** (Langfuse's and ClickStack's metadata stores)
  and the MCP servers are on the VM's internal Docker network only — not exposed by the
  firewall.

## After 14:00 IST

The VM is stopped and the firewall reverts to an allow-list, so the three
`35.200.218.190` links stop responding. The hosted demo, the artifacts, the exported
traces and the ClickHouse credentials above are unaffected by that — ClickHouse Cloud
is separate infrastructure and remains readable until the trial account lapses.
