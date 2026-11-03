# Eval run report

- Model: rag-lora-1b
- Judge: Qwen/Qwen3.8-27B-FP8 (threshold 4)
- Retrieval: off
- Dataset: datasets/rag_eval.jsonl (sha256 3656204dc5a891de84efa0db8cdf13435279befa573cf61e3af40b94060354ab)
- Start / end (UTC): 2026-10-23T19:37:31.714891+00:00 / 2026-10-23T19:38:10.029203+00:00

## Summary

| Metric | Value |
|---|---|
| Cases | 6/48 |
| Overall pass rate | 12.5% |
| Pass rate (exact) | 1/30 = 3.3% |
| Pass rate (judge) | 6/48 = 12.5% |
| Pass rate (retrieval) | n/a (not run) |
| Pass rate (quote) | n/a (not run) |
| Pass rate (tag: access) | 0/2 = 0.0% |
| Pass rate (tag: architecture) | 0/3 = 0.0% |
| Pass rate (tag: deploy) | 0/4 = 0.0% |
| Pass rate (tag: expenses) | 0/2 = 0.0% |
| Pass rate (tag: incident) | 0/4 = 0.0% |
| Pass rate (tag: multi-doc) | 0/4 = 0.0% |
| Pass rate (tag: near-miss) | 2/3 = 66.7% |
| Pass rate (tag: numeric) | 1/17 = 5.9% |
| Pass rate (tag: oncall) | 0/3 = 0.0% |
| Pass rate (tag: paraphrase) | 0/4 = 0.0% |
| Pass rate (tag: product) | 0/3 = 0.0% |
| Pass rate (tag: pto) | 0/2 = 0.0% |
| Pass rate (tag: reasoning) | 0/3 = 0.0% |
| Pass rate (tag: retention) | 1/4 = 25.0% |
| Pass rate (tag: runbook) | 0/9 = 0.0% |
| Pass rate (tag: support) | 0/2 = 0.0% |
| Pass rate (tag: unanswerable) | 5/6 = 83.3% |
| Mean judge score | 1.48 |
| Hallucination rate (unanswerable, judge score <= 2) | 1/6 = 16.7% |
| Latency p50 | 66 ms |
| Latency p95 | 107 ms |
| Total tokens | 3277 (prompt 2563, completion 714) |
| Total cost | $0.0000 |
| Errors | 0 |

## Per-question results

