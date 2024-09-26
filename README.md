# Currency Converter Application

# Overview 
The Currency Converter Application is a web app designed to help users convert currencies, view real-time exchange rates, analyze historical trends, and predict future currency rates. Built with Streamlit and Python, the app is useful for travelers, businesses, and financial analysts who need accurate and up-to-date exchange rate information.

# Features
- Real-Time Exchange Rates: Displays live exchange rates for multiple currencies.
- Currency Conversion: Instantly convert amounts between selected currencies.
- Historical Data: View and analyze past exchange rates.
- Future Predictions: Use AI models to predict future currency rates.
- Graphs and Charts: Visualize data with clear line and bar graphs.

# Who Can Use This?
- Travelers: Quickly check conversion rates for different currencies while traveling.
- Businesses: Get real-time updates on exchange rates to help with financial decisions.
- Analysts: Analyze currency trends to make informed predictions.

# Technologies Used
- Streamlit: Creates the interactive user interface.
- Python: Handles the application logic and data analysis.
- Docker: Packages the app for easy deployment and consistent performance.
- Pandas & NumPy: Libraries for data processing and analysis.
- StatsModels: For building the predictive models in the Future Prediction feature.
  
# How the Code is Organized
- [Main App (app.py)](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/app.py "Main App (app.py)"): The entry point that brings together all features.
Shows different tabs: Dashboard, Currency Bucket, Future Prediction, and Exchange Rates.
- Supporting Files:
- [dashboard.py:](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/dashboard.py "dashboard.py:") Displays key information and app metrics.
- [currency_bucket.py:](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/currency_bucket.py "currency_bucket.py:") Manages a list of currencies for easy access.
- [future_prediction.py:](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/future_prediction.py "future_prediction.py:") Uses AI to predict future exchange rates.
- [exchange_rate.py:](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/exchange_rate.py "exchange_rate.py:") Retrieves and shows live exchange rate data.
- [Requirements File](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/requirements.txt "Requirements File"): The requirements.txt file lists the Python packages you need to run this app.
  
# Docker Configuration:
- [Dockerfile:](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/Dockerfile "Dockerfile:") Specifies how the app should be built and run in a Docker container.
- [docker-compose.yml](https://github.com/atamalajopyetie/nt_mitwpu_hackathon/blob/main/docker-compose.yml "docker-compose.yml"): Helps manage and run the app using Docker Compose.
  
# Running the App Locally 
- Clone this repository to your computer. 
- Build and run the Docker container:
	 on bash Copy code
	 `docker-compose up --build`
	 Open your browser and go to http://localhost:8501 to view the app.

# Running the Python Code:

Before running the application, ensure you have the following installed:

- Python (version 3.8 or higher)
- Docker (optional but recommended for deployment)
- Pip (Python package manager)

Option 1: Running the App Locally (Without Docker)
Clone the Repository:

- Open your terminal (Command Prompt, PowerShell, or any other terminal) and run:
bash Copy code
`git clone <https://github.com/atamalajopyetie/nt_mitwpu_hackathon>`
Replace <https://github.com/atamalajopyetie/nt_mitwpu_hackathon> with the actual URL of your GitHub repository.
- Navigate to the Project Directory:
bash Copy code
`cd currency_converter_app`
- Install Dependencies:
- Install the required Python packages using pip:
bash Copy code
`pip install -r requirements.txt`
- Run the Application:
Run the app.py file using Python:
bash Copy code
`streamlit run app.py`
Access the App:
Open your web browser and go to:
arduino
Copy code
http://localhost:8501

Option 2: Running the App with Docker
Clone the Repository:

bash Copy code
`git clone <https://github.com/atamalajopyetie/nt_mitwpu_hackathon>`
- Navigate to the Project Directory:
bash Copy code
`cd currency_converter_app`
- Build and Run the Docker Container:
Build and start the application using Docker Compose:
bash Copy code
`docker-compose up --build`
- Access the App:
Once the container is running, go to:
arduino
Copy code
http://localhost:8501
Stopping the Application
To stop the application, press Ctrl + C in the terminal. If you're running it with Docker, you can stop the container with:

bash
Copy code
docker-compose down

# Future Plans AI Integration:
- Enhance the currency prediction feature using more advanced AI models.
- Firebase: Continue using Firebase to store data and keep the exchange rates up to date in real time.
