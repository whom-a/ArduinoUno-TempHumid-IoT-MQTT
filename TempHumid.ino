#include <dht.h>

dht DHT;

#define DHT11_PIN 7

void setup() {
  Serial.begin(9600);

}

void loop() {
  char buffer[64];
  float temp;
  float humid;
  int chk = DHT.read11(DHT11_PIN);
  Serial.println(DHT.temperature * 9/5 + 32);
  Serial.println(DHT.humidity);
  delay(500);

}
