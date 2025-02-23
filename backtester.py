from breezypythongui import EasyFrame
from portfolio import Portfolio
from stock import Stock

class Backtester(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.myPortfolio = Portfolio(10000)
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
        self.calculateButton = self.addButton(text="Calculate Portfolio Value", row=4, column=1)
        self.transactionList = self.addTextArea(text="", row=0, column=2, rowspan=3, width=50)

    def BuyStock(self):
        pass

    def SellStock(self):
        pass

def main():
    """Instantiates and pops up the window."""
    Backtester().mainloop()

if __name__ == "__main__":
    main()