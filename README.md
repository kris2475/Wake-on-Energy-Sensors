# Energy-as-a-Sensor IoT with On-Demand Wake-Up 🌱

## 🌟 Introduction

Swansea is building a Net Zero future, targeting clean air, energy-efficient buildings, and sustainable infrastructure. Achieving these goals requires **dense, real-time environmental data**, without the cost and maintenance burden of conventional sensor networks.

This project demonstrates a **battery-free IoT system** where energy harvested from light (OPV) and heat (TEG) becomes the sensor itself. Nodes remain in **ultra-low-power sleep**, optionally performing local sensing (e.g., PIR, RTC), but **transmitting data only when explicitly woken by the hub** via the Radio Controli 868 MHz wake-up module.  

**On-demand wake-up offers multiple advantages:**  
- **Reliability:** Only selected nodes transmit at a time, avoiding congestion and collisions that occur with hundreds of nodes transmitting simultaneously.  
- **Security:** Nodes are silent by default, reducing unauthorized transmissions and eavesdropping risks.  
- **Energy efficiency:** Nodes spend almost all their time in ultra-low-power sleep, transmitting only when their data is needed, enabling battery-free operation.

Each node monitors its energy buffer: voltage and current fluctuations encode environmental information such as room temperature changes, occupancy patterns, or heat loss. Advanced **ML/DL models and Bayesian optimisation** on the hub guide intelligent, on-demand wake-ups, prioritising nodes that will provide the most informative data.

Imagine a city where buildings, streets, and public spaces report their own energy use, heat efficiency, and air quality, all without wires, batteries, or constant maintenance. This system is scalable, sustainable, and intelligent, offering **hyperlocal insights** that enable Swansea to make **data-driven Net Zero decisions**—from retrofitting inefficient homes to optimizing public infrastructure.

**In short:** Energy powers the sensor, and advanced intelligence decides **when and which nodes communicate**, unlocking smarter, greener, and more reliable urban environments.

---

## 💪 Why I’m the Right Person to Make This Happen  

I combine **electronics engineering expertise** with formal training in **Machine Learning and Artificial Intelligence (Professional Certificate, Imperial College London)**, giving me the skills to deliver intelligent, energy-aware IoT systems:

- Designed and implemented **low-power, energy-harvesting sensor networks**.  
- Applied **ML/DL and Bayesian optimisation** to guide **hub-controlled wake-ups**, minimizing transmissions while maximizing information.  
- Experienced with **Radio Controli Wake-Up modules, TEGs, and OPVs**, enabling rapid prototyping of battery-free nodes.  
- Skilled in **HCI and data visualization**, turning environmental signals into actionable insights.  
- Vision for **scaling from single-node POC to hundreds of nodes**, aligned with Swansea’s Net Zero goals.

---

## 🌟 How It Works

1. **Energy Harvesting & Sensing:**  
   - Node collects ambient heat (TEG) and light (OPV).  
   - Optional environmental sensors (BME680) or local triggers (PIR, RTC) can sample locally.  
   - Energy buffer voltage/current fluctuations can themselves act as **passive sensor signals**.

2. **Hub-Controlled Wake-Up & Radio Silence:**  
   - Nodes remain in **ultra-low-power sleep**, transmitting **only when explicitly woken** via the Radio Controli 868 MHz wake-up signal.  
   - This ensures **network reliability**, prevents congestion, and maintains **radio silence**.  
   - Only selected nodes transmit, avoiding collisions even in dense deployments.

3. **Intelligent Node Selection:**  
   - Hub uses **ML/DL and Bayesian optimisation** to evaluate uncertainty or information gain across all nodes.  
   - Nodes with **highest expected value** are woken to transmit.  
   - This reduces energy use and maximizes the quality of collected data.

4. **Data Collection & Visualization:**  
   - Hub collects energy-as-sensor readings (and optional environmental data).  
   - Data can reveal **heat inefficiencies, air quality trends, or occupancy patterns**, while preserving energy and minimizing transmissions.

---

## 🏗️ Hardware Overview

**Node (End Device)**  
- ATmega4808 MCU  
- BME680 sensor (temperature, humidity, gas)  
- **Energy harvesters:** Prometeus TEG + Epishine OPV → supercapacitor buffer  
- **Radio Controli Wake-Up Module (868 MHz)** for ultra-low-power, hub-controlled operation  
- XBee S2C End Device (optional, for multi-node mesh forwarding)

**Hub (Coordinator)**  
- XBee S2C Coordinator via USB → PC or Raspberry Pi  
- Python hub script for **ML/DL inference, Bayesian optimisation, and selective wake-up**

---

## 🔄 Conceptual Workflow
