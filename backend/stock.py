# Base class for a stock
# Casen Ward

import backend.apis.finnhub as finnhub
import backend.services.score_calculator as score_calculator


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

#DJIA 30 stocks for testing purposes
DJIA_30 = {
    "MMM": "3M Company",
    "AXP": "American Express Company",
    "AAPL": "Apple Inc.",
    "BA": "Boeing Company",
    "CAT": "Caterpillar Inc.",
    "CVX": "Chevron Corporation",
    "CSCO": "Cisco Systems, Inc.",
    "KO": "The Coca-Cola Company",
    "DOW": "Dow Inc.",
    "GS": "Goldman Sachs Group, Inc.",
    "HD": "The Home Depot, Inc.",
    "IBM": "International Business Machines Corporation",
    "INTC": "Intel Corporation",
    "JNJ": "Johnson & Johnson",
    "JPM": "JPMorgan Chase & Co.",
    "MCD": "McDonald's Corporation",
    "MRK": "Merck & Co., Inc.",
    "MSFT": "Microsoft Corporation",
    "NKE": "Nike, Inc.",
    "PG": "Procter & Gamble Company",
    "CRM": "Salesforce, Inc.",
    "TRV": "The Travelers Companies, Inc.",
    "UNH": "UnitedHealth Group Incorporated",
    "VZ": "Verizon Communications Inc.",
    "V": "Visa Inc.",
    "WBA": "Walgreens Boots Alliance, Inc.",
    "WMT": "Walmart Inc.",
    "DIS": "The Walt Disney Company",
    "AMGN": "Amgen Inc.",
    "HON": "Honeywell International Inc.",
}

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = None
        self.current_price = None
        self.score = None
        self.consensus = None
        
    def set_symbol(self):
        pass
        #TODO - Need to retrieve from frontend
        
    def set_name(self):
        self.name = DJIA_30.get(self.symbol, "Unknown Company")  # Default to "Unknown Company" if symbol not found
    
    def set_currentPrice(self):
        self.current_price = finnhub.get_quote(self.symbol)["c"] # Current price is in the "c" field of the quote response
    
    def set_score(self):
        self.score = score_calculator.calculate_score(self)
        
    def set_consensus(self):
        self.consensus = final_rating(self.score)

        
    