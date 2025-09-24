
# P&G Retailer-Fulfilled Media Analytics (AWS Reference Project)

An end-to-end, interview-ready reference implementation for **Media Analytics & Attribution** in a **retailer-fulfilled** world (e.g., Customer → Amazon/Walmart/Target).

## What this repo contains
- **SQL schemas** for Redshift
- **dbt starter project** for transforms
- **Python** reference code for MTA, MMM-lite, and forecasting
- **Sample data** to run a local demo
- **Architecture diagram** and Make targets

> This is a skeleton for GitHub. Replace secrets, wire to your real infra, or run locally with sample CSVs.

## Architecture (AWS)
- Sources → S3 Data Lake → Redshift (warehouse) → ML (SageMaker/EMR) → QuickSight/APIs
- Orchestration via Airflow (MWAA) or local cron for demo

![architecture](diagrams/architecture.png)

## Quickstart (Local demo)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run simple demo: loads sample CSVs, applies MTA weights, prints channel credit
python src/ingest/load_sample.py
python src/attribution/mta.py --paths data/sample/paths_sample.csv --out data/sample/attribution_out.csv

# Run MMM-lite demo
python src/modeling/mmm.py --features data/sample/mmm_features_sample.csv --out data/sample/mmm_outputs.json

# Run forecasting demo
python src/forecast/forecast.py --hist data/sample/pos_sales_sample.csv --out data/sample/forecast_out.csv
```

## Repo layout
```
src/
  ingest/        # sample loaders
  transform/     # dbt seeds/hooks (placeholder)
  attribution/   # MTA & geo-lift demo
  modeling/      # MMM-lite (ridge) demo
  forecast/      # SARIMAX/Prophet-style demo
sql/schema/      # Redshift DDL
dbt/             # dbt starter
data/sample/     # synthetic CSVs
diagrams/        # architecture image
docker/          # dockerfile (optional)
```

## Disclaimers
- This is a **teaching** and interview-reference repo; adapt for production.
- Replace sample CSV with your internal feeds and secure secrets.
