import streamlit as st
import requests

# Function to fetch exchange rates
def fetch_exchange_rates(base_currency):
    url = f"https://v6.exchangerate-api.com/v6/c616daa3d69e101f81daa5f2/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    return data['conversion_rates']

# List of all currencies
CURRENCY_LIST = [
    "USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD",
    "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD",
    "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD",
    "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK",
    "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD",
    "FKP", "FOK", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF",
    "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
    "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY",
    "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA",
    "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN",
    "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR",
    "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON",
    "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD",
    "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN", "SYP", "SZL",
    "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD",
    "TZS", "UAH", "UGX", "UYU", "UZS", "VES", "VND", "VUV", "WST",
    "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]  # Your currency list here

# Streamlit application
def main():
    st.title("Custom Currency Basket")

    # Input base currency
    base_currency = st.selectbox("Select your Base Currency", options=CURRENCY_LIST,
                                  index=CURRENCY_LIST.index("INR"))

    st.write("---")  # Horizontal line for separation

    # Input currency distribution
    st.write("### Enter the distribution of your investment in different currencies:")
    currencies = st.multiselect("Select Currencies", options=CURRENCY_LIST, default=["USD"])
    weights = {}

    # User input for weights
    for currency in currencies:
        weight = st.number_input(f"Enter the weight for {currency} (%)", min_value=0.0, max_value=100.0, format="%.2f")
        weights[currency] = weight

    # Calculate total weight and validate
    total_weight = sum(weights.values())
    if total_weight > 100:
        st.error("Total weight exceeds 100%. Please adjust the weights.")
    elif total_weight < 100 and total_weight > 0:
        st.warning("Total weight is less than 100%. Adjust weights to distribute properly.")

    # Fetch exchange rates and calculate worth of investments in other currencies
    if st.button("Calculate Worth"):
        exchange_rates = fetch_exchange_rates(base_currency)
        total_basket_value = 0  # Initialize total basket value

        for currency, weight in weights.items():
            if weight > 0:  # Only calculate for non-zero weights
                # Calculate the value of the currency basket based on the weight and current exchange rate
                value_of_currency = weight / 100 * exchange_rates[currency]  # Weight in percentage
                total_basket_value += value_of_currency  # Accumulate total basket value

        # Display the total basket value
        st.write(f"### Total Basket Value: {total_basket_value:.2f} {base_currency}")

# Run the application
if __name__ == "__main__":
    main()
