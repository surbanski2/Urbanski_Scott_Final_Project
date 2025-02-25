"""
Author: Scott Urbanski
File: stock.py
Date Modified: 2025-02-25
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
        data = self.LookupQuote(date=date)
        firstDate = data.index[0]
        firstDateString = firstDate.strftime('%Y-%m-%d')
        if firstDateString != date:
            raise MarketClosed
        return data.iloc[0]["Open"]
    
    def GetClosingPrice(self, date):
        data = self.LookupQuote(date=date)
        print(data)
        firstDate = data.index[0]
        firstDateString = firstDate.strftime('%Y-%m-%d')
        if firstDateString != date:
            raise MarketClosed
        return data.iloc[0]["Close"]
    
    def GetQuote(self):
        data = self.LookupQuote()
        dataLength = len(data) - 1
        return data.iloc[dataLength]["Close"]
    
    def LookupQuote(self, date=None):
        data = yfinance.Ticker(self._ticker).history(start=date)
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


myStockTest = Stock("MGK")
print(myStockTest.GetClosingPrice("2022-02-02"))

    

    





