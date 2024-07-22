from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import timedelta

import os

project_dir = os.getcwd()

with DAG(
    "apartment_scraper",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "start_date": datetime(2024, 7, 20),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A DAG to automate web scraping with Scrapy",
    schedule=timedelta(days=1),
    start_date=datetime(2024, 7, 22),
    catchup=False,
    tags=["web scraper"],
) as dag:
    task_1 = BashOperator(
        task_id="scrape_data",
        bash_command=f"cd {project_dir}/src/simple_airflow_automation && poetry run scrapy crawl buyrentkenya",
        dag=dag,
    )
