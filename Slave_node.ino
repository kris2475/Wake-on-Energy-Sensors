// Slave XBee (ATMega4808 / End Device)

// Development

#include <Arduino.h>

void setup() {
  Serial1.begin(9600);  // XBee connected to Serial1
  Serial.begin(9600);   // Optional: Debugging on Serial USB
}

void loop() {
  // Simulate sensor reading
  int sensorValue = analogRead(A0);  

  // Send value to Coordinator
  Serial1.print("Sensor: ");
  Serial1.println(sensorValue);

  // Optional: Debug print
  Serial.print("Sent to Coordinator: ");
  Serial.println(sensorValue);

  delay(2000);  // Send every 2 seconds
}
