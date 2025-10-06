# XBee S2C Configuration Summary

## Table 1: Slave XBee (ATMega4808 / End Device) Settings
This module is configured as a Zigbee End Device with **Pin Hibernate (SM=1)**.  
The physical pin **Pin 9** **MUST** be tied to **VCC (3.3V)** to keep the module awake for continuous transmission.

| Parameter                 | Setting                 | Value (Example) | Key Purpose                                           |
|---------------------------|------------------------|----------------|------------------------------------------------------|
| Function Set              | ZIGBEE END DEVICE AT    |                | Defines the device as a standard network node.      |
| Coordinator Enable (CE)   | 0                      | End Device      | Confirms it is not the network creator.             |
| Sleep Mode (SM)           | 1                      | Pin Hibernate  | Activates Pin 9 control (tied HIGH to stay awake).  |
| PAN ID (ID)               | 1234                   | (Must match Coordinator) | Joins the correct wireless network.          |
| Destination Address Low (DL) | 1001               | (Must match Coordinator's MY) | Ensures all data is sent directly to the Coordinator. |
| Baud Rate (BD)            | 3                      | 9600 baud      | Matches the ATMega sketch's serial speed.          |
| API Enable (AP)           | 0                      | Transparent Mode | Treats the wireless link as a serial cable.       |

---

## Table 2: Master XBee (ESP32 / Coordinator) Settings
This module is configured as the Zigbee **Coordinator** and is set to **never sleep (SM=0)** to ensure continuous readiness for receiving messages and managing the network.

| Parameter                 | Setting                  | Value (Example) | Key Purpose                                           |
|---------------------------|-------------------------|----------------|------------------------------------------------------|
| Function Set              | ZIGBEE COORDINATOR AT    |                | Defines the device as the network creator and manager. |
| Coordinator Enable (CE)   | 1                       | Coordinator    | Explicitly sets the device as the Coordinator.      |
| Sleep Mode (SM)           | 0                       | No Sleep       | Ensures the module is permanently awake and listening. |
| PAN ID (ID)               | 1234                    | (Must match Slave/End Device) | Establishes the unique wireless network. |
| My Address (MY)           | 1001                    | (Example)      | This device's short address (used as the Slave's DL). |
| Destination Address Low (DL) | 1002                 | (Must match Slave's MY) | Ensures data sent from the Coordinator targets the Slave. |
| Baud Rate (BD)            | 3                       | 9600 baud      | Matches the ESP32 sketch's serial speed.          |
| API Enable (AP)           | 0                       | Transparent Mode | Treats the wireless link as a virtual serial connection. |
