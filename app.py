Python

import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="OLIVER TRADER PRO",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #080d16;
    color: white;
}
[data-testid="stSidebar"] {
    background: #101827;
}
h1, h2, h3 {
    color: #00e69a !important;
}
.metric-card {
    background: #111c2d;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #24364d;
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ OLIVER TRADER PRO")
st.caption("CRYPTO MARKET ANALYTICS PLATFORM")

st.divider()

st.subheader("📊 LIVE MARKET")

pairs = ["BTCUSDT", "ETHUSDT", "BNBUSDT",
         "XRPUSDT", "SOLUSDT"]

cols = st.columns(5)

for col, pair in zip(cols, pairs):
    try:
        response = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": pair},
            timeout=10
        )
        response.raise_for_status()
        price = float(response.json()["price"])

        with col:
            st.markdown('<div class="metric-card">',
                        unsafe_allow_html=True)
            st.metric(pair, f"${price:,.4f}")
            st.markdown('</div>', unsafe_allow_html=True)

    except Exception:
        with col:
            st.warning(pair + " unavailable")

st.divider()

st.subheader("📈 SIGNAL ANALYSIS")

st.info(
    "Signal engine is being prepared. "
    "Signals will be displayed after data validation."
)

st.subheader("📋 PERFORMANCE")

c1, c2, c3 = st.columns(3)

c1.metric("Total Signals", "0")
c2.metric("WIN", "0")
c3.metric("LOSS", "0")

st.caption(
    "OLIVER TRADER PRO | Analytics only | "
    "Not financial advice"
)
