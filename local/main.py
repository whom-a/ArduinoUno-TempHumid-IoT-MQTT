import serial
import time
import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client(client_id = "", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("Writer", "WriteWrite1")
client.connect("ea9819cacd5c4bf6a8c8c56167d3affe.s1.eu.hivemq.cloud", 8883)
time.sleep(2)
port = "COM3"
baud = 9600
unoSerial = serial.Serial(port, baud, timeout=1)
time.sleep(2);
i = 1

try:
    while True:
        time.sleep(0.49)
        if unoSerial.in_waiting > 0:
            temp = float(unoSerial.readline())
            humid = float(unoSerial.readline())
            try:
                client.publish("sensor/data", payload=("{"+f"\n\"temperature\" : {temp},\n\"humidity\" : {humid}\n"+"}"), qos=0)
            except Exception:
                client.connect("a7d10c4461e8473085b6d75573b34784.s1.eu.hivemq.cloud", 8883)
                time.sleep(2)

except KeyboardInterrupt:
    print("Demo over")
finally:
    unoSerial.close()
