from flask import render_template, redirect, request
from app import app
from models.books import books
from models.book import *


@app.route('/books') #default method is GET
def index():
    return render_template('index.html', title = "Home Page", books = books)

@app.route("/books/<index>") #this will return the details of a chosen book
def show_selected_book(index):
    return render_template("selected_book.html", book =books[int(index)]) #using the hyperlink added in the html/jinja file

#@app.route('/events', methods = ['POST'])
# def add_event():
#     date = request.form['date']
#     split_date = date.split("-")
#     date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
#     name = request.form['name']
#     guests = request.form['guests']
#     recurring = True if 'recurring' in request.form else False # will cause errors if not ticked hence else False is needed.
#     room_location = request.form['room_location']
#     description = request.form['description']
#     new_event = Event(date, name, guests, recurring, room_location, description)
#     add_new_event(new_event)
#     return render_template('index.html', title='Home', events=events) #add redirect here instead of render 

# @app.route("/books/book/<unique_id>", methods =['POST'])
# def remove_book(unique_id):
#     for book in books:
#         if unique_id == book.unique_id:
#             books.remove(book)
#     return redirect("/books")
