# Streaming App with Amazon Kinesis Data Analytics
This repository contains a real-time pipeline to ingest/receive data from a real-time stream of events and deploys a streaming application to aggregate some events in real time.

## Workflow 
The web application feeds event data to Kinesis Streams, the raw data is stored in an S3 bucket using Amazon Firehose, additionally, the aggregated data is stored in a sub folder on Amazon S3  (see diagram below)

![Copy of New Intro (2)](https://github.com/user-attachments/assets/4365a8cc-6d33-4cbe-91ac-85f613787e3a)

## Installation and Setup
1. Clone this repository.
2. Set up an AWS account and download your access and secret key from AWS IAM
3. Confugure AWS CLI on your terminal using `aws configure`
4. Type in your credentials
5. Navigate to `IAC` your terminal and type these commands `terraform init`, `terraform apply` to set up AWS infrastructure.

## Setting up streaming application

**Step 1:** Navigate to AWS Kinesis Data Streams, select `raw_data_stream` and click on `Process data in real time`

<img width="1074" alt="Screenshot 2024-07-31 at 11 21 23" src="https://github.com/user-attachments/assets/f1df9eaf-de35-4f41-b7b6-051add8ac7f4">

**Step 2:** Create an Apache Flink - Studio Notebook

<img width="1438" alt="Screenshot 2024-07-31 at 11 26 27" src="https://github.com/user-attachments/assets/56d02e53-a40c-444d-8f00-5da815baf6df">

**Step 3:** Type in a notebook name and select a database (This has already been created on the Terraform)

<img width="1440" alt="Screenshot 2024-07-31 at 11 27 08" src="https://github.com/user-attachments/assets/dc715f9a-ad18-402c-9d2c-11602c957ca2">

<img width="1440" alt="Screenshot 2024-07-31 at 11 27 25" src="https://github.com/user-attachments/assets/673598bf-6c6c-4abc-92a6-738d905a9bb3">

**Step 4:** Run the notebook and click `Open Apache Zeppelin`

<img width="1142" alt="Screenshot 2024-07-31 at 11 37 51" src="https://github.com/user-attachments/assets/2d27dc30-249b-411f-941f-8c3857d94619">

**Step 5:** Run the `CREATE TABLE raw_data_table` on `sql_queries file` in the repo

**Step 6:** Run the `producer.py` file to produce data

<img width="1400" alt="Screenshot 2024-07-31 at 12 01 28" src="https://github.com/user-attachments/assets/8fa9d7de-df43-4f28-8afd-571de9923c18">

****Step 7:** ** Run the `Query to perform aggregations`  on `sql_queries file` in the repo

<img width="1396" alt="Screenshot 2024-07-31 at 12 07 04" src="https://github.com/user-attachments/assets/c9497de7-3992-45c8-b2ed-bfee8cd7f178">

**Step 8:** Run the `CREATE TABLE aggregated_data_table` and `INSERT INTO aggregated_data_table` on `sql_queries file`

**Step 9:** Create a firehose to connect to S3, specify the source and directory structure

<img width="1397" alt="Screenshot 2024-07-31 at 12 14 34" src="https://github.com/user-attachments/assets/ac680a46-9639-4ce3-82d6-8828581c7eeb">

<img width="1402" alt="Screenshot 2024-07-31 at 12 15 09" src="https://github.com/user-attachments/assets/4ea7a085-5e0e-4fbb-ad5c-9339099f5c90">

## Raw data in the S3 Bucket
<img width="1440" alt="Screenshot 2024-07-31 at 12 30 45" src="https://github.com/user-attachments/assets/439ddcad-a29e-49b2-a5cf-c38adeb92b6e">





