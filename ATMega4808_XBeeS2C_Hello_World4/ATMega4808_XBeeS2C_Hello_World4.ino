int count = 0;

void setup() {
  Serial.begin(9600);   // Primary serial port for Tera Term (USB)
  Serial2.begin(9600);  // Secondary serial port for XBee
  Serial2.swap(0);      // Binds USART2 to Port F pins (PF0/PF1)
  delay(2000);          // Stable boot window for the XBee radio
}

void loop() {
  // Create the string payload once
  String message = "XBee Direct Test: " + String(count);

  // 1. Mirror locally to Tera Term via USB
  Serial.println(message);

  // 2. Transmit wirelessly via XBee
  Serial2.println(message);
  Serial2.flush(); // Ensure the hardware shift register empties completely

  delay(1000);
  count++;
}