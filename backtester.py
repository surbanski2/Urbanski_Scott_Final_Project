from breezypythongui import EasyFrame
from portfolio import Portfolio
from stock import Stock

class Backtester(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.myPortfolio = Portfolio(10,000)
        self.setTitle("Portfolio Backtester")
        self.setResizable(False)
        self.addLabel(text="Ticker:", row=0, column=0)
        self.addTextField(text="", row=0, column=1)
        self.addLabel(text="Quantity:", row=1, column=0)
        self.addTextField(text="0", row=1, column=1)
        self.addLabel(text="Date:", row=2, column=0)
        self.addTextField(text="yyyy-mm-dd", row=2, column=1)
        self.addButton(text="Buy Stock", row=3, column=0, command=self.BuyStock)
        self.addButton(text="Sell Stock", row=3, column=1, command=self.SellStock)
        self.addLabel(text=f"Portfolio Value: $10,000", row=4, column=0)
        self.addButton(text="Calculate Portfolio Value", row=4, column=1)
        self.addTextArea(text="", row=0, column=2, rowspan=3, width=50)

    def BuyStock(self):
        pass

    def SellStock(self):
        pass

def main():
    """Instantiates and pops up the window."""
    Backtester().mainloop()

if __name__ == "__main__":
    main()