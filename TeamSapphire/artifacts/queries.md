# Every query this investigation ran

**131 queries · 1,218,035,028 rows read · 52,932 ms of ClickHouse time.**

Each is the exact SQL sent to ClickHouse, with the rows it read and the
time it took, in execution order. Parameters appear as `{name:Type}` —
they are bound by the client, never string-formatted, so these are
runnable as-is once the window is substituted.

Every number in every diagnosis comes from one of these. Nothing in the
prose was computed anywhere else.

| # | Stage | Rows read | Time |
|---:|---|---:|---:|
| 1 | `detect:revenue` | 1,920 | 53.6 ms |
| 2 | `detect:requests` | 1,920 | 43.7 ms |
| 3 | `detect:fill_rate` | 1,920 | 53.7 ms |
| 4 | `detect:ecpm` | 1,920 | 46.3 ms |
| 5 | `detect:ctr` | 1,920 | 65.5 ms |
| 6 | `detect_segments:revenue` | 122,880 | 297.6 ms |
| 7 | `detect_segments:requests` | 122,880 | 123.3 ms |
| 8 | `detect_segments:fill_rate` | 122,880 | 209.7 ms |
| 9 | `detect_segments:ecpm` | 122,880 | 271.5 ms |
| 10 | `detect_segments:ctr` | 122,880 | 181.4 ms |
| 11 | `baseline:data_range` | 1 | 38.5 ms |
| 12 | `decompose:window_vs_baseline` | 4,800 | 49.4 ms |
| 13 | `localize:ecpm` | 307,200 | 52.9 ms |
| 14 | `characterize:ecpm:ad_format=video` | 15,872 | 47.6 ms |
| 15 | `characterize:baseline:ad_format=video` | 15,872 | 44.8 ms |
| 16 | `baseline:data_range` | 1 | 32.3 ms |
| 17 | `decompose:window_vs_baseline` | 3,840 | 47.3 ms |
| 18 | `localize:fill_rate` | 245,760 | 52.0 ms |
| 19 | `characterize:fill_rate:os_version=Android 15` | 15,872 | 47.6 ms |
| 20 | `characterize:baseline:os_version=Android 15` | 15,872 | 36.7 ms |
| 21 | `baseline:data_range` | 1 | 71.0 ms |
| 22 | `decompose:window_vs_baseline` | 2,880 | 110.5 ms |
| 23 | `localize:requests` | 184,320 | 64.7 ms |
| 24 | `characterize:requests:global` | 960 | 45.7 ms |
| 25 | `characterize:baseline:global` | 960 | 45.5 ms |
| 26 | `baseline:data_range` | 1 | 48.7 ms |
| 27 | `decompose:window_vs_baseline` | 3,840 | 72.1 ms |
| 28 | `localize:requests` | 245,760 | 81.9 ms |
| 29 | `characterize:requests:global` | 960 | 59.6 ms |
| 30 | `characterize:baseline:global` | 960 | 56.9 ms |
| 31 | `baseline:data_range` | 1 | 46.7 ms |
| 32 | `decompose:window_vs_baseline` | 2,880 | 61.8 ms |
| 33 | `localize:requests` | 184,320 | 69.2 ms |
| 34 | `characterize:requests:global` | 960 | 59.1 ms |
| 35 | `characterize:baseline:global` | 960 | 38.5 ms |
| 36 | `baseline:data_range` | 1 | 43.4 ms |
| 37 | `decompose:window_vs_baseline` | 2,880 | 45.4 ms |
| 38 | `localize:requests` | 184,320 | 88.1 ms |
| 39 | `characterize:requests:global` | 960 | 68.1 ms |
| 40 | `characterize:baseline:global` | 960 | 42.0 ms |
| 41 | `baseline:data_range` | 1 | 54.8 ms |
| 42 | `decompose:window_vs_baseline` | 2,880 | 57.7 ms |
| 43 | `localize:requests` | 184,320 | 96.0 ms |
| 44 | `characterize:requests:category=gaming` | 15,872 | 66.0 ms |
| 45 | `characterize:baseline:category=gaming` | 15,872 | 102.2 ms |
| 46 | `baseline:data_range` | 1 | 49.7 ms |
| 47 | `decompose:window_vs_baseline` | 3,840 | 51.9 ms |
| 48 | `localize:requests` | 245,760 | 181.6 ms |
| 49 | `characterize:requests:publisher_tier=tier_1` | 15,872 | 173.2 ms |
| 50 | `characterize:baseline:publisher_tier=tier_1` | 15,872 | 144.8 ms |
| 51 | `baseline:data_range` | 1 | 44.1 ms |
| 52 | `decompose:window_vs_baseline` | 4,800 | 238.7 ms |
| 53 | `localize:requests` | 307,200 | 128.3 ms |
| 54 | `characterize:requests:device_model=Galaxy A54` | 15,872 | 99.5 ms |
| 55 | `characterize:baseline:device_model=Galaxy A54` | 15,872 | 139.3 ms |
| 56 | `baseline:data_range` | 1 | 56.7 ms |
| 57 | `decompose:window_vs_baseline` | 3,840 | 77.7 ms |
| 58 | `localize:requests` | 245,760 | 92.4 ms |
| 59 | `characterize:requests:device_model=iPhone 15` | 15,872 | 119.3 ms |
| 60 | `characterize:baseline:device_model=iPhone 15` | 15,872 | 72.9 ms |
| 61 | `baseline:data_range` | 1 | 45.5 ms |
| 62 | `decompose:window_vs_baseline` | 4,800 | 59.2 ms |
| 63 | `localize:requests` | 307,200 | 79.0 ms |
| 64 | `characterize:requests:publisher_tier=tier_2` | 15,872 | 39.7 ms |
| 65 | `characterize:baseline:publisher_tier=tier_2` | 15,872 | 49.9 ms |
| 66 | `baseline:data_range` | 1 | 55.7 ms |
| 67 | `decompose:window_vs_baseline` | 2,880 | 53.6 ms |
| 68 | `localize:requests` | 184,320 | 58.9 ms |
| 69 | `characterize:requests:campaign_type=CPM` | 15,872 | 58.8 ms |
| 70 | `characterize:baseline:campaign_type=CPM` | 15,872 | 43.6 ms |
| 71 | `baseline:data_range` | 1 | 38.3 ms |
| 72 | `decompose:window_vs_baseline` | 3,840 | 51.4 ms |
| 73 | `localize:requests` | 245,760 | 204.7 ms |
| 74 | `characterize:requests:global` | 960 | 113.7 ms |
| 75 | `characterize:baseline:global` | 960 | 162.5 ms |
| 76 | `baseline:data_range` | 1 | 208.2 ms |
| 77 | `decompose:window_vs_baseline` | 4,800 | 108.0 ms |
| 78 | `localize:requests` | 307,200 | 97.3 ms |
| 79 | `characterize:requests:os_version=iOS 18.1` | 15,872 | 54.2 ms |
| 80 | `characterize:baseline:os_version=iOS 18.1` | 15,872 | 75.9 ms |
| 81 | `baseline:data_range` | 1 | 69.8 ms |
| 82 | `decompose:window_vs_baseline` | 4,800 | 80.1 ms |
| 83 | `localize:requests` | 307,200 | 124.5 ms |
| 84 | `characterize:requests:global` | 960 | 53.8 ms |
| 85 | `characterize:baseline:global` | 960 | 54.8 ms |
| 86 | `baseline:data_range` | 1 | 35.2 ms |
| 87 | `decompose:window_vs_baseline` | 2,880 | 63.7 ms |
| 88 | `localize:requests` | 184,320 | 72.0 ms |
| 89 | `characterize:requests:ad_format=native` | 15,872 | 120.1 ms |
| 90 | `characterize:baseline:ad_format=native` | 15,872 | 249.4 ms |
| 91 | `baseline:data_range` | 1 | 140.1 ms |
| 92 | `decompose:window_vs_baseline` | 4,800 | 70.8 ms |
| 93 | `localize:requests` | 307,200 | 92.0 ms |
| 94 | `characterize:requests:publisher_tier=tier_3` | 15,872 | 65.6 ms |
| 95 | `characterize:baseline:publisher_tier=tier_3` | 15,872 | 73.9 ms |
| 96 | `baseline:data_range` | 1 | 32.8 ms |
| 97 | `decompose:window_vs_baseline` | 2,880 | 275.2 ms |
| 98 | `localize:ecpm` | 184,320 | 330.7 ms |
| 99 | `characterize:ecpm:category=finance` | 15,872 | 170.4 ms |
| 100 | `characterize:baseline:category=finance` | 15,872 | 74.6 ms |
| 101 | `baseline:data_range` | 1 | 60.1 ms |
| 102 | `decompose:window_vs_baseline` | 4,800 | 84.5 ms |
| 103 | `localize:requests` | 307,200 | 88.0 ms |
| 104 | `characterize:requests:device_model=iPhone 15` | 15,872 | 109.0 ms |
| 105 | `characterize:baseline:device_model=iPhone 15` | 15,872 | 63.5 ms |
| 106 | `baseline:data_range` | 1 | 50.3 ms |
| 107 | `decompose:window_vs_baseline` | 4,800 | 88.7 ms |
| 108 | `localize:requests` | 307,200 | 81.3 ms |
| 109 | `characterize:requests:global` | 960 | 62.3 ms |
| 110 | `characterize:baseline:global` | 960 | 46.1 ms |
| 111 | `scan_intersect:regionxdevice_model` | 57,710,976 | 2060.8 ms |
| 112 | `scan_intersect:regionxos_version` | 57,710,976 | 2043.1 ms |
| 113 | `scan_intersect:regionxcategory` | 57,710,976 | 2301.5 ms |
| 114 | `scan_intersect:regionxpublisher_tier` | 57,710,976 | 2181.2 ms |
| 115 | `scan_intersect:regionxad_format` | 57,710,976 | 1755.8 ms |
| 116 | `scan_intersect:regionxcountry` | 57,710,976 | 2036.7 ms |
| 117 | `scan_intersect:device_modelxos_version` | 57,710,976 | 2003.9 ms |
| 118 | `scan_intersect:device_modelxcategory` | 57,710,976 | 2284.5 ms |
| 119 | `scan_intersect:device_modelxpublisher_tier` | 57,710,976 | 2232.6 ms |
| 120 | `scan_intersect:device_modelxad_format` | 57,710,976 | 1602.5 ms |
| 121 | `scan_intersect:device_modelxcountry` | 57,710,976 | 1984.8 ms |
| 122 | `scan_intersect:os_versionxcategory` | 57,710,976 | 2661.9 ms |
| 123 | `scan_intersect:os_versionxpublisher_tier` | 57,710,976 | 2235.0 ms |
| 124 | `scan_intersect:os_versionxad_format` | 57,710,976 | 1750.7 ms |
| 125 | `scan_intersect:os_versionxcountry` | 57,710,976 | 2155.5 ms |
| 126 | `scan_intersect:categoryxpublisher_tier` | 57,710,976 | 2125.3 ms |
| 127 | `scan_intersect:categoryxad_format` | 57,710,976 | 1728.7 ms |
| 128 | `scan_intersect:categoryxcountry` | 57,710,976 | 2317.6 ms |
| 129 | `scan_intersect:publisher_tierxad_format` | 57,710,976 | 1628.8 ms |
| 130 | `scan_intersect:publisher_tierxcountry` | 57,710,976 | 2280.8 ms |
| 131 | `scan_intersect:ad_formatxcountry` | 57,710,976 | 1857.3 ms |

