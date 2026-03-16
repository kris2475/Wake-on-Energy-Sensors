# Energy-as-a-Sensor IoT with On-Demand Wake-Up 🌱

## 🌟 Introduction

Swansea is building a Net Zero future, targeting clean air, energy-efficient buildings, and sustainable infrastructure. Achieving these goals requires **dense, real-time environmental data**, without the cost and maintenance burden of conventional sensor networks.  

This project demonstrates a **novel battery-free IoT system** where **energy harvested from the environment not only powers the nodes but also acts as a sensor itself**. Nodes remain in **ultra-low-power sleep**, optionally sampling locally, and **transmit data only when explicitly woken by the hub** via the Radio Controlii 868 MHz wake-up module.  

**What makes this approach unique:**  
- **Energy-as-a-sensor:** A node’s ability to respond (or fail to respond) provides environmental insight even before any sensor data is transmitted.  
- **Hub-controlled, on-demand wake-up:** Only the most informative nodes are woken, avoiding collisions, congestion, and wasted energy.  
- **Intelligent selection via ML/DL + Bayesian optimisation:** The hub maximises information gain while keeping the network silent and efficient.  
- **Battery-free, high-resolution sensing:** BME680 or optional sensors deliver rich environmental data only when needed.  
- **Deadness as signal:** Non-responsive nodes still convey meaningful environmental information — a subtle, powerful feature not exploited in conventional IoT networks.  

Imagine a city where buildings, streets, and public spaces report their own energy use, heat efficiency, and air quality, **without wires, batteries, or constant maintenance**, and with an intelligent system that **decides when and which nodes should speak**. This approach is **scalable, sustainable, and novel**, unlocking hyperlocal insights for **data-driven Net Zero decisions** in Swansea.  

---

## 🌟 How It Works

1. **Energy Harvesting & Sensing:**  
   - Nodes harvest energy from **light, heat, and human activity**.  
   - High-resolution measurements come from a **BME680 sensor** (temperature, humidity, air quality, gas) or other optional low-power sensors.  
   - Nodes remain in ultra-low-power sleep, waking only on hub request.  
   - The node’s **ability to respond** itself provides a **low-resolution environmental signal**.

2. **Hub-Controlled Wake-Up & Radio Silence:**  
   - The hub sends a **Radio Controlii 868 MHz wake-up signal** to selected nodes.  
   - Nodes transmit data **only when explicitly woken**, maintaining **radio silence** by default and preventing congestion.  
   - This architecture ensures **reliability and security** even in dense deployments.

3. **Energy-as-a-Sensor (Node State as Information):**  
   - A node’s response conveys information about local conditions:  
     - **Node responds:** sufficient energy harvested → high-resolution sensor data available.  
     - **Node fails to respond:** insufficient energy → hub deduces environmental conditions or low activity.  
   - Every node, whether transmitting or silent, contributes **informative insight** to the hub.

4. **Intelligent Node Selection:**  
   - The hub uses **ML/DL models and Bayesian optimisation** to select which nodes to wake based on **uncertainty and expected information gain**.  
   - This ensures the **most informative nodes are queried**, maximising value while minimising energy use and transmissions.

5. **Data Collection & Visualization:**  
   - High-resolution sensor data is logged and visualized to reveal **heat inefficiencies, air quality trends, occupancy patterns**, or other environmental insights.  
   - Low-resolution signals from node state complement this, providing a **multi-layered understanding** of environmental conditions.

---

## 🏗️ Hardware Overview

**Nodes (Slaves)**  
- ATmega4808 MCU  
- BME680 sensor (temperature, atm. pressure, humidity, total VOC)  
- **Energy harvesters:** Prometeus TEG + Epishine OPV + VP3-20/30/50/60 XIDAS Vibration Perpetual Power Pod → supercapacitor buffer  
- **Radio Controlii Wake-Up Module (915 MHz)** for ultra-low-power, hub-controlled operation  
- XBee S2C End Device

**Routers (Overseers)**
- ATmega4808 MCU  
- XBee S2C Router (for multi-node mesh forwarding)
  
**Hub (Master)**  
- XBee S2C Coordinator via USB → PC or Raspberry Pi  
- Python hub script for **ML/DL inference, Bayesian optimisation, and selective wake-up**

---

## 🔄 Conceptual Workflow

- Slave nodes (hundreds of them) are energy-harvesting, and only transmit when woken.
- Overseers (a few, strategically located) maintain mesh connectivity, enabling reliable on-demand communication.
- Master (a single hub) selects which node(s) to wake using ML/DL + Bayesian optimisation, learning from both node responses and "deadness".

Energy Harvest → Node Buffer → Local Sampling (optional)
↓
Ultra-Low-Power Sleep → No transmissions
↓
Radio Controli Wake-Up Signal from Hub
↓
Node response:
- If awake → Transmit high-res sensor data
- If silent → Hub infers low-res environmental info
↓
Hub evaluates ML/DL + Bayesian uncertainty → selects next nodes
↓
Hub logs & visualizes data
↓
Node returns to sleep

 DOI: 10.5281/zenodo.17266888
