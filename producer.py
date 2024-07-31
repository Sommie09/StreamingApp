import boto3
import json
import time
import random
import datetime

#Kinesis stream name
STREAM_NAME = "raw_data_stream"

#Function to generate random data
def generate_pageview():
    pageview = {
        'user_id': random.randint(1000, 9999),
        "postcode": random.choice(['SW1', 'SW2', 'SW3', 'SW4', 'NW1', 'NW2', 'NW3', 'NW4']),
        "webpage": random.choice(["https://netflix.com/"]),
        'timestamp': int(time.time())
    }
    return pageview

#Function to send data into the kinesis stream
def send_data(stream_name, kinesis_client):
    while True:
        try: 
            pageview = generate_pageview()
            print("pushing to kinesis ===", json.dumps(pageview))
            kinesis_client.put_record(
                StreamName=stream_name,
                Data=json.dumps(pageview),
                PartitionKey=str(pageview['user_id'])
            )
            time.sleep(1)
        except Exception as e:
            print(f"Error sending data: {e}")


if __name__ == '__main__':
    kinesis_client = boto3.client('kinesis',
                    region_name='eu-north-1',
                    aws_access_key_id='****',
                    aws_secret_access_key='****')
    
    send_data(STREAM_NAME, kinesis_client)