---

## `baseline:data_range` — 20 call(s)

1 rows · 38.5 ms

```sql
SELECT min(hour) AS first_hour FROM inmobi.events_hourly
```

## `characterize:baseline:ad_format=native` — 1 call(s)

15,872 rows · 249.4 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:ad_format=video` — 1 call(s)

15,872 rows · 44.8 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:campaign_type=CPM` — 1 call(s)

15,872 rows · 43.6 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:category=finance` — 1 call(s)

15,872 rows · 74.6 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:category=gaming` — 1 call(s)

15,872 rows · 102.2 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:device_model=Galaxy A54` — 1 call(s)

15,872 rows · 139.3 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:device_model=iPhone 15` — 2 call(s)

15,872 rows · 72.9 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:global` — 7 call(s)

960 rows · 45.5 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1)
```

## `characterize:baseline:os_version=Android 15` — 1 call(s)

15,872 rows · 36.7 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:os_version=iOS 18.1` — 1 call(s)

15,872 rows · 75.9 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:publisher_tier=tier_1` — 1 call(s)

15,872 rows · 144.8 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:publisher_tier=tier_2` — 1 call(s)

15,872 rows · 49.9 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:baseline:publisher_tier=tier_3` — 1 call(s)

15,872 rows · 73.9 ms

