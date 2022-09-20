from models.book import Book
from models.book_list import *
from flask import render_template, request, redirect
from app import app

@app.route('/books')
def index():
    return render_template('index.html',title='Home', books=books)


@app.route('/books', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre, False, None)

    add_new_book(new_book)
    return redirect("/books")

@app.route('/books/delete/<title>', methods=['POST'])
def remove(title):
    remove_book(title)
    return redirect("/books")

@app.route("/book/<booknum>")
def specific_order(booknum):
    return render_template("book.html", book = books[int(booknum)])

@app.route("/books/checkout/<title>", methods=['POST'])
def check_out(title):
    check_out_book(title)
    return redirect('/books')

@app.route("/books/checkin/<title>", methods=['POST'])
def check_in(title):
    check_in_book(title)
    return redirect('/books')