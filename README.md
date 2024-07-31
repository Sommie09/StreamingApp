<img width="990" alt="Screenshot 2024-07-31 at 12 14 19" src="https://github.com/user-attachments/assets/2887e69b-d951-43c2-9f85-0b7bffae8cc4"># Streaming App with Amazon Kinesis Data Analytics
This repository contains a real-time pipeline to ingest/receive data from a real-time stream of events and deploys a streaming application to aggregate some events in real time.

## Workflow 
The web application feeds event data to Kinesis Streams, the raw data is stored in an S3 bucket using Amazon Firehose, additionally, the aggregated data is stored in a sub folder on Amazon S3  (see diagram below)

![Copy of New Intro (2)](https://github.com/user-attachments/assets/354fad1b-fec8-4ce9-b49c-29d391afb979)

## Installation and Setup
1. Clone this repository.
2. Set up an AWS account and download your access and secret key from AWS IAM
3. Configure AWS CLI on your terminal using `aws configure`
4. Type in your credentials
5. Navigate to `IAC` in your terminal and type these commands `terraform init`, `terraform apply` to set up AWS infrastructure.

## Setting up streaming application

**Step 1:** Navigate to AWS Kinesis Data Streams, select `raw_data_stream` and click on `Process data in real-time`

<img width="1437" alt="Screenshot 2024-07-31 at 21 31 26" src="https://github.com/user-attachments/assets/18be809e-0311-43dc-8e90-7b357b6adc05">

**Step 2:** Create an Apache Flink - Studio Notebook

<img width="1142" alt="Screenshot 2024-07-31 at 11 24 24" src="https://github.com/user-attachments/assets/19a114e3-59c2-4de0-b679-c131a3e88598">

**Step 3:** Select a database (This was already been created on the Terraform)

<img width="989" alt="Screenshot 2024-07-31 at 11 24 31" src="https://github.com/user-attachments/assets/d9bd3607-1e61-4f15-ad5c-e439f3a90c14">

**Step 4:** Run the notebook and click `Open Apache Zeppelin`

<img width="1418" alt="Screenshot 2024-07-31 at 21 33 58" src="https://github.com/user-attachments/assets/df0c47c9-8b2b-4a23-bf13-0a594af384bb">

**Step 5:** On the notebook, run the `CREATE TABLE raw_data_table` on `sql_queries file` in the repo

**Step 6:** Run the `producer.py` file to produce data

<img width="1222" alt="Screenshot 2024-07-30 at 15 09 26" src="https://github.com/user-attachments/assets/74ddedfc-9aa1-425f-9386-c90a293d891d">

****Step 7:** Run the `Query to perform aggregations`  on `sql_queries file` in the repo

![WhatsApp Image 2024-07-30 at 17 02 00](https://github.com/user-attachments/assets/13f9e1ba-fde5-4bee-9658-deed8d4185cd)

**Step 8:** Run the `CREATE TABLE aggregated_data_table` and `INSERT INTO aggregated_data_table` on `sql_queries file`

**Step 9:** Create a firehose to connect to S3, specify the source and directory structure

<img width="990" alt="Screenshot 2024-07-31 at 12 14 19" src="https://github.com/user-attachments/assets/7037cc9d-3b35-478c-a148-d9e4e05edbca">

## Raw data in the S3 Bucket

<img width="1437" alt="Screenshot 2024-07-31 at 21 39 07" src="https://github.com/user-attachments/assets/caa88666-1a58-4389-bec4-e99ecbfcf700">

## Deploy the streaming application
<img width="1426" alt="Screenshot 2024-07-31 at 19 20 08" src="https://github.com/user-attachments/assets/4eee823a-bbe5-4547-8297-1c6ade59b10e">




