# source: http://www.steves-internet-guide.com/mosquitto-tls/
import paho.mqtt.client as mqtt
import time

broker="localhost"
port=8883
conn_flag=False

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
c.on_connect = on_connect
c.on_disconnect = on_disconnect
c.connect(broker, port)
while not conn_flag:
    time.sleep(1)
    print("waiting ", conn_flag)
    c.loop()
print("publishing")
c.publish("test/topic", "eric johnson")
c.loop()
c.disconnect()