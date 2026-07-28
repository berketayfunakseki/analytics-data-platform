"""Airflow DAG orchestrating Spark transformation and dbt models."""
from __future__ import annotations

from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="orders_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="0 6 * * *",
    catchup=False,
    tags=["data-engineering", "spark", "dbt"],
) as dag:
    transform = BashOperator(
        task_id="spark_transform",
        bash_command=(
            "spark-submit /opt/project/spark/jobs/transform_orders.py "
            "--source /opt/project/data/raw/orders.csv "
            "--target /opt/project/data/processed/orders"
        ),
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/project/dbt && dbt run --profiles-dir .",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/project/dbt && dbt test --profiles-dir .",
    )

    transform >> dbt_run >> dbt_test
