import yfinance

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker
        
    def GetOpeningPrice(self, date):
        data = yfinance.Ticker(self._ticker).history(start=date)
        if data.empty:
            raise InvalidTicker
        firstDate = data.index[0]
        firstDateString = firstDate.strftime('%Y-%m-%d')
        if firstDateString != date:
            raise MarketClosed
        return data.iloc[0]["Open"]
        
    """

    
    def GetClosingPrice(self, date):
        data = pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Close']
    
    def GetQuote(self):
        data = pdrData.DataReader(name=self._ticker, data_source="stooq")
        return data.iloc[0]['Close']
    """
    
class InvalidTicker(Exception):
    "Raised when a ticker is invalid"
    pass

class MarketClosed(Exception):
    "Raised when the stock market is closed"
    pass
    

    





