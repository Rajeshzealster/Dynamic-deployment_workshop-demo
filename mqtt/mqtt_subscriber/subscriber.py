#import RPi.GPIO as GPIO
import os
import paho.mqtt.client as mqtt
import json
# MQTT broker settings
broker_address = os.getenv('BROKER_ADDRESS', '192.168.0.204')
broker_port = int(os.getenv('BROKER_PORT', '30001'))
topic_author = os.getenv('DATA_TOPIC_AUTHOR', '')
threshold_temp= float(os.getenv('Temperature_Threshold','30.0'))
threshold_humid= float(os.getenv('Humidity_Threshold', '70.0'))
#broker_address = "192.168.0.251"
#broker_port = 1883
data_topic = "sensor/"+topic_author+"/data" if topic_author else "sensor/data"
temp_topic = "sensor/"+topic_author+"/temperature" if topic_author else "sensor/temperature"
humid_topic = "sensor/"+topic_author+"/humidity" if topic_author else "sensor/humidity"

# MQTT client initialization
client = mqtt.Client()
client.connect(broker_address, broker_port)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Received payload: " + payload)
    data = json.loads(payload)
    temperature = data["temperature"]
    humidity = data["humidity"]
    
    if temperature > threshold_temp:
        client.publish(temp_topic, temperature)
        print("Published to " + temp_topic)
        
    if humidity > threshold_humid:
        client.publish(humid_topic, humidity)
        print("Published to " + humid_topic)

# subscribe to data topic
client.subscribe(data_topic)

# set up callback function for incoming messages
client.on_message = on_message

# start loop to listen for incoming messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Cleanup")
#    GPIO.cleanup()
