from models.book import *
from datetime import datetime, timedelta

book1 = Book("The Martian", "Andy Weir", "Science fiction, Novel", False, None)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel, Fiction, Tragedy", False, None)
book3 = Book("The Catcher in the Rye", "J. D. Salinger","Novel, First-person narrative", False, None)
books= [book1,book2,book3]

def add_new_book(book):
    books.append(book)

# def remove_book(book):
#     for book in books:
#         if book.title == book:
#             books.remove(book)

def remove_book(book_name):
    book_to_remove = None
    for book in books:
        if book.title == book_name:
            book_to_remove = book
            break

    books.remove(book_to_remove)

def check_out_book(book_name):
    for book in books:
        if book.title == book_name:
            book.checked_out = True   
        dt = datetime.now()
        td = timedelta(days=28)
        return_date = dt + td
        year = return_date.strftime("%Y")
        month = return_date.strftime("%m")
        day = return_date.strftime("%d")
        book.return_date = f"{day}/{month}/{year}"

def check_in_book(book_name):
    for book in books:
        if book.title == book_name:
            book.checked_out = False
        