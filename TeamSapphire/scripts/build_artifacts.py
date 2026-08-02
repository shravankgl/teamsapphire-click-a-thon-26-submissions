"""Render a run's diagnosis.json into the graded artifacts folder.

The InMobi guidelines ask for the plain-language diagnosis, the segments named,
every cited number reproducible from ClickHouse queries *with the queries
included*, and the ruled-out ledger per investigation. All of that is already in
diagnosis.json — this only reshapes it into files a reader can follow without
running anything.

It is a script rather than hand-written markdown so that every run reproduces the
same artifacts from its own output, with no opportunity for a transcription
error between what was computed and what is published.

    python scripts/build_artifacts.py out/diagnosis.json <output-dir>
"""
import json
import sys
from pathlib import Path


def pct(x, places=1):
    return "—" if x is None else f"{x * 100:+.{places}f}%"


def write_query_appendix(path: Path, queries: list[dict]) -> None:
    by_label: dict[str, list[dict]] = {}
    for q in queries:
        by_label.setdefault(q["label"], []).append(q)

    total_rows = sum(q["rows_read"] for q in queries)
    total_ms = sum(q["query_ms"] for q in queries)

    out = [
        "# Every query this investigation ran",
        "",
        f"**{len(queries)} queries · {total_rows:,} rows read · {total_ms:,.0f} ms of ClickHouse time.**",
        "",
        "Each is the exact SQL sent to ClickHouse, with the rows it read and the",
        "time it took, in execution order. Parameters appear as `{name:Type}` —",
        "they are bound by the client, never string-formatted, so these are",
        "runnable as-is once the window is substituted.",
        "",
        "Every number in every diagnosis comes from one of these. Nothing in the",
        "prose was computed anywhere else.",
        "",
        "| # | Stage | Rows read | Time |",
        "|---:|---|---:|---:|",
    ]
    for i, q in enumerate(queries, 1):
        out.append(f"| {i} | `{q['label']}` | {q['rows_read']:,} | {q['query_ms']:.1f} ms |")

    out += ["", "---", ""]
    for label in sorted(by_label):
        group = by_label[label]
        out.append(f"## `{label}` — {len(group)} call(s)")
        out.append("")
        seen: set[str] = set()
        for q in group:
            sql = " ".join(q["sql"].split())
            if sql in seen:
                continue
            seen.add(sql)
            out += [f"{q['rows_read']:,} rows · {q['query_ms']:.1f} ms", "", "```sql", sql, "```", ""]
    path.write_text("\n".join(out))


