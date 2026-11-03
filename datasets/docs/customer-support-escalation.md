# Customer Support and Escalation

Owner: Support · Last reviewed: 2026-08

## Support tiers

- Tier 1: support agents handle account, billing and Console questions.
- Tier 2: support engineers investigate data, tag and alert problems.
- Tier 3: the engineering on-call for the team that owns the affected service.

## Response-time SLAs

| Plan | First response | Coverage |
|---|---|---|
| Starter | 1 business day | Email only |
| Fleet | 4 hours | 24/5 |
| Sovereign | 30 minutes for urgent tickets | 24/7, plus a dedicated CSM |

## Escalating to engineering

Tier 2 escalates with `/escalate`, which creates a ticket in the ENG-ESC queue and notifies the owning team's on-call. Engineering must respond within 2 business hours for Fleet tickets and within 30 minutes for urgent Sovereign tickets.

## Disputed excursions

When a customer says an excursion alert was a false alarm, Tier 2 pulls the shipment's raw readings and the tag's calibration certificate. Tags are recalibrated every 12 months. If the tag was past its calibration date when the excursion fired, the customer gets a credit.

## SLA credits

Each SLA breach earns a credit of 10% of the monthly fee, up to 30% in any one month. The Head of Support approves credits.
