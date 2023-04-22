from flask import render_template, redirect, request
from app import app
from models.books import books
from models.book import *


@app.route('/books') #default method is GET
def index():
    return render_template('index.html', title = "Home Page", books = books)