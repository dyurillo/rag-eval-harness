# Access Control Policy

Owner: Security · Last reviewed: 2026-06

## Production access

Only the Platform team has standing production access. Everyone else requests just-in-time (JIT) access, for example `skr access request --role prod-read --duration 4h`. A grant lasts at most 8 hours. A `prod-write` grant also needs approval from a second person on the Platform team.

## Break-glass

The `breakglass` account is for SEV1 incidents when JIT access isn't working. Its credentials are kept in a sealed vault entry. Using it automatically pages the Head of Security, every action taken with it is recorded in the audit log, and the person who used it must file a break-glass report within 24 hours.

## Customer data

Support engineers can view a customer's shipment data only when an open support ticket references it. "View as customer" sessions are logged and expire after 60 minutes.

## Laptops and keys

Company laptops must use full-disk encryption and lock after 5 minutes of inactivity. Every employee gets two hardware security keys: one for daily use and one kept as a backup.

## Reviews and offboarding

Managers review their team's access every quarter. When someone leaves the company, all of their access is revoked within 4 hours of the end of their last working day.
