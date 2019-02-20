# source: https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub.py
import paho.mqtt.client as mqtt
import json
import sqlite3

conn = sqlite3.connect('ip_mqtt_sensor.db')
sqlc = conn.cursor()
sqlc.execute('''CREATE TABLE sensor
             (timestamp text, temp_avg real, boardid text)''')
conn.commit()

def save_to_db(conn, sqlc, data_tuple):
    sqlc.execute('INSERT INTO sensor VALUES (?, ?, ?)', data_tuple)
    conn.commit()

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    data = json.loads(str(msg.payload.decode("utf-8","ignore")))
    data_tuple = (data["timestamp"], data["temp_avg"], data["boardid"])
    save_to_db(conn, sqlc, data_tuple)

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.tls_set("./ca.crt")
mqttc.tls_insecure_set(True)
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