| id | result | exact | judge | retrieval | quote | judge score | judge reason | latency (ms) | cost (USD) |
|---|---|---|---|---|---|---|---|---|---|
| q01 | fail | fail | fail | skip | skip | 1 | The model claims the information is not provided, which contradicts the reference answer that explicitly states the f... | 107 | 0.000000 |
| q02 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer found in the reference. | 61 | 0.000000 |
| q03 | fail | n/a | fail | skip | skip | 1 | The model claims the information is not provided, which contradicts the reference answer that gives a specific timefr... | 152 | 0.000000 |
| q04 | fail | n/a | fail | skip | skip | 1 | The model provides incorrect times (2:00 AM and 3:00 AM) that contradict the reference answer (Tuesdays at 10:00 Cent... | 139 | 0.000000 |
| q05 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer and explicitly stated it did not know. | 30 | 0.000000 |
| q06 | fail | n/a | fail | skip | skip | 1 | The response merely restates the condition of the question and fails to provide any information about the escalation ... | 73 | 0.000000 |
| q07 | fail | n/a | fail | skip | skip | 1 | The model response describes a medical condition (hepatitis) instead of the company's incident severity criteria, com... | 97 | 0.000000 |
| q08 | fail | fail | fail | skip | skip | 1 | The model states the update is needed within 24 hours, which directly contradicts the reference answer's requirement ... | 85 | 0.000000 |
| q09 | fail | fail | fail | skip | skip | 1 | The model claims the information is not specified, which contradicts the reference answer that provides specific dead... | 84 | 0.000000 |
| q10 | fail | n/a | fail | skip | skip | 1 | The model claims the information is not provided, whereas the reference answer explicitly states that the engineer ca... | 101 | 0.000000 |
| q11 | fail | fail | fail | skip | skip | 1 | The model failed to provide the specific progression details found in the reference answer, claiming instead that the... | 60 | 0.000000 |
| q12 | fail | n/a | fail | skip | skip | 1 | The model response directly contradicts the reference answer by stating that canaries do not roll back automatically,... | 44 | 0.000000 |
| q13 | fail | fail | fail | skip | skip | 1 | The response incorrectly identifies the operations team as the approver, whereas the reference answer specifies the o... | 72 | 0.000000 |
| q14 | fail | fail | fail | skip | skip | 1 | The model incorrectly states the freeze happens in the third quarter, whereas the reference answer specifies it occur... | 61 | 0.000000 |
| q15 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer and explicitly stated it did not know. | 30 | 0.000000 |
| q16 | fail | fail | fail | skip | skip | 1 | The model failed to identify the correct service (excursion-engine) and incorrectly stated that the answer was not in... | 61 | 0.000000 |
| q17 | fail | n/a | fail | skip | skip | 1 | The model claims the information is missing, which contradicts the reference answer that provides specific RPO and RT... | 76 | 0.000000 |
| q18 | pass | pass | pass | skip | skip | 4 | The response correctly identifies the 30-day retention period but omits the detail about moving to Parquet files in o... | 77 | 0.000000 |
| q19 | fail | fail | fail | skip | skip | 1 | The model provides a specific time (10:00 AM UTC) which is not mentioned in the reference answer and contradicts the ... | 85 | 0.000000 |
| q20 | fail | fail | fail | skip | skip | 1 | The model failed to provide the specific criteria found in the reference answer, claiming instead that the informatio... | 61 | 0.000000 |
| q21 | fail | fail | fail | skip | skip | 1 | The model failed to provide the answer contained in the reference, claiming the text did not contain it. | 62 | 0.000000 |
| q22 | fail | n/a | fail | skip | skip | 1 | The model's response is non-committal and fails to provide the specific prohibition and severity level stated in the ... | 37 | 0.000000 |
| q23 | fail | fail | fail | skip | skip | 1 | The model provides a generic technical explanation (data skew/ingestion) that completely misses the specific internal... | 78 | 0.000000 |
| q24 | fail | fail | fail | skip | skip | 1 | The model claims the information is not provided, which contradicts the reference answer that explicitly states the d... | 88 | 0.000000 |
| q25 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct carriers (NorthSpan and Corvel Mobile) and instead claimed the information wa... | 58 | 0.000000 |
| q26 | fail | n/a | fail | skip | skip | 1 | The response is vague and misses the specific quantitative thresholds (3% of tags, 4 consecutive check-ins) and time ... | 66 | 0.000000 |
| q27 | fail | fail | fail | skip | skip | 1 | The model suggests generic causes like network congestion or bugs, whereas the reference answer specifically identifi... | 73 | 0.000000 |
| q28 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer (7 years) and instead claimed the information was not available. | 92 | 0.000000 |
| q29 | fail | fail | fail | skip | skip | 1 | The model claims the information is not provided, which contradicts the reference answer that specifies the backup du... | 75 | 0.000000 |
| q30 | fail | fail | fail | skip | skip | 1 | The model failed to answer the question and instead claimed it was incomplete, contradicting the reference answer. | 34 | 0.000000 |
| q31 | fail | fail | fail | skip | skip | 1 | The model failed to provide the specific duration (8 hours) and additional requirements stated in the reference answe... | 76 | 0.000000 |
| q32 | fail | n/a | fail | skip | skip | 1 | The model claims the information is not in the context, which contradicts the reference answer that provides specific... | 88 | 0.000000 |
| q33 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct per diem amount stated in the reference answer. | 30 | 0.000000 |
| q34 | fail | fail | fail | skip | skip | 1 | The model response claims the information is not in the context, which contradicts the reference answer that provides... | 88 | 0.000000 |
| q35 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct definition of Thaw Day, instead claiming the information was not in the text. | 60 | 0.000000 |
| q36 | fail | fail | fail | skip | skip | 1 | The response contradicts the reference answer by stating the user must work, whereas the reference instructs them to ... | 76 | 0.000000 |
| q37 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer and explicitly stated it did not know. | 31 | 0.000000 |
| q38 | fail | n/a | fail | skip | skip | 1 | The response is generic and fails to mention the specific procedural steps (pulling raw readings/calibration certific... | 69 | 0.000000 |
| q39 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer and explicitly stated it did not know, contradicting the reference inf... | 31 | 0.000000 |
| q40 | fail | n/a | fail | skip | skip | 1 | The model claims the information is not specified, which contradicts the reference answer that provides a specific ro... | 89 | 0.000000 |
| q41 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct severity (SEV1) and incorrectly stated that the information was insufficient,... | 57 | 0.000000 |
| q42 | fail | fail | fail | skip | skip | 1 | The model failed to provide the correct answer and explicitly stated it did not know. | 30 | 0.000000 |
| q43 | pass | n/a | pass | n/a | skip | 5 | The response correctly identifies that the answer is not available without inventing any information. | 30 | 0.000000 |
| q44 | pass | n/a | pass | n/a | skip | 5 | The model correctly identified that the answer is not available and did not invent any information. | 30 | 0.000000 |
| q45 | fail | n/a | fail | n/a | skip | 1 | The model invents a specific, confident answer (AWS) that is not present in the documents. | 65 | 0.000000 |
| q46 | pass | n/a | pass | n/a | skip | 5 | The model correctly identified that the answer is not in the documents and did not invent any information. | 30 | 0.000000 |
| q47 | pass | n/a | pass | n/a | skip | 5 | The response correctly states that the procedure is not provided in the text and does not invent any information. | 92 | 0.000000 |
| q48 | pass | n/a | pass | n/a | skip | 5 | The response correctly states that the answer is not known, aligning with the fact that the documents do not contain ... | 29 | 0.000000 |

## Failures

### q01 - exact, judge

**Question:** How often does a Skerrow Tag send a reading?

**Response:**

    The provided information does not state how often a Skerrow Tag sends a reading.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not provided, which contradicts the reference answer that explicitly states the frequency is every 90 seconds.

### q02 - exact, judge

**Question:** How long does the battery in a Skerrow Tag v3 last?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer found in the reference.

### q03 - judge

**Question:** With default settings, roughly how long does a shipment's temperature have to stay out of range before Skerrow declares an excursion?

**Response:**

    The provided information does not include the timeframe for a shipment's temperature to stay out of range before Skerrow declares an excursion.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not provided, which contradicts the reference answer that gives a specific timeframe.

### q04 - judge

**Question:** When does the on-call rotation hand off?

**Response:**

    The on-call rotation hand off is typically at 2:00 AM and 3:00 AM.

**Retrieved docs:** (none)

**Judge:** score 1 - The model provides incorrect times (2:00 AM and 3:00 AM) that contradict the reference answer (Tuesdays at 10:00 Central).

### q05 - exact, judge

**Question:** How much is the weekly stipend for a primary on-call shift?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer and explicitly stated it did not know.

### q06 - judge

**Question:** If the primary on-call doesn't acknowledge a SEV1 page, what happens?

**Response:**

    The primary on-call doesn't acknowledge a SEV1 page.

**Retrieved docs:** (none)

**Judge:** score 1 - The response merely restates the condition of the question and fails to provide any information about the escalation process described in the reference answer.

### q07 - judge

**Question:** What makes an incident a SEV1?

**Response:**

    SEV1 is a type of viral hepatitis that is caused by the hepatitis B virus (HBV).

**Retrieved docs:** (none)

**Judge:** score 1 - The model response describes a medical condition (hepatitis) instead of the company's incident severity criteria, completely contradicting the reference answer.

### q08 - exact, judge

**Question:** How soon after declaring a SEV1 does the status page need an update?

**Response:**

    The status page needs an update within 24 hours of declaring a SEV1.

**Retrieved docs:** (none)

**Judge:** score 1 - The model states the update is needed within 24 hours, which directly contradicts the reference answer's requirement of within 20 minutes.

### q09 - exact, judge

**Question:** When is the postmortem draft due for a SEV1?

**Response:**

    The postmortem draft due for a SEV1 is not specified in the provided information.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not specified, which contradicts the reference answer that provides specific deadlines.

### q10 - judge

**Question:** Can the engineer who is debugging a SEV1 also be its incident commander?

**Response:**

    The provided information does not state whether the engineer who is debugging a SEV1 can be its incident commander.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not provided, whereas the reference answer explicitly states that the engineer cannot be the incident commander.

### q11 - exact, judge

**Question:** How does a production canary progress?

**Response:**

    The provided information does not contain the answer to the question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the specific progression details found in the reference answer, claiming instead that the information was not available.

### q12 - judge

**Question:** What makes a canary roll back automatically?

**Response:**

    Canaries do not roll back automatically.

**Retrieved docs:** (none)

**Judge:** score 1 - The model response directly contradicts the reference answer by stating that canaries do not roll back automatically, whereas the reference specifies the conditions under which they do.

### q13 - exact, judge

**Question:** Outside of an incident, who has to approve a hotfix during a deploy freeze?

**Response:**

    The answer is: The deploy freeze is typically managed by the operations team.

**Retrieved docs:** (none)

**Judge:** score 1 - The response incorrectly identifies the operations team as the approver, whereas the reference answer specifies the on-call engineering manager and the Head of Platform.

### q14 - exact, judge

**Question:** When does the quarterly deploy freeze happen?

**Response:**

    The quarterly deploy freeze happens in the third quarter of the year.

**Retrieved docs:** (none)

**Judge:** score 1 - The model incorrectly states the freeze happens in the third quarter, whereas the reference answer specifies it occurs during the last 5 business days of every quarter.

### q15 - exact, judge

**Question:** How many partitions does the readings.raw Kafka topic have?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer and explicitly stated it did not know.

### q16 - exact, judge

**Question:** Which service checks readings against a shipment's temperature range?

**Response:**

    The provided text does not contain the answer to the question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to identify the correct service (excursion-engine) and incorrectly stated that the answer was not in the text.

### q17 - judge

**Question:** What are the disaster recovery RPO and RTO?

**Response:**

    The provided text does not contain information about disaster recovery RPO and RTO.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is missing, which contradicts the reference answer that provides specific RPO and RTO values.

### q19 - exact, judge

**Question:** At what consumer lag does the IngestLagHigh alert fire?

**Response:**

    The IngestLagHigh alert fire occurs at 10:00 AM UTC.

**Retrieved docs:** (none)

**Judge:** score 1 - The model provides a specific time (10:00 AM UTC) which is not mentioned in the reference answer and contradicts the actual conditions (message count and age) described in the reference.

### q20 - exact, judge

**Question:** When should an ingest backlog be upgraded from SEV2 to SEV1?

**Response:**

    The provided information does not contain the answer to this question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the specific criteria found in the reference answer, claiming instead that the information was not available.

### q21 - exact, judge

**Question:** What's the maximum number of normalizer replicas, and why is there a limit?

**Response:**

    The provided text does not contain the answer to the question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the answer contained in the reference, claiming the text did not contain it.

### q22 - judge

**Question:** Can I reset the consumer offsets to clear an ingest backlog?

**Response:**

    It depends on the consumer.

**Retrieved docs:** (none)

**Judge:** score 1 - The model's response is non-committal and fails to provide the specific prohibition and severity level stated in the reference answer.

### q23 - exact, judge

**Question:** One Kafka partition is way behind and the rest look fine. What's probably going on and what should I do?

**Response:**

    The problem is likely a data skew or a problem with the data ingestion process.

**Retrieved docs:** (none)

**Judge:** score 1 - The model provides a generic technical explanation (data skew/ingestion) that completely misses the specific internal cause (chatty tag on firmware 3.2.x) and the required remediation steps (quarantine and notify Firmware team) found in the reference answer.

### q24 - exact, judge

**Question:** How many hours of readings can a tag hold while it has no connection?

**Response:**

    The provided information does not state how many hours a tag can hold while it has no connection.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not provided, which contradicts the reference answer that explicitly states the duration is up to 72 hours.

### q25 - exact, judge

**Question:** Which cellular carriers do Skerrow Tags use?

**Response:**

    The provided text does not contain the answer to the question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct carriers (NorthSpan and Corvel Mobile) and instead claimed the information was not in the text.

### q26 - judge

**Question:** When does the TagsOfflineSpike alert fire?

**Response:**

    The TagsOfflineSpike alert fire occurs when the tags are offline.

**Retrieved docs:** (none)

**Judge:** score 1 - The response is vague and misses the specific quantitative thresholds (3% of tags, 4 consecutive check-ins) and time frame (6 minutes) defined in the reference answer.

### q27 - exact, judge

**Question:** Tags on both carriers are going offline at the same time. What's the likely cause?

**Response:**

    Possible causes include network congestion, a major outage, or a software bug.

**Retrieved docs:** (none)

**Judge:** score 1 - The model suggests generic causes like network congestion or bugs, whereas the reference answer specifically identifies 'tagbroker' as the likely cause and advises paging the Platform on-call.

### q28 - exact, judge

**Question:** How long are raw readings kept for customers on the Sovereign plan?

**Response:**

    The provided information does not state how long raw readings are kept for customers on the Sovereign plan.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer (7 years) and instead claimed the information was not available.

### q29 - exact, judge

**Question:** How long are backups of the core database kept?

**Response:**

    The provided information does not state how long backups of the core database are kept.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not provided, which contradicts the reference answer that specifies the backup duration.

### q30 - exact, judge

**Question:** Who can put a legal hold on data?

**Response:**

    The question is incomplete.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to answer the question and instead claimed it was incomplete, contradicting the reference answer.

### q31 - exact, judge

**Question:** What's the longest stretch of temporary production access I can get?

**Response:**

    The provided context does not contain information about the longest stretch of temporary production access.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the specific duration (8 hours) and additional requirements stated in the reference answer, claiming instead that the information was not available.

### q32 - judge

**Question:** What happens when someone uses the break-glass account?

**Response:**

    The provided context does not contain information about what happens when someone uses the break-glass account.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not in the context, which contradicts the reference answer that provides specific details about the break-glass account procedure.

### q33 - exact, judge

**Question:** What's the per diem for international travel?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct per diem amount stated in the reference answer.

### q34 - exact, judge

**Question:** Who needs to approve a $2,000 expense?

**Response:**

    The provided context does not state who needs to approve a $2,000 expense.

**Retrieved docs:** (none)

**Judge:** score 1 - The model response claims the information is not in the context, which contradicts the reference answer that provides a specific approval authority.

### q35 - exact, judge

**Question:** What is Thaw Day?

**Response:**

    The provided text does not contain the answer to the question.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct definition of Thaw Day, instead claiming the information was not in the text.

### q36 - exact, judge

**Question:** I'm scheduled for on-call during my vacation. What do I need to do?

**Response:**

    You need to do what you're scheduled for during your vacation.

**Retrieved docs:** (none)

**Judge:** score 1 - The response contradicts the reference answer by stating the user must work, whereas the reference instructs them to arrange a swap.

### q37 - exact, judge

**Question:** What's the first-response SLA for urgent tickets on the Sovereign plan?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer and explicitly stated it did not know.

### q38 - judge

**Question:** A customer says an excursion alert was a false alarm. How does support handle it?

**Response:**

    Support should acknowledge the customer's statement and offer to investigate further.

**Retrieved docs:** (none)

**Judge:** score 1 - The response is generic and fails to mention the specific procedural steps (pulling raw readings/calibration certificates) or the outcome (credit if past calibration date) described in the reference answer.

### q39 - exact, judge

**Question:** Excursion alerts are running 12 minutes late for one customer, and it's during the quarterly freeze. Who can approve a hotfix?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer and explicitly stated it did not know, contradicting the reference information.

### q40 - judge

**Question:** If tags on both carriers drop offline, which on-call rotation gets paged and what does it cover?

**Response:**

    The provided information does not specify which on-call rotation gets paged and what it covers.

**Retrieved docs:** (none)

**Judge:** score 1 - The model claims the information is not specified, which contradicts the reference answer that provides a specific rotation and coverage.

### q41 - exact, judge

**Question:** A carrier outage lasted 80 hours. What severity should the incident be?

**Response:**

    The provided information does not allow for a severity assessment.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct severity (SEV1) and incorrectly stated that the information was insufficient, contradicting the reference answer.

### q42 - exact, judge

**Question:** How long is the record of actions taken with the break-glass account kept?

**Response:**

    I do not know.

**Retrieved docs:** (none)

**Judge:** score 1 - The model failed to provide the correct answer and explicitly stated it did not know.

### q45 - judge

**Question:** Which cloud provider runs the us-central production region?

**Response:**

    Amazon Web Services (AWS) runs the us-central production region.

**Retrieved docs:** (none)

**Judge:** score 1 - The model invents a specific, confident answer (AWS) that is not present in the documents.
