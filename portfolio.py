from stock import Stock


class Portfolio:

    def __init__(self, cash):
        self._cash = cash
        self._stocks = {}

    def AbleToBuy(self, quantity, price):

        """
        Checks to see if the user can purchase the stock

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        ableToBuy: a Boolean value determining whether or not the user can afford the purchase
        """
        
        ableToBuy = True
        if quantity * price > self._cash:
            ableToBuy = False
        return ableToBuy
    
    def DebitCash(self, quantity, price):

        """
        Removes cash from the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """

        totalCost = quantity * price
        self._cash = self._cash - totalCost

    def AddStock(self, ticker, quantity):

        """
        Adds stock to the portfolio

        Arguments:
        ticker: the stock ticker
        quantity: the number of shares purchased

        Returns:
        N/A
        
        """

        if ticker in self._stocks:
            self._stocks[ticker] = self._stocks[ticker] + quantity
        else:
            self._stocks[ticker] = quantity

    def AbleToSell(self, quantity, ticker):

        """
        Checks to see if the user can sell the stock

        Arguments:
        quantity: the number of shares purchased
        ticker: the stock ticker

        Returns:
        ableToSell: a Boolean value determining whether or not the user can sell the stock
        """
                
        ableToSell = False
        if ticker in self._stocks:
            if self._stocks[ticker] >= quantity:
                ableToSell = True
        return ableToSell

    def CreditCash(self, quantity, price):

        """
        Adds cash to the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """

        totalProceeds = quantity * price        
        self._cash = self._cash + totalProceeds

    def RemoveStock(self, ticker, quantity):

        """
        Removes stock from the portfolio

        Arguments:
        ticker: the stock ticker
        quantity: the number of shares purchased

        Returns:
        N/A
        
        """

        self._stocks[ticker] = self._stocks[ticker] - quantity

    def CalculatePortfolioValue(self):
        portfolioValue = 0
        portfolioValue = portfolioValue + self._cash
        for ticker in self._stocks:
            quantity = self._stocks[ticker]
            stock = Stock(ticker)
            portfolioValue = portfolioValue + (quantity*stock.GetQuote())
        return portfolioValue




