import pandas_datareader.data as pdrData
import pandas


class Stock:

    def __init__(self, ticker):
        self._ticker = ticker
        
    def GetOpeningPrice(self, date):
        try:
            data = pandas.DataFrame(pdrData.DataReader(name=self._ticker, data_source="stooq", start=date))
            theDate = data.index[-1]
            test = pandas.Timestamp.date(theDate)
            print(type(test))
            print(test)
        except: 
            raise InvalidTicker

        
        
        
        
 
        """
        data = pdrData.DataReader(name=self._ticker, data_source="stooq")
        if data.empty:
            raise InvalidTicker
    
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
    

    





