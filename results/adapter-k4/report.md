# Eval run report

- Model: rag-lora-1b
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=4)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:39:29.877790+00:00 / 2026-10-23T19:40:05.681497+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 27/48 |
| Overall pass rate | 56.2% |
| Pass rate (exact) | 17/30 = 56.7% |
| Pass rate (judge) | 27/48 = 56.2% |
| Pass rate (retrieval) | 42/42 = 100.0% |
| Pass rate (quote) | 45/48 = 93.8% |
| Quote compliance (answered questions only) | 32/35 = 91.4% |
| Pass rate (tag: access) | 0/2 = 0.0% |
| Pass rate (tag: architecture) | 1/3 = 33.3% |
| Pass rate (tag: deploy) | 4/4 = 100.0% |
| Pass rate (tag: expenses) | 2/2 = 100.0% |
| Pass rate (tag: incident) | 3/4 = 75.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 3/3 = 100.0% |
| Pass rate (tag: numeric) | 11/17 = 64.7% |
| Pass rate (tag: oncall) | 0/3 = 0.0% |
| Pass rate (tag: paraphrase) | 2/4 = 50.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 2/2 = 100.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 3/4 = 75.0% |
| Pass rate (tag: runbook) | 4/9 = 44.4% |
| Pass rate (tag: support) | 0/2 = 0.0% |
| Pass rate (tag: unanswerable) | 6/6 = 100.0% |
| Mean judge score | 3.33 |
| Hallucination rate (unanswerable, judge score <= 2) | 0/6 = 0.0% |
| Retrieval hit@4 | 100.0% |
| Retrieval recall@4 | 98.8% |
| Latency p50 | 250 ms |
| Latency p95 | 580 ms |
| Total tokens | 25426 (prompt 22733, completion 2693) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | fail | 5 | The response correctly states that the Skerrow Tag reports a reading every 90 seconds over LTE-M, which fully matches... | 593 | 0.000000 |
| q02 | pass | pass | pass | pass | pass | 5 | The model correctly states that the battery lasts about 14 months, which matches the reference answer exactly. | 339 | 0.000000 |
| q03 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 ... | 271 | 0.000000 |
| q04 | fail | n/a | fail | pass | pass | 1 | The response describes the general on-call structure but fails to provide the specific handoff time and duration requ... | 404 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and instead claimed the information was missing. | 53 | 0.000000 |
| q06 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and ... | 292 | 0.000000 |
| q07 | pass | n/a | pass | pass | pass | 5 | The model response accurately lists all four criteria for a SEV1 incident as defined in the reference answer, with on... | 528 | 0.000000 |
| q08 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer regarding the 20-minute initial update and subsequent 30-... | 342 | 0.000000 |
| q09 | pass | pass | pass | pass | pass | 5 | The model correctly states that the draft is due within 3 business days and the review meeting within 7 business days... | 268 | 0.000000 |
| q10 | fail | n/a | fail | pass | pass | 1 | The model failed to answer the question and contradicted the reference answer by claiming the context was insufficient. | 51 | 0.000000 |
| q11 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer's details regarding traffic percentages and durations. | 376 | 0.000000 |
| q12 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified ... | 377 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies both required approvers as stated in the reference answer. | 242 | 0.000000 |
| q14 | pass | pass | pass | pass | pass | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 235 | 0.000000 |
| q15 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies the number of partitions (96) and the keying strategy (by tag ID), fully matc... | 392 | 0.000000 |
| q16 | fail | fail | fail | pass | pass | 1 | The model identifies the 'normalizer' service, which is incorrect; the reference answer states that 'excursion-engine... | 266 | 0.000000 |
| q17 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the specific RPO and RTO values stated in the reference answer. | 59 | 0.000000 |
| q18 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-day duration but omits the specific detail about moving to Parquet files in ... | 174 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately captures all conditions and thresholds specified in the reference answer. | 483 | 0.000000 |
| q20 | fail | fail | fail | pass | pass | 1 | The response describes SEV2 criteria rather than the specific conditions for upgrading an ingest backlog to SEV1 as s... | 470 | 0.000000 |
| q21 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer and instead claimed the information was missing, contradicting the ref... | 50 | 0.000000 |
| q22 | pass | n/a | pass | pass | pass | 4 | The response correctly states that offsets should not be reset, but it omits the specific consequence (SEV1) mentione... | 173 | 0.000000 |
| q23 | pass | pass | pass | pass | pass | 5 | The response correctly identifies the cause (chatty tag on firmware 3.2.x), the diagnostic step (find ID on dashboard... | 580 | 0.000000 |
| q24 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer (72 hours) and incorrectly stated that the context did not contain the... | 51 | 0.000000 |
| q25 | fail | fail | fail | pass | pass | 1 | The model response fails to identify the specific carriers (NorthSpan and Corvel Mobile) and instead provides unrelat... | 932 | 0.000000 |
| q26 | pass | n/a | pass | pass | fail | 5 | The model response accurately captures all key details from the reference answer, including the threshold (3%), scope... | 438 | 0.000000 |
| q27 | fail | fail | fail | pass | pass | 1 | The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the referenc... | 180 | 0.000000 |
| q28 | fail | fail | fail | pass | pass | 1 | The response discusses database architecture and does not answer the question about data retention duration. | 243 | 0.000000 |
| q29 | pass | pass | pass | pass | pass | 4 | The response correctly states the 35-day retention period but omits the detail about point-in-time recovery for the l... | 242 | 0.000000 |
| q30 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies that only the General Counsel can place or lift a legal hold, which fully ali... | 202 | 0.000000 |
| q31 | fail | fail | fail | pass | pass | 1 | The response fails to answer the specific question about the duration of temporary access and instead provides unrela... | 132 | 0.000000 |
| q32 | fail | n/a | fail | pass | pass | 2 | The response correctly identifies the usage context (SEV1/JIT failure) but completely omits the critical consequences... | 285 | 0.000000 |
| q33 | pass | pass | pass | pass | pass | 5 | The model correctly identifies the international travel per diem as $85 per day, matching the reference answer. | 271 | 0.000000 |
| q34 | pass | pass | pass | pass | pass | 5 | The model correctly identifies that a director must approve the expense because it falls within the $500 to $5,000 ra... | 272 | 0.000000 |
| q35 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies Thaw Day as a company-wide holiday on the first Friday of March, matching the... | 385 | 0.000000 |
| q36 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer, including the specific timeframe and system requirement. | 355 | 0.000000 |
| q37 | fail | fail | fail | pass | pass | 1 | The model provides an incorrect SLA time (4 hours vs 30 minutes) and incorrect coverage (24/5 vs 24/7), directly cont... | 155 | 0.000000 |
| q38 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subseq... | 331 | 0.000000 |
| q39 | fail | fail | fail | pass | pass | 1 | The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference... | 250 | 0.000000 |
| q40 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the context, contradicting the reference answer. | 53 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct severity (SEV1) and incorrectly stated that the answer was not in the context. | 52 | 0.000000 |
| q42 | fail | fail | fail | pass | pass | 1 | The response fails to answer the question about the retention period (400 days) and instead provides unrelated detail... | 418 | 0.000000 |
| q43 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 57 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 50 | 0.000000 |
| q45 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 51 | 0.000000 |
| q46 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 52 | 0.000000 |
| q47 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the documents do not contain the answer and does not invent any information. | 54 | 0.000000 |
| q48 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the provided context does not contain the answer and does not invent any infor... | 52 | 0.000000 |

## Failures

### q03 - judge

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    By default, Skerrow declares an excursion after 3 consecutive out-of-range readings.
    Quote: "By default, Skerrow declares an excursion after 3 consecutive out-of-range readings." [company-overview]

**Retrieved docs:** company-overview, architecture-overview, incident-severity

**Judge:** score 3 - The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 minutes) requested by the question, missing the key quantitative answer.

