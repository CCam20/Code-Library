from models.book import *

book1 = Book("The Martian", "Andy Weir", "Science fiction, Novel", True)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel, Fiction, Tragedy", False)
book3 = Book("The Catcher in the Rye", "J. D. Salinger","Novel, First-person narrative", True)
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