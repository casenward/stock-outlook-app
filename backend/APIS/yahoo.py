## Yahoo Finance API integration
## Casen Ward

import yfinance as yf

rating_scores = {
    "strong buy": 50,
    "buy": 38,
    "hold": 20,            #These scores can be adjusted (temporary values until further analysis and testing)
    "sell": 8,
    "strong sell": 0
}


def getYahoo_consensus(stock: str) -> tuple[str, int]:
    ticker = yf.Ticker(stock)        #takes the parameter stock, ex: "AAPL"

    try:
        recs = ticker.recommendations_summary        # Fetch recommendations summary

        if recs is None or recs.empty:
            return ("no data", 0)     # No recommendations data available ()

        latest = recs.iloc[-1]  # most recent update
        # ex: 'strongBuy', 'buy', 'hold', 'sell', 'strongSell'
        counts = {
            "strong buy": latest.get("strongBuy", 0),
            "buy": latest.get("buy", 0),
            "hold": latest.get("hold", 0),      #default to 0 if key not found
            "sell": latest.get("sell", 0),
            "strong sell": latest.get("strongSell", 0),
        }

        consensus_text = max(counts, key=counts.get)        # Get the recommendation with the highest count
        consensus_score = rating_scores[consensus_text]        # Map the consensus text to its score

        return (consensus_text, consensus_score)

    except Exception as e:
        raise Exception(f"Yahoo Finance API error: {e}")

#Used to get historical data for a stock (will end up being used for charts)
def get_candles(symbol, interval, start, end):
    ticker = yf.Ticker(symbol)        # Create a Ticker object
    hist = ticker.history(interval=interval, start=start, end=end)         # Fetch historical market data 
    return hist            # Returns a DataFrame with the historical data


# test
if __name__ == "__main__":
    stock = "AMZN"
    text, score = getYahoo_consensus(stock)
    print(f"Yahoo consensus for {stock}: {text} (score: {score})")
    hist = get_candles("AAPL", "1d", "2023-01-01", "2023-10-01")
    print(hist)
