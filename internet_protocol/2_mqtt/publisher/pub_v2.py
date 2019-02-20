# https://stackoverflow.com/questions/26745519/converting-dictionary-to-json-in-python
import csv
import time
import paho.mqtt.client as mqtt
import json

broker="mosquitto"
port=8883
conn_flag=False
time.sleep(3)

def on_connect(client, userdata, flags, rc):
    global conn_flag
    conn_flag=True
    print("connected ", conn_flag)

def on_log(client, userdata, level, buf):
    print("buffer ", buf)

def on_disconnect(client, userdata, rc):
    print("disconnected")

c = mqtt.Client()
c.on_log = on_log
c.tls_set("./ca.crt")
c.tls_insecure_set(True)
c.on_connect = on_connect
c.on_disconnect = on_disconnect
c.connect(broker, port)

while not conn_flag:
    time.sleep(1)
    print("waiting ", conn_flag)
    c.loop()

print("publishing")

column_name = ["timestamp", "temp_avg", "boardid"]

with open('data.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        d = dict((c_name, row[c_name]) for c_name in column_name if c_name in row)
        print(d)
        print(json.dumps(d))
        c.publish("test/topic", json.dumps(d))
        c.loop()
        time.sleep(2)

csvFile.close()
c.disconnect()