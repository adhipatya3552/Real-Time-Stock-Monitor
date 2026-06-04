import sys
from pathlib import Path
import importlib

PARENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(PARENT_DIR.parent))

for module_name in ['config', 'src.data_ingestion', 'src.train_model', 'src.anomaly_detector', 'main']:
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])

import streamlit as st
import pandas as pd
import plotly.express as px
from config import STOCKS
from main import run_pipeline

st.set_page_config(page_title="Stock Monitoring System", layout="wide")

st.title("📈 Real-Time Indian Stock Monitoring System")

# Stock selection
options = list(STOCKS.keys()) + ["Custom Symbol..."]
selected_stock_name = st.sidebar.selectbox("Select Stock", options)

if selected_stock_name == "Custom Symbol...":
    selected_stock_symbol = st.sidebar.text_input(
        "Enter Yahoo Finance Ticker Symbol (e.g., AAPL, GOOG, TATASTEEL.NS)",
        value="AAPL"
    ).strip().upper()
else:
    selected_stock_symbol = STOCKS[selected_stock_name]

@st.cache_resource(show_spinner=False, ttl=15)
def load_data(stock_symbol):
    try:
        df = run_pipeline(stock_symbol)
        return df
    except Exception as e:
        # Return empty dataframe on failure
        return pd.DataFrame()

if not selected_stock_symbol:
    st.info("Please enter a valid stock ticker symbol in the sidebar.")
else:
    with st.spinner(f"Loading data for {selected_stock_symbol}..."):
        df = load_data(selected_stock_symbol)

    if df.empty or "Close" not in df.columns:
        st.error(f"No data found for ticker symbol '{selected_stock_symbol}'. Please verify the symbol and try again.")
    else:
        latest = df.iloc[-1]
        anomaly_count = len(df[df["Anomaly"] == -1])

        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"₹ {latest['Close']:.2f}" if "NS" in selected_stock_symbol or "BO" in selected_stock_symbol else f"$ {latest['Close']:.2f}")
        col2.metric("Volume", f"{int(latest['Volume'])}")
        col3.metric("Anomalies Found", anomaly_count)

        st.divider()

        st.subheader("📊 Stock Price Trend")
        fig_price = px.line(df, x="Datetime", y="Close")
        st.plotly_chart(fig_price, width='stretch')

        st.divider()

        st.subheader("📈 Moving Averages")
        fig_ma = px.line(df, x="Datetime", y=["Close", "MA_5", "MA_10"])
        st.plotly_chart(fig_ma, width='stretch')

        st.divider()

        st.subheader("🚨 Anomaly Detection")
        normal = df[df["Anomaly"] == 1]
        anomalies = df[df["Anomaly"] == -1]

        fig_anomaly = px.scatter(normal, x="Datetime", y="Close")
        fig_anomaly.add_scatter(
            x=anomalies["Datetime"],
            y=anomalies["Close"],
            mode="markers",
            name="Anomaly"
        )
        st.plotly_chart(fig_anomaly, width='stretch')

        st.divider()

        st.subheader("📋 Detected Anomalies")
        st.dataframe(anomalies[["Datetime", "Close", "Volatility"]])