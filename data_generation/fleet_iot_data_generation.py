from __future__ import print_function

# Below are list of imports
import boto3
import random as rd
import numpy as np
import time
import json
import data_generation_utils

# Initiate the AWS IOT and AWS DynamoDb clinet
iot = boto3.client('iot-data',region_name='us-west-2')
dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
fleet_table = dynamodb.Table('Fleet-Details')

# Get the list of registered Fleets
response = fleet_table.scan()
fleets = {} 
for item in response['Items']:
    fleets[item['serial-number']] = item['initialMileage']

## Initialize the Initial values
FL1502_distance=float(fleets['FL1502'])
FL1000_distance=float(fleets['FL1000'])
for iter in range(8):
    velocity=0
    temperature=70
    for i in range(720):
        velocity=data_generation_utils.get_velocity(i,velocity)
        temperature=data_generation_utils.get_temperature(i,temperature)
        FL1502_distance=data_generation_utils.get_distance(FL1502_distance,velocity)
        FL1000_distance=data_generation_utils.get_distance(FL1000_distance,velocity)
        iot_event_1={'FLEET' : 'FL1502', 'MILEAGE' : FL1502_distance, 'VELOCITY' : velocity, 'TEMPERATURE' : temperature, 'LOAD': 35000}
        iot_event_2={'FLEET' : 'FL1000', 'MILEAGE' : FL1000_distance, 'VELOCITY' : velocity, 'TEMPERATURE' : temperature, 'LOAD': 35000}
        print(iot_event_1)
        print(iot_event_2)
        response1 = iot.publish(topic='/fleet/device/data',payload=json.dumps(iot_event_1))
        response2 = iot.publish(topic='/fleet/device/data',payload=json.dumps(iot_event_2))
        time.sleep(5)
