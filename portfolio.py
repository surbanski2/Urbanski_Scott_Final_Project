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
    
    def PurchaseStock(self, quantity, price, ticker):

        """
        Removes cash from the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """

        if ticker in self._stocks:
            self._stocks[ticker] = self._stocks[ticker] + quantity
        else:
            self._stocks[ticker] = quantity

        totalCost = quantity * price
        self._cash = self._cash - totalCost

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

    def SellStock(self, quantity, price, ticker):

        """
        Adds cash to the portfolio

        Arguments:
        quantity: the number of shares purchased
        price: the purchase price

        Returns:
        N/A
        
        """

        self._stocks[ticker] = self._stocks[ticker] - quantity
        totalProceeds = quantity * price        
        self._cash = self._cash + totalProceeds

    def CalculatePortfolioValue(self):
        portfolioValue = 0
        portfolioValue = portfolioValue + self._cash
        for ticker in self._stocks:
            quantity = self._stocks[ticker]
            stock = Stock(ticker)
            portfolioValue = portfolioValue + (quantity*stock.GetQuote())
        return portfolioValue




