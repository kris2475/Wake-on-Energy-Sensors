# Energy-as-a-Sensor IoT 🌱

A **battery-free IoT sensor** that uses the energy it harvests to sense its environment and only transmits data **on demand**. This proof-of-principle demonstrates how **buildings, rooms, and urban spaces can self-report** while minimizing energy use, advancing Net Zero goals.

---

## 🌟 Key Features

- **Energy-as-a-Sensor:** The harvested energy itself provides insight into environmental conditions (heat, light, occupancy).  
- **On-Demand IoT:** Nodes sleep by default and only transmit when the hub requests data, maximizing efficiency.  
- **Self-Powered & Sustainable:** No batteries required; nodes are powered entirely by TEG (heat) and OPV (light).  
- **Scalable:** Single-node POC can grow into a mesh network with selected routers for city- or building-scale deployments.  
- **Net Zero Alignment:** Ideal for monitoring building efficiency, air quality, or human activity with minimal energy footprint.

---

## 🏗️ Hardware Overview

**Node (End Device)**  
- ATmega4808 MCU  
- BME680 sensor (temperature, humidity, gas)  
- Prometeus TEG + Epishine OPV → supercapacitor buffer  
- XBee S2C End Device (sleeping mode)

**Hub (Coordinator)**  
- XBee S2C Coordinator via USB → PC or Raspberry Pi  
- Python hub script for **on-demand wake-up**, data logging, and visualization

---

## 🔄 Workflow

1. Node continuously harvests energy, monitoring buffer voltage/current.  
2. Node remains in **deep sleep** until the hub sends a **wake-up request**.  
3. Node wakes and transmits **energy-as-a-sensor data** along with optional sensor readings.  
4. Hub logs data and optionally visualizes energy trends and environment patterns.  
5. Node returns to deep sleep until next request.
