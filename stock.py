"""
Author: Scott Urbanski
File: stock.py
Date Modified: 2025-02-28
Description: This module contains the class
             definition for a stock
             as well as exceptions for 
             an InvalidTicker and MarketClosed.
"""

import yfinance

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker
        
    def GetOpeningPrice(self, date):
        """
        Gets the opening price of a stock on a specific date

        Arguments:
        date: a String value of the desired date

        Returns:
        openingPrice: a Float64 value representing the opening price on the desired date
        """

        # using the LookupQuote function to load in stock market data beginning with the desired date
        # if the user happened to enter an invalid ticker, the LookupQuote function would raise an InvalidTicker error
        data = self.LookupQuote(date=date)
        # the first index of the loaded dataframe is assigned to the firstDate variable
        firstDate = data.index[0]
        # formatting the firstDate variable to a string format of yyyy-mm-dd
        firstDateString = firstDate.strftime('%Y-%m-%d')
        # comparing the first date of the loaded dataframe with the date parameter
        # if they are not equivalent that means that the LookupQuote function had no data available for the user's date and moved
        # to the next available trading day; hence a MarketClosed error is raised
        if firstDateString != date:
            raise MarketClosed
        # otherwise, the cell from the first row of the Open column is stored into openingPrice and returned
        openingPrice = data.iloc[0]["Open"]
        return openingPrice
    
    def GetClosingPrice(self, date):
        """
        Gets the closing price of a stock on a specific date

        Arguments:
        date: a String value of the desired date

        Returns:
        closingPrice: a Float64 value representing the closing price on the desired date
        """

        # using the LookupQuote function to load in stock market data beginning with the desired date
        # if the user happened to enter an invalid ticker, the LookupQuote function would raise an InvalidTicker error
        data = self.LookupQuote(date=date)
        # the first index of the loaded dataframe is assigned to the firstDate variable
        firstDate = data.index[0]
        # formatting the firstDate variable to a string format of yyyy-mm-dd
        firstDateString = firstDate.strftime('%Y-%m-%d')
        # comparing the first date of the loaded dataframe with the date parameter
        # if they are not equivalent that means that the LookupQuote function had no data available for the user's date and moved
        # to the next available trading day; hence a MarketClosed error is raised
        if firstDateString != date:
            raise MarketClosed
        # otherwise, the cell from the first row of the Close column is stored into closingPrice and returned
        closingPrice = data.iloc[0]["Close"]
        return closingPrice
    
    def GetQuote(self):
        """
        Gets the most recent closing of a stock

        Arguments:
        N/A

        Returns:
        quote: a Float64 value representing the most recent closing price
        """

        # obtaining stock data using the LookupQuote function and assigning it to data variable
        data = self.LookupQuote()
        # the last row of the dataframe will be the most recent trading day's data
        # the Close value is assigned to quote and returned
        quote = data.iloc[-1]["Close"]
        return quote
    
    def LookupQuote(self, date=None):
        """
        Obtains stock market data for a stock

        Arguments:
        date (optional): a String date value to search from

        Returns:
        data: a dataframe of stock market information
        """

        # using the history method of the Ticker class to obtain historical stock data
        # an optional date argument will determine what date to begin the dataframe with
        data = yfinance.Ticker(self._ticker).history(start=date)
        # if the dataframe is empty, that means that no market data was found
        # hence the ticker was invalid and an InvalidTicker exception is raised
        # otherwise, the dataframe is returned
        if data.empty:
            raise InvalidTicker
        else:
            return data
    
class InvalidTicker(Exception):
    "Raised when a ticker is invalid"
    pass

class MarketClosed(Exception):
    "Raised when the stock market is closed"
    pass





    

    





