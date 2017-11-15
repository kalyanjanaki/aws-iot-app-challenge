# Description of the Function
This is the [Lambda Function](https://aws.amazon.com/lambda/) that is triggered by Kinesis Stream. The tire wear analysis  that is done in
the kinesis analytics application using input events from IOT and enriched events with in application is published to kinesis stream. The Kinesis stream triggers the LAmbda Function.

This function updates the Dynamo-Db table with latest Mileage of the Fleet and Expected Tire wear. It also publishes the Tire wear to real-time Dashboard.
