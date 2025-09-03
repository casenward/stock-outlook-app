## Yahoo Finance API integration
## Casen Ward

import yfinance as yf

rating_scores = {
    "strong buy": 2,
    "buy": 1,
    "hold": 0,         #rating system 
    "sell": -1,
    "strong sell": -2
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
            "hold": latest.get("hold", 0),
            "sell": latest.get("sell", 0),
            "strong sell": latest.get("strongSell", 0),
        }

        consensus_text = max(counts, key=counts.get)
        consensus_score = rating_scores[consensus_text]

        return (consensus_text, consensus_score)

    except Exception as e:
        raise Exception(f"Yahoo Finance API error: {e}")


# test
if __name__ == "__main__":
    stock = "TSLA"
    text, score = getYahoo_consensus(stock)
    print(f"Yahoo consensus for {stock}: {text} (score: {score})")
