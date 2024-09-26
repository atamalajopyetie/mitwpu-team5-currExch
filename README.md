#Currency Converter Application

#Overview
The Currency Converter Application is a web app designed to help users convert currencies, view real-time exchange rates, analyze historical trends, and predict future currency rates. Built with Streamlit and Python, the app is useful for travelers, businesses, and financial analysts who need accurate and up-to-date exchange rate information.

#Features
1. Real-Time Exchange Rates: Displays live exchange rates for multiple currencies.
2. Currency Conversion: Instantly convert amounts between selected currencies.
3. Historical Data: View and analyze past exchange rates.
4. Future Predictions: Use AI models to predict future currency rates.
5. Graphs and Charts: Visualize data with clear line and bar graphs.
   
#Who Can Use This?
- Travelers: Quickly check conversion rates for different currencies while traveling.
- Businesses: Get real-time updates on exchange rates to help with financial decisions.
- Analysts: Analyze currency trends to make informed predictions.

#Technologies Used
- Streamlit: Creates the interactive user interface.
- Python: Handles the application logic and data analysis.
- Docker: Packages the app for easy deployment and consistent performance.
- Pandas & NumPy: Libraries for data processing and analysis.
- StatsModels: For building the predictive models in the Future Prediction feature.

#How the Code is Organized
- Main App (app.py): The entry point that brings together all features.
- Shows different tabs: Dashboard, Currency Bucket, Future Prediction, and Exchange Rates.
- Supporting Files:
  1. dashboard.py: Displays key information and app metrics.
  2. currency_bucket.py: Manages a list of currencies for easy access.
  3. future_prediction.py: Uses AI to predict future exchange rates.
  4. exchange_rate.py: Retrieves and shows live exchange rate data.
  5. Requirements File: The requirements.txt file lists the Python packages you need to run this app.

#Docker Configuration:
- Dockerfile: Specifies how the app should be built and run in a Docker container.
- docker-compose.yml: Helps manage and run the app using Docker Compose.

#Running the App Locally
-Clone this repository to your computer.
-Build and run the Docker container:
   - on bash Copy code
   - docker-compose up --build
   - Open your browser and go to http://localhost:8501 to view the app.

#Future Plans
AI Integration: Enhance the currency prediction feature using more advanced AI models.
Firebase: Continue using Firebase to store data and keep the exchange rates up to date in real time.
