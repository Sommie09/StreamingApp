provider "aws" {
  profile = "ChisomAWS"
  region  = "eu-north-1"
}

resource "aws_kinesis_stream" "raw_data_stream" {
  name             = "raw_data_stream"
  shard_count      = 1
  retention_period = 24
}

resource "aws_kinesis_stream" "aggregated_data_stream" {
  name             = "aggregated_data_stream"
  shard_count      = 1
  retention_period = 24
}

resource "aws_s3_bucket" "pageviews-data" {
  bucket = "pageviews-data"
}

resource "aws_glue_catalog_database" "page_views_db" {
  name = "page_views_db"
}
