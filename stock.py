import pandas_datareader.data as pdrData

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker
        self._price = 0.0

    def GetOpeningPrice(self, date):
        return pdrData.DataReader(name=self._ticker, data_source="stooq", start=date, end=date)



testStock = Stock('MGK')
print(testStock.GetOpeningPrice('2025-02-18'))

