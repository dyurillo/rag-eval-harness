# Data Retention Policy

Owner: Data · Last reviewed: 2026-04

## Retention by data class

| Data | Retention |
|---|---|
| Raw readings, Sovereign plan | 7 years |
| Raw readings, Starter and Fleet plans | 2 years |
| Alert history | 3 years |
| Support tickets | 5 years |
| Application logs | 21 days |
| Audit logs | 400 days |
| Customer contact information | Deleted 90 days after the contract ends |

## Hot and cold storage

Readings stay in TimescaleDB for 30 days. After that they're moved to Parquet files in object storage, where they're kept for the rest of their retention period.

## Backups

The `core` Postgres database is backed up nightly, and backups are kept for 35 days. Point-in-time recovery is available for the last 7 days.

## Deletion requests

The Data team handles customer data deletion requests through the DATA-DEL ticket queue. Each request must be completed within 30 days.

## Legal holds

A legal hold overrides every retention period and deletion request. Only the General Counsel can place or lift a legal hold.
