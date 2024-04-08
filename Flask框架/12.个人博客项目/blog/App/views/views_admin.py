from flask import Blueprint, request, render_template, redirect, jsonify
from ..models.models_admin import *
from ..models.models import *
from functools import wraps
import time

admin = Blueprint('admin', __name__)

# 装饰器： 登录验证
def login_required(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        # 判断用户是否已登录
        user_id = request.cookies.get('user_id', None)
        if user_id:
            user = AdminUserModel.query.get(user_id)
            request.user = user
            return fn(*args, **kwargs)
        else:
            return redirect('/admin/login/')
    return inner

# 后台管理-首页
@admin.route('/', methods=['GET', 'POST'])
@admin.route('/admin/index/', methods=['GET', 'POST'])
@login_required
def index():
    # 获取cookie， 得到登录用户
    # user_id = request.cookies.get('user_id', None)
    # if user_id:
    #     # 登录后，进入后台管理首页
    #     user = AdminUserModel.query.get(user_id)
    #     categorys = CategoryModel.query.filter()
    #     aritcles = ArticleModel.query.filter()
    #     photos = PhotoModel.query.filter()
    #     return render_template('admin/index.html',
    #                            username=user.name,
    #                            categorys=categorys,
    #                            aritcles=aritcles,
    #                            photos=photos
    #                            )
    # else:
    #     #  如果没有登录，则跳转到登录页面
    #     return redirect('/admin/login/')

    user = request.user
    categorys = CategoryModel.query.filter()
    aritcles = ArticleModel.query.filter()
    photos = PhotoModel.query.filter()

    return render_template('admin/index.html',
                                      username=user.name,
                                      categorys=categorys,
                                      aritcles=aritcles,
                                      photos=photos
                                      )

# 后台管理-登录
@admin.route('/admin/login/', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'GET':
        return render_template('admin/login.html')

    elif request.method == 'POST':
        username = request.form.get('username')
        userpwd = request.form.get('userpwd')

        # 登录验证：验证用户名和密码是否匹配
        user = AdminUserModel.query.filter_by(name=username, passwd=userpwd).first()
        if user:
            # 登录成功
            response = redirect('/admin/index/')
            response.set_cookie('user_id', str(user.id), max_age=7 * 24 * 3600)
            return response
        else:
            return 'Login Failed'

# 后台管理-退出登录
@admin.route('/admin/logout/', methods=['GET', 'POST'])
def admin_logout():
    response = redirect('/admin/login/')
    response.delete_cookie('user_id')
    return response

# 后台管理-分类管理
@admin.route('/admin/category/')
@login_required
def admin_category():
    categorys = CategoryModel.query.all()
    return render_template('admin/category.html',
                           username=request.user,
                           categorys=categorys
                           )

# 后台管理-添加分类
@admin.route('/admin/addcategory/', methods=['GET', 'POST'])
@login_required
def admin_add_category():
    if request.method == 'POST':
        name = request.form.get('name')
        describe = request.form.get('describe')

        # 添加分类
        category = CategoryModel()
        category.name = name
        category.describe = describe

        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            print(f'{e}')
            db.session.rollback()
        return redirect('/admin/category/')

    else:
        return "请求方式错误！"

# 后台管理-删除分类
@admin.route('/admin/delcategory/', methods=['GET', 'POST'])
@login_required
def admin_del_category():
    if request.method != 'POST':
        return jsonify({'code': 400, 'msg': '请求方式错误!'})

    id = request.form.get('id')
    category = CategoryModel.query.get(id)
    # 删除分类
    try:
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        return jsonify({'code': 500, 'msg': f'删除过程中发生错误: {str(e)}'})

    return jsonify({'code': 200, 'msg':'删除成功!'})

# 后台管理-更新分类
@admin.route('/admin/updatecategory/<id>/', methods=['GET', 'POST'])
@login_required
def admin_update_category(id):

    if request.method == 'POST':
        name = request.form.get('name')
        describe = request.form.get('describe')

        # 修改
        category = CategoryModel.query.get(id)
        category.name = name
        category.describe = describe
        try:
            db.session.commit()
        except Exception as e:
            print(f'e')

        return redirect('/admin/category/')


    category = CategoryModel.query.get(id)
    return render_template('admin/category_update.html',
                           category=category)

# 后台管理-文章管理
@admin.route('/admin/article/')
@login_required
def admin_article():
    articles = ArticleModel.query.all()
    return render_template('admin/article.html',
                           username=request.user.name,
                           articles=articles
                           )

# 后台管理-添加文章
@admin.route('/admin/addarticle/', methods=['GET', 'POST'])
@login_required
def admin_add_article():

    if request.method == 'GET':
        categorys = CategoryModel.query.all()
        return render_template('admin/article_add.html',
                           username=request.user.name,
                           categorys=categorys
                           )
    elif request.method == 'POST':
        name = request.form.get('name')
        keywords = request.form.get('keywords')
        content = request.form.get('content')
        category = request.form.get('category')
        img = request.files.get('img')
        # 图片存储路径
        img_name = f'{time.time()}-{img.filename}'
        img_url = f'/static/home/uploads/{img_name}'
        print(category)

        # 添加文章
        try:
            article = ArticleModel()
            article.name = name
            article.keyword = keywords
            article.content = content
            article.category_id = category
            article.img = img_url
            db.session.add(article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(f'{e}')
        else:
            # 如果上面添加到数据库成功，手动将图片存入本地
            img_data = img.read()
            with open(f'App/{img_url}', 'wb') as fp:
                fp.write(img_data)
                fp.flush()

        return redirect('/admin/article/')


# 后台管理-更新文章
@admin.route('/admin/updatearticle/<id>/', methods=['GET', 'POST'])
@login_required
def admin_update_article(id):

    if request.method == 'POST':
        name = request.form.get('name')
        keywords = request.form.get('keywords')
        content = request.form.get('content')
        category = request.form.get('category')

        # 修改文章
        article = ArticleModel.query.get(id)
        article.name = name
        article.keywords = keywords
        article.content = content
        article.category_id = category

        try:
            print(article.category_id)
            db.session.commit()
        except Exception as e:
            print(f'{e}')
        return redirect('/admin/article/')
    elif request.method == 'GET':
        categorys = CategoryModel.query.all()
        article = ArticleModel.query.get(id)
        return render_template('admin/article_update.html',
                                username=request.user.name,
                                article=article,
                                categorys=categorys,
                                )


# 后台管理-删除文章
@admin.route('/admin/delarticle/', methods=['GET', 'POST'])
@login_required
def admin_del_article():
    if request.method != 'POST':
        return jsonify({'code': 400, 'msg': '请求方式错误!'})
    
    id = request.form.get('id')
    article = ArticleModel.query.get(id)
    # 删除文章
    try:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'code': 200, 'msg':'删除成功!'})
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        return jsonify({'code': 500, 'msg': f'删除过程中发生错误: {str(e)}'})