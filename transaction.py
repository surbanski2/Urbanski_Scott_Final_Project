"""
Author: Scott Urbanski
File: transaction.py
Date Modified: 2025-02-25
Description: This module contains the class
             definition for a stock transaction.
"""



class Transaction:

    def __init__(self, bought, quantity, ticker, price, date):
        self._bought = bought
        self._quantity = quantity
        self._ticker = ticker
        self._price = price
        self._date = date

    def OutputString(self):
        """
        Creates a string description of a stock transaction

        Arguments:
        N/A

        Returns:
        outputString: a String value describing the stock transaction 
        """

        outputString = ""
        # if the bought property is True, the user bought stock so "Bought" is used for the string
        if self._bought == True:
            outputString = f"Bought {self._quantity} shares of {self._ticker} at a price of ${self._price} on {self._date}."
        # otherwise the bought property is False, so the user sold stock so "Sold" is used for the string
        else:
            outputString = f"Sold {self._quantity} shares of {self._ticker} at a price of ${self._price} on {self._date}."
        return outputString