```sql
SELECT requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String}
```

## `characterize:ecpm:ad_format=video` — 1 call(s)

15,872 rows · 47.6 ms

```sql
SELECT hour, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:ecpm:category=finance` — 1 call(s)

15,872 rows · 170.4 ms

```sql
SELECT hour, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:fill_rate:os_version=Android 15` — 1 call(s)

15,872 rows · 47.6 ms

```sql
SELECT hour, if(requests > 0, fills / requests, 0) AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:ad_format=native` — 1 call(s)

15,872 rows · 120.1 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:campaign_type=CPM` — 1 call(s)

15,872 rows · 58.8 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:category=gaming` — 1 call(s)

15,872 rows · 66.0 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:device_model=Galaxy A54` — 1 call(s)

15,872 rows · 99.5 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:device_model=iPhone 15` — 2 call(s)

15,872 rows · 119.3 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:global` — 7 call(s)

960 rows · 45.7 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) ORDER BY hour
```

## `characterize:requests:os_version=iOS 18.1` — 1 call(s)

15,872 rows · 54.2 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:publisher_tier=tier_1` — 1 call(s)

15,872 rows · 173.2 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:publisher_tier=tier_2` — 1 call(s)

15,872 rows · 39.7 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `characterize:requests:publisher_tier=tier_3` — 1 call(s)

