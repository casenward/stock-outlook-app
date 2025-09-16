# Base class for a stock
# Casen Ward

import backend.apis.finnhub as finnhub


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
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.current_price = None
        self.metrics = {}
        self.consensus = None
        self.candles = None
        
    def set_symbol(self):
        pass
        #TODO - Need to retrieve from frontend
        
    def set_name(self):
        self.name = DJIA_30.get(self.symbol, "Unknown Company")  # Default to "Unknown Company" if symbol not found
    
    def set_currentPrice(self):
        self.current_price = finnhub.get_quote(self.symbol)["c"] # Current price is in the "c" field of the quote response
    
    def set_metrics(self):
        self.metrics = finnhub.get_metrics(self.symbol)["metric"] # Metrics are in the "metric" field of the metrics response
        
    def set_consensus(self):
        pass
        #TODO - Need to write the consensus calculator file and import it here

    def set_candles(self):
        self.candles = finnhub.get_candles(self.symbol)