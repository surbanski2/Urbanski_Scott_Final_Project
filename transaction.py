class Transaction:

    def __init__(self, bought, quantity, ticker, price, date):
        self._bought = bought
        self._quantity = quantity
        self._ticker = ticker
        self._price = price
        self._date = date

    def OutputString(self):
        outputString = ""
        if self._bought == True:
            outputString = f"Bought {self._quantity} shares of {self._ticker} at a price of ${self._price} on {self._date}."
        else:
            outputString = f"Sold {self._quantity} shares of {self._ticker} at a price of ${self._price} on {self._date}."
        return outputString
