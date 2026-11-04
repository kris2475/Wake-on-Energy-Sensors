# Wireless Counter: ATmega4808 & XBee S2C (Transparent Mode)

This repository contains the Arduino code and hardware configuration details for establishing a transparent point-to-multipoint/broadcast wireless link between a custom ATmega4808 PCB and an XBee S2C Coordinator connected to a PC (XCTU / Serial Monitor).

## System Architecture


| Component / Interface | Destination | Physical Connection / Protocol | Role |
| :--- | :--- | :--- | :--- |
| **ATmega4808 (`Serial0`)** | PC / Host System | USB Bridge | Local serial output for debugging (Tera Term) |
| **ATmega4808 (`Serial2`)** | XBee End Device | PCB Traces (`PF0` / `PF1`) | Hardware serial interface to local radio |
| **XBee End Device** | XBee Coordinator | Wireless (802.15.4 RF) | Transmits serial packets over RF link |
| **XBee Coordinator** | PC / Host System | USB Adapter | Receives RF stream and forwards data to XCTU Serial Monitor |



* **Local Debugging:** `Serial` outputs telemetry directly to Tera Term over USB.
* **Wireless Data Link:** `Serial2` (mapped to pins `PF0` / `PF1`) streams data into the local End Device XBee.

## XBee Hardware Configurations (XCTU)

### 1. End Device (Mounted on ATmega4808 PCB)

| Parameter | Setting | Description |
| ----- | ----- | ----- |
| **CH** Channel | `C` | Operating RF Channel |
| **ID** PAN ID | `1234` | Network ID Matching Coordinator |
| **DH** Destination Address High | `0` | Broadcast / Coordinator Target |
| **DL** Destination Address Low | `FFFF` | Broadcast Mode |
| **CE** Coordinator Enable | `End Device [0]` | Configures module as End Device |
| **BD** Interface Data Rate | `9600 [3]` | UART Baud Rate matching ATmega4808 |
| **NB** Parity | `No Parity [0]` | Standard 8N1 Framing |
| **RO** Packetization Timeout | `0` | Prevents leading character truncation by transmitting instantly on character input |
| **AP** API Enable | `API disabled [0]` | Transparent Pass-Through Mode |

### 2. Coordinator (Connected to PC / XCTU)

| Parameter | Setting | Description |
| ----- | ----- | ----- |
| **CH** Channel | `C` | Operating RF Channel |
| **ID** PAN ID | `1234` | Network ID Matching End Device |
| **DH** Destination Address High | `0` | Default Target |
| **DL** Destination Address Low | `FFFF` | Broadcast Target |
| **CE** Coordinator Enable | `Coordinator [1]` | Configures module as Central Network Coordinator |
| **BD** Interface Data Rate | `9600 [3]` | UART Baud Rate matching XCTU Console |
| **NB** Parity | `No Parity [0]` | Standard 8N1 Framing |
| **RO** Packetization Timeout | `3` | Standard character timeout window before flushing RF buffer to PC |
| **AP** API Enable | `API disabled [0]` | Transparent Pass-Through Mode |

## Arduino Firmware (`ATmega4808_XBeeS2C_Hello_World4.ino`)

Ensure you have MegaCoreX installed in your Arduino IDE settings when building for the ATmega4808 target.

```cpp
int count = 0;

void setup() {
  Serial.begin(9600);   // Primary serial port for Tera Term (USB debugging)
  Serial2.begin(9600);  // Secondary serial port wired to XBee DIN/DOUT
  Serial2.swap(0);      // Binds USART2 explicitly to Port F pins (PF0 = TX, PF1 = RX)
  delay(2000);          // Boot stabilisation window for XBee hardware reset
}

void loop() {
  // Construct data string payload
  String message = "XBee Direct Test: " + String(count);

  // 1. Local telemetry mirror via USB
  Serial.println(message);

  // 2. Wireless transmission via XBee
  Serial2.println(message);
  Serial2.flush(); // Ensure the hardware shift register empties completely before loop pause

  delay(1000);
  count++;
}
