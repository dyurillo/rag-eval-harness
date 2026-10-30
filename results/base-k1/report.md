# Eval run report

- Model: google/gemma-3-1b-it
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=1)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:35:27.398361+00:00 / 2026-10-23T19:36:08.485579+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 25/48 |
| Overall pass rate | 52.1% |
| Pass rate (exact) | 17/30 = 56.7% |
| Pass rate (judge) | 25/48 = 52.1% |
| Pass rate (retrieval) | 36/42 = 85.7% |
| Pass rate (quote) | 20/48 = 41.7% |
| Quote compliance (answered questions only) | 9/34 = 26.5% |
| Pass rate (tag: access) | 2/2 = 100.0% |
| Pass rate (tag: architecture) | 3/3 = 100.0% |
| Pass rate (tag: deploy) | 3/4 = 75.0% |
| Pass rate (tag: expenses) | 0/2 = 0.0% |
| Pass rate (tag: incident) | 2/4 = 50.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 2/3 = 66.7% |
| Pass rate (tag: numeric) | 10/17 = 58.8% |
| Pass rate (tag: oncall) | 1/3 = 33.3% |
| Pass rate (tag: paraphrase) | 1/4 = 25.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 1/2 = 50.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 2/4 = 50.0% |
| Pass rate (tag: runbook) | 3/9 = 33.3% |
| Pass rate (tag: support) | 1/2 = 50.0% |
| Pass rate (tag: unanswerable) | 5/6 = 83.3% |
| Mean judge score | 3.21 |
| Hallucination rate (unanswerable, judge score <= 2) | 1/6 = 16.7% |
| Retrieval hit@1 | 85.7% |
| Retrieval recall@1 | 81.0% |
| Latency p50 | 136 ms |
| Latency p95 | 262 ms |
| Total tokens | 14125 (prompt 12268, completion 1857) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | fail | 5 | The model response correctly states the frequency (every 90 seconds) and the network (LTE-M), fully matching the refe... | 198 | 0.000000 |
| q02 | pass | pass | pass | pass | fail | 5 | The model correctly states the battery life is about 14 months, matching the reference answer. | 169 | 0.000000 |
| q03 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 ... | 203 | 0.000000 |
| q04 | pass | n/a | pass | pass | fail | 4 | The response correctly identifies the day and time of the handoff but omits the specific detail about the 15-minute h... | 133 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and incorrectly stated that the information was not available. | 36 | 0.000000 |
| q06 | fail | n/a | fail | pass | fail | 2 | The response incorrectly states that the engineering manager is paged directly, omitting the secondary on-call step a... | 186 | 0.000000 |
| q07 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the answer contained in the reference, claiming the context was insufficient. | 35 | 0.000000 |
| q08 | pass | pass | pass | pass | fail | 5 | The model response accurately states the 20-minute initial update and 30-minute subsequent updates, matching the refe... | 234 | 0.000000 |
| q09 | pass | pass | pass | pass | fail | 4 | The response correctly states the 3 business day deadline for the draft but omits the additional detail about the rev... | 114 | 0.000000 |
| q10 | fail | n/a | fail | pass | pass | 2 | The model correctly answers 'No' but fails to provide the specific reasoning required by the reference answer (that t... | 89 | 0.000000 |
| q11 | fail | fail | fail | pass | fail | 1 | The response describes how to start a deploy but fails to provide the specific traffic progression percentages and du... | 153 | 0.000000 |
| q12 | pass | n/a | pass | pass | fail | 5 | The response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified in the... | 155 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies both required approvers as stated in the reference answer. | 185 | 0.000000 |
| q14 | pass | pass | pass | pass | fail | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 177 | 0.000000 |
| q15 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the number of partitions (96) but omits the detail about the keying strategy (keyed... | 123 | 0.000000 |
| q16 | pass | pass | pass | pass | fail | 4 | The model correctly identifies the service name but omits the specific details about reading from 'readings.clean' an... | 43 | 0.000000 |
| q17 | pass | n/a | pass | pass | pass | 4 | The response correctly identifies the RPO and RTO values but omits the location of the disaster-recovery replica ment... | 122 | 0.000000 |
| q18 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-day duration but omits the specific detail about moving to Parquet files in ... | 129 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately reflects all conditions and thresholds specified in the reference answer. | 338 | 0.000000 |
| q20 | fail | fail | fail | fail | pass | 1 | The model failed to provide the specific criteria found in the reference answer, claiming the information was missing. | 42 | 0.000000 |
| q21 | pass | pass | pass | pass | fail | 5 | The response correctly identifies the maximum number of replicas as 48 and accurately explains the reason for the lim... | 262 | 0.000000 |
| q22 | pass | n/a | pass | pass | pass | 4 | The response correctly answers 'No' and cites the relevant policy against resetting offsets, but it omits the specifi... | 94 | 0.000000 |
| q23 | fail | fail | fail | pass | fail | 3 | The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediat... | 223 | 0.000000 |
| q24 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer (72 hours) and instead claimed the information was not in the context. | 45 | 0.000000 |
| q25 | fail | fail | fail | fail | pass | 2 | The response mentions the existence of two carriers but fails to name them, which is the core information requested b... | 158 | 0.000000 |
| q26 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the condition for the alert but omits the specific time duration ('about 6 minutes'... | 244 | 0.000000 |
| q27 | fail | pass | fail | pass | fail | 2 | The model explicitly states that the context does not contain the answer, which contradicts the reference answer that... | 152 | 0.000000 |
| q28 | fail | fail | fail | fail | fail | 1 | The response fails to provide the specific duration (7 years) requested and instead offers a generic statement about ... | 132 | 0.000000 |
| q29 | fail | pass | fail | pass | pass | 3 | The response correctly states the 35-day retention period but omits the important detail about point-in-time recovery... | 144 | 0.000000 |
| q30 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the General Counsel as the person who can place or lift a legal hold, but it omits ... | 81 | 0.000000 |
| q31 | pass | pass | pass | pass | fail | 4 | The response correctly identifies the 8-hour limit but omits the additional requirement for a second approver mention... | 102 | 0.000000 |
| q32 | pass | n/a | pass | pass | fail | 4 | The response correctly identifies the three main consequences (paging, logging, reporting) but omits the specific usa... | 293 | 0.000000 |
| q33 | fail | fail | fail | pass | fail | 1 | The response discusses a specific local exception for Duluth employees and fails to provide the requested internation... | 148 | 0.000000 |
| q34 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer and incorrectly stated that the context did not contain the information. | 38 | 0.000000 |
| q35 | pass | pass | pass | pass | fail | 5 | The model correctly identifies Thaw Day as a company-wide holiday on the first Friday of March, matching the referenc... | 125 | 0.000000 |
| q36 | fail | fail | fail | fail | pass | 1 | The response provides a vague reference to a policy instead of the specific actions (arranging a swap and recording i... | 89 | 0.000000 |
| q37 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-minute SLA but omits the additional details about 24/7 coverage and the dedi... | 150 | 0.000000 |
| q38 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subseq... | 183 | 0.000000 |
| q39 | fail | fail | fail | pass | pass | 1 | The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference... | 169 | 0.000000 |
| q40 | fail | n/a | fail | pass | fail | 3 | The response correctly identifies the Platform team as the on-call rotation but omits the specific components covered... | 202 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 2 | The response provides the correct threshold (72 hours) but fails to state the required severity (SEV1), which is the ... | 103 | 0.000000 |
| q42 | fail | fail | fail | pass | fail | 1 | The response fails to provide the specific retention period (400 days) requested in the question and instead provides... | 223 | 0.000000 |
| q43 | pass | n/a | pass | n/a | fail | 5 | The response correctly identifies that the documents do not contain the answer and does not invent any information. | 136 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 36 | 0.000000 |
| q45 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 39 | 0.000000 |
| q46 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 36 | 0.000000 |
| q47 | fail | n/a | fail | n/a | fail | 1 | The model invents a confident answer by quoting specific technical details (reporting interval, temperature range) th... | 188 | 0.000000 |
| q48 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 36 | 0.000000 |

## Failures

### q03 - judge, quote

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    Skerrow declares an excursion after 3 consecutive out-of-range readings.
    Quote: “By default, Skerrow declares an excursion after 3 consecutive out-of-range readings.” [doc-id]

**Retrieved docs:** company-overview

**Judge:** score 3 - The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 minutes) requested by the question, missing the key quantitative answer.

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** oncall-policy

**Judge:** score 1 - The model failed to provide the correct answer ($340) and incorrectly stated that the information was not available.

### q06 - judge, quote

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    If the primary doesn't acknowledge a SEV1 page, Klaxon pages the team's engineering manager.
    Quote: "If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary."

**Retrieved docs:** oncall-policy

**Judge:** score 2 - The response incorrectly states that the engineering manager is paged directly, omitting the secondary on-call step and the specific time intervals defined in the reference.

### q07 - judge

**Question:** What makes an incident a SEV1?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the answer contained in the reference, claiming the context was insufficient.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    No, the provided context does not contain the answer.
    Quote: “The IC coordinates the response and handles communication.”

**Retrieved docs:** incident-severity

**Judge:** score 2 - The model correctly answers 'No' but fails to provide the specific reasoning required by the reference answer (that the IC comes from a rotation and cannot be the debugger), instead claiming the context is insufficient.

### q11 - exact, judge, quote

**Question:** How does a production canary progress?

**Response:**

    Production deploys are started with `skr deploy <service>` and always go through a canary.
    Quote: "<Production deploys are started with `skr deploy <service>` and always go through a canary>"

**Retrieved docs:** deploy-process

**Judge:** score 1 - The response describes how to start a deploy but fails to provide the specific traffic progression percentages and durations required by the reference answer.

### q20 - exact, judge, retrieval

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    The context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the specific criteria found in the reference answer, claiming the information was missing.

### q23 - exact, judge, quote

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    One partition is far behind the others, likely due to a “chatty tag”.
    Quote: “If one partition is far behind the others, the usual cause is a “chatty tag”: a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval.”

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 3 - The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediation steps (quarantine command and notifying the Firmware team).

### q24 - exact, judge, retrieval

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** data-retention

**Judge:** score 1 - The model failed to provide the correct answer (72 hours) and instead claimed the information was not in the context.

### q25 - exact, judge, retrieval

**Question:** Which cellular carriers do Skerrow Tags use?

**Response:**

    Skerrow Tags send readings over LTE-M through one of two cellular carriers.
    Quote: “Skerrow Tags send readings over LTE-M through one of two cellular carriers.” [architecture-overview]

**Retrieved docs:** architecture-overview

**Judge:** score 2 - The response mentions the existence of two carriers but fails to name them, which is the core information requested by the question.

### q26 - judge, quote

**Question:** When does the TagsOfflineSpike alert fire?

**Response:**

    The Alerts fires when more than 3% of active tags in a single carrier region miss 4 consecutive check-ins. [runbook-tag-offline]
    Quote: "If the context contains the answer, reply with the answer in one or two sentences, then on the next line a supporting quote in exactly this form: <sentence>"

**Retrieved docs:** runbook-tag-offline

**Judge:** score 3 - The response correctly identifies the condition for the alert but omits the specific time duration ('about 6 minutes') mentioned in the reference answer.

### q27 - judge, quote

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    The provided context does not contain the answer.
    Quote: "If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

**Judge:** score 2 - The model explicitly states that the context does not contain the answer, which contradicts the reference answer that provides a specific cause and action.

### q28 - exact, judge, retrieval, quote

**Question:** How long are raw readings kept for customers on the Sovereign plan?

**Response:**

    The Data Retention Policy says how long each kind of data is kept.
    Quote: “The Data Retention Policy says how long each kind of data is kept.” [doc-id]

**Retrieved docs:** architecture-overview

**Judge:** score 1 - The response fails to provide the specific duration (7 years) requested and instead offers a generic statement about the policy's existence.

### q29 - judge

**Question:** How long are backups of the core database kept?

**Response:**

    Backups are kept for 35 days.
    Quote: “The `core` Postgres database is backed up nightly, and backups are kept for 35 days.” [data-retention]

**Retrieved docs:** data-retention

**Judge:** score 3 - The response correctly states the 35-day retention period but omits the important detail about point-in-time recovery for the last 7 days.

### q33 - exact, judge, quote

**Question:** What's the per diem for international travel?

**Response:**

    Employees who live in Duluth don’t get a per diem when working at the Duluth office.
    Quote: “Employees who live in Duluth don’t get a per diem when working at the Duluth office.”

**Retrieved docs:** expense-and-travel

**Judge:** score 1 - The response discusses a specific local exception for Duluth employees and fails to provide the requested international travel per diem amount.

### q34 - exact, judge, retrieval

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 1 - The model failed to provide the correct answer and incorrectly stated that the context did not contain the information.

### q36 - exact, judge, retrieval

**Question:** I'm scheduled for on-call during my vacation. What do I need to do?

**Response:**

    Quote: “The Time Off and Leave policy sets how much notice you need to give.” [oncall-policy]

**Retrieved docs:** oncall-policy

**Judge:** score 1 - The response provides a vague reference to a policy instead of the specific actions (arranging a swap and recording it in Klaxon) required by the reference answer.

### q38 - judge, quote

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    Tier 2 pulls the shipment’s raw readings and the tag’s calibration certificate.
    Quote: "When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment’s raw readings and the tag’s calibration certificate."

**Retrieved docs:** customer-support-escalation

**Judge:** score 3 - The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subsequent steps regarding the 12-month calibration cycle and the customer credit policy.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    The on-call engineering manager and the Head of Platform can approve a hotfix.
    Quote: “A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.” [deploy-process]

**Retrieved docs:** deploy-process

**Judge:** score 1 - The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference states the incident commander can approve it alone.

### q40 - judge, quote

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    The Platform is paged on-call when tags on both carriers drop offline.
    Quote: "[runbook-tag-offline] 3. If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers. Page the Platform on-call."

**Retrieved docs:** runbook-tag-offline

**Judge:** score 3 - The response correctly identifies the Platform team as the on-call rotation but omits the specific components covered (tagbroker, Kafka, databases, deploy pipeline) which are explicitly requested in the question.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    Quote: “A carrier outage only loses data if it lasts longer than 72 hours.” [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

**Judge:** score 2 - The response provides the correct threshold (72 hours) but fails to state the required severity (SEV1), which is the direct answer to the question.

### q42 - exact, judge, quote

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    The record of actions taken with the break-glass account is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.
    Quote: “The person who used it must file a break-glass report within 24 hours.” [doc-id]

**Retrieved docs:** access-control

**Judge:** score 1 - The response fails to provide the specific retention period (400 days) requested in the question and instead provides irrelevant information about reporting deadlines.

### q47 - judge, quote

**Question:** What's the procedure for replacing the battery in a Skerrow Tag?

**Response:**

    Quote: “The Skerrow Tag v3 reports a reading every 90 seconds over LTE-M, works from -40 °C to +70 °C, and its battery lasts about 14 months.” [doc-id]

**Retrieved docs:** company-overview

**Judge:** score 1 - The model invents a confident answer by quoting specific technical details (reporting interval, temperature range) that are not in the provided documents and do not answer the question about battery replacement.
