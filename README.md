# cryptocurrency_pipeline

## Cryptocurrency ETL Pipeline with Apache Airflow

## Overview:
This repository hosts an Extract, Transform, Load (ETL) pipeline designed for fetching cryptocurrency data from major cryptocurrency websites. The pipeline focuses on data extraction and transformation phases, with indicator development in progress. It leverages Apache Airflow for orchestration, Docker for containerization, and the request package in Python for data retrieval.

## Features:
1. Extraction of cryptocurrency data from major sources
2. Transformation of raw data into a structured format
3. Orchestrated workflow managed by Apache Airflow
4. Scalable and containerized deployment using Docker

## Installation:
To set up the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Docker and Apache Airflow.
3. Set up the necessary environment variables.
4. Run the Docker container to deploy the pipeline.

## Usage:
After installation, you can execute the pipeline using Apache Airflow's UI or CLI. The pipeline will automatically fetch cryptocurrency data from designated sources, perform necessary transformations, and store the processed data in a database or file system.
