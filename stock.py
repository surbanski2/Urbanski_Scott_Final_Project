import pandas_datareader as pd

class Stock:

    def __init__(self, ticker):
        self._ticker = ticker
        self._price = 0.0

    def GetOpeningPrice(self):
        self._price = pd.get_data_yahoo(self._ticker)

    def GetClosingPrice(self):
        self._price = pd.get_data_yahoo()

def main():
    testStock = Stock('MGK')
    print(testStock.GetOpeningPrice())

if __name__ == "__main__":
    main()