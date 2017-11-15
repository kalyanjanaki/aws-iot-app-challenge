# Description Of the Function

This is the [Lambda Function](https://aws.amazon.com/lambda/) that is triggered by [Kinesis Analytics](https://aws.amazon.com/kinesis/analytics/)
application. The Kinesis Analytics application read the messages from Firehouse Stream and calls the lambda function to precorcess the record.

The incoming IOT message from Fleet contains the Base64 encoded image of terrain. The lambda function passes the images to
[AWS Rekognition](https://aws.amazon.com/rekognition/) and gets rank of terrain as good,average,bad.
