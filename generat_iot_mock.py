from __future__ import print_function

import boto3
import random as rd
import numpy as np
import time
import json


iot = boto3.client('iot-data',region_name='us-west-2')
dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
fleet_table = dynamodb.Table('Fleet-Details')
#response = fleet_table.scan()
fleets = []
#for item in response['Items']:
#    fleets.append(item['serial-number'])
#print(fleets)
fleets.append("FL200")
fleets.append("FL100")
initial_mileage_vals = {"FL200" : 49500, "FL100": 27600}
iot_data = {}
for fleet in fleets:
    print("calculating values for fleet: ",fleet)
    ini_mil = initial_mileage_vals[fleet]
    print("initial mileage of fleet is: ", ini_mil)
    mile_array = []
    for num in range(0,359):
        current_mil = ini_mil +  (float(rd.randint(35,65))/360.0)
        ini_mil = current_mil
        mile_array.append(current_mil)
    terrain_array = np.random.choice([1,2,3,4,5],360,True,[0.85,0.1,0.04,0.008,0.002])
    iot_vals = {"mil_data" : mile_array,"ter_data": terrain_array}
    iot_data[fleet] = iot_vals

for i in range(0,359):
    for fleet in fleets:
        iot_event = {"fleet" : fleet, "mileage": iot_data[fleet]['mil_data'][i], "terrain": iot_data[fleet]["ter_data"][i]}
        print(iot_event)
        response = iot.publish(topic='/fleet/device/data',payload=json.dumps(iot_event))
    time.sleep(5)
