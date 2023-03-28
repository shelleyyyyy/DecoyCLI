

import paho.mqtt.client as mqtt
import time
import sys

def mqtt_stuff(c1, c2):
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("broker.emqx.io", 1883, 60)

    while True:
        client.publish(payload=c1, topic=c2)
        time.sleep(3)
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    # client.loop_forever()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <device> <topic>')
        sys.exit(1)

    c1 = sys.argv[1]
    c2 = sys.argv[2]
    mqtt_stuff(c1, c2)




mqtt_stuff()