15,872 rows · 65.6 ms

```sql
SELECT hour, requests AS metric_value, requests AS requests, if(requests > 0, fills / requests, 0) AS fill_rate, if(fills > 0, impressions / fills, 0) AS render_rate, (if(impressions > 0, revenue / impressions, 0)) * 1000 AS ecpm FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalHour({ctx:UInt16}) AND hour <= {end:DateTime} + toIntervalHour({ctx:UInt16}) AND dim_name = {dim_name:String} AND dim_value = {dim_value:String} ORDER BY hour
```

## `decompose:window_vs_baseline` — 20 call(s)

4,800 rows · 49.4 ms

```sql
SELECT 0 AS weeks_back, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} UNION ALL SELECT 1 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) UNION ALL SELECT 2 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) UNION ALL SELECT 3 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) UNION ALL SELECT 4 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(4) AND hour <= {end:DateTime} - toIntervalWeek(4) ORDER BY weeks_back
```

3,840 rows · 47.3 ms

```sql
SELECT 0 AS weeks_back, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} UNION ALL SELECT 1 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) UNION ALL SELECT 2 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) UNION ALL SELECT 3 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) ORDER BY weeks_back
```

2,880 rows · 110.5 ms

```sql
SELECT 0 AS weeks_back, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} UNION ALL SELECT 1 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) UNION ALL SELECT 2 AS weeks_back, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) ORDER BY weeks_back
```

