# On-Call Policy

Owner: Platform · Last reviewed: 2026-06

## Rotations

Every engineering team that owns a production service runs its own on-call rotation, with a primary and a secondary. The Platform team runs the infrastructure rotation, which covers tagbroker, Kafka, the databases and the deploy pipeline.

Rotations last 7 days and hand off on Tuesdays at 10:00 Central. Handoff is a 15-minute call in which the outgoing primary walks through open incidents and any alert that fired more than twice during the week.

Incident commanders come from a separate IC rotation. See Incident Severity Levels.

## Joining the rotation

Engineers become eligible for on-call after 60 days at Tallowmoth. Before their first primary shift, they shadow the current primary for two full rotation weeks. Nobody is primary for more than one week in any five-week window.

## Paging and acknowledgement

Pages are sent by Klaxon, our internal paging service. Acknowledgement targets:

- SEV1: within 5 minutes
- SEV2: within 15 minutes
- SEV3: next business day. SEV3 alerts never page outside business hours.

## Escalation

If the primary doesn't acknowledge a SEV1 or SEV2 page within its target, Klaxon pages the secondary. If the page is still unacknowledged 10 minutes after that, Klaxon pages the team's engineering manager.

## Compensation

On-call stipends apply to primary and secondary shifts on team rotations:

- Primary: $340 per week
- Secondary: $150 per week

An engineer who gets more than 3 after-hours pages in a single on-call week receives one day off in lieu, to be taken within the following month.

## Swaps

Engineers arrange swaps among themselves and record them in Klaxon so pages reach the right person. If you're scheduled for on-call during planned time off, the Time Off and Leave policy sets how much notice you need to give.
