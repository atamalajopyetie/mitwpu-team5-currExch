import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import warnings
import numpy as np

# Suppress warnings for clarity
warnings.simplefilter('ignore', ConvergenceWarning)

# Function to load data from CSV
def load_data():
    data = pd.read_csv('updated_newest.csv')
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    return data

# Function to fit SARIMA model and make predictions
def forecast_currency_rate(data, currency, periods=365):
    # Prepare data for the model
    currency_data = data[['Date', currency]].dropna()
    currency_data.set_index('Date', inplace=True)

    # Fit SARIMA model
    model = SARIMAX(currency_data[currency], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit(disp=False)

    # Forecast future values
    forecast = model_fit.get_forecast(steps=periods)
    forecast_index = pd.date_range(start=currency_data.index[-1] + pd.Timedelta(days=1), periods=periods)
    forecast_values = forecast.predicted_mean
    conf_int = forecast.conf_int()

    return forecast_index, forecast_values, conf_int

# Function to plot historical data and future predictions
def plot_predictions(data, currency, forecast_index, forecast_values, conf_int):
    plt.figure(figsize=(12, 6))

    # Plot historical data
    plt.plot(data['Date'], data[currency], label="Historical Data", color='blue')

    # Plot forecasted data
    plt.plot(forecast_index, forecast_values, label="Predicted Data", linestyle='--', color='red')

    # Plot confidence intervals
    plt.fill_between(forecast_index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.5, label='Confidence Interval')

    plt.title(f'Currency Rate Prediction for {currency}', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Exchange Rate', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend(fontsize=12)
    plt.grid()
    st.pyplot(plt)
    plt.close()

# Streamlit app for future prediction
def main():
    st.title("Currency Rate Prediction")

    # Load data
    data = load_data()

    # User selects currency
    currency_options = [col for col in data.columns if col != 'Date']
    selected_currency = st.selectbox("Select Currency", currency_options)

    # Number of periods to forecast (up to 10 years)
    periods = st.slider("Select number of days to forecast", min_value=365, max_value=3650, value=365)

    if st.button("Predict"):
        # Forecast future currency rates
        forecast_index, forecast_values, conf_int = forecast_currency_rate(data, selected_currency, periods=periods)

        # Plot historical and forecasted values
        plot_predictions(data, selected_currency, forecast_index, forecast_values, conf_int)

# To run only the future prediction page
if __name__ == "__main__":
    main()
