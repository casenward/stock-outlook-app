## This file contains the Stock class, which is used to represent a stock and its associated data.

## Author: Casen Ward

class Stock:
    def __init__(self, symbol, name, sector, industry, price, consensus):
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.industry = industry
        self.price = price
        self.consensus = consensus

    def display_info(self):
        ## todo
        pass

    def get_consensus(self):
        return self.consensus

    def print_terminal(self):  ##temporary
        print(f"{self.symbol} | {self.name} | {self.price} | {self.consensus}")
