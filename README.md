# 🛡️ NIDS: AI-Powered Network Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?logo=streamlit)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)](https://xgboost.ai/)


An enterprise-grade Cybersecurity dashboard that uses Machine Learning to detect network anomalies (Dos, R2L, U2R, Probing) in real-time. Built with **XGBoost** and **Streamlit**.

---

## 🌟 Key Features
- **Live Stream Simulator**: Real-time visualization of network traffic and anomaly probability.
- **Batch Scanner**: Upload CSV logs to analyze thousands of connections instantly.
- **Deep Forensics**: Inspect individual packets to see specific risk scores and threat levels.
- **Threat Intelligence**: Categorizes traffic into SAFE, LOW, MEDIUM, HIGH, or CRITICAL risk.
- **Model Telemetry**: View feature importance and performance metrics directly in the app.

---

## 🚀 Performance Benchmarks
The system was trained on the **NSL-KDD dataset** and benchmarked against 6 different algorithms. **XGBoost** was selected as the final engine due to its superior performance.

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **XGBoost** | **99.70%** | **99.79%** | **99.57%** | **99.68%** |
| Random Forest | 99.66% | 99.87% | 99.40% | 99.64% |
| MLP (Neural Net) | 99.44% | 99.36% | 99.45% | 99.40% |
| KNN | 99.27% | 99.49% | 98.94% | 99.21% |

---

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **ML Framework:** Scikit-Learn, XGBoost
- **Dashboard:** Streamlit (Glassmorphic UI)
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib, Seaborn

---

## 💻 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/AdityaSankanPal/network-intrusion-detection-system.git 
cd Network-Intrusion-Detection-System
```
### 2. Run the Web locally 
```bash
cd Network-Intrusion-Detection-System/NIDS_WebApp
./ run_nids.bat(Windowns)
or
./run_nids.sh(MAC/linux)
```
 



