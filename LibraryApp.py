# Kurt Chiu 101190261
# COMP 2152 - Assignment - Winter 2020
"""
Library: users should be able to search for books by title or
by author, should be able to search by book category
(fiction, non-fiction, autobiographies, travel, etc.).
The user should be able to purchase one or more books
in any combination of authors, titles, categories, etc.
The application should generate and display a receipt
stating the list of books selected and their return due dates.

 Outside of scope given description:
 -Ability to modify books within library (add, remove from database).
 -Handle duplicate books on cart (assume user wants multiple copies)
 -Remove books from cart

 Within scope:
 -Search book by title, author, category.
 -Add books to cart
 -Output receipt to file(cart). Due dates will be a constant of 3 weeks ahead of current time.

 Added functionality:
 -View cart
 """

from Shelf import Shelf
from Cart import Cart
import sqlite3
import sys


def get_integer(message=""):
    result = input(message)
    try:
        result = int(result)
    except ValueError as e:
        print("!!!Invalid input, could not convert to integer.\n", e)
    except:
        print("Unexpected error: ", sys.exc_info()[0])

    return result


def save_receipt_to_file(cart):
    receipt_file = open("Receipt" + cart.id + ".txt", "w")
    receipt_file.write(cart.get_receipt())
    receipt_file.close()


def get_filter(cursor, filter):
    cursor.execute('''SELECT DISTINCT ''' + filter + ''' FROM Books ''')
    result_set = cursor.fetchall()
    list_of_filter_options = []
    index = 1
    print("***List of books by " + filter + "***")
    for row in result_set:
        print(str(index) + ") " + row[0])
        list_of_filter_options.append(row[0])
        index += 1
    print()
    # index will be the largest after the for loop, ergo can be used as max value
    inp = -1
    while inp < 1 or inp > index - 1:
        inp = get_integer(message="Select a " + filter + " by inputting a whole number within the list.")
    return str(list_of_filter_options[int(inp) - 1])


def add_book_to_cart(book_shelf, my_cart):
    # Accepts book ID from shelf to add to my_cart
    max = len(book_shelf.books)
    inp = get_integer(message="Select an option by inputting a whole number within the above list."
                              "\nOr enter 0 to return to the main menu.")
    if inp < 0 or inp > max:
        print("Failed. Invalid ID. Returning to main menu.")
    elif inp is 0:
        print("Returning to main menu.")
    else:
        book = book_shelf.books[inp - 1]
        my_cart.add_book(book.title, book.author, book.category)
        print("Success! Added '" + book.title + "' to cart.. Returning to main menu.")


def view_books_no_filter(book_shelf, my_cart):
    # Load library without filters and show entire library
    book_shelf.fill_books(c)
    print(book_shelf.get_books())
    add_book_to_cart(book_shelf, my_cart)


def view_books_with_filter(book_shelf, my_cart):
    # Search with criteria defined by user
    print("\n*********Search Menu*********")
    print("1) Search books by approximate title")
    print("2) Search books by approximate author name")
    print("3) View all authors and filter books")
    print("4) View all genres and filter books")

    inp = -1
    while inp < 1 or inp > 4:
        inp = get_integer(message="Select an option by inputting a whole number within the above list.")

    # Populates book_shelf with relevant rows based on search criteria and database
    if inp is 1:
        title_input = input("Please enter a title to search for")
        book_shelf.fill_books(cursor=c, filter_type="approxtitle", filter=title_input)
        print("\n***List of books with title resembling: " + title_input + "***")
    elif inp is 2:
        author_input = input("Please enter an author to search for")
        book_shelf.fill_books(cursor=c, filter_type="approxauthor", filter=author_input)
        print("\n***List of books with author resembling: " + author_input + "***")
    elif inp is 3:
        filter = get_filter(c, "author")
        book_shelf.fill_books(c, "author", filter)
        print("\n***List of books with author of: " + filter + "***")
    elif inp is 4:
        filter = get_filter(c, "category")
        book_shelf.fill_books(c, "category", filter)
        print("\n***List of books with genre of: " + filter + "***")

    print(book_shelf.get_books())
    # Adds books to cart pulled from current shelf
    add_book_to_cart(book_shelf, my_cart)


def main_menu_loop():
    book_shelf = Shelf()
    my_cart = Cart()
    inp = -1
    while inp is not 5:
        inp = -1
        print("\n*****Welcome to the Library Application Main Menu*****")
        print("1) Add a book to my cart by viewing all books")
        print("2) Add a book to my cart by searching")
        print("3) View my cart")
        print("4) Print my receipt")
        print("5) Exit")
        while inp < 1 or inp > 5:
            inp = get_integer(message="Select an option by inputting a whole number within the above list.")

        if inp is 1:
            view_books_no_filter(book_shelf, my_cart)
        elif inp is 2:
            view_books_with_filter(book_shelf, my_cart)
        elif inp is 3:
            print("******List of books within cart******")
            print(my_cart.get_books())
        elif inp is 4:
            save_receipt_to_file(my_cart)
            print("****RECEIPT GENERATED IN ROOT FOLDER****")

    print("\n***Closing application. Goodbye!***")


if __name__ == '__main__':
    conn = sqlite3.connect("LibraryApp.sqlite")
    c = conn.cursor()

    # Allows database result sets to be accessed like an associative array
    c.row_factory = sqlite3.Row  # Row is a constant
    main_menu_loop()

    if conn:
        conn.close()
