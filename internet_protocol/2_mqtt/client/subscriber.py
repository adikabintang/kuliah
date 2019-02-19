# source: https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub.py
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.tls_set("./ca.crt")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log
mqttc.connect("localhost", 8883, 60)
#mqttc.subscribe("#", 0)
mqttc.subscribe("test/topic", 0)

mqttc.loop_forever()