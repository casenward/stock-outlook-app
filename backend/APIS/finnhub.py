# Finnhub API integration
# Casen Ward

import os
import requests
from dotenv import load_dotenv
import datetime
import time

load_dotenv() # Load environment variables from .env file

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")      # Finnhub API key from environment variable
URL = "https://finnhub.io/api/v1"        # Finnhub base URL

# Get the stocks quote (current price and other data)
def get_quote(symbol):
    url = f"{URL}/quote"    #sets url as the constant URL + endpoint
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}    #symbol = stock tucker ex: "AAPL", token = api key
    r = requests.get(url, params=params)    #makes a get request to the url with the parameters
    r.raise_for_status()       # Raise an error for bad responses
    return r.json()         #returns the response as a json object

# Get the current metrics for a stock
def get_metrics(symbol):
    url = f"{URL}/stock/metric"
    params = {"symbol": symbol, "metric": "all", "token": FINNHUB_API_KEY}    #metric = all gets all available metrics
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

# Test
if __name__ == "__main__":
    print(get_quote("AAPL"))
    print(get_metrics("AAPL"))

