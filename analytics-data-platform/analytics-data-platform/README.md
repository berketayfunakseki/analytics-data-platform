# Analytics Data Platform

A portfolio data-engineering project that demonstrates an end-to-end batch analytics pipeline using **Apache Airflow**, **PySpark / Apache Spark**, **dbt**, **PostgreSQL**, **Parquet**, **Docker**, and **GitHub Actions CI**.

## Architecture

1. **Airflow** orchestrates the batch workflow.
2. **PySpark** validates, types, deduplicates, and transforms raw order events into partition-friendly Parquet data.
3. **PostgreSQL** acts as the analytics warehouse target.
4. **dbt** creates staging and mart models, including a daily-sales fact table and data-quality tests.
5. **Docker Compose** defines a reproducible local Postgres + Airflow environment.
6. **GitHub Actions** performs syntax and project-structure checks.

## Skills demonstrated

Data engineering, ETL/ELT, data pipelines, workflow orchestration, Apache Airflow, Apache Spark, PySpark, dbt, SQL, PostgreSQL, data warehousing, dimensional modeling, data quality, Parquet, Docker, CI/CD, analytics engineering.

## Repository structure

```text
airflow/dags/orders_pipeline.py      # pipeline orchestration
spark/jobs/transform_orders.py       # Spark transformation job
dbt/models/staging/stg_orders.sql    # typed staging model
dbt/models/marts/fct_daily_sales.sql # analytics mart
dbt/models/schema.yml                # dbt tests / documentation
sql/init.sql                         # warehouse bootstrap
data/raw/orders.csv                  # small reproducible sample
```

## Pipeline flow

`raw CSV -> PySpark validation/deduplication -> Parquet -> PostgreSQL staging -> dbt staging -> dbt marts/tests`

The repository is designed as a portfolio reference implementation rather than a claim of production-scale operation.
