# Architecture Overview

Owner: Platform · Last reviewed: 2026-07

## Data flow

1. Skerrow Tags send readings over LTE-M through one of two cellular carriers.
2. Readings arrive at tagbroker, our MQTT broker cluster.
3. ingest-gateway (Go) validates each reading, drops duplicates and writes it to the Kafka topic `readings.raw`, which has 96 partitions keyed by tag ID.
4. normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`. Calibration offsets are looked up in the `core` database.
5. Two consumers read `readings.clean`. excursion-engine checks each reading against its shipment's temperature range. ledger-writer stores readings in TimescaleDB.
6. When excursion-engine detects an excursion, it passes the event to alert-relay, which sends SMS, email and webhook notifications.

## Storage

- TimescaleDB holds recent readings ("hot" storage). Older readings are moved to Parquet files in object storage. The Data Retention Policy says how long each kind of data is kept.
- A Postgres database called `core` holds customers, shipments, users, alert rules and tag calibration data.

## Customer-facing services

skerrow-api (Python) serves Skerrow Console and the public REST API. Webhook delivery for Fleet and Sovereign customers runs inside alert-relay.

## Regions and disaster recovery

Production runs in the us-central region. A disaster-recovery replica runs in ca-east, with help from the Halifax team. The recovery point objective (RPO) is 5 minutes and the recovery time objective (RTO) is 2 hours. Failing over is a manual decision made by the Head of Platform or the CTO.
