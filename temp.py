from __future__ import print_function

# Below are list of imports
import boto3
import random as rd
import numpy as np
import time
import json

# Initiate the AWS IOT and AWS DynamoDb clinet
iot = boto3.client('iot-data',region_name='us-west-2')
dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
fleet_table = dynamodb.Table('Fleet-Details')

# Get the list of registered Fleets
response = fleet_table.scan()
fleets = {} 
for item in response['Items']:
    fleets[item['serial-number']] = item['initialMileage']
print(fleets)


