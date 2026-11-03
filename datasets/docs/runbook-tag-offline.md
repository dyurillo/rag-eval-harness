# Runbook: Tags Offline Spike (TagsOfflineSpike)

Owner: Ingest · Last reviewed: 2026-09

## Alert

`TagsOfflineSpike` fires when more than 3% of active tags in a single carrier region miss 4 consecutive check-ins, which is about 6 minutes at the standard reporting interval.

## What it usually means

Most spikes are cellular carrier outages, not problems on our side. Tags buffer up to 72 hours of readings locally and send them when they reconnect, so a carrier outage only loses data if it lasts longer than 72 hours.

## Steps

1. On the "Tags / Connectivity" dashboard, split the offline tags by carrier: NorthSpan or Corvel Mobile.
2. If the drop is limited to one carrier, open a ticket with that carrier and post a status page update describing "delayed telemetry". Don't call it an outage: the readings are buffered, not lost.
3. If tags on both carriers are dropping, the problem is probably tagbroker rather than the carriers. Page the Platform on-call.

## Customer communication

If any Sovereign customer has affected shipments, notify their CSM within 30 minutes of the alert.

## Remote reboots

`skr tag reboot <tag_id>` restarts a tag remotely, but it drains the battery. Reboot a tag at most once per 24 hours, and don't use reboots during a carrier outage at all.