### q04 - judge

**Question:** When does the on-call rotation hand off?

**Response:**

    Every engineering team that owns a production service runs its own on-call rotation, with a primary and a secondary. The Platform team runs the infrastructure rotation, which covers tagbroker, Kafka, the databases and the deploy pipeline.
    Quote: "Every engineering team that owns a production service runs its own on-call rotation, with a primary and a secondary." [oncall-policy]

**Retrieved docs:** oncall-policy, pto-and-leave

**Judge:** score 1 - The response describes the general on-call structure but fails to provide the specific handoff time and duration requested in the question.

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** oncall-policy, incident-severity, pto-and-leave

**Judge:** score 1 - The model failed to provide the correct answer ($340) and instead claimed the information was missing.

### q06 - judge

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary.
    Quote: "If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary." [oncall-policy]

**Retrieved docs:** oncall-policy, runbook-tag-offline, incident-severity

**Judge:** score 3 - The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and the subsequent escalation to the engineering manager (10 minutes later) mentioned in the reference answer.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity, deploy-process, oncall-policy

**Judge:** score 1 - The model failed to answer the question and contradicted the reference answer by claiming the context was insufficient.

### q16 - exact, judge

**Question:** Which service checks readings against a shipment's temperature range?

**Response:**

    normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`.
    Quote: "normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`." [architecture-overview]

**Retrieved docs:** architecture-overview, company-overview, customer-support-escalation, access-control

**Judge:** score 1 - The model identifies the 'normalizer' service, which is incorrect; the reference answer states that 'excursion-engine' performs the check.

### q17 - judge

**Question:** What are the disaster recovery RPO and RTO?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** architecture-overview, data-retention, company-overview, runbook-tag-offline

**Judge:** score 1 - The model failed to provide the specific RPO and RTO values stated in the reference answer.

### q20 - exact, judge

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:
    - Alert delivery is delayed by more than 4 minutes at p95.
    - A single Sovereign customer has a full outage.
    - Skerrow Console is unavailable while ingest and alerting still work.
    Quote: "An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:" [incident-severity]

**Retrieved docs:** incident-severity, runbook-ingest-backlog

**Judge:** score 1 - The response describes SEV2 criteria rather than the specific conditions for upgrading an ingest backlog to SEV1 as stated in the reference answer.

