import streamlit as st

# Importing your modules
import dashboard
import currency_bucket
import future_prediction
import exchange_rate

st.set_page_config(layout="wide")


# Define a function to display content based on the selected tab
def display_page(tab):

    if tab == "Exchange Rates":
        exchange_rate.main()
    elif tab == "Currency Bucket":
        currency_bucket.main()
    elif tab == "Home":
        dashboard.main()
    elif tab == "Future Prediction":
        future_prediction.main()


# Set up the top navigation using tabs
tabs = st.tabs(["Home", "Currency Bucket", "Future Prediction", "Exchange Rates"])

# Display the selected tab
with tabs[0]:
    display_page("Home")
with tabs[1]:
    display_page("Currency Bucket")
with tabs[2]:
    display_page("Future Prediction")
with tabs[3]:
    display_page("Exchange Rates")