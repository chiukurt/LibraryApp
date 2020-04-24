# Kurt Chiu 101190261
# COMP 2152 - Assignment - Winter 2020
"""
Object to hold books. Inherited by Cart and Shelf.

Ability to add books objects to list.
Ability to return formatted string of all books.

Chose list because referencing with index is the best choice.
Books can have share titles, authors or genres ergo require a unique identifier
"""
from Book import Book


class BookCollection():
    def __init__(self):
        self.books = []

    # Populate the books array with a single entry given information
    def add_book(self, title, author, category):
        self.books.append(Book(title, author, category))

    # Returns a formatted string for presentation of all books within the object currently
    def get_books(self):
        book_number = 1
        book_list = ""
        for book in self.books:
            book_list += (str(book_number) + ") " + book.category + " - " + book.title + " by " + book.author)
            book_list += "\n"
            book_number += 1
        return book_list
