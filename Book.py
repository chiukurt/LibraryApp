# Kurt Chiu 101190261
# COMP 2152 - Assignment - Winter 2020
"""
Object to hold information on a single book.
"""


class Book:
    def __init__(self, title="", author="", category=""):
        self.title = title
        self.author = author
        self.category = category
