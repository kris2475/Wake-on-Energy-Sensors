# Energy-as-a-Sensor IoT with On-Demand Wake-Up 

## Introduction

Swansea is building a Net Zero future, targeting clean air, energy-efficient buildings and sustainable infrastructure. Achieving these ambitions requires dense, real-time environmental intelligence without the energy consumption, installation costs and maintenance burden of conventional sensor networks.

Wake-on-Energy introduces a battery-free IoT architecture in which harvested energy serves two purposes: powering distributed sensor nodes and providing an implicit source of information about their surrounding environment. Crucially, this includes energy arising as a physical consequence of human activity. Waste heat from televisions, computers and household appliances, energy from lighting, and mechanical energy from movement can all provide opportunities for local energy harvesting. The availability and accumulation of this energy can therefore reveal patterns of environmental activity before conventional sensor measurements are requested.

The network exploits this relationship through energy-informed, Bayesian-controlled sensing. Nodes operate in ultra-low-power states and communicate only when explicitly interrogated by a central hub via the Radio Controlii 868 MHz wake-up module, subject to their available energy and operating state. 

**Rather than polling every node, the hub uses Bayesian inference and information-gain optimisation to prioritise those expected to provide the most useful additional information.** 

Node availability and non-response are also treated as observations, interpreted in the context of energy history and network uncertainty.

The central contribution is the integration of energy harvesting as both a power source and an implicit information channel with intelligent, selective sensing. Rather than simply collecting environmental data, Wake-on-Energy uses the energy consequences of activity to inform what the network should measure next, potentially reducing unnecessary sensing, communication and maintenance while enabling more efficient environmental monitoring and building-energy management.

The longer-term ambition is to support distributed, self-sustaining environmental intelligence for Swansea's Net Zero infrastructure, including air-quality monitoring, building utilisation and adaptive heating.

---

## How It Works

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

5. **Data Collection & Visualisation:**  
   - High-resolution sensor data is logged and visualized to reveal **heat inefficiencies, air quality trends, occupancy patterns**, or other environmental insights.  
   - Low-resolution signals from node state complement this, providing a **multi-layered understanding** of environmental conditions.

---

## Hardware Overview

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

## Conceptual Workflow

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
Hub logs & visualises data
↓
Node returns to sleep

 DOI: 10.5281/zenodo.17266888
