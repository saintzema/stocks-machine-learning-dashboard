import streamlit as st
import pandas as pd
from src.backend import get_kraken_data, trade_to_ohlc
from src.feature_store_api import FeatureStore
from src.ml_model import train_model, predict_buy_sell

# Instantiating Feature Store
feature_store = FeatureStore()

st.title("Machine Learning Trade Prediction Dashboard")

# Input for cryptocurrency pair
pair = st.text_input("Enter Cryptocurrency Pair (e.g., BTCUSD):", "BTCUSD")

if st.button("Fetch Data"):
    with st.spinner("Fetching data..."):
        try:
            # Fetch raw data and convert to OHLC
            trades = get_kraken_data(pair)
            st.write("Raw Trades Data", trades.head())
            
            ohlc = trade_to_ohlc(trades)
            st.write("OHLC Data Before Prediction", ohlc.head())

            # Train the model and make predictions
            model = train_model(ohlc)
            ohlc_with_predictions = predict_buy_sell(ohlc, model)
            
            # Display OHLC data with predictions
            st.write("OHLC Data with Predictions", ohlc_with_predictions)

            # Save to Feature Store
            feature_store.save_features(pair, ohlc_with_predictions)
            st.success("Data processed, predictions made, and saved!")
        except Exception as e:
            st.error(f"Error: {e}")

# Display saved features
if st.button("Show Saved Features"):
    saved_features = feature_store.get_features(pair)
    if not saved_features.empty:
        st.write("Saved Features", saved_features)
    else:
        st.warning("No features saved for this pair.")
