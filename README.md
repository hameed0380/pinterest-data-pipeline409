# Pinterest Data Pipeline


## Table of Contents
- [Project Overview](#project-overview)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Project Overview
This is a end to end AWS-hosted data pipeline inspired by Pinterest's experiment processing pipeline. The pipeline is developed using a Lambda architecture. 

![Images](Images/CloudPinterestPipeline.png)

## Description
The Pinterest Data Pipeline project is an end-to-end AWS-hosted data pipeline, drawing inspiration from Pinterest’s experimental processing pipeline. Employing a Lambda architecture, it seamlessly integrates batch and streaming data processing.

Batch data ingestion occurs through Kafka deployed on an EC2 instance, facilitated by AWS API Gateway and AWS Managed Streaming for Apache Kafka (MSK). Subsequently, this data is stored in an AWS S3 bucket. For batch processing, data is retrieved from the S3 bucket into Databricks, where Apache Spark is utilized for processing.

Streaming data, on the other hand, is processed in near real-time by Spark Structured Streaming within Databricks, leveraging data from AWS Kinesis. The processed streaming data is then stored in Databricks Delta Tables for long-term retention.


The process involves:
- Data Emulation: This involves crafting a script to extract data from an RDS DB, simulating the process of data posting.
- Data Processing via Kafka: Utilizing Kafka for efficient data ingestion, ensuring smooth handling of incoming data streams.
- Storing Data in S3: Data is stored in an S3 bucket, ensuring seamless accessibility for potential analyses and usage scenarios.
- API Development with API Gateway: A custom API, integrated with API Gateway, is developed to streamline the flow of data into the Kafka cluster, subsequently storing it in the S3 bucket.
- Integration with Databricks: Connecting the S3 bucket to Databricks for comprehensive batch analysis of Pinterest data, enabling in-depth insights.
- Managed Workflows with Apache Airflow (MWAA): Employing MWAA to orchestrate intricate data workflows using Directed Acyclic Graphs (DAGs), automating and overseeing the data pipeline with efficiency.
- Real-Time Data Handling with Kinesis: Integrating AWS Kinesis Data Streams to enhance the pipeline's capabilities for real-time data management, ensuring agility in processing live data feeds.

## Installation
In order to view  the project on your local machine, run this command in an appropriate directory:

   ``` bash
   git clone https://github.com/hameed0380/pinterest-data-pipeline409.git
   cd pinterest-data-pipeline409
   ```


## Usage
- `user_posting_emulation.py`: script that extracts pinterest data from MySQL database and uploads it to S3 bucket using API Gateway that goes through an MSK cluster on EC2 instance.
- `user_posting_emulation_streaming.py`: script that streams real-time data to AWS Kinesis.
- `pinterest_data`: contains data about posts being updated to Pinterest.
- `geolocation_data`: contains data about the geolocation of each Pinterest post found in `pinterest_data`.
- `user_data`: contains data about the user that has uploaded each post found in `pinterest_data`.
- `0e284c63dbbf_dag.py`: A Dag file which runs the data_cleaning notebook file on databricks daily.
- `Streaming_from_kinesis.ipynb`: script to read real-time kinesis data, cleans the data and saves in delta table on databricks.
- `Mount the S3 bucket to Databricks 2024-02-21 16_03_34.ipynb`: script to run on databricks to mount the S3 bucket onto databricks.
- `clean_dataframe.ipynb`: script which reads JSON files from mounted S3 bucket and stores the contents as dataframes and performs cleaning process.

## File Structure
    .
    ├── Databricks-Notebooks
    │   ├── Mount the S3 bucket to Databricks 2024-02-21 16_03_34.ipynb
    │   ├── Streaming_from_kinesis.ipynb
    │   └── clean_dataframe.ipynb
    ├── Images
    │   └── CloudPinterestPipeline.png
    ├── README.md
    ├── dag
    │   └── 0e284c63dbbf_dag.py
    ├── user_posting_emulation.py
    └── user_posting_emulation_streaming.py
