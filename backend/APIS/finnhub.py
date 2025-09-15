# Finnhub API integration
# Casen Ward

import os
import requests
from dotenv import load_dotenv
import datetime
import time

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
URL = "https://finnhub.io/api/v1"

# Get the stocks quote (current price and other data)
def get_quote(symbol):
    url = f"{URL}/quote"
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

# Get the current metrics for a stock
def get_metrics(symbol):
    url = f"{URL}/stock/metric"
    params = {"symbol": symbol, "metric": "all", "token": FINNHUB_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    print(get_quote("AAPL"))
    print(get_metrics("AAPL"))