### q21 - exact, judge

**Question:** What's the maximum number of normalizer replicas, and why is there a limit?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog, pto-and-leave, access-control

**Judge:** score 1 - The model failed to provide the correct answer and instead claimed the information was missing, contradicting the reference answer.

### q24 - exact, judge

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** data-retention, architecture-overview, incident-severity, runbook-tag-offline

**Judge:** score 1 - The model failed to provide the correct answer (72 hours) and incorrectly stated that the context did not contain the answer.

### q25 - exact, judge

**Question:** Which cellular carriers do Skerrow Tags use?

**Response:**

    1. Skerrow Tags send readings over LTE-M through one of two cellular carriers.
    2. Readings arrive at tagbroker, our MQTT broker cluster.
    3. ingest-gateway (Go) validates each reading, drops duplicates and writes it to the Kafka topic `readings.raw`, which has 96 partitions keyed by tag ID.
    4. normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`. Calibration offsets are looked up in the `core` database.
    5. Two consumers read `readings.clean`. excursion-engine checks each reading against its shipment's temperature range. ledger-writer stores readings in TimescaleDB.
    6. When excursion-engine detects an excursion, it passes the event to alert-relay, which sends SMS, email and webhook notifications.
    Quote: "1. Skerrow Tags send readings over LTE-M through one of two cellular carriers." [architecture-overview]

**Retrieved docs:** architecture-overview, runbook-tag-offline, company-overview

**Judge:** score 1 - The model response fails to identify the specific carriers (NorthSpan and Corvel Mobile) and instead provides unrelated technical details about the data pipeline.

### q27 - exact, judge

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    Most spikes are cellular carrier outages, not problems on our side.
    Quote: "Most spikes are cellular carrier outages, not problems on our side." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline, pto-and-leave

**Judge:** score 1 - The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the reference identifies it as a tagbroker issue requiring a page to Platform on-call.

### q28 - exact, judge

**Question:** How long are raw readings kept for customers on the Sovereign plan?

**Response:**

    - A Postgres database called `core` holds customers, shipments, users, alert rules and tag calibration data.
    Quote: "A Postgres database called `core` holds customers, shipments, users, alert rules and tag calibration data." [architecture-overview]

**Retrieved docs:** architecture-overview, data-retention, runbook-ingest-backlog, customer-support-escalation

**Judge:** score 1 - The response discusses database architecture and does not answer the question about data retention duration.

### q31 - exact, judge

**Question:** What's the longest stretch of temporary production access I can get?

**Response:**

    Only the Platform team has standing production access.
    Quote: "Only the Platform team has standing production access." [access-control]

**Retrieved docs:** access-control, pto-and-leave, company-overview

**Judge:** score 1 - The response fails to answer the specific question about the duration of temporary access and instead provides unrelated information about standing access.

### q32 - judge

**Question:** What happens when someone uses the break-glass account?

**Response:**

    The `breakglass` account is for SEV1 incidents when JIT access isn't working. Its credentials are kept in a sealed vault entry.
    Quote: "The `breakglass` account is for SEV1 incidents when JIT access isn't working." [access-control]

**Retrieved docs:** access-control, runbook-tag-offline, customer-support-escalation

**Judge:** score 2 - The response correctly identifies the usage context (SEV1/JIT failure) but completely omits the critical consequences (paging Head of Security, audit logging, and 24-hour report requirement) specified in the reference answer.

### q37 - exact, judge

**Question:** What's the first-response SLA for urgent tickets on the Sovereign plan?

**Response:**

    4 hours | 24/5 |
    Quote: "4 hours | 24/5 |" [customer-support-escalation]

**Retrieved docs:** customer-support-escalation, data-retention

**Judge:** score 1 - The model provides an incorrect SLA time (4 hours vs 30 minutes) and incorrect coverage (24/5 vs 24/7), directly contradicting the reference answer.

### q38 - judge

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate.
    Quote: "When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate." [customer-support-escalation]

**Retrieved docs:** customer-support-escalation, access-control, architecture-overview

**Judge:** score 3 - The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subsequent steps regarding the 12-month calibration cycle and the customer credit policy.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.
    Quote: "A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform." [deploy-process]

**Retrieved docs:** deploy-process, customer-support-escalation, access-control, runbook-ingest-backlog

**Judge:** score 1 - The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference states the incident commander can approve it alone.

### q40 - judge

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-tag-offline, incident-severity, oncall-policy

**Judge:** score 1 - The model failed to provide the answer contained in the context, contradicting the reference answer.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-tag-offline, incident-severity

**Judge:** score 1 - The model failed to provide the correct severity (SEV1) and incorrectly stated that the answer was not in the context.

### q42 - exact, judge

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    Using it automatically pages the Head of Security, every action taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.
    Quote: "Using it automatically pages the Head of Security, every action taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours." [data-retention]

**Retrieved docs:** access-control, architecture-overview, oncall-policy, data-retention

**Judge:** score 1 - The response fails to answer the question about the retention period (400 days) and instead provides unrelated details about paging and reporting.
