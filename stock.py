import pandas_datareader.data as pdrData

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker

    def ValidTicker(self):
        validTicker = True
        data = pdrData.get_data_stooq(self._ticker)
        if data.empty:
            validTicker = False
        return validTicker
    
    def MarketOpen(self, date):
        marketOpen = True
        data = pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        if data.empty:
            marketOpen = False
        return marketOpen
        
    def GetOpeningPrice(self, date):
        data =  pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Open']
    
    def GetClosingPrice(self, date):
        data = pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Close']
    
    def GetQuote(self):
        data = pdrData.DataReader(name=self._ticker, data_source="stooq")
        return data.iloc[0]['Close']
    
myTest = Stock("MGK")
print(myTest.MarketOpen("2025-03-23"))
    





