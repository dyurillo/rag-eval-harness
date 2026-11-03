# Eval run report

- Model: rag-lora-1b
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=2)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:38:53.068210+00:00 / 2026-10-23T19:39:29.451372+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 25/48 |
| Overall pass rate | 52.1% |
| Pass rate (exact) | 16/30 = 53.3% |
| Pass rate (judge) | 25/48 = 52.1% |
| Pass rate (retrieval) | 40/42 = 95.2% |
| Pass rate (quote) | 43/48 = 89.6% |
| Quote compliance (answered questions only) | 31/34 = 91.2% |
| Pass rate (tag: access) | 2/2 = 100.0% |
| Pass rate (tag: architecture) | 1/3 = 33.3% |
| Pass rate (tag: deploy) | 4/4 = 100.0% |
| Pass rate (tag: expenses) | 1/2 = 50.0% |
| Pass rate (tag: incident) | 2/4 = 50.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 2/3 = 66.7% |
| Pass rate (tag: numeric) | 12/17 = 70.6% |
| Pass rate (tag: oncall) | 1/3 = 33.3% |
| Pass rate (tag: paraphrase) | 2/4 = 50.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 1/2 = 50.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 3/4 = 75.0% |
| Pass rate (tag: runbook) | 3/9 = 33.3% |
| Pass rate (tag: support) | 1/2 = 50.0% |
| Pass rate (tag: unanswerable) | 4/6 = 66.7% |
| Mean judge score | 3.12 |
| Hallucination rate (unanswerable, judge score <= 2) | 2/6 = 33.3% |
| Retrieval hit@2 | 95.2% |
| Retrieval recall@2 | 90.5% |
| Latency p50 | 236 ms |
| Latency p95 | 468 ms |
| Total tokens | 18468 (prompt 15835, completion 2633) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | pass | 5 | The model correctly states that the Skerrow Tag reports a reading every 90 seconds over LTE-M, which fully matches th... | 417 | 0.000000 |
| q02 | pass | pass | pass | pass | pass | 5 | The model correctly states that the battery lasts about 14 months, which matches the reference answer exactly. | 330 | 0.000000 |
| q03 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 ... | 271 | 0.000000 |
| q04 | pass | n/a | pass | pass | pass | 4 | The response correctly identifies the day and time of the handoff but omits the specific detail about the 15-minute h... | 274 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and instead claimed the information was missing. | 50 | 0.000000 |
| q06 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and ... | 287 | 0.000000 |
| q07 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the reference, claiming the context was insufficient. | 57 | 0.000000 |
| q08 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer regarding the 20-minute initial update and subsequent 30-... | 332 | 0.000000 |
| q09 | pass | pass | pass | pass | pass | 5 | The model correctly states that the draft is due within 3 business days and the review meeting within 7 business days... | 257 | 0.000000 |
| q10 | fail | n/a | fail | pass | pass | 1 | The model failed to answer the question and contradicted the reference answer by claiming the context did not contain... | 47 | 0.000000 |
| q11 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer's details regarding traffic percentages and durations. | 360 | 0.000000 |
| q12 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified ... | 355 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies both required approvers as stated in the reference answer. | 236 | 0.000000 |
| q14 | pass | pass | pass | pass | pass | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 289 | 0.000000 |
| q15 | pass | pass | pass | pass | pass | 5 | The model response explicitly states that the readings.raw topic has 96 partitions keyed by tag ID, which fully match... | 925 | 0.000000 |
| q16 | fail | fail | fail | pass | fail | 1 | The model identifies the 'normalizer' service, which is incorrect; the reference answer states that 'excursion-engine... | 257 | 0.000000 |
| q17 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the specific RPO and RTO values stated in the reference answer. | 57 | 0.000000 |
| q18 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-day duration but omits the specific detail about moving to Parquet files in ... | 164 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately captures all conditions and thresholds specified in the reference answer. | 468 | 0.000000 |
| q20 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer and incorrectly stated that the context did not contain the information. | 53 | 0.000000 |
| q21 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer (48 replicas and the reason) and instead claimed the information was m... | 48 | 0.000000 |
| q22 | pass | n/a | pass | pass | pass | 4 | The response correctly states that offsets should not be reset, but it omits the specific consequence (SEV1) mentione... | 161 | 0.000000 |
| q23 | fail | fail | fail | pass | pass | 3 | The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediat... | 441 | 0.000000 |
| q24 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer (72 hours) and incorrectly stated that the context did not contain the... | 54 | 0.000000 |
| q25 | fail | fail | fail | pass | pass | 1 | The model response fails to identify the specific carriers (NorthSpan and Corvel Mobile) and instead provides unrelat... | 927 | 0.000000 |
| q26 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures all key details from the reference answer, including the threshold (3%), scope... | 436 | 0.000000 |
| q27 | fail | fail | fail | pass | pass | 1 | The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the referenc... | 172 | 0.000000 |
| q28 | fail | fail | fail | pass | pass | 1 | The response discusses storage architecture but fails to answer the specific question about data retention duration f... | 300 | 0.000000 |
| q29 | pass | pass | pass | pass | pass | 4 | The response correctly states the 35-day retention period but omits the detail about point-in-time recovery for the l... | 231 | 0.000000 |
| q30 | pass | pass | pass | pass | pass | 5 | The model response is identical to the reference answer and correctly identifies that only the General Counsel can pl... | 153 | 0.000000 |
| q31 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 8-hour limit but omits the additional requirement for a second approver mention... | 125 | 0.000000 |
| q32 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures all key points from the reference answer: the specific use case (SEV1 when JIT... | 447 | 0.000000 |
| q33 | pass | pass | pass | pass | fail | 5 | The model response correctly states the per diem amount as $85 per day, which fully matches the reference answer. | 159 | 0.000000 |
| q34 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer and incorrectly stated that the context did not contain the information. | 48 | 0.000000 |
| q35 | fail | fail | fail | pass | pass | 1 | The response describes a different holiday period (December/January) and does not mention Thaw Day or the first Frida... | 182 | 0.000000 |
| q36 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer, including the specific timeframe and system requirement. | 345 | 0.000000 |
| q37 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-minute SLA but omits the additional details about 24/7 coverage and the dedi... | 167 | 0.000000 |
| q38 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subseq... | 323 | 0.000000 |
| q39 | fail | fail | fail | pass | pass | 1 | The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference... | 238 | 0.000000 |
| q40 | fail | n/a | fail | pass | pass | 1 | The response identifies the likely cause (tagbroker) but fails to answer the specific questions about which on-call r... | 228 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 1 | The model response fails to answer the question about severity and instead provides irrelevant information about the ... | 174 | 0.000000 |
| q42 | fail | fail | fail | pass | pass | 1 | The response fails to answer the question about the retention period (400 days) and instead provides unrelated detail... | 401 | 0.000000 |
| q43 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 48 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 48 | 0.000000 |
| q45 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the provided context does not contain the answer and does not invent any infor... | 51 | 0.000000 |
| q46 | fail | n/a | fail | n/a | fail | 1 | The model invents a confident answer by describing the rotation structure instead of stating that the documents do no... | 300 | 0.000000 |
| q47 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the documents do not contain the answer and does not invent any information. | 54 | 0.000000 |
| q48 | fail | n/a | fail | n/a | fail | 1 | The model invents a specific, unverified claim about shipping dates and provides an irrelevant quote instead of stati... | 240 | 0.000000 |

## Failures

### q03 - judge

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    By default, Skerrow declares an excursion after 3 consecutive out-of-range readings.
    Quote: "By default, Skerrow declares an excursion after 3 consecutive out-of-range readings." [company-overview]

**Retrieved docs:** company-overview, architecture-overview

**Judge:** score 3 - The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 minutes) requested by the question, missing the key quantitative answer.

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** oncall-policy

