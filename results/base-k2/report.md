# Eval run report

- Model: google/gemma-3-1b-it
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=2)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:36:08.928713+00:00 / 2026-10-23T19:36:50.042103+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 28/48 |
| Overall pass rate | 58.3% |
| Pass rate (exact) | 19/30 = 63.3% |
| Pass rate (judge) | 28/48 = 58.3% |
| Pass rate (retrieval) | 40/42 = 95.2% |
| Pass rate (quote) | 17/48 = 35.4% |
| Quote compliance (answered questions only) | 6/36 = 16.7% |
| Pass rate (tag: access) | 1/2 = 50.0% |
| Pass rate (tag: architecture) | 2/3 = 66.7% |
| Pass rate (tag: deploy) | 4/4 = 100.0% |
| Pass rate (tag: expenses) | 1/2 = 50.0% |
| Pass rate (tag: incident) | 3/4 = 75.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 2/3 = 66.7% |
| Pass rate (tag: numeric) | 13/17 = 76.5% |
| Pass rate (tag: oncall) | 1/3 = 33.3% |
| Pass rate (tag: paraphrase) | 2/4 = 50.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 2/2 = 100.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 3/4 = 75.0% |
| Pass rate (tag: runbook) | 3/9 = 33.3% |
| Pass rate (tag: support) | 1/2 = 50.0% |
| Pass rate (tag: unanswerable) | 5/6 = 83.3% |
| Mean judge score | 3.44 |
| Hallucination rate (unanswerable, judge score <= 2) | 1/6 = 16.7% |
| Retrieval hit@2 | 95.2% |
| Retrieval recall@2 | 90.5% |
| Latency p50 | 166 ms |
| Latency p95 | 342 ms |
| Total tokens | 17992 (prompt 15835, completion 2157) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | fail | 5 | The model response correctly states the frequency (every 90 seconds) and the network (LTE-M), fully matching the refe... | 215 | 0.000000 |
| q02 | pass | pass | pass | pass | fail | 5 | The model correctly states the battery life is about 14 months, matching the reference answer. | 181 | 0.000000 |
| q03 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 ... | 211 | 0.000000 |
| q04 | pass | n/a | pass | pass | fail | 4 | The response correctly identifies the day and time but omits the detail about the 15-minute handoff call mentioned in... | 198 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and incorrectly stated that the context did not contain the ans... | 37 | 0.000000 |
| q06 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies that the secondary is paged but omits the specific 5-minute timeframe and the subse... | 139 | 0.000000 |
| q07 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the context, contradicting the reference answer. | 44 | 0.000000 |
| q08 | pass | pass | pass | pass | fail | 5 | The model response accurately states the 20-minute initial update and 30-minute subsequent updates, matching the refe... | 244 | 0.000000 |
| q09 | pass | pass | pass | pass | fail | 5 | The model response accurately states the deadline for the postmortem draft (3 business days) and the review meeting (... | 255 | 0.000000 |
| q10 | pass | n/a | pass | pass | fail | 4 | The response correctly answers 'No' and cites the relevant rule, but it incorrectly claims the context does not conta... | 126 | 0.000000 |
| q11 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects the reference answer's details regarding traffic percentages and durations. | 289 | 0.000000 |
| q12 | pass | n/a | pass | pass | fail | 5 | The model response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified ... | 280 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model correctly identifies both required approvers as stated in the reference answer. | 188 | 0.000000 |
| q14 | pass | pass | pass | pass | fail | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 180 | 0.000000 |
| q15 | pass | pass | pass | pass | fail | 5 | The model correctly identifies the number of partitions (96) and includes the keying detail (tag ID) from the referen... | 145 | 0.000000 |
| q16 | fail | fail | fail | pass | fail | 1 | The model response identifies 'Normalizer' instead of the correct service 'excursion-engine'. | 38 | 0.000000 |
| q17 | pass | n/a | pass | pass | fail | 5 | The response correctly identifies the RPO as 5 minutes, the RTO as 2 hours, and the location as ca-east, matching all... | 253 | 0.000000 |
| q18 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-day duration but omits the specific detail about moving to Parquet files in ... | 131 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects all conditions and thresholds specified in the reference answer. | 342 | 0.000000 |
| q20 | fail | fail | fail | pass | pass | 1 | The model failed to provide the specific criteria found in the reference answer, claiming the information was missing. | 36 | 0.000000 |
| q21 | pass | pass | pass | pass | fail | 5 | The response correctly identifies the maximum number of replicas as 48 and accurately explains the reason for the lim... | 199 | 0.000000 |
| q22 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the reference, stating instead that the context did not contain it. | 39 | 0.000000 |
| q23 | fail | fail | fail | pass | fail | 3 | The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediat... | 225 | 0.000000 |
| q24 | fail | fail | fail | fail | pass | 1 | The response discusses database storage architecture (TimescaleDB/Parquet) instead of answering the specific question... | 130 | 0.000000 |
| q25 | fail | fail | fail | pass | fail | 1 | The response fails to name the specific carriers (NorthSpan and Corvel Mobile) required by the reference answer. | 146 | 0.000000 |
| q26 | pass | n/a | pass | pass | fail | 4 | The response correctly identifies the condition for the alert but omits the approximate time duration ('about 6 minut... | 425 | 0.000000 |
| q27 | fail | fail | fail | pass | fail | 1 | The model response contradicts the reference answer by attributing the issue to carrier outages and data buffering, w... | 241 | 0.000000 |
| q28 | pass | pass | pass | pass | fail | 5 | The model correctly states that raw readings are kept for 7 years, which matches the reference answer exactly. | 143 | 0.000000 |
| q29 | fail | pass | fail | pass | pass | 3 | The response correctly states the 35-day retention period but omits the important detail about point-in-time recovery... | 100 | 0.000000 |
| q30 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the General Counsel as the person who can place or lift a legal hold, but it omits ... | 75 | 0.000000 |
| q31 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the 8-hour limit but omits the additional requirement for a second approver mention... | 100 | 0.000000 |
| q32 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the 24-hour report requirement and the SEV1 context, but it omits the automatic pag... | 224 | 0.000000 |
| q33 | pass | pass | pass | pass | fail | 5 | The model response explicitly states the per diem for international travel is $85 per day, which matches the referenc... | 202 | 0.000000 |
| q34 | fail | fail | fail | fail | pass | 1 | The model response discusses approval for a hotfix during a freeze, which is unrelated to the question about approvin... | 127 | 0.000000 |
| q35 | pass | pass | pass | pass | fail | 5 | The model correctly identifies Thaw Day as a company-wide holiday on the first Friday of March, matching the referenc... | 126 | 0.000000 |
| q36 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects the reference answer, including the specific timeframe and system requirement. | 218 | 0.000000 |
| q37 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the 30-minute SLA but omits the additional details about 24/7 coverage and the dedi... | 166 | 0.000000 |
| q38 | fail | n/a | fail | pass | fail | 1 | The response discusses data access permissions rather than the specific procedure for handling false alarms (checking... | 184 | 0.000000 |
| q39 | fail | fail | fail | pass | pass | 1 | The model incorrectly identifies the approvers as the on-call engineering manager and Head of Platform, whereas the r... | 182 | 0.000000 |
| q40 | fail | n/a | fail | pass | fail | 1 | The model identifies the wrong on-call rotation (IC rotation instead of Platform infrastructure) and fails to mention... | 273 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 2 | The response provides the correct threshold for data loss but fails to state the required severity level (SEV1), whic... | 100 | 0.000000 |
| q42 | fail | fail | fail | pass | fail | 2 | The response fails to answer the specific question about the retention period (400 days) and instead provides unrelat... | 284 | 0.000000 |
| q43 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 35 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 36 | 0.000000 |
| q45 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 41 | 0.000000 |
| q46 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 36 | 0.000000 |
| q47 | fail | n/a | fail | n/a | pass | 1 | The response invents a confident answer by providing specific technical details and a quote that are not in the docum... | 389 | 0.000000 |
| q48 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 43 | 0.000000 |

## Failures

### q03 - judge, quote

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    Skerrow declares an excursion after 3 consecutive out-of-range readings.
    Quote: “By default, Skerrow declares an excursion after 3 consecutive out-of-range readings.” [doc-id]

**Retrieved docs:** company-overview, architecture-overview

**Judge:** score 3 - The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 minutes) requested by the question, missing the key quantitative answer.

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** oncall-policy

**Judge:** score 1 - The model failed to provide the correct answer ($340) and incorrectly stated that the context did not contain the answer.

### q06 - judge, quote

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    Klaxon pages the secondary.
    Quote: “If the primary doesn’t acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary.”

**Retrieved docs:** oncall-policy, runbook-tag-offline

**Judge:** score 3 - The response correctly identifies that the secondary is paged but omits the specific 5-minute timeframe and the subsequent escalation to the engineering manager after 10 more minutes.

### q07 - judge

**Question:** What makes an incident a SEV1?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the answer contained in the context, contradicting the reference answer.

### q16 - exact, judge, quote

**Question:** Which service checks readings against a shipment's temperature range?

**Response:**

    Normalizer [doc-id]

**Retrieved docs:** architecture-overview, company-overview

**Judge:** score 1 - The model response identifies 'Normalizer' instead of the correct service 'excursion-engine'.

### q20 - exact, judge

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** incident-severity, runbook-ingest-backlog

**Judge:** score 1 - The model failed to provide the specific criteria found in the reference answer, claiming the information was missing.

### q22 - judge

**Question:** Can I reset the consumer offsets to clear an ingest backlog?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 1 - The model failed to provide the answer contained in the reference, stating instead that the context did not contain it.

### q23 - exact, judge, quote

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    The “chatty tag” on firmware 3.2.x is likely the cause, as it sends a reading every second instead of at the normal interval.
    Quote: “a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval.”

**Retrieved docs:** runbook-ingest-backlog, runbook-tag-offline

**Judge:** score 3 - The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediation steps (quarantine command and notifying the Firmware team).

### q24 - exact, judge, retrieval

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    Quote: “TimescaleDB holds recent readings ("hot" storage). Older readings are moved to Parquet files in object storage.” [data-retention]

**Retrieved docs:** data-retention, architecture-overview

**Judge:** score 1 - The response discusses database storage architecture (TimescaleDB/Parquet) instead of answering the specific question about tag buffer capacity during disconnection.

### q25 - exact, judge, quote

**Question:** Which cellular carriers do Skerrow Tags use?

**Response:**

    Skerrow Tags send readings over LTE-M through one of two cellular carriers.
    Quote: "Skerrow Tags send readings over LTE-M through one of two cellular carriers."

**Retrieved docs:** architecture-overview, runbook-tag-offline

**Judge:** score 1 - The response fails to name the specific carriers (NorthSpan and Corvel Mobile) required by the reference answer.

### q27 - exact, judge, quote

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    Tags on both carriers are going offline at the same time because tags buffer up to 72 hours of readings locally and send them when they reconnect, so a carrier outage only loses data if it lasts longer than 72 hours.
    Quote: "Most spikes are cellular carrier outages, not problems on our side."

**Retrieved docs:** runbook-tag-offline

**Judge:** score 1 - The model response contradicts the reference answer by attributing the issue to carrier outages and data buffering, whereas the reference identifies the cause as a tagbroker issue requiring a page to the Platform on-call.

### q29 - judge

**Question:** How long are backups of the core database kept?

**Response:**

    The backups of the core database are kept for 35 days.
    Quote: “The provided context does not contain the answer.”

**Retrieved docs:** data-retention, architecture-overview

**Judge:** score 3 - The response correctly states the 35-day retention period but omits the important detail about point-in-time recovery for the last 7 days.

### q32 - judge, quote

**Question:** What happens when someone uses the break-glass account?

**Response:**

    When someone uses the break-glass account, its credentials are kept in a sealed vault entry, and the person who used it must file a break-glass report within 24 hours.
    Quote: "The `breakglass` account is for SEV1 incidents when JIT access isn't working."

**Retrieved docs:** access-control

**Judge:** score 3 - The response correctly identifies the 24-hour report requirement and the SEV1 context, but it omits the automatic paging of the Head of Security and the recording of actions in the audit log, which are key parts of the reference answer.

### q34 - exact, judge, retrieval

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    Quote: “A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.” [runbook-ingest-backlog]

**Retrieved docs:** runbook-ingest-backlog, deploy-process

**Judge:** score 1 - The model response discusses approval for a hotfix during a freeze, which is unrelated to the question about approving a $2,000 expense.

### q38 - judge, quote

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    Support engineers can view a customer’s shipment data only when an open support ticket references it.
    Quote: "Support engineers can view a customer’s shipment data only when an open support ticket references it." [customer-support-escalation]

**Retrieved docs:** customer-support-escalation, access-control

**Judge:** score 1 - The response discusses data access permissions rather than the specific procedure for handling false alarms (checking calibration and issuing credits) described in the reference.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    The on-call engineering manager and the Head of Platform can approve a hotfix.
    Quote: “A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.” [deploy-process]

**Retrieved docs:** deploy-process, customer-support-escalation

**Judge:** score 1 - The model incorrectly identifies the approvers as the on-call engineering manager and Head of Platform, whereas the reference states the incident commander can approve it alone.

### q40 - judge, quote

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    The on-call rotation that gets paged is the one staffed by senior engineers and engineering managers, which changes weekly.
    Quote: “Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly. The IC coordinates the response and handles communication. The IC must not be the person debugging.”

**Retrieved docs:** runbook-tag-offline, incident-severity

**Judge:** score 1 - The model identifies the wrong on-call rotation (IC rotation instead of Platform infrastructure) and fails to mention the specific services covered.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    Quote: “a carrier outage only loses data if it lasts longer than 72 hours.” [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

**Judge:** score 2 - The response provides the correct threshold for data loss but fails to state the required severity level (SEV1), which is the direct answer to the question.

### q42 - exact, judge, quote

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    The record of actions taken with the break-glass account is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.
    Quote: “The record of actions taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.” [doc-id]

**Retrieved docs:** access-control, architecture-overview

**Judge:** score 2 - The response fails to answer the specific question about the retention period (400 days) and instead provides unrelated information about filing a report within 24 hours.

### q47 - judge

**Question:** What's the procedure for replacing the battery in a Skerrow Tag?

**Response:**

    The current hardware is Tag v3, which reports a reading every 90 seconds over LTE-M, works from -40 °C to +70 °C, and its battery lasts about 14 months.
    Quote: "The Skerrow Tag is a battery-powered sensor that records temperature and humidity. It reports a reading every 90 seconds over LTE-M, works from -40 °C to +70 °C, and its battery lasts about 14 months."

**Retrieved docs:** company-overview

**Judge:** score 1 - The response invents a confident answer by providing specific technical details and a quote that are not in the documents, failing to state that the procedure is not described.
