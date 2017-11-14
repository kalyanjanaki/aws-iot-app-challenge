from __future__ import print_function

import base64
import boto3
import json

print('Loading function')

# Initialize the AWS rekognition Clinet
client = boto3.client('rekognition')

def lambda_handler(event, context):
    output = []
    
    for record in event['records']:
        payload = base64.b64decode(record['data'])
        payload = json.loads(payload)
        #Process Images Data to get the Road Terrain Condition
        image_data = str(payload['IMAGE'])
        print(payload['LOAD'])
        print(image_data)
        image_binary = base64.b64decode(image_data)
        terrain = 1
        try:
            response = client.detect_labels(
                Image={
                    'Bytes': image_binary
                })
            road_confidence = 0
            for label in response['Labels']:
                if(label['Name'] == 'Road'):
                    road_confidence = label['Confidence']
            if(road_confidence > 95.0):
                terrain = 1
            elif(road_confidence > 60.0 and road_confidence < 95.0):
                terrain = 2
            else:
                terrain = 3
        except:
            print("Error While Image Processing")
        
        #Format the Output payload
        processed_payload = {'FLEET' : payload['FLEET'], 'VELOCITY' : payload['VELOCITY'],
                    'MILEAGE' : payload['MILEAGE'], 'TEMPERATURE' : payload['TEMPERATURE'],
                    'LOAD': payload['LOAD'], 'TERRAIN' : terrain}
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(processed_payload))
        }
        
        output.append(output_record)
    return {'records': output}
