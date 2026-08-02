import { useMemo } from "react";
import type { EChartsOption } from "echarts";
import echarts, { EChartsReactCore } from "@/echarts-setup";
import type { Decomposition, Factor } from "@/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const FACTOR_LABEL: Record<Factor, string> = {
  requests: "Requests",
  fill_rate: "Fill rate",
  render_rate: "Render rate",
  ecpm: "eCPM",
};
const FACTOR_ORDER: Factor[] = ["requests", "fill_rate", "render_rate", "ecpm"];

const FLAT_THRESHOLD = 0.01; // |pct_change| < 1% reads as flat

type Status = "flat" | "moved" | "primary";

function statusOf(pctChange: number, factor: Factor, primaryFactor: Factor): Status {
  if (factor === primaryFactor) return "primary";
  if (Math.abs(pctChange) < FLAT_THRESHOLD) return "flat";
  return "moved";
}

// dataviz skill status palette, dark-surface steps (#1a1a19 chart surface).
const STATUS_COLOR: Record<Status, string> = {
  flat: "#0ca30c", // good
  moved: "#fab219", // warning
  primary: "#d03b3b", // critical
};

function formatValue(factor: Factor, value: number): string {
  if (factor === "requests") return value.toLocaleString(undefined, { maximumFractionDigits: 0 });
  if (factor === "ecpm") return `$${value.toFixed(4)}`;
  return `${(value * 100).toFixed(2)}%`;
}

export function MetricTree({ decomposition }: { decomposition: Decomposition }) {
  const factors = decomposition.factors;
  const ordered = useMemo(
    () => [...factors].sort((a, b) => FACTOR_ORDER.indexOf(a.factor) - FACTOR_ORDER.indexOf(b.factor)),
    [factors],
  );

  const option: EChartsOption = useMemo(
    () => ({
      backgroundColor: "transparent",
      grid: { left: 90, right: 55, top: 10, bottom: 20 },
      tooltip: {
        trigger: "item",
        backgroundColor: "#232322",
        borderColor: "rgba(255,255,255,0.1)",
        textStyle: { color: "#ffffff" },
        formatter: (p: any) =>
          `${FACTOR_LABEL[ordered[p.dataIndex].factor]}: ${(ordered[p.dataIndex].pct_change * 100).toFixed(2)}%`,
      },
      xAxis: {
        type: "value",
        axisLabel: { formatter: (v: number) => `${v}%`, color: "#898781" },
        axisLine: { lineStyle: { color: "#383835" } },
        splitLine: { lineStyle: { color: "#2c2c2a" } },
      },
      yAxis: {
        type: "category",
        data: ordered.map((f) => FACTOR_LABEL[f.factor]),
        axisLabel: { color: "#c3c2b7" },
        axisLine: { lineStyle: { color: "#383835" } },
        axisTick: { show: false },
      },
      series: [
        {
          type: "bar",
          data: ordered.map((f) => ({
            value: Number((f.pct_change * 100).toFixed(3)),
            itemStyle: {
              color: STATUS_COLOR[statusOf(f.pct_change, f.factor, decomposition.primary_factor)],
              borderRadius: 3,
            },
          })),
          barWidth: 36,
          markLine: {
            symbol: "none",
            silent: true,
            lineStyle: { color: "#383835" },
            label: { show: false },
            data: [{ xAxis: 0 }],
          },
        },
      ],
    }),
    [ordered, decomposition.primary_factor],
  );

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-base">Metric tree — which factor moved</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          {factors.map((f) => {
            const status = statusOf(f.pct_change, f.factor, decomposition.primary_factor);
            const color = STATUS_COLOR[status];
            return (
              <div
                key={f.factor}
                className="rounded-lg border p-3 text-left"
                style={{ borderColor: `${color}66`, backgroundColor: `${color}14` }}
              >
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full" style={{ backgroundColor: color }} />
                  <span className="text-xs font-medium text-muted-foreground">{FACTOR_LABEL[f.factor]}</span>
                </div>
                <div className="mt-1 text-lg font-semibold text-foreground">
                  {f.pct_change >= 0 ? "+" : ""}
                  {(f.pct_change * 100).toFixed(2)}%
                </div>
                <div className="mt-1 text-xs text-muted-foreground">
                  {formatValue(f.factor, f.actual)} vs {formatValue(f.factor, f.baseline)}
                </div>
              </div>
            );
          })}
        </div>
        <EChartsReactCore echarts={echarts} option={option} style={{ height: 320 }} notMerge />
      </CardContent>
    </Card>
  );
}
