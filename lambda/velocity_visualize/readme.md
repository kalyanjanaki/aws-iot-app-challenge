# Description Of the Function

This is the [Lambda Function](https://aws.amazon.com/lambda/) that is triggered by [AWS IOT Rule Engine](http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html). It takes the velocity of the Fleet from IOT message and publishes the same to [Pubnub](https://www.pubnub.com/) Broker. The fleet-dasborad which is subscribed to same Pubnub broker displays the rea-time veiw to the Fleet velocity.

This Python 2.7 runtime lambda uses third-party libraries. So it is packaged as Zip File. Please use the entire zip file to deploy the lambda.
