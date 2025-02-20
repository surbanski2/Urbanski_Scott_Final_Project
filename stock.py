import pandas_datareader.data as pdrData
import datetime as dt

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker

    def ValidTicker(self):
        validTicker = True
        data = pdrData.get_data_stooq(self._ticker)
        if data.empty:
            validTicker = False
        return validTicker
        

    

    def GetOpeningPrice(self, date):
        data =  pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Open']
    
    def GetClosingPrice(self, date):
        data = pdrData.DataReader(name=self, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Close']
    



testStock = Stock('PIK')
print(testStock.ValidTicker())

