import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Page config
st.set_page_config(page_title="TradeIQ - Stock Market Predictor", page_icon="📊", layout="wide")

# Custom CSS for gradients and styling
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            color: white;
        }
        h1, h2, h3, h4 {
            text-align: center;
            font-family: 'Arial Black', sans-serif;
        }
        .stTextInput > div > div > input {
            border: 2px solid #00c6ff;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton button {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            border: none;
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Load Model
model = load_model("C:/Users/samar/Project/TradeIQ/Stock Prediction Model.keras")

# Title
st.title('📊 TradeIQ - AI Stock Predictor 📊')
st.markdown("### Smarter Trading with Machine Learning")

# User Input with Search Button
col1, col2 = st.columns([3,1])
with col1:
    stock = st.text_input('Enter Stock Symbol (e.g., GOOG, AAPL, MSFT)', 'GOOG')
with col2:
    search = st.button("🔍 Search")

start = '2012-01-01'
end = '2022-12-31'

# Fetch Data when search clicked
if search:
    data = yf.download(stock, start, end)

    # Show Stock Data
    st.subheader('📌 Latest Stock Data')
    st.dataframe(data.tail().style.background_gradient(cmap="Blues"))

    # Train/Test Split
    data_train = pd.DataFrame(data.Close[0:int(len(data)*0.80)])
    data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

    scaler = MinMaxScaler(feature_range=(0, 1))
    past_100_days = data_train.tail(100)
    data_test = pd.concat([past_100_days, data_test], ignore_index=True)
    data_test_scale = scaler.fit_transform(data_test)

    # Moving Averages
    st.subheader('📈 Price vs MA50')
    ma_50 = data.Close.rolling(50).mean()
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(ma_50, 'r', linewidth=2, label="MA50")
    ax1.plot(data.Close, 'g', linewidth=1.5, label="Close Price")
    ax1.set_facecolor("#0e1117")
    ax1.grid(alpha=0.3)
    ax1.legend()
    st.pyplot(fig1)

    st.subheader('📈 Price vs MA50 vs MA100')
    ma_100 = data.Close.rolling(100).mean()
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(ma_50, 'r', linewidth=2, label="MA50")
    ax2.plot(ma_100, 'b', linewidth=2, label="MA100")
    ax2.plot(data.Close, 'g', linewidth=1.5, label="Close Price")
    ax2.set_facecolor("#0e1117")
    ax2.grid(alpha=0.3)
    ax2.legend()
    st.pyplot(fig2)

    st.subheader('📈 Price vs MA100 vs MA200')
    ma_200 = data.Close.rolling(200).mean()
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(ma_100, 'r', linewidth=2, label="MA100")
    ax3.plot(ma_200, 'b', linewidth=2, label="MA200")
    ax3.plot(data.Close, 'g', linewidth=1.5, label="Close Price")
    ax3.set_facecolor("#0e1117")
    ax3.grid(alpha=0.3)
    ax3.legend()
    st.pyplot(fig3)

    # Prepare Data for Prediction
    x, y = [], []
    for i in range(100, data_test_scale.shape[0]):
        x.append(data_test_scale[i-100:i])
        y.append(data_test_scale[i, 0])

    x, y = np.array(x), np.array(y)

    # Predictions
    predicted = model.predict(x)
    scale = 1 / scaler.scale_
    predicted = predicted * scale
    y = y * scale

    # Plot Predictions
    st.subheader('🔮 Original Price vs Predicted Price')
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    ax4.plot(y, 'g', linewidth=1.8, label="Original Price")
    ax4.plot(predicted, 'r', linewidth=2, linestyle="--", label="Predicted Price")
    ax4.set_facecolor("#0e1117")
    ax4.grid(alpha=0.3)
    ax4.legend()
    st.pyplot(fig4)

    # Footer
    st.markdown("""
    ---
    Built with 💖 by Samarth Dharpure | 2025 📊 TradeIQ
    """)
