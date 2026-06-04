# Real-Time Stock Monitoring & Anomaly Detection System

<div align="center">

![Project Logo](https://img.shields.io/badge/Stock--Monitor-Real--Time-blue?style=for-the-badge&logo=trending-up&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Isolation%20Forest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

**A real-time stock market dashboard and pipeline that fetches financial data, calculates technical indicators, and applies machine learning (Isolation Forest) to detect trading and pricing anomalies automatically.**

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Roadmap](#-roadmap)

---

## 📈 Overview
The **Real-Time Stock Monitoring & Anomaly Detection System** is designed to provide traders and analysts with immediate, interactive, and automated insights into stock market trends and volatility. 

Using Yahoo Finance (`yfinance`), it pulls live and historical market data at custom granular intervals (e.g., 15 minutes). It applies a robust machine learning model—**Isolation Forest**—trained dynamically in-memory to discover outlier price movements and volume anomalies. The results are rendered instantly on a beautifully designed Streamlit web application.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ⚡ **Live Stock Data Ingestion** | Fetches live and historical price/volume data using `yfinance` API |
| 🎛️ **Custom Ticker Support** | Select from popular pre-defined Indian stocks or type in any custom global symbol (e.g. `AAPL`, `GOOG`, `TATASTEEL.NS`) |
| 🚨 **ML Anomaly Detection** | Dynamic in-memory training of an Isolation Forest model to detect pricing and return anomalies |
| 📈 **Technical Indicators** | Dynamically calculates rolling Simple Moving Averages (`MA_5`, `MA_10`), volatility, and percentage price returns |
| 📊 **Interactive Plotly Visuals** | Line charts for price trends and moving averages, plus scatter plots highlighting detected anomalies |
| 💱 **Currency Auto-Formatting** | Automatically displays Rupees (`₹`) for Indian NSE/BSE stocks and Dollars (`$`) for global tickers |
| 🛡️ **Graceful Error Handling** | Displays helpful UI warnings for invalid tickers or API connectivity issues instead of crashing |
| ⚡ **Fast In-Memory Cache** | Caches trained machine learning models for each ticker to avoid redundant retraining |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          STREAMLIT DASHBOARD                        │
│                                                                      │
│  ┌───────────────────────┐   ┌────────────────────────────────────┐ │
│  │   Sidebar Selector    │──▶│      Custom Ticker Text Input      │ │
│  │  (Pre-defined / Custom│   │      (e.g., RELIANCE.NS, AAPL)     │ │
│  └───────────────────────┘   └────────────────────────────────────┘ │
│                                                │                    │
└────────────────────────────────────────────────┼────────────────────┘
                                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         PROCESSING PIPELINE                         │
│                                                                      │
│  ┌──────────────────────┐      Downloads 30d 15m intervals          │
│  │ 1. Data Ingestion    │◀─────────────────────────────────────────││ (Yahoo Finance API)
│  └──────────────────────┘                                           │
│            │                                                        │
│            ▼                                                        │
│  ┌──────────────────────┐      Removes NaNs, converts timestamps    │
│  │ 2. Preprocessing     │                                           │
│  └──────────────────────┘                                           │
│            │                                                        │
│            ▼                                                        │
│  ┌──────────────────────┐      Computes MA_5, MA_10, Volatility,    │
│  │ 3. Feature Eng.      │      and percentage returns               │
│  └──────────────────────┘                                           │
│            │                                                        │
│            ▼                                                        │
│  ┌──────────────────────┐      Trains Isolation Forest (if not      │
│  │ 4. Model Cache /     │      cached) & labels anomalies (-1 / 1)  │
│  │    Anomaly Detection │                                           │
│  └──────────────────────┘                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit | Fast, interactive web application dashboard |
| **Data Fetching** | yfinance | Downloads historical and live stock market data |
| **Data Processing** | Pandas & NumPy | Cleans data and engineers sliding-window technical features |
| **Machine Learning** | Scikit-Learn | Dynamic Isolation Forest model for anomaly detection |
| **Visualization** | Plotly Express | Interactive line plots, moving averages, and scatter charts |

---

## 📁 Project Structure

```
real-time-stock-monitor/
├── dashboard/
│   └── app.py              # Streamlit frontend dashboard & UI rendering
├── src/
│   ├── anomaly_detector.py # Runs prediction using the fitted model
│   ├── data_ingestion.py   # Downloads raw data from yfinance
│   ├── feature_engineering.py# Computes indicators (MA, Volatility, Returns)
│   ├── preprocessing.py     # Clean data and formats DateTime timestamps
│   └── train_model.py       # Trains an Isolation Forest on engineered features
├── models/                 # Directory reserved for model exports
├── notebook/               # Directory reserved for Jupyter notebooks
├── config.py               # Pre-defined mapping of Indian stock tickers
├── main.py                 # Pipeline manager coordinating ingestion, features, & ML
├── requirements.txt        # Project package dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
* **Python** 3.8 or higher installed on your local machine.

### 1. Clone & Setup Directory
```bash
git clone https://github.com/adhipatya3552/Real-Time-Stock-Monitor.git
cd Real-Time-Stock-Monitor
```

### 2. Create and Activate Virtual Environment
* **On Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **On macOS / Linux:**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
The application will automatically open in your default browser at **`http://localhost:8501`**.

---

## ⚙️ How It Works

### Step 1 — Select or Enter Stock Ticker
Select a stock from the pre-defined dropdown (Reliance, TCS, SBI, HDFC, etc.) or choose **"Custom Symbol..."** and type any ticker (e.g. `TSLA` or `INFY.NS`).

### Step 2 — Fetch Live Data
The app triggers [src/data_ingestion.py](file:///d:/Builds/work/real-time-stock-monitor/src/data_ingestion.py) which downloads 30 days of 15-minute interval historical data from the Yahoo Finance API.

### Step 3 — Preprocess & Feature Engineering
* Missing rows are dropped, and index is reset.
* The system calculates five key features used to profile market behavior:
  * **MA_5 & MA_10**: 5-period and 10-period rolling moving averages of the Close price.
  * **Volatility**: 10-period rolling standard deviation of the Close price.
  * **Price Return**: Percentage return from the previous period.

### Step 4 — Anomaly Detection
The pipeline feeds features to [src/train_model.py](file:///d:/Builds/work/real-time-stock-monitor/src/train_model.py). An **Isolation Forest** (with a contamination factor of 2%) labels outlier candles as `-1` (Anomaly) and typical sessions as `1` (Normal). To keep performance snappy, models are cached in-memory inside [main.py](file:///d:/Builds/work/real-time-stock-monitor/main.py).

### Step 5 — Interactive UI Charts
The UI updates instantly to display:
* Metrics for current price, volume, and total anomaly count.
* Main price line chart.
* Close price overlayed with moving averages.
* Interactive scatter plot highlighting anomalous trades.
* A tabular list of detected anomalies.

---

## 🗺️ Roadmap
- [x] In-memory caching for machine learning models
- [x] Technical features calculation (Moving Averages, Volatility, Returns)
- [x] Isolation Forest anomaly detection engine
- [x] Streamlit web interface with sidebar controls
- [x] Custom Yahoo Finance ticker input in the UI
- [x] Dynamic currency formatting based on stock exchange
- [x] Error handling for empty data response
- [ ] Export anomalies table as CSV or PDF report
- [ ] Multi-stock comparison charts on the dashboard
- [ ] Email/Slack alerting integration for detected real-time anomalies
- [ ] Support for custom model configuration (contamination, random state) from the sidebar

---

<div align="center">

Built with ❤️ for real-time market analysis.

</div>
