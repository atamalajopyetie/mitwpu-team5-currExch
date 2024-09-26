import streamlit as st
import requests
import pandas as pd


# Function to get exchange rates
def get_exchange_rates(base_currency='USD'):
    url = f'https://v6.exchangerate-api.com/v6/67663e5c57d81adae0ce6789/latest/{base_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data. Please check the API key and base currency.")
        return None


def main():
    # Streamlit UI
    st.title("Currency Exchange Rates(USD)")

    # Get current exchange rates
    data = get_exchange_rates('USD')

    if data:
        # Extract relevant information
        currencies = data['conversion_rates']

        # Create a DataFrame
        currency_list = []
        for code, rate in currencies.items():
            currency_list.append({
                'Currency Code': code,
                'Description': f"Exchange rate of {code} against USD",
                'Exchange Rate': rate
            })

        df = pd.DataFrame(currency_list)

        # Dropdown for currency selection
        currency_options = df['Currency Code'].tolist()
        selected_currency = st.selectbox("Select a Currency Code:", options=[''] + currency_options)

        # Filter the DataFrame based on the selected currency
        if selected_currency:
            df = df[df['Currency Code'] == selected_currency]

        # Display the DataFrame in full width and height
        st.write("<style>.dataframe {width: 100%; height: 100%;}</style>",
                 unsafe_allow_html=True)  # Make DataFrame full width
        st.dataframe(df, use_container_width=True, height=600)  # Set to use full container width and define height


if __name__ == "__main__":
    main()