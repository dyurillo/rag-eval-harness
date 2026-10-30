# Deploy Process

Owner: Platform · Last reviewed: 2026-08

## Pipeline

Every merge to `main` builds a container image, runs the test suite and deploys automatically to staging. Production deploys are started with `skr deploy <service>` and always go through a canary.

## Canary

The canary sends 5% of production traffic to the new version for 25 minutes, then 50% for 15 minutes, then 100%. It rolls back automatically if the error rate goes above 0.8%, or if p95 latency rises 30% or more over the previous version's baseline.

## Deploy windows

Production deploys are allowed Monday through Thursday, 09:00 to 15:00 Central. There are no production deploys on Fridays, on weekends, or during a freeze.

## Freezes

- Quarterly freeze: the last 5 business days of each quarter, when many customers run compliance audits.
- Holiday freeze: December 18 through January 3.

## Hotfixes during a freeze

A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform. During a declared SEV1, the incident commander can approve a hotfix on their own.

## Rollback

`skr rollback <service>` returns a service to its previous version. The previous version is kept warm for 48 hours after each deploy, so a rollback within that window takes under two minutes.

## Database migrations

Migrations must stay backward compatible for one release, so the previous application version can still run against the new schema. Migrations run as their own deploy step and never ship together with an application change. A migration that touches more than 10 million rows needs a review from the Data team before it runs.
