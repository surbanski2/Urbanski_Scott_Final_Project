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


    

    





