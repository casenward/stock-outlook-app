import backend.apis.finnhub as finnhub
import backend.apis.yahoo as yahoo
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from backend.stock import Stock

import time

one_year_ago = int(time.time()) - 365 * 24 * 60 * 60
today = int(time.time())




def final_rating(score: float) -> str:
    if score >= 90:
        return "Strong Buy"
    elif score >= 75:
        return "Buy"
    elif score >= 50:
        return "Hold"
    elif score >= 30:
        return "Sell"
    else:
        return "Strong Sell"


def calculate_consensus(stock_obj) -> str:
    yahoo_score = yahoo.getYahoo_consensus(stock_obj.symbol)[1] * 0.6
    momentum_score = get_momentum_score(stock_obj) * 0.1
    pb_score = get_pb_ratio_score(stock_obj) * 0.1
    pe_score = get_pe_ratio_score(stock_obj) * 0.1
    dividend_score = get_dividend_yield_score(stock_obj) * 0.1
    total_score = yahoo_score + momentum_score + pb_score + pe_score + dividend_score
    return final_rating(total_score)


import time

def get_momentum_score(stock_obj: "Stock") -> float:
    if stock_obj.current_price is None:
        stock_obj.set_currentPrice()
    current_price = stock_obj.current_price
    one_year_ago = int(time.time()) - 365 * 24 * 60 * 60
    today = int(time.time())
    candles = finnhub.get_candles(stock_obj.symbol, "D", one_year_ago, today)
    if not candles or "c" not in candles or not candles["c"]:
        return 50
    one_year_ago_price = candles["c"][0]
    if one_year_ago_price == 0:
        return 50
    momentum = ((current_price - one_year_ago_price) / one_year_ago_price) * 100
    if momentum >= 20:
        return 100
    elif momentum >= 10:
        return 80
    elif momentum >= 0:
        return 60
    elif momentum >= -10:
        return 40
    elif momentum >= -20:
        return 20
    else:
        return 0



def get_pb_ratio_score(stock_obj) -> float:
    return 60


def get_pe_ratio_score(stock_obj) -> float:
    return 70

def get_dividend_yield_score(stock_obj) -> float:
    return 80


if __name__ == "__main__":
    from backend.stock import Stock
    test_stock = Stock("AAPL", "Apple Inc.")
    test_stock.set_currentPrice()
    test_stock.set_consensus()
    print(f"Stock: {test_stock.symbol}, Current Price: {test_stock.current_price}, Consensus: {test_stock.consensus}")
