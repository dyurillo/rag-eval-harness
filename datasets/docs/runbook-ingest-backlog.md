# Runbook: Ingest Backlog (IngestLagHigh)

Owner: Ingest · Last reviewed: 2026-09

## Alert

`IngestLagHigh` fires when consumer lag on `readings.raw` is above 400,000 messages for 5 minutes, or when the oldest unprocessed message is more than 3 minutes old.

## Severity

Treat it as a SEV2 by default. Upgrade to SEV1 if lag passes 2,000,000 messages or excursion alerts are delayed by more than 10 minutes.

## Diagnosis

1. Open the "Ingest / Lag" dashboard and check whether the lag is spread across all partitions or concentrated in one.
2. Check normalizer pods for restarts or out-of-memory kills.
3. Check TimescaleDB write latency. If ledger-writer is slow, the problem may be downstream of normalizer.

## Scaling normalizer

If lag is spread evenly across partitions, scale normalizer up with `skr scale normalizer --replicas 24`. The ceiling is 48 replicas. Beyond that, normalizer's calibration lookups overload the `core` database and the backlog gets worse, not better.

## Single hot partition

If one partition is far behind the others, the usual cause is a "chatty tag": a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval. Find the tag ID on the dashboard, quarantine it with `skr tag quarantine <tag_id>`, and let the Firmware team know.

## Do not reset consumer offsets

Never reset or skip consumer offsets to clear a backlog. Skipping offsets throws away readings, and any loss of readings is a SEV1.
