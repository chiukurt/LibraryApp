# Kurt Chiu 101190261
# COMP 2152 - Assignment - Winter 2020
"""
Object to hold books for the user to view.

Inherits BookCollection
Fills with books according to search criteria.
"""
from Book import Book
from BookCollection import BookCollection
import sqlite3


class Shelf(BookCollection):
    def __init__(self):
        BookCollection.__init__(self)

    # Fills shelf based on criteria using database entries
    def fill_books(self, cursor, filter_type="", filter=""):
        self.books.clear()
        if filter_type is "":
            query = ''' SELECT * FROM Books '''
        elif filter_type is "approxtitle":
            query = '''SELECT * FROM Books WHERE title LIKE "%''' + filter + '''%"'''

        elif filter_type is "approxauthor":
            query = '''SELECT * FROM Books WHERE author LIKE "%''' + filter + '''%"'''
        else:
            query = '''SELECT * FROM Books WHERE ''' + filter_type + ''' LIKE "''' + filter + '''"'''

        try:
            cursor.execute(query)
            result_set = cursor.fetchall()
            for row in result_set:
                self.books.append(Book(row["title"], row["author"], row["category"]))
        except sqlite3.OperationalError as e:
            print("Tables not found! Please ensure LibraryApp.sqlite is within root folder!", e)
