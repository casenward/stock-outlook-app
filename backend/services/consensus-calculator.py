# Calculates our consensus score for a given stock
# Casen Ward

from backend import stock
import backend.apis.yahoo as yahoo
import backend.apis.finnhub as finnhub

class ConsensusCalculator():
    def __init__(self):
        self.analyst_rating = ""
        self.momentum = 0
        self.pb_ratio = 0
        self.de_ratio = 0
        self.roe = 0

    
    def set_analyst_rating(self, rating):
        self.analyst_rating = yahoo.getYahoo_consensus(stock)[1]  # Get the consensus score from Yahoo Finance