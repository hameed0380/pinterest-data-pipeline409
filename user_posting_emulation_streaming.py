import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
from datetime import datetime
import uuid


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()

def convert_datetime(data):
    # Get the key and value of the dictionary in data
    for key, value in data.items():
        # When it is an instance of datetime convert values to isoformat
        if isinstance(value, datetime):
            data[key] = value.isoformat()
    return data

def send_to_kinesis(data, stream_name):
            invoke_url = f"https://243jgiou7i.execute-api.us-east-1.amazonaws.com/test_deployment/streams/{stream_name}/record"
            #To send JSON messages you need to follow this structure

            data  = convert_datetime(data)

            payload = json.dumps({
                "StreamName": stream_name,
                "Data": data,
                "PartitionKey": str(uuid.uuid4())
            })

            headers = {'Content-Type': 'application/json'}
            response = requests.request("PUT", invoke_url, headers=headers, data=payload)
            print(response.json())
            print(response.status_code)
            return response

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            # print(pin_result)
            # print(geo_result)
            # print(user_result)


            send_to_kinesis(user_result, "streaming-0e284c63dbbf-pin")
            send_to_kinesis(geo_result, "streaming-0e284c63dbbf-geo")
            send_to_kinesis(pin_result, "streaming-0e284c63dbbf-user")

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


