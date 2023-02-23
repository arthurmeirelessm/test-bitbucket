import time as t
import json
import random
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

print('step 1')
ENDPOINT = "a31u4cydo52hqe-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "a1b23cd45e"
PATH_TO_CERT = "certificates/ac226756f66e71cd18a18edceeb13f7ea1b9d0f10da4d3ba89c2d86ed4579c40-certificate.pem.crt"
PATH_TO_KEY = "certificates/ac226756f66e71cd18a18edceeb13f7ea1b9d0f10da4d3ba89c2d86ed4579c40-private.pem.key"
PATH_TO_ROOT = "certificates/AmazonRootCA1.pem"
TOPIC = "client/iot/wearable"
RANGE = 10000

try:
    myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    myAWSIoTMQTTClient.connect()
    print('Begin Publish')
    devices_ids = ['111', '222', '333', '444', '555', '666', '777', '888', '999', '000']
    for i in range (RANGE):
        date = t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
        data = {}
        data["device_id"] = random.choice(devices_ids)
        data["temperature"] = random.uniform(20, 40)
        data["oxygen"] = random.uniform(10, 30)
        data["pression"] = random.uniform(10, 20)
        data["date"] = date

        myAWSIoTMQTTClient.publish(TOPIC, json.dumps(data), 1)
        print("Published: '" + json.dumps(data) + "' to the topic: " + "'client/testing'")
        t.sleep(0.1)
        print('Publish End')
    myAWSIoTMQTTClient.disconnect()

except Exception as e:
    print(e)

   