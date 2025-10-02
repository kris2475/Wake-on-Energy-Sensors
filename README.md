# Energy-as-a-Sensor IoT with On-Demand Wake-Up 🌱

## 🌟 Introduction (Investor/Stakeholder Friendly)

Swansea is building a **Net Zero future**, with ambitious targets for clean air, energy-efficient buildings, and sustainable infrastructure. Yet achieving these goals requires **dense, real-time environmental data**, without adding maintenance overhead or battery waste.

This project demonstrates a **battery-free IoT system** where the **energy harvested from light and heat becomes the sensor itself**. Nodes remain in **ultra-low-power sleep**, waking **only on demand via the Radio Controli 868 MHz module**, transmitting data when it is most valuable.

Imagine a city where **buildings, streets, and public spaces can report their own energy use, heat efficiency, and air quality**, all without wires, batteries, or constant maintenance. This system is **scalable, sustainable, and intelligent**, offering hyperlocal insights that enable Swansea to make **data-driven decisions** toward its Net Zero vision — from retrofitting inefficient homes to optimizing public infrastructure.

**In short:** Energy powers the sensor, and the sensor talks only when needed — unlocking smarter, greener, and more responsive urban environments.

---

## 💪 Why I’m the Right Person to Make This Happen  

I combine **electronics engineering expertise** with hands-on experience in **IoT, HCI, and ML/DL**, the exact skill set needed to execute this vision:

- Designed and implemented **low-power sensor networks** and embedded systems.  
- Developed **smart, on-demand sensing strategies** using ML and Bayesian optimisation.  
- Skilled in **data visualization and HCI**, turning complex environmental signals into actionable insights.  
- Experienced with **Radio Controli Wake-Up modules, TEGs, and OPVs**, enabling rapid prototyping and deployment.  
- Vision for **scaling from single-node POC to hundreds of self-powered nodes** across Swansea, fully aligned with Net Zero goals.

---

## 🌟 Key Features

- **Energy-as-a-Sensor:** Harvested energy from light and heat encodes environmental information.  
- **On-Demand IoT:** Nodes remain asleep and wake only via **Radio Controli 868 MHz signals** when data is needed.  
- **Self-Powered & Sustainable:** No batteries; powered entirely by harvested energy.  
- **Scalable Architecture:** Single-node POC can expand into a mesh network with selected routers.  
- **Net Zero Alignment:** Monitors building efficiency, air quality, or human activity with minimal energy footprint.

---

## 🏗️ Hardware Overview

**Node (End Device)**  
- ATmega4808 MCU  
- BME680 sensor (temperature, humidity, gas)  
- Prometeus TEG + Epishine OPV → supercapacitor buffer  
- **Radio Controli Wake-Up Module (868 MHz)** for ultra-low-power sleep and on-demand wake-up  
- XBee S2C End Device (optional, for mesh communication)

**Hub (Coordinator)**  
- XBee S2C Coordinator via USB → PC or Raspberry Pi  
- Python hub script for **on-demand wake-up**, data logging, and visualization  

---

## 🔄 Workflow

1. Node harvests energy continuously from light and heat.  
2. Node remains in **ultra-low-power sleep** using the Radio Controli module.  
3. Hub sends **wake-up signal (868 MHz)** to the node when data is required.  
4. Node wakes and transmits **energy-as-a-sensor data** plus optional environmental sensor readings.  
5. Hub logs and visualizes data. Node returns to sleep until next request.  

---

## 💡 Demonstration Ideas

- Plot **buffer voltage over time** to visualize harvested energy trends.  
- Show **on-demand wake-ups triggered via Radio Controli**, highlighting energy-efficient operation.  
- Compare energy data with BME680 readings to demonstrate **energy-as-a-sensor correlation**.  

---
