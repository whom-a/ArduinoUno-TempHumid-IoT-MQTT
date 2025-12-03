from flask import Flask
import json
import time
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
from paho import mqtt
app = Flask(__name__)
temprature = 0.0
humidity = 0.0
ran = 0
lastupdate = "never"
def turnin(humidity, temprature, lastupdate):
    return f"<h1>Current Temperature and Humidity at Sensor</h1><p>Temperature: {temprature}</p><p>Humidity: {humidity}%</p><p>Last Update: {lastupdate}</p>"

    
def on_message(client, userdata, msg):
    jsonny = msg.payload.decode()
    data = json.loads(jsonny)
    global temprature
    global humidity
    global ran
    global lastupdate
    humidity = data["humidity"]
    lastupdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    temprature = data["temperature"]
    ran = 1
    

@app.route('/')
def system_info():
    global ran
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("Reader", "ReadRead1")
    client.on_message = on_message
    client.connect("ea9819cacd5c4bf6a8c8c56167d3affe.s1.eu.hivemq.cloud", 8883)
    time.sleep(0.25)
    client.subscribe("#", qos=0)
    client.loop_start()
    hlep = 0
    while True:
        if ran==1:
            client.loop_stop()
            ran = 0
            return turnin(humidity, temprature, lastupdate)
        else:
            hlep +=1
            time.sleep(1)
            if hlep >= 5:
                return turnin(humidity, temprature, lastupdate)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
