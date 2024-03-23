import random
from flask import Blueprint, request, render_template
from .models import *

blue = Blueprint('user', __name__)


@blue.route('/', methods=['GET', 'POST'])
def index():
    return 'Index'


# 多表操作

# 一对多
# 增加数据
@blue.route('/addgrade/', methods=['GET', 'POST'])
def add_grade():
    # 添加班级
    grades = []
    for i in range(0, 9):
        grade = Grade()
        grade.name = f'Jay{i}-' + str(random.randint(10, 99))
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        db.session.flush()

    return 'Grade Add Success!'


@blue.route('/addstu/', methods=['GET', 'POST'])
def add_stu():
    # 添加学生
    students = []
    for i in range(0, 9):
        student = Student()
        student.name = f'Lucy{i}'
        student.age = i
        student.gradeid = random.randint(67, 70)
        students.append(student)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        db.session.flush()

    return 'Students Add Success!'


# 修改
@blue.route('/updatestu/', methods=['POST', 'GET'])
def update_stu():
    stu = Student.query.first()
    stu.age = 100
    try:
        db.session.commit()
    except Exception as e:
        print(f'{e}')

    return 'Update Success!'


# 删除
@blue.route('/delstu/', methods=['POST', 'GET'])
def del_stu():
    # 删除学生
    stu = Student.query.first()
    try:
        db.session.delete(stu)
        db.session.commit()
    except Exception as e:
        print(f'{e}')

    return 'Delete Student Success!'


@blue.route('/delgrade/', methods=['POST', 'GET'])
def del_grade():
    # 删除班级
    grade = Grade.query.first()
    try:
        db.session.delete(grade)
        db.session.commit()
    except Exception as e:
        print(f'{e}')

    return 'Delete Grade Success!'


# 查询
@blue.route('/getstu/', methods=['POST', 'GET'])
def get_stu():
    # 查询某学生所在的班级： 反向引用grade
    stu = Student.query.get(4)
    print(stu.name, stu.age, stu.gradeid, stu.grade)

    # 查询某班级下的所有学生
    grade = Grade.query.get(70)
    print(grade.name)
    print(grade.students)
    for stu in grade.students:
        print(stu.name, stu.age, stu.gradeid)

    return 'OK'


# ------------------多对多---------------------#
# 添加数据
@blue.route('/adduser/', methods=['POST', 'GET'])
def add_user():
    # 添加用户
    users = []
    for i in range(10, 14):
        user = User()
        user.name = f'Tom{i}'
        user.age = i
        users.append(user)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        db.session.flush()

    return 'Users Add Success!'


@blue.route('/addmovie/', methods=['POST', 'GET'])
def add_movie():
    # 添加用户
    movies = []
    for i in range(1, 4):
        movie = Movie()
        movie.name = f'功夫熊猫{i}'
        movies.append(movie)
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e:
        print(f'{e}')
        db.session.rollback()
        db.session.flush()

    return 'Movies Add Success!'


@blue.route('/addcollect/', methods=['POST', 'GET'])
def add_collect():
    # 用户收藏电影
    user = User.query.get(1)
    movie = Movie.query.get(1)

    user.movies.append(movie)
    db.session.commit()

    return 'Add Success!'


# 查询
@blue.route('/getcollect/', methods=['POST', 'GET'])
def get_collect():
    # 查找某一个用户收藏的所有电影
    user = User.query.get(1)
    print(user.movies)

    # 查找收藏了某电影的所有用户
    movie = Movie.query.get(3)
    print(movie.users)
    print(list(movie.users))
    return 'Success!'


# 修改：和单表操作
# 删除
@blue.route('/deluser/', methods=['POST', 'GET'])
def del_user():
    # 级联删除
    user = User.query.get(1)
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(f'{e}')

    return 'Delete User Success!'