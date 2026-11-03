# Tallowmoth Systems: Company Overview

Owner: People Ops · Last reviewed: 2026-07

Tallowmoth Systems builds Skerrow, a cold-chain monitoring platform for refrigerated freight. Shippers of vaccines, biologics, seafood and fresh produce use Skerrow to prove that their goods stayed within the allowed temperature range from the loading dock to the receiving bay.

## History

Tallowmoth was founded in 2019 in Duluth, Minnesota, by Imogen Varga and Rafael Odum. The first Skerrow Tags shipped to pilot customers in 2020. The company opened an office in Halifax, Nova Scotia in 2022 to support Canadian customers and to help run the disaster-recovery region. Most employees work remotely in the US or Canada.

## Leadership

- Imogen Varga, CEO
- Rafael Odum, CTO
- Dana Whitlock, CFO
- Priya Halvorsen, Head of Platform
- Marcus Feld, Head of Security
- Lena Szabo, Head of Support
- Owen Achterberg, General Counsel

## Product

The Skerrow platform has three parts:

- **Skerrow Tag**: a battery-powered sensor that records temperature and humidity. The current hardware is Tag v3. It reports a reading every 90 seconds over LTE-M, works from -40 °C to +70 °C, and its battery lasts about 14 months.
- **Skerrow Cloud**: the backend that ingests readings, detects excursions and sends alerts. See the Architecture Overview.
- **Skerrow Console**: the web dashboard where customers track shipments, set temperature ranges and download compliance reports.

## Plans

Customers buy one of three plans. Starter is for small shippers. Fleet adds API access and webhooks. Sovereign adds extended data retention, a dedicated customer success manager (CSM) and 24/7 support for urgent issues. As of mid-2026, Tallowmoth serves about 380 shipper customers.

## Teams

Tallowmoth has 214 employees. Engineering has 78 people in six teams: Ingest, Routing, Alerts, Platform, Data and Firmware. Platform owns infrastructure, deploy tooling and production access. Firmware owns the Tag hardware and the software that runs on it. Customer Support and Customer Success are part of Operations.

## Glossary

- **Excursion**: a period when a shipment's temperature is outside the customer's allowed range. By default, Skerrow declares an excursion after 3 consecutive out-of-range readings. Customers can change this per shipment.
- **Check-in**: a single report from a tag.
- **Lane**: a recurring shipping route between two sites.
- **skr**: the internal command-line tool for deploys, scaling, tag management and access requests.
