import pandas_datareader.data as pdrData

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker

    def GetOpeningPrice(self, date):
        data =  pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)
        return data.iloc[0]['Open']
    
    



testStock = Stock('MGK')
print(testStock.GetOpeningPrice('2025-02-18'))

