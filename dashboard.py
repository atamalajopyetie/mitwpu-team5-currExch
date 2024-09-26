import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Function to load data from CSV
def load_data():
    data = pd.read_csv('updated_newest.csv')
    # Convert the 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    return data


# Function to plot trends for selected currencies
def plot_trends(data, selected_currencies, start_date, end_date):
    # Convert start_date and end_date to datetime for comparison
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the data based on selected date range
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    plt.figure(figsize=(12, 6))
    for currency in selected_currencies:
        plt.plot(filtered_data['Date'], filtered_data[currency], label=currency)

    plt.title('Currency Trends', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Exchange Rate', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend(fontsize=12)
    plt.grid()
    plt.tight_layout()  # Adjust layout to prevent clipping
    st.pyplot(plt)
    plt.close()


# Function to calculate min, max, and risk level
def calculate_stats_and_risk(data, selected_currencies, start_date, end_date):
    # Convert start_date and end_date to datetime for comparison
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the data based on selected date range
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # Create an empty list to store the stats and risk for each currency
    stats_list = []

    for currency in selected_currencies:
        min_val = filtered_data[currency].min()
        max_val = filtered_data[currency].max()
        std_dev = filtered_data[currency].std()

        # Determine risk based on standard deviation
        if std_dev < 0.5:
            risk_level = 'Low'
        elif std_dev < 1.5:
            risk_level = 'Medium'
        else:
            risk_level = 'High'

        # Append the stats to the list as a dictionary
        stats_list.append({
            'Currency': currency,
            'Min Value': min_val,
            'Max Value': max_val,
            'Risk Level': risk_level
        })

    # Convert the list of dictionaries to a DataFrame
    stats_df = pd.DataFrame(stats_list)

    return stats_df


# Streamlit application
def main():
    st.title("Currency Trend Analysis")

    # Load the currency data
    data = load_data()

    # User selects currencies
    currency_options = [col for col in data.columns if col != 'Date']
    selected_currencies = st.multiselect("Select currencies to analyze", currency_options)

    # User selects duration type
    duration_type = st.radio("Select Duration Type", ['Custom', 'Month', 'Year'])

    if duration_type == 'Custom':
        # Input for custom date range
        st.write("### Select Custom Date Range")
        start_date = st.date_input("Start date", value=data['Date'].min().date())
        end_date = st.date_input("End date", value=data['Date'].max().date())

    elif duration_type == 'Month':
        # Input for month range
        st.write("### Select Month Range")
        start_month = st.selectbox("Start Month", list(range(1, 13)), index=0)
        start_year = st.selectbox("Start Year", list(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)), index=0)
        end_month = st.selectbox("End Month", list(range(1, 13)), index=11)
        end_year = st.selectbox("End Year", list(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)), index=len(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)) - 1)

        start_date = pd.to_datetime(f"{start_year}-{start_month}-01")
        end_date = pd.to_datetime(f"{end_year}-{end_month}-01") + pd.offsets.MonthEnd(1)  # Get last day of the end month

    elif duration_type == 'Year':
        # Input for year range
        st.write("### Select Year Range")
        start_year = st.selectbox("Start Year", list(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)), index=0)
        end_year = st.selectbox("End Year", list(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)), index=len(range(int(data['Date'].dt.year.min()), int(data['Date'].dt.year.max()) + 1)) - 1)

        start_date = pd.to_datetime(f"{start_year}-01-01")
        end_date = pd.to_datetime(f"{end_year}-12-31")  # Get last day of the end year

    if st.button("Show Trends"):
        if selected_currencies:
            # Plot trends for selected currencies
            plot_trends(data, selected_currencies, start_date, end_date)

            # Calculate and display min, max, and risk level for selected currencies
            stats_df = calculate_stats_and_risk(data, selected_currencies, start_date, end_date)
            st.write("### Min, Max, and Risk Level for Selected Currencies")
            st.table(stats_df)
        else:
            st.warning("Please select at least one currency.")


if __name__ == "__main__":
    main()
