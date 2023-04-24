from flask import render_template, redirect, request
from app import app
from models.books import *
from models.book import *

@app.route("/home")
def home():
    return render_template('home.html', title = "Home Page")


@app.route('/books') #default method is GET
def index():
    return render_template('index.html', title = "Books", books = books)

@app.route("/books/<index>") #this will return the details of a chosen book
def show_selected_book(index):
    return render_template("selected_book.html", book =books[int(index)]) #using the hyperlink added in the html/jinja file

@app.route("/books/add")
def books_add():
    return render_template("add_book.html")

@app.route('/books', methods = ['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    loaned = True if 'loaned' in request.form else False # will cause errors if not ticked hence else False is needed.
    location = request.form['location']
    synopsis = request.form['synopsis']
    unique_id = request.form['unique_id']
    new_book = Book(title, author, genre, loaned, location, synopsis, unique_id)
    add_new_book(new_book)
    return redirect("/books")

@app.route("/books/delete/<unique_id>", methods =['POST'])
def remove_book(unique_id):
    for book in books:
        if unique_id == book.unique_id:
            books.remove(book)
    return redirect("/home")
