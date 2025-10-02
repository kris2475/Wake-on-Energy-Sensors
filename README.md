# Energy-as-a-Sensor IoT with On-Demand Wake-Up 🌱

## 🌟 Introduction (Investor/Stakeholder Friendly)

Swansea is building a **Net Zero future**, targeting clean air, energy-efficient buildings, and sustainable infrastructure. Achieving these goals requires **dense, real-time environmental data**, without the cost and maintenance burden of conventional sensor networks.

This project demonstrates a **battery-free IoT system** where **energy harvested from light (OPV) and heat (TEG) becomes the sensor itself**. Nodes remain in **ultra-low-power sleep**, waking **only on demand via the Radio Controli 868 MHz wake-up module**, transmitting data when it is most valuable.

Each node monitors its energy buffer: **voltage and current fluctuations encode environmental information**, such as room temperature changes, occupancy patterns, or heat loss. Advanced **ML/DL models and Bayesian optimisation** on the hub guide **intelligent, on-demand wake-ups**, prioritising nodes that will provide the most informative data.

Imagine a city where **buildings, streets, and public spaces report their own energy use, heat efficiency, and air quality**, all without wires, batteries, or constant maintenance. This system is **scalable, sustainable, and intelligent**, offering hyperlocal insights that enable Swansea to make **data-driven Net Zero decisions**—from retrofitting inefficient homes to optimizing public infrastructure.

**In short:** Energy powers the sensor, and **advanced intelligence decides when the sensor communicates**, unlocking smarter, greener, and more responsive urban environments.

---

## 💪 Why I’m the Right Person to Make This Happen  

I bring a combination of **electronics engineering expertise** and formal training in **Machine Learning and Artificial Intelligence (Professional Certificate, Imperial College London)**. This background enables me to design **energy-aware, intelligent IoT systems** that can scale from a single node to hundreds:

- Designed and implemented **low-power, energy-harvesting sensor networks**.  
- Applied **ML/DL and Bayesian optimisation** to guide on-demand wake-ups based on uncertainty in environmental measurements.  
- Experienced with **Radio Controli Wake-Up modules, TEGs, and OPVs**, enabling rapid prototyping of self-powered nodes.  
- Skilled in **data visualization and HCI**, translating complex environmental signals into actionable insights.  
- Vision for **scaling a single-node POC into a mesh network**, aligned with Swansea’s Net Zero goals.

---

## 🌟 How It Works

1. **Harvesting Energy as a Sensor:**  
   - Node collects ambient heat via **TEG** and light via **OPV**.  
   - Energy flows into a buffer (supercapacitor), whose **voltage and current fluctuations encode environmental conditions**.

2. **On-Demand Wake-Up via Radio Controli:**  
   - Node stays in **ultra-low-power sleep** to preserve energy.  
   - The **Radio Controli 868 MHz module** listens continuously for wake-up signals.  
   - Hub triggers nodes only when data is needed or uncertainty is high.

3. **Intelligent Node Selection:**  
   - Hub uses **ML/DL models and Bayesian optimisation** to estimate uncertainty in environmental measurements.  
   - Nodes with the **highest expected information gain** are woken first.  
   - This approach allows hundreds of nodes to operate efficiently without unnecessary transmissions.

4. **Data Collection & Visualization:**  
   - Hub collects energy-as-sensor readings and optional environmental sensor data.  
   - Visualized data can reveal **heat inefficiencies, air quality trends, or occupancy patterns**, all while conserving energy.

---

## 🏗️ Hardware Overview

**Node (End Device)**  
- ATmega4808 MCU  
- BME680 sensor (temperature, humidity, gas)  
- **Energy harvesters:** Prometeus TEG + Epishine OPV → supercapacitor buffer  
- **Radio Controli Wake-Up Module (868 MHz)** for ultra-low-power, on-demand operation  
- XBee S2C End Device (optional, for mesh forwarding)

**Hub (Coordinator)**  
- XBee S2C Coordinator via USB → PC or Raspberry Pi  
- Python hub script for **on-demand wake-up, ML/DL inference, and Bayesian optimisation**

---

## 🔄 Workflow Diagram (Conceptual)
