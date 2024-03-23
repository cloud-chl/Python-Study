import random
from flask import Blueprint, request, render_template
from .models import *

blue = Blueprint('book', __name__)


@blue.route('/', methods=['GET', 'POST'])
@blue.route('/bookindex/', methods=['GET', 'POST'])
def book_index():
    return render_template('book_index.html')


@blue.route('/booklist/', methods=['GET', 'POST'])
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)


@blue.route('/bookdetail/<int:bid>/', methods=['GET', 'POST'])
def book_detail(bid):
    book = Book.query.get(bid)
    return render_template('book_detail.html', book=book)


# 作者详情
@blue.route('/authordetail/<int:aid>/', methods=['GET', 'POST'])
def author_detail(aid):
    author = Author.query.get(aid)
    return render_template('author_detail.html', author=author)


# 出版社详情
@blue.route('/publisherdetail/<int:pid>/', methods=['GET', 'POST'])
def publisher_detail(pid):
    publisher = Publisher.query.get(pid)
    return render_template('publisher_detail.html', publisher=publisher)
