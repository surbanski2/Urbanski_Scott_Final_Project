"""
Author: Scott Urbanski
File: backtester.py
Date Modified: 2025-02-28
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
import portfolio
from transaction import Transaction
import stock
from dateutil import parser
from datetime import datetime
import pygal
import copy

class Backtester(EasyFrame):
    """Displays a GUI for entering stock transactions and calculating and displaying results."""

    def __init__(self):
        """Sets up the window and the components."""
        EasyFrame.__init__(self)
        self.myPortfolio = portfolio.Portfolio(10000)
        self.myTransactions = []
        self.myPortfolioSnapshots = []
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
        self.graphButton = self.addButton(text="Visualize Portfolio", row=5, column=0, columnspan=2, command=self.VisuializePortfolio)

    def BuyStock(self): 
        """
        Attempts to purchase stock based on the user's inputs

        Arguments:
        N/A

        Returns:
        N/A
        """

        # creates a stock object based on the user's ticker input
        userStock = stock.Stock(self.tickerInput.getText())

        try:
            # if the user has entered an invalid quantity, an error message is produced
            if self.ValidQuantity() == False:
            # if the user has entered a non-date in the date field, an error message is produced
                self.messageBox(title="Error", message="Quantity of shares must be positive!")
            # if the user has entered a non-date in the date field, an error message is produced
            elif self.ValidDate() == False:
                self.messageBox(title="Error", message="You have entered an invalid date!")
            # if the user has entered a date that is either in the future or prior to the most recent transaction, an error message is produced
            elif self.AcceptableDate() == False:
                self.messageBox(title="Error", message="You must enter a date between the ranges.")
            else:
                # the stock is added to the portfolio and cash is removed
                self.myPortfolio.PurchaseStock(float(self.quantityInput.getText()), userStock.GetOpeningPrice(self.dateInput.getText()), userStock._ticker)
                # a transaction is added to the list of transactions
                self.myTransactions.append(Transaction(True, float(self.quantityInput.getText()), userStock._ticker,userStock.GetOpeningPrice(self.dateInput.getText()), self.dateInput.getText()))
                # the latest transaction's documentation is added to the text area for the user to see
                self.transactionList.appendText(self.myTransactions[-1].OutputString() + "\n")
                # the date of the transaction and portfolio value at that date are added as a tuple to the snapshots for viewing as a chart
                self.myPortfolioSnapshots.append((parser.parse(self.dateInput.getText()),self.myPortfolio.CalculatePortfolioValue(date=self.dateInput.getText())))
                # the date of the most recent transaction is updated to ensure transactions are added chronologically
                self.currentDate = self.dateInput.getText()

        # if the user has entered a ticker that does not exist, the InvalidTicker exception will be raised and an error message shown
        except stock.InvalidTicker:
            self.messageBox(title="Error", message="You have entered an invalid ticker!")
        # if the user has entered a date when the stock market was closed, the MarketClosed exception will be raised and an error message shown
        except stock.MarketClosed:
            self.messageBox(title="Error", message="The stock market was closed!")
        # if the user does not have enough funds, the InsufficientFunds exception will be raised and an error message shown
        except portfolio.InsufficientFunds:
            self.messageBox(title="Error", message="You do not have enough funds to purchase the desired quantity!")
        finally:
            # all the entry fields are reset to their original state
            self.ResetFields()


    def SellStock(self):
        """
        Attempts to sell stock based on the user's inputs

        Arguments:
        N/A

        Returns:
        N/A
        """

        # creates a stock object based on the user's ticker input
        userStock = stock.Stock(self.tickerInput.getText())

        try:
            # if the user has entered an invalid quantity, an error message is produced
            if self.ValidQuantity() == False:
                self.messageBox(title="Error", message="Quantity of shares must be positive!")
            # if the user has entered a non-date in the date field, an error message is produced
            elif self.ValidDate() == False:
                self.messageBox(title="Error", message="You have entered an invalid date!")
            # if the user has entered a date that is either in the future or prior to the most recent transaction, an error message is produced
            elif self.AcceptableDate() == False:
                self.messageBox(title="Error", message="You must enter a date between the ranges.")
            # if all the tests resulted in True and no exceptions were raised, the user can sell the stock
            else:
                # the stock is removed from the portfolio and cash is added
                self.myPortfolio.SellStock(float(self.quantityInput.getText()), userStock.GetClosingPrice(date=self.dateInput.getText()), userStock._ticker)
                # a transaction is added to the list of transactions
                self.myTransactions.append(Transaction(False, float(self.quantityInput.getText()), userStock._ticker,userStock.GetClosingPrice(date=self.dateInput.getText()), self.dateInput.getText()))
                # the latest transaction's documentation is added to the text area for the user to see
                self.transactionList.appendText(self.myTransactions[-1].OutputString() + "\n")
                # the date of the transaction and portfolio value at that date are added as a tuple to the snapshots for viewing as a chart
                self.myPortfolioSnapshots.append((parser.parse(self.dateInput.getText()),self.myPortfolio.CalculatePortfolioValue(date=self.dateInput.getText())))
                # the date of the most recent transaction is updated to ensure transactions are added chronologically
                self.currentDate = self.dateInput.getText()
        # if the user has entered a ticker that does not exist, the InvalidTicker exception will be raised and an error message shown
        except stock.InvalidTicker:
            self.messageBox(title="Error", message="You have entered an invalid ticker!")
        # if the user has entered a date when the stock market was closed, the MarketClosed exception will be raised and an error message shown
        except stock.MarketClosed:
            self.messageBox(title="Error", message="The stock market was closed!")
        # if the user does not have enough shares to sell, the InsufficientShares exception will be raised and an error message shown
        except portfolio.InsufficientShares:
            self.messageBox(title="Error", message="You do not have enough shares to sell the desired quantity!")
        finally:
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
        """
        Tests to ensure the user has entered a date that is in the past but occurred after the most recent transaction date

        Arguments:
        N/A

        Returns:
        acceptableDate: a Boolean value determining whether or not the user has entered an appropriate date
        """

        acceptableDate = True
        # the parser compares the most recent transaction date (currentDate) and the date the user has entered
        # if the user has entered a date earlier than the currentDate, acceptableDate is False
        if parser.parse(self.currentDate) > parser.parse(self.dateInput.getText()):
            acceptableDate = False
        # the parser compares the user's date and today's date
        # if the user has entered a date in the future, acceptableDate is False
        if parser.parse(self.dateInput.getText()) > datetime.now():
            acceptableDate = False
        return acceptableDate
    
    def CaclulatePortfolio(self):
        """
        Calculates the present-day value of the portfolio

        Arguments:
        N/A

        Returns:
        N/A
        """

        # Updates the label's text to show the current portfolio value; a date of None is used to get the most recent prices
        self.portfolioLabel["text"] = f"Portfolio Value: ${self.myPortfolio.CalculatePortfolioValue(date=None) :,.2f}"
    
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

    def VisuializePortfolio(self):
        """
        Creates a line graph of the portfolio's valuation over time

        Arguments:
        N/A

        Returns:
        N/A
        """

        views = copy.deepcopy(self.myPortfolioSnapshots)
        views.append((datetime.now(), self.myPortfolio.CalculatePortfolioValue(date=None)))
        chart = pygal.Line()
        dates = []
        values = []
        for items in views:
            dates.append(items[0].strftime('%Y-%m-%d'))
            values.append(items[1])
        chart.x_labels = dates
        chart.add('Portfolio Value', values)
        chart.render_in_browser()

        print(self.myPortfolioSnapshots)









        """


        # points to the list of snapshots
        views = self.myPortfolioSnapshots
        # adds another snapshot of the present day value
        views.append((datetime.now(), self.myPortfolio.CalculatePortfolioValue(date=None)))
        # creates the line chart
        chart = pygal.DateLine()
        # uses a comprehension to add the tuples from views to the chart
        chart.add('Portfolio Value', [view for view in views])
        # renders the chart in the browser
        chart.render_in_browser()

        """

def main():
    """Instantiates and pops up the window."""
    Backtester().mainloop()

if __name__ == "__main__":
    # checks to see if the script's __name__ variable is main (ie not an imported module) and runs the main() function
    main()

