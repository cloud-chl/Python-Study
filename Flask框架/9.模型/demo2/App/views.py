# views.py : 路由 + 视图函数

from flask import Blueprint
from sqlalchemy import desc, and_, or_, not_

from .models import *


blue = Blueprint('user', __name__)


@blue.route('/', methods=['GET','POST'])
def index():

    return 'Index'


# 单表操作
# 增删改查

# 增： 添加数据
@blue.route('/adduser/', methods=['POST','GET'])
def user_add():
    # 添加一条数据
    # u = User()
    # u.name = 'Cai'
    # u.age = 24
    # db.session.add(u)   # 将u对象添加刀session中
    # db.session.commit() # 同步到数据库中

    # 同时添加多条数据
    users = []
    for i in range(10, 30):
        u = User()
        u.name = 'Cai' + str(i)
        u.age = i
        users.append(u)
    try:
        db.session.add_all(users)
        db.session.commit() # 事务提交
    except Exception as e:
        db.session.rollback()   # 回滚
        db.session.flush()
        return f"fail: {e}"

    return 'success!'


# 删： 删除数据
# 找到要删除的数据，然后删除
@blue.route('/deluser/', methods=['GET', 'POST'])
def user_del():
    u = User.query.first() # 查询第一条数据
    try:
        db.session.delete(u)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()

    return 'success!'


# 改： 修改数据
# 找到要修改的数据，然后修改
@blue.route('/edituser/', methods=['GET', 'POST'])
def user_edit():
    u = User.query.first() # 查询第一条数据
    u.age = 1000
    db.session.commit()

    return 'Success!'


# 查： 查询数据
# 条件
@blue.route('/getuser/', methods=['GET', 'POST'])
def user_get():
    users = User.query.all()
    # print(users)
    # print(User.query)

    # filter(): 过滤，得到查询集，类似SQL中的where
    users = User.query.filter()
    # print(users, type(users))   # 查询集
    # print(list(users))

    # get()：查询到对应主键的数据对象
    user = User.query.get(15)
    # print(user, type(user)) # User 对象 <class 'App.models.User'>
    # print(user.name, user.age)  # 获取数据的属性

    # filter() :类似SQL中的where
    # filter_by()  : 用于等值操作的过滤
    # users = User.query.filter(User.age==20)
    # users = User.query.filter_by(age=20)
    users = User.query.filter(User.age>20)  # 可以用于非等值操作
    # print(list(users))

    # first() : 第一条数据
    # first_or_404() : 第一条数据，如果不存在则抛出404错误
    user = User.query.first()
    # user = User.query.filter_by(age=100).first_or_404()
    # print(user)

    # count() : 统计查询集中的数据条数
    users = User.query.filter(User.age>=200)
    # print(users.count()) # 1

    # limit() : 前几条
    # offset() : 跳过前几条
    users = User.query.offset(3).limit(4)
    # print(list(users))

    # order_by() : 排序
    users = User.query.order_by('age') # 升序
    users = User.query.order_by(desc('age')) # 降序
    # print(list(users))

    # 逻辑运算： and_, or_, not_
    users = User.query.filter(User.age>20, User.age<25) # 且， 常用
    users = User.query.filter(and_(User.age>20, User.age<25))    # 且
    users = User.query.filter(or_(User.age>25, User.age<20))    # 或
    users = User.query.filter(not_(or_(User.age>25, User.age<20)))    # 非
    # print(list(users))

    # 查询属性
    # contains() : 模糊查找，类似SQL中的like
    users = User.query.filter(User.name.contains('2'))
    # in_(): 其中之一
    users = User.query.filter(User.age.in_([10, 20, 30, 40, 50]))
    # startswith(), endswith()
    users = User.query.filter(User.name.startswith('Cai'))
    users = User.query.filter(User.name.endswith('2'))
    # __gt__: 大于
    users = User.query.filter(User.age.__gt__(25))
    print(list(users))
    return 'Success!'
