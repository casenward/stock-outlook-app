import backend.apis.finnhub as finnhub
import backend.stock as stock
import backend.apis.yahoo as yahoo


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


def calculate_consensus(stock) -> str:
    return final_rating(yahoo.getYahoo_consensus(stock)[1] * .6 + get_momentum_score(stock) * .1 + get_pb_ratio_score(stock) * .1 + get_pe_ratio_score(stock) * .1 + get_dividend_yield_score(stock) * .1)

def get_momentum_score(stock) -> float:
    pass
    #TODO - implement momentum score calculation
    return 50  # Placeholder value
    
def get_pb_ratio_score(stock) -> float:
    pass
    #TODO - implement PB ratio score calculation
    return 60  # Placeholder value
    
def get_pe_ratio_score(stock) -> float:
    pass
    #TODO - implement PE ratio score calculation
    return 70  # Placeholder value
    
def get_dividend_yield_score(stock) -> float:
    pass
    #TODO - implement dividend yield score calculation
    return 80  # Placeholder value

if __name__ == "__main__":
    test_stock = "AAPL"
    consensus = calculate_consensus(test_stock)
    print(f"Consensus for {test_stock}: {consensus}")

    