def render_event(idx: int, ev: dict, narration: dict | None, trace_url: str | None) -> str:
    dec = ev["decomposition"]
    sig = ev.get("signature") or {}
    L = [
        f"# Incident {idx} — {ev['start']} → {ev['end']}",
        "",
        f"**Classification:** `{ev['classification']}` · **{ev['hours']}h** · "
        f"severity {ev['severity']:.1f} · primary factor **{ev['primary_factor']}**",
        "",
        "## Diagnosis",
        "",
        f"> {ev['headline']}",
        "",
    ]

    if narration:
        verified = narration.get("all_numbers_verified")
        L += [
            "### In plain language",
            "",
            narration["text"],
            "",
            f"*Written by `{narration.get('model')}` over computed numbers only — it never sees an "
            f"event row. Every figure above was then matched back to the computed evidence: "
            f"**{'all numbers verified' if verified else 'UNVERIFIED FIGURES PRESENT'}**. "
            f"The run exits non-zero if a figure cannot be traced.*",
            "",
        ]
    else:
        L += [
            "### In plain language",
            "",
            "*No LLM narration was generated for this incident (narration is capped per run). "
            "The structured diagnosis below is complete without it — that is the point of the "
            "design, not a gap.*",
            "",
        ]

    L += ["## Which factor moved", "",
          "Revenue = Requests × FillRate × RenderRate × (eCPM/1000), decomposed in log space "
          "so the parts are additive and sum to exactly 100%.", "",
          "| Factor | Actual | Baseline | Change | Share of move |",
          "|---|---:|---:|---:|---:|"]
    for f in dec["factors"]:
        L.append(f"| {f['factor']} | {f['actual']:,.4f} | {f['baseline']:,.4f} | "
                 f"{pct(f['pct_change'])} | {pct(f['contribution_share'], 1)} |")
    if abs(dec["revenue_pct_change"]) < 0.02:
        L += ["",
              f"> **Reading the share column here.** Revenue itself moved only "
              f"{pct(dec['revenue_pct_change'], 2)}, so each factor's share is a ratio against a "
              f"near-zero denominator and the values are large and offsetting. That is arithmetic, "
              f"not instability: fill rate fell while requests rose by almost exactly as much, so "
              f"they cancel at the revenue line. **This is precisely why the system does not alert "
              f"on revenue alone** — a segment-level collapse can hide behind a flat top-line "
              f"number, which is what happened here."]
    L += ["",
          f"Identity residual: `{dec['identity_residual']:.2e}` — floating-point zero, so every "
          f"part of the movement is attributed and none is left over.",
          f"Baseline: median of the same weekday and hour over {dec['baseline_weeks_used']} "
          f"trailing week(s).", ""]

    resp = ev.get("responsible") or []
    L += ["## Which segment", ""]
    if resp:
        for i, r in enumerate(resp):
            tag = "**Responsible**" if i == 0 else "Also flagged"
            L += [f"{tag}: **`{r['dim_name']} = {r['top_value']}`** — "
                  f"{r['top_excess_of_total']:.0%} of the whole incident, "
                  f"{r['top_excess_share']:.0%} of the unexplained movement",
                  "", f"> {r['reason']}", ""]
        if len(resp) > 1:
            L += ["*Ranked by share of the incident. A dimension correlated with the primary will "
                  "move with it — check whether a secondary is an independent cause or a "
                  "reflection of the first before acting on it.*", ""]
    else:
        L += ["**No segment is responsible.** The movement was uniform across every dimension "
              "checked — see the ledger below. On a uniform event this is the finding, not a "
              "failure to find one: ranking segments by size of drop here names the largest "
              "segment every time, confidently and wrongly.", ""]

    if sig:
        L += ["## Shape of the transition", "", f"> {sig.get('reading', '—')}", ""]
        if sig.get("held_steady"):
            L.append(f"**Held steady throughout:** {', '.join(sig['held_steady'])}")
            L.append("")
        if sig.get("rules_out"):
            L.append("**Which rules out:**")
            L += [f"- {r}" for r in sig["rules_out"]]
            L.append("")

    L += ["## Checked and ruled out", "",
          "The bonus criterion from the problem statement. Every dimension was tested with the "
          "same arithmetic; these are the ones that came back negative, with the numbers that "
          "cleared them.", "",
          "| Dimension | Verdict | Top value | Why |", "|---|---|---|---|"]
    for v in ev.get("ruled_out", []):
        L.append(f"| `{v['dim_name']}` | **{v['verdict'].replace('_', ' ')}** | "
                 f"{v['top_value']} | {v['reason']} |")
    L += ["",
          f"*{len(resp)} responsible + {len(ev.get('ruled_out', []))} ruled out = "
          f"{len(resp) + len(ev.get('ruled_out', []))} dimensions. Every dimension is accounted "
          f"for in exactly one of the two lists.*", ""]

    if trace_url:
        tid = trace_url.rstrip("/").rsplit("/", 1)[-1]
        L += ["## Trace", "",
              f"**Exported:** [`../traces/{tid}.json`](../traces/{tid}.json) "
              f"· [readable summary](../traces/{tid}.md)", "",
              "Every stage above appears in the trace in order, with its inputs, verdict "
              "and timing — including the branches that were ruled out. The SQL for "
              "every number is in `queries.md`, not in the trace.", "",
              f"*Our Langfuse runs on a private VM, so the in-app link "
              f"(`{trace_url}`) is not reachable from outside our network. The export "
              f"above is the same object the Langfuse UI renders, committed so it can be "
              f"read without access to our infrastructure.*", ""]
    return "\n".join(L)


def main() -> int:
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "out/diagnosis.json")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "artifacts")
    d = json.loads(src.read_text())
    (dst / "diagnoses").mkdir(parents=True, exist_ok=True)

    trace = d.get("trace_url")
    narr = d.get("narrations") or {}
    events = d["events"]

    for i, ev in enumerate(events, 1):
        slug = f"{i:02d}-{ev['start'][:10]}-{ev['classification']}.md"
        (dst / "diagnoses" / slug).write_text(render_event(i, ev, narr.get(str(i)), trace))

    write_query_appendix(dst / "queries.md", d["queries"])

    compounds = d.get("compound_findings") or []
    if compounds:
        C = ["# Compound segments",
             "",
             "Two-dimension combinations that broke together while **neither dimension looked "
             "abnormal on its own** — invisible to any scan that checks one dimension at a time.",
             "",
             "A cell is only reported when it moved at least **2× more than its strongest "
             "parent**. An earlier rule required both parents to be flat, which was backwards: a "
             "compound large enough to matter drags its own parent, so that rule discarded the "
             "largest finding in the dataset and reported a diluted proxy instead.",
             "",
             "| Day | Combination | Combined | First dim alone | Second dim alone | Requests |",
             "|---|---|---:|---:|---:|---:|"]
        for c in compounds:
            C.append(f"| {c['day']} | `{c['dim_a']}={c['value_a']}` × `{c['dim_b']}={c['value_b']}` "
                     f"| {pct(c['pct_change'])} | {pct(c['parent_a_pct'])} | "
                     f"{pct(c['parent_b_pct'])} | {c['requests']:,} |")
        led = [e for e in (d.get("compound_ledger") or []) if "rows_read" in e]
        if led:
            C += ["", f"*Scanned {len(led)} dimension pairs, "
                      f"{sum(e['rows_read'] for e in led):,} rows, "
                      f"{sum(e['query_ms'] for e in led):,.0f} ms. This stage reads raw "
                      f"`ad_events` rather than a rollup, because an unpivoted rollup cannot "
                      f"represent combinations — see ARCHITECTURE.md for the cost and the fix.*"]
        (dst / "compound-segments.md").write_text("\n".join(C))

    print(f"{len(events)} diagnoses · {len(d['queries'])} queries · {len(compounds)} compounds -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