**Judge:** score 1 - The model failed to provide the correct answer ($340) and instead claimed the information was missing.

### q06 - judge

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary.
    Quote: "If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary." [oncall-policy]

**Retrieved docs:** oncall-policy, runbook-tag-offline

**Judge:** score 3 - The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and the subsequent escalation to the engineering manager after 10 more minutes.

### q07 - judge

**Question:** What makes an incident a SEV1?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the answer contained in the reference, claiming the context was insufficient.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity, deploy-process

**Judge:** score 1 - The model failed to answer the question and contradicted the reference answer by claiming the context did not contain the answer.

### q16 - exact, judge, quote

**Question:** Which service checks readings against a shipment's temperature range?

**Response:**

    normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`.
    Quote: "normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean"." [architecture-overview]

**Retrieved docs:** architecture-overview, company-overview

**Judge:** score 1 - The model identifies the 'normalizer' service, which is incorrect; the reference answer states that 'excursion-engine' performs the check.

### q17 - judge

**Question:** What are the disaster recovery RPO and RTO?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** architecture-overview, data-retention

**Judge:** score 1 - The model failed to provide the specific RPO and RTO values stated in the reference answer.

### q20 - exact, judge

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity, runbook-ingest-backlog

**Judge:** score 1 - The model failed to provide the correct answer and incorrectly stated that the context did not contain the information.

### q21 - exact, judge

**Question:** What's the maximum number of normalizer replicas, and why is there a limit?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog, pto-and-leave

**Judge:** score 1 - The model failed to provide the correct answer (48 replicas and the reason) and instead claimed the information was missing.

### q23 - exact, judge

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    If one partition is far behind the others, the usual cause is a "chatty tag": a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval.
    Quote: "If one partition is far behind the others, the usual cause is a "chatty tag": a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval." [runbook-ingest-backlog]

**Retrieved docs:** runbook-ingest-backlog, runbook-tag-offline

**Judge:** score 3 - The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediation steps (quarantine command and notifying the Firmware team).

### q24 - exact, judge, retrieval

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** data-retention, architecture-overview

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

**Retrieved docs:** architecture-overview, runbook-tag-offline

**Judge:** score 1 - The model response fails to identify the specific carriers (NorthSpan and Corvel Mobile) and instead provides unrelated technical details about the data pipeline.

### q27 - exact, judge

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    Most spikes are cellular carrier outages, not problems on our side.
    Quote: "Most spikes are cellular carrier outages, not problems on our side." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

**Judge:** score 1 - The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the reference identifies it as a tagbroker issue requiring a page to Platform on-call.

### q28 - exact, judge

**Question:** How long are raw readings kept for customers on the Sovereign plan?

**Response:**

    - TimescaleDB holds recent readings ("hot" storage). Older readings are moved to Parquet files in object storage.
    - A Postgres database called `core` holds customers, shipments, users, alert rules and tag calibration data.
    Quote: "TimescaleDB holds recent readings ("hot" storage)." [architecture-overview]

**Retrieved docs:** architecture-overview, data-retention

**Judge:** score 1 - The response discusses storage architecture but fails to answer the specific question about data retention duration for the Sovereign plan.

### q34 - exact, judge, retrieval

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog, deploy-process

**Judge:** score 1 - The model failed to provide the correct answer and incorrectly stated that the context did not contain the information.

### q35 - exact, judge

**Question:** What is Thaw Day?

**Response:**

    The company also shuts down from December 24 through January 1.
    Quote: "The company also shuts down from December 24 through January 1." [pto-and-leave]

**Retrieved docs:** pto-and-leave, access-control

**Judge:** score 1 - The response describes a different holiday period (December/January) and does not mention Thaw Day or the first Friday of March.

### q38 - judge

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate.
    Quote: "When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate." [customer-support-escalation]

**Retrieved docs:** customer-support-escalation, access-control

**Judge:** score 3 - The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subsequent steps regarding the 12-month calibration cycle and the customer credit policy.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.
    Quote: "A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform." [deploy-process]

**Retrieved docs:** deploy-process, customer-support-escalation

**Judge:** score 1 - The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference states the incident commander can approve it alone.

### q40 - judge

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers.
    Quote: "If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline, incident-severity

**Judge:** score 1 - The response identifies the likely cause (tagbroker) but fails to answer the specific questions about which on-call rotation gets paged and what that rotation covers.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    Most spikes are cellular carrier outages, not problems on our side.
    Quote: "Most spikes are cellular carrier outages, not problems on our side." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

**Judge:** score 1 - The model response fails to answer the question about severity and instead provides irrelevant information about the cause of spikes.

### q42 - exact, judge

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    Using it automatically pages the Head of Security, every action taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.
    Quote: "Using it automatically pages the Head of Security, every action taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours." [access-control]

**Retrieved docs:** access-control, architecture-overview

**Judge:** score 1 - The response fails to answer the question about the retention period (400 days) and instead provides unrelated details about paging and reporting.

### q46 - judge, quote

**Question:** What's the weekly stipend for being on the incident commander rotation?

**Response:**

    Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly.
    Quote: "Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly." [incident-severity]

**Retrieved docs:** incident-severity, deploy-process

**Judge:** score 1 - The model invents a confident answer by describing the rotation structure instead of stating that the documents do not contain the stipend information.

### q48 - judge, quote

**Question:** How many Skerrow Tags did Tallowmoth ship in 2025?

**Response:**

    The first Skerrow Tags shipped to pilot customers in 2020.
    Quote: "Tallowmoth was founded in 2019 in Duluth, Minnesota, by Imogen Varga and Rafael Odum." [company-overview]

**Retrieved docs:** company-overview

**Judge:** score 1 - The model invents a specific, unverified claim about shipping dates and provides an irrelevant quote instead of stating that the documents do not contain the answer.
