class Portfolio:

    def __init__(self, cash):
        self._cash = cash
        self._stocks = {}

    @property
    def cash(self):
        return self._cash
    
    @property
    def stocks(self):
        return self._stocks
    
    def DebitCash(self, amount):
        self._cash = self._cash - amount

    def CreditCash(self, amount):
        self._cash = self._cash + amount

