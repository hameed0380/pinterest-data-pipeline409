# pinterest-data-pipeline409


## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Description](#description)
- [File Structure](#file-structure)
- [Installation](#installation)
- [License](#license)

## Project Overview
This is a end to end AWS-hosted data pipeline inspired by Pinterest's experiment processing pipeline. The pipeline is developed using a Lambda architecture. 

![Images](Images/CloudPinterestPipeline.png)

## Description
The process involves:
- Data Emulation: This involves crafting a script to extract data from an RDS DB, simulating the process of data posting.
- Data Processing via Kafka: Utilizing Kafka for efficient data ingestion, ensuring smooth handling of incoming data streams.
- Storing Data in S3: Data is stored in an S3 bucket, ensuring seamless accessibility for potential analyses and usage scenarios.
- API Development with API Gateway: A custom API, integrated with API Gateway, is developed to streamline the flow of data into the Kafka cluster, subsequently storing it in the S3 bucket.
- Integration with Databricks: Connecting the S3 bucket to Databricks for comprehensive batch analysis of Pinterest data, enabling in-depth insights.
- Managed Workflows with Apache Airflow (MWAA): Employing MWAA to orchestrate intricate data workflows using Directed Acyclic Graphs (DAGs), automating and overseeing the data pipeline with efficiency.
- Real-Time Data Handling with Kinesis: Integrating AWS Kinesis Data Streams to enhance the pipeline's capabilities for real-time data management, ensuring agility in processing live data feeds.


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



## Installation
In order to view  the project on your local machine, run this command in an appropriate directory:

   ``` bash
   git clone https://github.com/hameed0380/pinterest-data-pipeline409.git
   cd pinterest-data-pipeline409
   ```