## `detect:ctr` — 1 call(s)

1,920 rows · 65.5 ms

```sql
WITH target AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(impressions > 0, clicks / impressions, 0) AS metric_value, impressions AS denom FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour < {end:DateTime} ), hist AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(impressions > 0, clicks / impressions, 0) AS metric_value FROM inmobi.events_hourly WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.metric_value, t.denom ORDER BY t.hour
```

## `detect:ecpm` — 1 call(s)

1,920 rows · 46.3 ms

```sql
WITH target AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(impressions > 0, revenue / impressions * 1000, 0) AS metric_value, 0 AS denom FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour < {end:DateTime} ), hist AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(impressions > 0, revenue / impressions * 1000, 0) AS metric_value FROM inmobi.events_hourly WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.metric_value, t.denom ORDER BY t.hour
```

## `detect:fill_rate` — 1 call(s)

1,920 rows · 53.7 ms

```sql
WITH target AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(requests > 0, fills / requests, 0) AS metric_value, requests AS denom FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour < {end:DateTime} ), hist AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(requests > 0, fills / requests, 0) AS metric_value FROM inmobi.events_hourly WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.metric_value, t.denom ORDER BY t.hour
```

## `detect:requests` — 1 call(s)

1,920 rows · 43.7 ms

```sql
WITH target AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, requests AS metric_value, 0 AS denom FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour < {end:DateTime} ), hist AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests AS metric_value FROM inmobi.events_hourly WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.metric_value, t.denom ORDER BY t.hour
```

## `detect:revenue` — 1 call(s)

1,920 rows · 53.6 ms

```sql
WITH target AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, revenue AS metric_value, 0 AS denom FROM inmobi.events_hourly WHERE hour >= {start:DateTime} AND hour < {end:DateTime} ), hist AS ( SELECT hour, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, revenue AS metric_value FROM inmobi.events_hourly WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.metric_value, t.denom ORDER BY t.hour
```

## `detect_segments:ctr` — 1 call(s)

122,880 rows · 181.4 ms

```sql
WITH target AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(impressions > 0, clicks / impressions, 0) AS metric_value, impressions AS denom FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour < {end:DateTime} AND requests >= {min_volume:UInt32} ), hist AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(impressions > 0, clicks / impressions, 0) AS metric_value FROM inmobi.events_hourly_by_dim WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.dim_name AS dim_name, t.dim_value AS dim_value, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dim_name = h.dim_name AND t.dim_value = h.dim_value AND t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.dim_name, t.dim_value, t.metric_value, t.denom ORDER BY t.hour
```

## `detect_segments:ecpm` — 1 call(s)

122,880 rows · 271.5 ms

```sql
WITH target AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(impressions > 0, revenue / impressions * 1000, 0) AS metric_value, 0 AS denom FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour < {end:DateTime} AND requests >= {min_volume:UInt32} ), hist AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(impressions > 0, revenue / impressions * 1000, 0) AS metric_value FROM inmobi.events_hourly_by_dim WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.dim_name AS dim_name, t.dim_value AS dim_value, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dim_name = h.dim_name AND t.dim_value = h.dim_value AND t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.dim_name, t.dim_value, t.metric_value, t.denom ORDER BY t.hour
```

## `detect_segments:fill_rate` — 1 call(s)

122,880 rows · 209.7 ms

```sql
WITH target AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, if(requests > 0, fills / requests, 0) AS metric_value, requests AS denom FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour < {end:DateTime} AND requests >= {min_volume:UInt32} ), hist AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, if(requests > 0, fills / requests, 0) AS metric_value FROM inmobi.events_hourly_by_dim WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.dim_name AS dim_name, t.dim_value AS dim_value, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dim_name = h.dim_name AND t.dim_value = h.dim_value AND t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.dim_name, t.dim_value, t.metric_value, t.denom ORDER BY t.hour
```

