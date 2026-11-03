# Eval run report

- Model: rag-lora-1b
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: on (k=1)
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:38:10.489163+00:00 / 2026-10-23T19:38:52.639197+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 26/48 |
| Overall pass rate | 54.2% |
| Pass rate (exact) | 16/30 = 53.3% |
| Pass rate (judge) | 26/48 = 54.2% |
| Pass rate (retrieval) | 36/42 = 85.7% |
| Pass rate (quote) | 44/48 = 91.7% |
| Quote compliance (answered questions only) | 32/35 = 91.4% |
| Pass rate (tag: access) | 2/2 = 100.0% |
| Pass rate (tag: architecture) | 3/3 = 100.0% |
| Pass rate (tag: deploy) | 3/4 = 75.0% |
| Pass rate (tag: expenses) | 1/2 = 50.0% |
| Pass rate (tag: incident) | 2/4 = 50.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 2/3 = 66.7% |
| Pass rate (tag: numeric) | 11/17 = 64.7% |
| Pass rate (tag: oncall) | 1/3 = 33.3% |
| Pass rate (tag: paraphrase) | 1/4 = 25.0% |
| Pass rate (tag: product) | 2/3 = 66.7% |
| Pass rate (tag: pto) | 0/2 = 0.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 3/4 = 75.0% |
| Pass rate (tag: runbook) | 3/9 = 33.3% |
| Pass rate (tag: support) | 1/2 = 50.0% |
| Pass rate (tag: unanswerable) | 5/6 = 83.3% |
| Mean judge score | 3.23 |
| Hallucination rate (unanswerable, judge score <= 2) | 1/6 = 16.7% |
| Retrieval hit@1 | 85.7% |
| Retrieval recall@1 | 81.0% |
| Latency p50 | 216 ms |
| Latency p95 | 429 ms |
| Total tokens | 14559 (prompt 12268, completion 2291) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | pass | pass | pass | pass | fail | 5 | The model correctly states that the Skerrow Tag reports a reading every 90 seconds over LTE-M, which fully matches th... | 430 | 0.000000 |
| q02 | pass | pass | pass | pass | pass | 5 | The model correctly states that the battery lasts about 14 months, which matches the reference answer exactly. | 313 | 0.000000 |
| q03 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the 3 consecutive readings rule but fails to calculate the actual time duration (3 ... | 258 | 0.000000 |
| q04 | pass | n/a | pass | pass | pass | 4 | The response correctly identifies the day and time of the handoff but omits the specific detail about the 15-minute h... | 259 | 0.000000 |
| q05 | fail | fail | fail | pass | pass | 1 | The model failed to provide the correct answer ($340) and instead claimed the information was missing. | 49 | 0.000000 |
| q06 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and ... | 276 | 0.000000 |
| q07 | fail | n/a | fail | pass | pass | 1 | The response describes the staffing of the incident commander rather than defining the criteria that make an incident... | 301 | 0.000000 |
| q08 | pass | pass | pass | pass | pass | 5 | The model response accurately reflects the reference answer regarding the 20-minute initial update and subsequent 30-... | 317 | 0.000000 |
| q09 | pass | pass | pass | pass | pass | 5 | The model response accurately states both the draft deadline (3 business days) and the review meeting deadline (7 bus... | 319 | 0.000000 |
| q10 | fail | n/a | fail | pass | pass | 1 | The model failed to provide the correct answer and instead claimed the information was missing, contradicting the ref... | 48 | 0.000000 |
| q11 | fail | fail | fail | pass | pass | 1 | The response describes how to start a deploy but fails to provide the specific traffic progression details (5% for 25... | 213 | 0.000000 |
| q12 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures both conditions (error rate > 0.8% and p95 latency increase >= 30%) specified ... | 350 | 0.000000 |
| q13 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies both required approvers as stated in the reference answer. | 231 | 0.000000 |
| q14 | pass | pass | pass | pass | pass | 5 | The model correctly identifies the timing as the last 5 business days of each quarter, matching the reference answer. | 221 | 0.000000 |
| q15 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies the number of partitions (96) and the keying strategy (by tag ID), fully matc... | 385 | 0.000000 |
| q16 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the service (excursion-engine) and its function, but omits the specific details abo... | 191 | 0.000000 |
| q17 | pass | n/a | pass | pass | pass | 4 | The response correctly identifies the RPO and RTO values but omits the location of the disaster-recovery replica ment... | 279 | 0.000000 |
| q18 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 30-day duration but omits the specific detail about moving to Parquet files in ... | 159 | 0.000000 |
| q19 | pass | pass | pass | pass | fail | 5 | The model response accurately captures all conditions and thresholds specified in the reference answer. | 468 | 0.000000 |
| q20 | fail | fail | fail | fail | pass | 1 | The model failed to provide the answer contained in the reference, claiming the context was insufficient. | 54 | 0.000000 |
| q21 | fail | pass | fail | pass | pass | 3 | The response correctly identifies the maximum number of replicas (48) but completely omits the reason for the limit (... | 144 | 0.000000 |
| q22 | pass | n/a | pass | pass | pass | 4 | The response correctly states that offsets should not be reset, but it omits the specific consequence (SEV1) mentione... | 158 | 0.000000 |
| q23 | fail | fail | fail | pass | pass | 3 | The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediat... | 429 | 0.000000 |
| q24 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer (72 hours) and incorrectly stated that the context did not contain the... | 53 | 0.000000 |
| q25 | fail | fail | fail | fail | pass | 2 | The response mentions that there are two carriers but fails to name them, which is the core information requested by ... | 216 | 0.000000 |
| q26 | pass | n/a | pass | pass | pass | 5 | The model response accurately captures all key details from the reference answer, including the threshold (3%), scope... | 416 | 0.000000 |
| q27 | fail | fail | fail | pass | pass | 1 | The model failed to provide the answer contained in the context, whereas the reference answer identifies the likely c... | 46 | 0.000000 |
| q28 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer (7 years) and instead claimed the information was not in the context. | 48 | 0.000000 |
| q29 | pass | pass | pass | pass | pass | 4 | The response correctly states the 35-day retention period but omits the detail about point-in-time recovery for the l... | 227 | 0.000000 |
| q30 | pass | pass | pass | pass | pass | 5 | The model response correctly identifies that only the General Counsel can place or lift a legal hold, which fully ali... | 191 | 0.000000 |
| q31 | pass | pass | pass | pass | pass | 4 | The response correctly identifies the 8-hour limit but omits the additional requirement for a second approver mention... | 124 | 0.000000 |
| q32 | pass | n/a | pass | pass | pass | 4 | The response correctly identifies the three main consequences (paging, logging, reporting) but omits the specific usa... | 386 | 0.000000 |
| q33 | pass | pass | pass | pass | fail | 5 | The model response correctly states the per diem amount as $85 per day, matching the reference answer exactly. | 156 | 0.000000 |
| q34 | fail | fail | fail | fail | pass | 1 | The model failed to provide the correct answer and incorrectly stated that the context did not contain the information. | 47 | 0.000000 |
| q35 | fail | fail | fail | pass | pass | 1 | The response describes a different holiday period (December/January) and does not mention Thaw Day or the first Frida... | 181 | 0.000000 |
| q36 | fail | fail | fail | fail | pass | 1 | The response fails to provide the specific actions required (arranging a swap and recording it in Klaxon) and instead... | 296 | 0.000000 |
| q37 | pass | pass | pass | pass | pass | 5 | The model response accurately states the 30-minute SLA, 24/7 coverage, and dedicated CSM, matching the reference answ... | 257 | 0.000000 |
| q38 | fail | n/a | fail | pass | pass | 3 | The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subseq... | 312 | 0.000000 |
| q39 | fail | fail | fail | pass | pass | 1 | The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference... | 231 | 0.000000 |
| q40 | fail | n/a | fail | pass | pass | 1 | The response identifies the likely cause (tagbroker) but fails to answer the specific questions about which on-call r... | 227 | 0.000000 |
| q41 | fail | fail | fail | pass | pass | 1 | The model response fails to answer the question about severity and instead provides irrelevant information about the ... | 177 | 0.000000 |
| q42 | fail | fail | fail | pass | pass | 1 | The response fails to answer the question about the retention period (400 days) and instead provides unrelated detail... | 385 | 0.000000 |
| q43 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 47 | 0.000000 |
| q44 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 48 | 0.000000 |
| q45 | fail | n/a | fail | n/a | fail | 1 | The model invents a confident answer by stating the region name as if it were the provider, failing to acknowledge th... | 125 | 0.000000 |
| q46 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 48 | 0.000000 |
| q47 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the answer is not in the documents and does not invent any information. | 48 | 0.000000 |
| q48 | pass | n/a | pass | n/a | pass | 5 | The response correctly identifies that the provided context does not contain the answer and does not invent any infor... | 48 | 0.000000 |

## Failures

### q03 - judge

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    By default, Skerrow declares an excursion after 3 consecutive out-of-range readings.
    Quote: "By default, Skerrow declares an excursion after 3 consecutive out-of-range readings." [company-overview]

**Retrieved docs:** company-overview

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

**Retrieved docs:** oncall-policy

**Judge:** score 3 - The response correctly identifies that the secondary is paged but omits the specific time thresholds (5 minutes) and the subsequent escalation to the engineering manager (10 minutes later) mentioned in the reference answer.

### q07 - judge

**Question:** What makes an incident a SEV1?

**Response:**

    Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly.
    Quote: "Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly." [incident-severity]

**Retrieved docs:** incident-severity

**Judge:** score 1 - The response describes the staffing of the incident commander rather than defining the criteria that make an incident SEV1, thus failing to answer the question.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the correct answer and instead claimed the information was missing, contradicting the reference answer.

### q11 - exact, judge

**Question:** How does a production canary progress?

**Response:**

    Production deploys are started with `skr deploy <service>` and always go through a canary.
    Quote: "Production deploys are started with `skr deploy <service>` and always go through a canary." [deploy-process]

**Retrieved docs:** deploy-process

**Judge:** score 1 - The response describes how to start a deploy but fails to provide the specific traffic progression details (5% for 25 mins, 50% for 15 mins, 100%) required by the reference answer.

### q20 - exact, judge, retrieval

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** incident-severity

**Judge:** score 1 - The model failed to provide the answer contained in the reference, claiming the context was insufficient.

### q21 - judge

**Question:** What's the maximum number of normalizer replicas, and why is there a limit?

**Response:**

    The ceiling is 48 replicas.
    Quote: "The ceiling is 48 replicas." [runbook-ingest-backlog]

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 3 - The response correctly identifies the maximum number of replicas (48) but completely omits the reason for the limit (database overload/backlog) which is a key part of the question.

### q23 - exact, judge

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    If one partition is far behind the others, the usual cause is a "chatty tag": a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval.
    Quote: "If one partition is far behind the others, the usual cause is a "chatty tag": a tag on firmware 3.2.x that sends a reading every second instead of at the normal interval." [runbook-ingest-backlog]

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 3 - The response correctly identifies the cause (chatty tag on firmware 3.2.x) but completely omits the required remediation steps (quarantine command and notifying the Firmware team).

### q24 - exact, judge, retrieval

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** data-retention

**Judge:** score 1 - The model failed to provide the correct answer (72 hours) and incorrectly stated that the context did not contain the answer.

### q25 - exact, judge, retrieval

**Question:** Which cellular carriers do Skerrow Tags use?

**Response:**

    1. Skerrow Tags send readings over LTE-M through one of two cellular carriers.
    Quote: "1. Skerrow Tags send readings over LTE-M through one of two cellular carriers." [architecture-overview]

**Retrieved docs:** architecture-overview

**Judge:** score 2 - The response mentions that there are two carriers but fails to name them, which is the core information requested by the question.

### q27 - exact, judge

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-tag-offline

**Judge:** score 1 - The model failed to provide the answer contained in the context, whereas the reference answer identifies the likely cause as tagbroker.

### q28 - exact, judge, retrieval

**Question:** How long are raw readings kept for customers on the Sovereign plan?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** architecture-overview

**Judge:** score 1 - The model failed to provide the correct answer (7 years) and instead claimed the information was not in the context.

### q34 - exact, judge, retrieval

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    The provided context does not contain the answer.

**Retrieved docs:** runbook-ingest-backlog

**Judge:** score 1 - The model failed to provide the correct answer and incorrectly stated that the context did not contain the information.

### q35 - exact, judge

**Question:** What is Thaw Day?

**Response:**

    The company also shuts down from December 24 through January 1.
    Quote: "The company also shuts down from December 24 through January 1." [pto-and-leave]

**Retrieved docs:** pto-and-leave

**Judge:** score 1 - The response describes a different holiday period (December/January) and does not mention Thaw Day or the first Friday of March.

### q36 - exact, judge, retrieval

**Question:** I'm scheduled for on-call during my vacation. What do I need to do?

**Response:**

    If you're scheduled for on-call during planned time off, the Time Off and Leave policy sets how much notice you need to give.
    Quote: "If you're scheduled for on-call during planned time off, the Time Off and Leave policy sets how much notice you need to give." [oncall-policy]

**Retrieved docs:** oncall-policy

**Judge:** score 1 - The response fails to provide the specific actions required (arranging a swap and recording it in Klaxon) and instead gives a vague, non-actionable statement about notice periods.

### q38 - judge

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate.
    Quote: "When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate." [customer-support-escalation]

**Retrieved docs:** customer-support-escalation

**Judge:** score 3 - The response correctly identifies the initial action (pulling readings and certificate) but omits the critical subsequent steps regarding the 12-month calibration cycle and the customer credit policy.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform.
    Quote: "A hotfix during a freeze needs approval from both the on-call engineering manager and the Head of Platform." [deploy-process]

**Retrieved docs:** deploy-process

**Judge:** score 1 - The model incorrectly identifies the approvers as the engineering manager and Head of Platform, whereas the reference states the incident commander can approve it alone.

### q40 - judge

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers.
    Quote: "If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers." [runbook-tag-offline]

**Retrieved docs:** runbook-tag-offline

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

**Retrieved docs:** access-control

**Judge:** score 1 - The response fails to answer the question about the retention period (400 days) and instead provides unrelated details about paging and reporting.

### q45 - judge, quote

**Question:** Which cloud provider runs the us-central production region?

**Response:**

    Production runs in the us-central region.
    Quote: "Production runs in the us-central region." [architecture-overview]

**Retrieved docs:** architecture-overview

**Judge:** score 1 - The model invents a confident answer by stating the region name as if it were the provider, failing to acknowledge that the documents do not contain the answer.
