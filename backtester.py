"""
Author: Scott Urbanski
File: backtester.py
Date Modified: 2025-02-23
Description: This GUI application allows the user to enter
             a stock ticker, a quantity, and a date. The
             user can then choose to either buy or sell 
             the stock. After making the desired transactions,
             the user can then click the Calculate button
             to see how much the portfolio would have 
             increased (or decreased) in value at the present
             day.
"""

from breezypythongui import EasyFrame
from portfolio import Portfolio
from transaction import Transaction
from stock import Stock
from dateutil import parser
import datetime

class Backtester(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.myPortfolio = Portfolio(10000)
        self.myTransactions = []
        self.currentDate = "1900-01-01"
        self.setTitle("Portfolio Backtester")
        self.setResizable(False)
        self.tickerLabel = self.addLabel(text="Ticker:", row=0, column=0)
        self.tickerInput = self.addTextField(text="", row=0, column=1)
        self.quantityLabel = self.addLabel(text="Quantity:", row=1, column=0)
        self.quantityInput = self.addTextField(text="0", row=1, column=1)
        self.dateLabel = self.addLabel(text="Date:", row=2, column=0)
        self.dateInput = self.addTextField(text="yyyy-mm-dd", row=2, column=1)
        self.buyButton = self.addButton(text="Buy Stock", row=3, column=0, command=self.BuyStock)
        self.sellButton = self.addButton(text="Sell Stock", row=3, column=1, command=self.SellStock)
        self.portfolioLabel = self.addLabel(text=f"Portfolio Value: ${self.myPortfolio.CalculatePortfolioValue() :,.2f}", row=4, column=0)
        self.calculateButton = self.addButton(text="Calculate Portfolio Value", row=4, column=1, command=self.CaclulatePortfolio)
        self.transactionList = self.addTextArea(text="", row=0, column=2, rowspan=3, width=50)

    def BuyStock(self): 
        """
        Attempts to purchase stock based on the user's inputs

        Arguments:
        N/A

        Returns:
        N/A
        """

        # creates a stock object based on the user's ticker input
        userStock = Stock(self.tickerInput.getText())
        # tests if the user has entered a valid stock ticker
        if userStock.ValidTicker() == True:
            # tests if the user has entered a valid quantity
            if self.ValidQuantity() == True:
                # tests if the user has entered a valid date
                if self.ValidDate() == True:
                    if self.AcceptableDate() == True:
                        # tests if the stock market was open on the date the user selected
                        if userStock.MarketOpen(self.dateInput.getText()) == True:
                            # tests if the user can afford to purchase the stock he/she wants to purchase
                            if self.myPortfolio.AbleToBuy(float(self.quantityInput.getText()), userStock.GetOpeningPrice(self.dateInput.getText())) == True:
                                # if the user can afford it, then the stock ticker and its quantity are added to the portfolio
                                self.myPortfolio.AddStock(userStock._ticker, float(self.quantityInput.getText()))
                                # the appropriate amount of cash is removed from the portfolio
                                self.myPortfolio.DebitCash(float(self.quantityInput.getText()), userStock.GetOpeningPrice(self.dateInput.getText()))
                                # a transaction is added to the list of transactions
                                self.myTransactions.append(Transaction(True, float(self.quantityInput.getText()), userStock._ticker,userStock.GetOpeningPrice(self.dateInput.getText()), self.dateInput.getText()))
                                # the most recent transaction is outputted to the text area to confirm the purchase was successful
                                self.transactionList.appendText(self.myTransactions[-1].OutputString() + "\n")
                                self.currentDate = self.dateInput.getText()
                            else:
                                self.messageBox(title="Error", message="You cannot afford to purchase the entered quantity!")
                        else:
                            self.messageBox(title="Error", message="The stock market was not open!")  
                    else:
                        self.messageBox(title="Error", message="You must enter a date between the ranges.")
                else:
                    self.messageBox(title="Error", message="You have entered an invalid date!")

            else:
                self.messageBox(title="Error", message="Quantity of shares must be positive!")
        else:
            self.messageBox(title="Error", message="You have entered an invalid ticker!")
        # all the entry fields are reset to their original state
        self.ResetFields()

        print(self.currentDate)

    def SellStock(self):
        """
        Attempts to sell stock based on the user's inputs

        Arguments:
        N/A

        Returns:
        N/A
        """

        # creates a stock object based on the user's ticker input
        userStock = Stock(self.tickerInput.getText())
        # tests if the user has entered a valid stock ticker
        if userStock.ValidTicker() == True:
            # tests if the user has entered a valid quantity
            if self.ValidQuantity() == True:
                # tests if the user has entered a valid date
                if self.ValidDate() == True:
                    if self.AcceptableDate() == True:
                         # tests if the stock market was open on the date the user selected
                        if userStock.MarketOpen(self.dateInput.getText()) == True:
                            # tests if the user has the stock in the portfolio to sell
                            if self.myPortfolio.AbleToSell(float(self.quantityInput.getText()), userStock._ticker) == True:
                                # if the user can sell it, then the stock ticker and its quantity are removed from the portfolio
                                self.myPortfolio.RemoveStock(userStock._ticker, float(self.quantityInput.getText()))
                                 # the appropriate amount of cash is added from the portfolio
                                self.myPortfolio.CreditCash(float(self.quantityInput.getText()), userStock.GetClosingPrice(self.dateInput.getText()))
                                # a transaction is added to the list of transactions
                                self.myTransactions.append(Transaction(False, float(self.quantityInput.getText()), userStock._ticker,userStock.GetClosingPrice(self.dateInput.getText()), self.dateInput.getText()))
                                # the most recent transaction is outputted to the text area to confirm the purchase was successful
                                self.transactionList.appendText(self.myTransactions[-1].OutputString() + "\n")
                                self.currentDate = self.dateInput.getText()
                            else:
                                self.messageBox(title="Error", message="You do not have enough shares to sell!")
                        else:
                            self.messageBox(title="Error", message="The stock market was not open!")
                    else:
                        self.messageBox(title="Error", message="The date must be between the previous transaction date and the present day!")
                else:
                    self.messageBox(title="Error", message="You have entered an invalid date!")
            else:
                self.messageBox(title="Error", message="Quantity of shares must be positive!")
        else:
            self.messageBox(title="Error", message="You have entered an invalid ticker!")
        # all the entry fields are reset to their original state

        self.ResetFields()

    def ValidQuantity(self):
        """
        Tests if the user has entered a valid quantity

        Arguments:
        N/A

        Returns:
        validQuantity: a Boolean value determining whether or not the user has entered an appropriate quantity
        """
        # the user is assumed to have entered a valid quantity
        validQuantity = True
        try:
            # the user's input is converted to a float and checked to make sure it is greater than zero
            # if it is less than or equal to zero, or if an error has occurred, validQuantity is set to False
            if float(self.quantityInput.getText()) <= 0:
                validQuantity = False
        except:
            validQuantity = False
        return validQuantity
    
    def ValidDate(self):
        """
        Tests if the user has entered a valid date

        Arguments:
        N/A

        Returns:
        validDate: a Boolean value determining whether or not the user has entered an appropriate date
        """
        # the user is assumed to have entered a valid date
        validDate = True
        try:
            # the parser module's parse method attempts to parse the date the user has supplied
            # if it fails to parse the date, then an error has occurred and validDate os set to False
            parser.parse(self.dateInput.getText())
        except:
            validDate = False
        return validDate
    
    def AcceptableDate(self):
        acceptableDate = True
        if parser.parse(self.currentDate) > parser.parse(self.dateInput.getText()):
            acceptableDate = False
        if parser.parse(self.dateInput.getText()) > datetime.datetime.now():
            acceptableDate = False
        return acceptableDate
    
    def CaclulatePortfolio(self):
        self.portfolioLabel["text"] = f"Portfolio Value: ${self.myPortfolio.CalculatePortfolioValue() :,.2f}"
        print(self.myPortfolio._stocks)
        print(self.myPortfolio._cash)
    
    def ResetFields(self):
        """
        Returns the entry fields to their original state

        Arguments:
        N/A

        Returns:
        N/A
        """

        self.tickerInput.setText("")
        self.quantityInput.setText("0")
        self.dateInput.setText("yyyy-mm-dd")

def main():
    """Instantiates and pops up the window."""
    Backtester().mainloop()

if __name__ == "__main__":
    main()