## `detect_segments:requests` — 1 call(s)

122,880 rows · 123.3 ms

```sql
WITH target AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, requests AS metric_value, 0 AS denom FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour < {end:DateTime} AND requests >= {min_volume:UInt32} ), hist AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests AS metric_value FROM inmobi.events_hourly_by_dim WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.dim_name AS dim_name, t.dim_value AS dim_value, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dim_name = h.dim_name AND t.dim_value = h.dim_value AND t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.dim_name, t.dim_value, t.metric_value, t.denom ORDER BY t.hour
```

## `detect_segments:revenue` — 1 call(s)

122,880 rows · 297.6 ms

```sql
WITH target AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, requests, fills, impressions, clicks, revenue, revenue AS metric_value, 0 AS denom FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour < {end:DateTime} AND requests >= {min_volume:UInt32} ), hist AS ( SELECT hour, dim_name, dim_value, toDayOfWeek(hour) AS dow, toHour(hour) AS hod, revenue AS metric_value FROM inmobi.events_hourly_by_dim WHERE hour < {end:DateTime} ) SELECT t.hour AS hour, t.dim_name AS dim_name, t.dim_value AS dim_value, t.metric_value AS actual, t.denom AS denom, quantileExact(0.5)(h.metric_value) AS baseline, stddevPop(h.metric_value) AS spread, count() AS baseline_samples FROM target AS t INNER JOIN hist AS h ON t.dim_name = h.dim_name AND t.dim_value = h.dim_value AND t.dow = h.dow AND t.hod = h.hod WHERE h.hour < t.hour AND h.hour >= t.hour - toIntervalWeek({weeks:UInt8}) GROUP BY t.hour, t.dim_name, t.dim_value, t.metric_value, t.denom ORDER BY t.hour
```

## `localize:ecpm` — 2 call(s)

307,200 rows · 52.9 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value UNION ALL SELECT 3 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) GROUP BY dim_name, dim_value UNION ALL SELECT 4 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(4) AND hour <= {end:DateTime} - toIntervalWeek(4) GROUP BY dim_name, dim_value
```

184,320 rows · 330.7 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value
```

## `localize:fill_rate` — 1 call(s)

245,760 rows · 52.0 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value UNION ALL SELECT 3 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) GROUP BY dim_name, dim_value
```

## `localize:requests` — 17 call(s)

184,320 rows · 64.7 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value
```

245,760 rows · 81.9 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value UNION ALL SELECT 3 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) GROUP BY dim_name, dim_value
```

307,200 rows · 128.3 ms

```sql
SELECT 0 AS weeks_back, dim_name, dim_value, sum(requests) AS requests, sum(fills) AS fills, sum(impressions) AS impressions, sum(clicks) AS clicks, sum(revenue) AS revenue FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} AND hour <= {end:DateTime} GROUP BY dim_name, dim_value UNION ALL SELECT 1 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(1) AND hour <= {end:DateTime} - toIntervalWeek(1) GROUP BY dim_name, dim_value UNION ALL SELECT 2 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(2) AND hour <= {end:DateTime} - toIntervalWeek(2) GROUP BY dim_name, dim_value UNION ALL SELECT 3 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(3) AND hour <= {end:DateTime} - toIntervalWeek(3) GROUP BY dim_name, dim_value UNION ALL SELECT 4 AS weeks_back, dim_name, dim_value, sum(requests), sum(fills), sum(impressions), sum(clicks), sum(revenue) FROM inmobi.events_hourly_by_dim WHERE hour >= {start:DateTime} - toIntervalWeek(4) AND hour <= {end:DateTime} - toIntervalWeek(4) GROUP BY dim_name, dim_value
```

## `scan_intersect:ad_formatxcountry` — 1 call(s)

57,710,976 rows · 1857.3 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, CAST(ad_format AS String) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:categoryxad_format` — 1 call(s)

