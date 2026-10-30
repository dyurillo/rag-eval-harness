# Incident Severity Levels

Owner: Platform · Last reviewed: 2026-05

## Declaring an incident

Anyone at Tallowmoth can declare an incident by typing `/sev declare` in the #incidents channel. If you're unsure between two severities, declare the higher one. It can be downgraded later.

## SEV1

An incident is a SEV1 if any of these is true:

- Ingest or alert delivery is down for more than 10% of active tags.
- Any temperature readings have been permanently lost, whether in our systems, in transit, or because a tag's local buffer filled up.
- Excursion alerts are delayed by more than 10 minutes for any customer.
- A security breach involving customer data is confirmed.

## SEV2

An incident is a SEV2 if any of these is true and it doesn't meet the SEV1 criteria:

- Alert delivery is delayed by more than 4 minutes at p95.
- A single Sovereign customer has a full outage.
- Skerrow Console is unavailable while ingest and alerting still work.

## SEV3

Internal tooling problems, minor bugs with a workaround, and single-customer issues on Starter or Fleet plans that don't affect alerting.

## Incident commander

Every SEV1 has an incident commander (IC) from the IC rotation, which is staffed by senior engineers and engineering managers and changes weekly. The IC coordinates the response and handles communication. The IC must not be the person debugging. A SEV2 gets an IC only if the on-call primary asks for one.

## Communication

- SEV1: update the public status page within 20 minutes of declaring the incident, then every 30 minutes until it's resolved. Notify Customer Success immediately.
- SEV2: a status page update is at the discretion of the IC or on-call primary. Notify Customer Success within 1 hour.
- SEV3: no external communication.

## Postmortems

Postmortems are blameless. For a SEV1, the postmortem draft is due within 3 business days of resolution, and the review meeting must happen within 7 business days. SEV2 postmortems are due within 10 business days. SEV3 incidents don't need a postmortem. Action items are tracked as tickets with the `pm-action` label.
