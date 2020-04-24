# Kurt Chiu 101190261
# COMP 2152 - Assignment - Winter 2020
"""
Object to hold books user wishes to purchase.

Inherits BookCollection
Generates unique receipt ID
Allows retrieval of receipt string
"""
from Book import Book
from Shelf import Shelf
from BookCollection import BookCollection
from datetime import date, timedelta
import time


class Cart(BookCollection):
    def __init__(self):
        self.id = str(round(time.time()))
        BookCollection.__init__(self)

    def get_receipt(self):
        receipt = "***Receipt for " + self.id + "***\n"
        receipt += (self.get_books())
        receipt += ("Borrow date: " + str(date.today()))
        receipt += ("\nReturn date: " + str(date.today() + timedelta(days=21)))
        return receipt