57,710,976 rows · 1728.7 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_apps','category', app_id) AS va, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:categoryxcountry` — 1 call(s)

57,710,976 rows · 2317.6 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_apps','category', app_id) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:categoryxpublisher_tier` — 1 call(s)

57,710,976 rows · 2125.3 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_apps','category', app_id) AS va, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:device_modelxad_format` — 1 call(s)

57,710,976 rows · 1602.5 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:device_modelxcategory` — 1 call(s)

57,710,976 rows · 2284.5 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:device_modelxcountry` — 1 call(s)

57,710,976 rows · 1984.8 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:device_modelxos_version` — 1 call(s)

57,710,976 rows · 2003.9 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:device_modelxpublisher_tier` — 1 call(s)

57,710,976 rows · 2232.6 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:os_versionxad_format` — 1 call(s)

57,710,976 rows · 1750.7 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:os_versionxcategory` — 1 call(s)

57,710,976 rows · 2661.9 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:os_versionxcountry` — 1 call(s)

57,710,976 rows · 2155.5 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:os_versionxpublisher_tier` — 1 call(s)

57,710,976 rows · 2235.0 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:publisher_tierxad_format` — 1 call(s)

57,710,976 rows · 1628.8 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS va, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:publisher_tierxcountry` — 1 call(s)

57,710,976 rows · 2280.8 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxad_format` — 1 call(s)

57,710,976 rows · 1755.8 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, CAST(ad_format AS String) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxcategory` — 1 call(s)

57,710,976 rows · 2301.5 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','category', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxcountry` — 1 call(s)

57,710,976 rows · 2036.7 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','country', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxdevice_model` — 1 call(s)

57,710,976 rows · 2060.8 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','device_model', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxos_version` — 1 call(s)

57,710,976 rows · 2043.1 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','os_version', geo_device_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```

## `scan_intersect:regionxpublisher_tier` — 1 call(s)

57,710,976 rows · 2181.2 ms

```sql
WITH cells AS ( SELECT toDate(event_time) AS day, toDayOfWeek(event_time) AS dow, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS metric_value, count() AS requests FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, dow, va, vb HAVING requests >= {minreq:UInt32} ), pa AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_geo_device','region', geo_device_id) AS va, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, va ), pb AS ( SELECT toDate(event_time) AS day, dictGetString('inmobi.dict_apps','publisher_tier', app_id) AS vb, (sum(is_filled)) / (count()) AS v FROM inmobi.ad_events WHERE event_time >= {start:DateTime} - toIntervalWeek({weeks:UInt8}) AND event_time <= {end:DateTime} GROUP BY day, vb ) SELECT t.day AS day, t.va AS va, t.vb AS vb, t.metric_value AS actual, t.requests AS requests, quantileExact(0.5)(h.metric_value) AS baseline, any(pa_now.v) AS pa_now, quantileExact(0.5)(pa_hist.v) AS pa_base, any(pb_now.v) AS pb_now, quantileExact(0.5)(pb_hist.v) AS pb_base FROM cells AS t INNER JOIN cells AS h ON t.va=h.va AND t.vb=h.vb AND t.dow=h.dow AND h.day < t.day INNER JOIN pa AS pa_now ON pa_now.day = t.day AND pa_now.va = t.va INNER JOIN pa AS pa_hist ON pa_hist.va = t.va AND toDayOfWeek(pa_hist.day)=t.dow AND pa_hist.day < t.day INNER JOIN pb AS pb_now ON pb_now.day = t.day AND pb_now.vb = t.vb INNER JOIN pb AS pb_hist ON pb_hist.vb = t.vb AND toDayOfWeek(pb_hist.day)=t.dow AND pb_hist.day < t.day WHERE t.day >= toDate({start:DateTime}) GROUP BY day, va, vb, actual, requests
```
