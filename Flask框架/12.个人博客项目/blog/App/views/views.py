from flask import Blueprint, request, render_template
from ..models.models import *

blog = Blueprint('user', __name__)


@blog.route('/', methods=['GET', 'POST'])
@blog.route('/index/', methods=['GET', 'POST'])
def blog_index():
    photos = PhotoModel.query.limit(6)
    categorys = CategoryModel.query.all()
    articles = ArticleModel.query.all()
    commends = articles[:4]
    return render_template('home/index.html',
                           categorys=categorys,
                           photos=photos,
                           articles=articles,
                           commends=commends)


# 博客-我的相册
@blog.route('/photos/', methods=['GET', 'POST'])
def blog_photos():
    photos = PhotoModel.query.limit(6)
    return render_template('home/photos.html', photos=photos)


# 博客-我的日记
@blog.route('/article/', methods=['GET', 'POST'])
def blog_article():
    categorys = CategoryModel.query.all()
    articles = ArticleModel.query.all()
    return render_template('home/article.html',
                           categorys=categorys,
                           articles=articles)


# 博客-关于我
@blog.route('/about/', methods=['GET', 'POST'])
def blog_about():
    categorys = CategoryModel.query.all()
    photos = PhotoModel.query.limit(6)
    return render_template('home/about.html',
                           categorys=categorys,
                           photos=photos)