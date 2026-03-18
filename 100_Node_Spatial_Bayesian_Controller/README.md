# Spatial Bayesian Wake-on-Energy Controller
### Adaptive Territorial Inference for UAV-Aided IoT Data Harvesting

[![Field Simulation](https://img.shields.io/badge/Simulation-High--Fi-green)](https://github.com/kris2475)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📡 The Concept: "Silence is a Signal"
In standard IoT, a non-responsive node is typically logged as a "timeout error." In a **Wake-on-Energy** system, however, silence is a vital spatial data point. This project demonstrates how a master node (such as a UAV Data Mule) can map a 100-node territorial grid using **Gaussian Process Regression (GPR)** to replace exhaustive, energy-intensive polling with mathematical inference.

Instead of pinging all 100 nodes, the controller uses an **RBF Kernel** to infer the energy state of entire neighbourhoods. By analysing just 9 pings, the system identifies "Hotspots" (active nodes) and "Dead Zones" (shaded or depleted nodes) with high statistical certainty.

---

## 🚁 Research Significance: UAV "Surgical Extraction"
As part of research into autonomous aerial data-harvesting, this framework addresses two mission-critical challenges:

1.  **Endurance & Efficiency:** By eliminating the "loiter time" usually wasted waiting for timeouts from energy-starved sensors, the UAV can navigate a "surgical" path exclusively to active nodes.
2.  **COMSEC (Communications Security):** Reducing 100 pings to a mere 9 drastically minimises the UAV’s RF footprint, ensuring mission discretion in sensitive or high-integrity operational zones.

---

## 🛠️ Technical Architecture

### 1. Environment Model (Multi-Cloud Suppression)
The simulation generates a 10x10 grid with uniform ambient illumination, interrupted by randomised **shading events** (clouds or physical obstacles).
* **High-Fi (+1.0):** The node has harvested sufficient energy to transmit.
* **Lo-Fi (-0.8):** The node is in shade; the harvested energy storage is below the wake-up threshold.

### 2. The Bayesian Controller
The system uses a **Gaussian Process Regressor** with specific "Surgical" tuning:
* **Kernel:** $C(1.0) \times RBF(length\_scale=2.0)$ — This balances territorial "green" coverage with sharp "red" boundaries around shaded zones.
* **Alpha ($\alpha = 1e-6$):** This forces the model to treat silence as an absolute fact (a no-go zone), preventing success signals from "bleeding" into dead zones.
* **Acquisition (UCB):** Uses an Upper Confidence Bound ($\mu + \beta\sigma$) with $\beta=4.0$ to aggressively scout "uncertain" white space.

---

## 📊 Performance Metrics
* **Communication Overhead:** ~9% (9 pings vs 100).
* **Energy Savings:** Projected >90% reduction in radio uptime for the UAV Master node.
* **Spatial Awareness:** Achieving territorial certainty across a 100-node grid in 9 iterations.

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy matplotlib scikit-learn

python grid_100_dynamic_bayesian_sim6.py
