"""
Author: Scott Urbanski
File: portfolio.py
Date Modified: 2025-02-28
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
        Attempts to purchase stock

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price
        ticker: the stock ticker

        Returns:
        N/A
        """

        # the total cost is equal to the number of shares purchased times the price
        totalCost = quantity * price
        # if the cost is less than or equal to the cash on hand, the cost is subtracted from cash
        # otherwise, there are not enough funds and the InsufficientFunds exception is raised
        if totalCost <= self._cash:
            self._cash = self._cash - totalCost
        else:
            raise InsufficientFunds

        # checking to see if the portfolio already has the stock in it
        # if it does, the purchase quantity is added to the previous quantity
        # otherwise, a new entry in the dictionary is added with the purchase quantity
        if ticker in self._stocks:
            self._stocks[ticker] = self._stocks[ticker] + quantity
        else:
            self._stocks[ticker] = quantity

    def SellStock(self, quantity, price, ticker):

        """
        Attempts to sell stock

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price
        ticker: the stock ticker

        Returns:
        N/A
        """

        # if the ticker is not in the portfolio, the stock cannot be sold and an InsufficientShares exception is raised
        # if the ticker is in the portfolio, but the quantity sold is greater than the quantity on hand, an InsufficientShares exception is raised
        if ticker not in self._stocks:
            raise InsufficientShares
        elif quantity > self._stocks[ticker]:
            raise InsufficientShares
        else:
            # otherwise, the ticker's quantity in the portfolio is updated
            self._stocks[ticker] = self._stocks[ticker] - quantity
            # the proceeds from the sale is equal to the price times the quantity sold
            totalProceeds = quantity * price        
            # the proceeds are added to the portfolio's cash
            self._cash = self._cash + totalProceeds

    def CalculatePortfolioValue(self, date=None):
        """
        Calculates the portfolio worth on a given date

        Arguments:
        date (optional): a String value representing the date the portfolio is calculated on

        Returns:
        N/A
        """

        portfolioValue = 0
        # the total cash is added to the portfolio worth
        portfolioValue = portfolioValue + self._cash
        # going through each ticker in the portfolio
        for ticker in self._stocks:
            # assiging the value for each ticker within the dictionary to the quantity variable
            quantity = self._stocks[ticker]
            # creating a stock object with the given ticker so that quotes can be obtained
            stock = Stock(ticker)
            # if no date is supplied in the date argument, the present value is calculated with the GetQuote method and multiplied by the quantity of shares
            # that is then added to the portfolio value
            if date is None:
                portfolioValue = portfolioValue + (quantity*stock.GetQuote())
            else:
                # otherwise, the GetClosingPrice method is used with the given date and multiplied by the quantity
                # that is then added to the portfolio value
                portfolioValue = portfolioValue + (quantity*stock.GetClosingPrice(date=date))
        return portfolioValue
    
class InsufficientFunds(Exception):
    """Raises an exception for insufficient funds"""
    pass

class InsufficientShares(Exception):
    """Raises an exception for insuffiient shares"""
    pass




