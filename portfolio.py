"""
Author: Scott Urbanski
File: portfolio.py
Date Modified: 2025-02-25
Description: This module contains the class
             definition for an investing portfolio
             as well as InsufficientFunds and 
             InsufficientShares exceptions.
"""

from stock import Stock

class Portfolio:

    def __init__(self, cash):
        self._cash = cash
        self._stocks = {}

    
    def PurchaseStock(self, quantity, price, ticker):

        """
        Removes cash from the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """

        totalCost = quantity * price
        if totalCost <= self._cash:
            self._cash = self._cash - totalCost
        else:
            raise InsufficientFunds

        if ticker in self._stocks:
            self._stocks[ticker] = self._stocks[ticker] + quantity
        else:
            self._stocks[ticker] = quantity

    def SellStock(self, quantity, price, ticker):

        """
        Adds cash to the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """
        if ticker not in self._stocks:
            raise InsufficientShares
        elif quantity > self._stocks[ticker]:
            raise InsufficientShares
        else:
            self._stocks[ticker] = self._stocks[ticker] - quantity
            totalProceeds = quantity * price        
            self._cash = self._cash + totalProceeds

    def CalculatePortfolioValue(self, date=None):
        portfolioValue = 0
        portfolioValue = portfolioValue + self._cash
        for ticker in self._stocks:
            quantity = self._stocks[ticker]
            stock = Stock(ticker)
            if date is None:
                portfolioValue = portfolioValue + (quantity*stock.GetQuote())
            else:
                portfolioValue = portfolioValue + (quantity*stock.GetClosingPrice(date=date))
        return portfolioValue
    
class InsufficientFunds(Exception):
    """Raises an exception for insufficient funds"""
    pass

class InsufficientShares(Exception):
    """Raises an exception for insuffiient shares"""
    pass




