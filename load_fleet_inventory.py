from __future__ import print_function

import boto3
import random as rd
import numpy as np
import time
import json


iot = boto3.client('iot-data',region_name='us-west-2')
dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
fleet_table = dynamodb.Table('Fleet-Details')

with open("fleet_inventory", "r") as ins:
    for line in ins:
        data = line.split()
        mileage = { "FR" : data[5],"FL" : data[6],"ML1" : data[7],"ML2" : data[8],"MR1" : data[9],
                   "MR2" : data[10],"RL" : data[11],"RR" : data[12]}
        threadLength = {"FR" : data[13],"FL": data[14],"ML1": data[15],"ML2": data[16],"MR1": data[17],
                        "MR2": data[18],"RL": data[19],"RR": data[20]}
        fleet = {"serial-number" : data[0],"truck-type" : data[1]+" "+data[2],"customer" : data[3],"wheels": data[4],
                 "initialMileage": data[5],"mileage": mileage,"threadLength": threadLength}
        fleet_table.put_item(Item = fleet)
