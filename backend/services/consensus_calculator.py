## This class calculates the consensus price for a given stock based on various factors.

class ConsensusCalculator:
    def __init__(self, stock):
        self.stock = stock
        self.finnhub_consensus = None
        self.yahoo_consensus = None
        self.financial_modeling_prep_consensus = None

    def calculate_consensus(self):
        ## todo
        pass