# Eval run report

- Model: google/gemma-3-1b-it
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=4)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:36:50.483370+00:00 / 2026-10-23T19:37:31.269408+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 30/48 |
| Overall pass rate | 62.5% |
| Pass rate (exact) | 19/30 = 63.3% |
| Pass rate (judge) | 30/48 = 62.5% |
| Pass rate (retrieval) | 42/42 = 100.0% |
| Pass rate (quote) | 14/48 = 29.2% |
| Quote compliance (answered questions only) | 3/37 = 8.1% |
| Pass rate (tag: access) | 2/2 = 100.0% |
| Pass rate (tag: architecture) | 2/3 = 66.7% |
| Pass rate (tag: deploy) | 4/4 = 100.0% |
| Pass rate (tag: expenses) | 0/2 = 0.0% |
| Pass rate (tag: incident) | 1/4 = 25.0% |
| Pass rate (tag: multi-doc) | 1/4 = 25.0% |
| Pass rate (tag: near-miss) | 3/3 = 100.0% |
| Pass rate (tag: numeric) | 12/17 = 70.6% |
| Pass rate (tag: oncall) | 1/3 = 33.3% |
| Pass rate (tag: paraphrase) | 2/4 = 50.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 2/2 = 100.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 4/4 = 100.0% |
| Pass rate (tag: runbook) | 4/9 = 44.4% |
| Pass rate (tag: support) | 1/2 = 50.0% |
| Pass rate (tag: unanswerable) | 6/6 = 100.0% |
| Mean judge score | 3.54 |
| Hallucination rate (unanswerable, judge score <= 2) | 0/6 = 0.0% |
| Retrieval hit@4 | 100.0% |
| Retrieval recall@4 | 98.8% |
| Latency p50 | 159 ms |
| Latency p95 | 289 ms |
| Total tokens | 24709 (prompt 22733, completion 1976) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | fail | 5 | The model response accurately states the frequency (every 90 seconds) and the network type (LTE-M), fully matching th... | 216 | 0.000000 |
| q02 | pass | pass | pass | pass | fail | 5 | The model correctly states that the battery lasts about 14 months, which fully agrees with the reference answer. | 289 | 0.000000 |
| q03 | fail | n/a | fail | pass | fail | 2 | The response correctly identifies the 3-reading rule but fails to provide the requested time duration or the reasonin... | 120 | 0.000000 |
| q04 | pass | n/a | pass | pass | fail | 4 | The response correctly identifies the day and time but omits the detail about the 15-minute handoff call mentioned in... | 201 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and instead claimed the information was missing. | 42 | 0.000000 |
| q06 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies that the secondary is paged but omits the specific timeframes (5 minutes) and the s... | 196 | 0.000000 |
| q07 | fail | n/a | fail | pass | fail | 2 | The response only includes one of the four criteria for a SEV1 incident, omitting the other three important conditions. | 145 | 0.000000 |
| q08 | fail | fail | fail | pass | fail | 2 | The response omits the critical initial 20-minute update requirement and provides an irrelevant quote about notifying... | 113 | 0.000000 |
| q09 | pass | pass | pass | pass | fail | 5 | The model response accurately states the deadline for the postmortem draft (3 business days) and the review meeting (... | 264 | 0.000000 |
| q10 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the reference, claiming the context was insufficient instead of s... | 37 | 0.000000 |
| q11 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects the specific traffic percentages and durations outlined in the reference answer. | 149 | 0.000000 |
| q12 | pass | n/a | pass | pass | fail | 5 | The model response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified ... | 287 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies both required approvers as stated in the reference answer. | 194 | 0.000000 |
| q14 | pass | pass | pass | pass | fail | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 173 | 0.000000 |
| q15 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the number of partitions (96) but omits the detail about being keyed by tag ID. | 93 | 0.000000 |
| q16 | fail | fail | fail | pass | fail | 1 | The model identifies 'Normalizer' instead of 'excursion-engine' and describes unit conversion rather than checking ag... | 119 | 0.000000 |
| q17 | pass | n/a | pass | pass | fail | 5 | The response correctly identifies the RPO as 5 minutes, the RTO as 2 hours, and the location as ca-east, matching all... | 264 | 0.000000 |
| q18 | pass | pass | pass | pass | fail | 5 | The response correctly states the 30-day duration and the subsequent move to Parquet files in object storage, fully m... | 172 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects all conditions and thresholds specified in the reference answer. | 353 | 0.000000 |
| q20 | fail | fail | fail | pass | fail | 1 | The response provides a general definition of SEV2 but fails to mention the specific criteria (lag > 2,000,000 messag... | 202 | 0.000000 |
| q21 | pass | pass | pass | pass | fail | 5 | The response correctly identifies the maximum number of replicas as 48 and accurately explains the reason (database o... | 272 | 0.000000 |
| q22 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the reference, stating instead that the context did not contain it. | 47 | 0.000000 |
| q23 | fail | fail | fail | pass | fail | 1 | The model identifies the wrong root cause (tagbroker vs. chatty tag) and provides incorrect remediation steps that co... | 177 | 0.000000 |
| q24 | fail | fail | fail | pass | fail | 1 | The model states the tag holds 4 minutes of readings, which directly contradicts the reference answer of 72 hours. | 166 | 0.000000 |
| q25 | pass | pass | pass | pass | fail | 5 | The model correctly identifies both cellular carriers mentioned in the reference answer. | 156 | 0.000000 |
| q26 | pass | n/a | pass | pass | fail | 5 | The model response accurately captures all key details from the reference answer regarding the threshold (3%), scope ... | 242 | 0.000000 |
| q27 | fail | fail | fail | pass | fail | 1 | The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the referenc... | 243 | 0.000000 |
| q28 | pass | pass | pass | pass | pass | 5 | The model correctly identifies the retention period as 7 years, matching the reference answer. | 108 | 0.000000 |
| q29 | pass | pass | pass | pass | pass | 4 | The response correctly states the 35-day retention period but omits the detail about point-in-time recovery for the l... | 164 | 0.000000 |
| q30 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies that only the General Counsel can place or lift a legal hold, matching the re... | 126 | 0.000000 |
| q31 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the 8-hour limit but omits the additional requirement for a second approver mention... | 107 | 0.000000 |
| q32 | pass | n/a | pass | pass | fail | 5 | The model response accurately captures all key points from the reference answer: the specific use case (SEV1/JIT fail... | 336 | 0.000000 |
| q33 | fail | fail | fail | pass | fail | 1 | The response discusses a specific local exception for Duluth employees rather than providing the requested internatio... | 159 | 0.000000 |
| q34 | fail | fail | fail | pass | fail | 1 | The model incorrectly identifies the approver as a manager for an expense under $500, whereas the reference states a ... | 65 | 0.000000 |
| q35 | pass | pass | pass | pass | fail | 5 | The model correctly identifies Thaw Day as a company-wide holiday on the first Friday of March, matching the referenc... | 133 | 0.000000 |
| q36 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects the reference answer, including the specific timeframe and system requirement. | 265 | 0.000000 |
| q37 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the 30-minute SLA but omits the additional details about 24/7 coverage and the dedi... | 179 | 0.000000 |
| q38 | fail | n/a | fail | pass | fail | 3 | The response misses the specific actions of pulling raw readings and the calibration certificate, as well as the 12-m... | 167 | 0.000000 |
| q39 | fail | pass | fail | pass | fail | 1 | The model incorrectly identifies the approvers as the on-call engineering manager and Head of Platform, whereas the r... | 169 | 0.000000 |
| q40 | pass | n/a | pass | pass | fail | 5 | The model correctly identifies the Platform team and lists all the specific components covered by the rotation as sta... | 130 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct severity (SEV1) and incorrectly stated that the answer was not in the context. | 41 | 0.000000 |
| q42 | fail | fail | fail | pass | fail | 1 | The model fails to provide the specific retention period (400 days) requested in the question and instead provides un... | 278 | 0.000000 |
| q43 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the documents do not contain the answer and does not invent any information. | 49 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 41 | 0.000000 |
| q45 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 42 | 0.000000 |
| q46 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 39 | 0.000000 |
| q47 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the documents do not contain the answer and does not invent any information. | 44 | 0.000000 |
| q48 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 39 | 0.000000 |

## Failures

### q03 - judge, quote

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    An excursion is declared after 3 consecutive out-of-range readings. [doc-id]

**Retrieved docs:** company-overview, architecture-overview, incident-severity

**Judge:** score 2 - The response correctly identifies the 3-reading rule but fails to provide the requested time duration or the reasoning connecting readings to time, which is the core of the question.

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** oncall-policy, incident-severity, pto-and-leave

**Judge:** score 1 - The model failed to provide the correct answer ($340) and instead claimed the information was missing.

### q06 - judge, quote

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    If the primary doesn't acknowledge a SEV1 page, Klaxon pages the secondary.
    Quote: "If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary."

**Retrieved docs:** oncall-policy, runbook-tag-offline, incident-severity

**Judge:** score 3 - The response correctly identifies that the secondary is paged but omits the specific timeframes (5 minutes) and the subsequent escalation to the engineering manager (10 minutes later) mentioned in the reference answer.

### q07 - judge, quote

**Question:** What makes an incident a SEV1?

**Response:**

    An incident is a SEV1 if any of these is true:
    - Ingest or alert delivery is down for more than 10% of active tags.

**Retrieved docs:** incident-severity

**Judge:** score 2 - The response only includes one of the four criteria for a SEV1 incident, omitting the other three important conditions.

### q08 - exact, judge, quote

**Question:** How soon after declaring a SEV1 does the status page need an update?

**Response:**

    SEV1: every 30 minutes until it’s resolved.
    Quote: “Notify Customer Success immediately.” [doc-id]

**Retrieved docs:** incident-severity, runbook-tag-offline, oncall-policy

**Judge:** score 2 - The response omits the critical initial 20-minute update requirement and provides an irrelevant quote about notifying Customer Success.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** incident-severity, deploy-process, oncall-policy

**Judge:** score 1 - The model failed to provide the answer contained in the reference, claiming the context was insufficient instead of stating that the engineer cannot be the incident commander.

### q16 - exact, judge, quote

**Question:** Which service checks readings against a shipment's temperature range?

**Response:**

    Normalizer converts units, applies each tag's calibration offsets and writes the result to `readings.clean`. [readings.clean]

**Retrieved docs:** architecture-overview, company-overview, customer-support-escalation, access-control

**Judge:** score 1 - The model identifies 'Normalizer' instead of 'excursion-engine' and describes unit conversion rather than checking against temperature ranges.

### q20 - exact, judge, quote

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:
    Quote: "An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:"

**Retrieved docs:** incident-severity, runbook-ingest-backlog

**Judge:** score 1 - The response provides a general definition of SEV2 but fails to mention the specific criteria (lag > 2,000,000 messages or delay > 10 minutes) required to upgrade to SEV1.

### q22 - judge

**Question:** Can I reset the consumer offsets to clear an ingest backlog?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog, architecture-overview, incident-severity

**Judge:** score 1 - The model failed to provide the answer contained in the reference, stating instead that the context did not contain it.

### q23 - exact, judge, quote

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    The problem is likely tagbroker, as the other tags are dropping, and the platform is pageated.
    Quote: "If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers."

**Retrieved docs:** runbook-ingest-backlog, runbook-tag-offline, oncall-policy

**Judge:** score 1 - The model identifies the wrong root cause (tagbroker vs. chatty tag) and provides incorrect remediation steps that contradict the reference answer.

### q24 - exact, judge, quote

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    A tag can hold 4 minutes of readings while it has no connection.
    Quote: "An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:"

**Retrieved docs:** data-retention, architecture-overview, incident-severity, runbook-tag-offline

**Judge:** score 1 - The model states the tag holds 4 minutes of readings, which directly contradicts the reference answer of 72 hours.

### q27 - exact, judge, quote

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    Most spikes are cellular carrier outages, not problems on our side. Tags buffer up to 72 hours of readings locally and send them when they reconnect, so a carrier outage only loses data if it lasts longer than 72 hours.
    Quote: "Most spikes are cellular carrier outages, not problems on our side."

**Retrieved docs:** runbook-tag-offline, pto-and-leave

**Judge:** score 1 - The model response contradicts the reference answer by attributing the issue to carrier outages, whereas the reference identifies it as a tagbroker issue requiring a page to the Platform on-call.

### q33 - exact, judge, quote

**Question:** What's the per diem for international travel?

**Response:**

    Employees who live in Duluth don't get a per diem when working at the Duluth office.
    Quote: "Employees who live in Duluth don't get a per diem when working at the Duluth office."

**Retrieved docs:** expense-and-travel, company-overview

**Judge:** score 1 - The response discusses a specific local exception for Duluth employees rather than providing the requested international travel per diem amount.

### q34 - exact, judge, quote

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    Under $500: your manager [expense-and-travel]

**Retrieved docs:** runbook-ingest-backlog, deploy-process, expense-and-travel

**Judge:** score 1 - The model incorrectly identifies the approver as a manager for an expense under $500, whereas the reference states a director is required for the $500-$5,000 range.

### q38 - judge, quote

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    Support engineers investigate data, tag and alert problems when a customer says an excursion alert was a false alarm.
    Quote: “If the tag was past its calibration date when the excursion fired, the customer gets a credit.”

**Retrieved docs:** customer-support-escalation, access-control, architecture-overview

**Judge:** score 3 - The response misses the specific actions of pulling raw readings and the calibration certificate, as well as the 12-month recalibration interval, though it correctly identifies the credit outcome.

### q39 - judge, quote

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    The on-call engineering manager and the Head of Platform can approve a hotfix.
    Quote: “During a declared SEV1, the incident commander can approve a hotfix on their own.” [doc-id]

**Retrieved docs:** deploy-process, customer-support-escalation, access-control, runbook-ingest-backlog

**Judge:** score 1 - The model incorrectly identifies the approvers as the on-call engineering manager and Head of Platform, whereas the reference states the incident commander can approve it.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-tag-offline, incident-severity

**Judge:** score 1 - The model failed to provide the correct severity (SEV1) and incorrectly stated that the answer was not in the context.

### q42 - exact, judge, quote

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    The record of actions taken with the break-glass account is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.
    Quote: “The record of actions taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.”

**Retrieved docs:** access-control, architecture-overview, oncall-policy, data-retention

**Judge:** score 1 - The model fails to provide the specific retention period (400 days) requested in the question and instead provides unrelated information about filing a report.
