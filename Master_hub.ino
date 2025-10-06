// Master XBee (ESP32 / Coordinator)

// Development

#include <Arduino.h>

void setup() {
  Serial.begin(9600);     // Debug/Monitor
  Serial2.begin(9600, SERIAL_8N1, 16, 17); // RX=16, TX=17 to XBee
}

void loop() {
  // Check if data received from Slave
  while (Serial2.available()) {
    String msg = Serial2.readStringUntil('\n');
    Serial.print("Received from Slave: ");
    Serial.println(msg);
  }

  // Optional: send a message to Slave
  // Serial2.println("Hello from Coordinator");

  delay(100);
}

