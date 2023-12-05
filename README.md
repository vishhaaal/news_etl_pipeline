

# Snowflake, Airflow, and S3 Integration

This project demonstrates an ETL (Extract, Transform, Load) process using Snowflake, Airflow, and S3 to extract news data from an API, stage it in S3, and load it into Snowflake.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Introduction

This project utilizes Airflow, Snowflake, and S3 to extract news data from a specific API, transform it into a suitable format, stage it in an S3 bucket, and finally load it into a Snowflake table for further analysis.

## Dependencies

- Airflow
- Snowflake Python Connector
- Python 3.x
- Pandas
- Requests

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vishhaaal/news_etl_pipeline.git
   cd news_etl_pipeline
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Airflow Configuration:**

   - Configure Airflow connections for Snowflake (`snowflake_conn`) and S3 (`s3_conn`) in the Airflow web UI.

4. **Snowflake Configuration:**

   - Ensure the Snowflake connection parameters are correctly set in the code (SnowflakeOperator tasks).

5. **S3 Configuration:**

   - Adjust S3 bucket details in the `extract_and_stage_to_s3` Python function.

## Usage

1. **Run the Airflow DAG:**

   - Ensure Airflow is up and running.
   - Place the Python script containing the DAG in the Airflow DAGs folder.
   - The DAG will be scheduled to run daily (`schedule_interval = '@daily'`).

2. **Monitoring:**

   - Use the Airflow UI to monitor the DAG execution and view logs.

## Project Structure

- `dags/`: Contains the Airflow DAG script.
- `scripts/`: Python scripts for ETL tasks.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Fork the repository, make changes, and submit a pull request following the contribution guidelines.

