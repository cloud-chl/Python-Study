from .exts import db


# 多表关系
# 一对多
#   班级：学生= 1：N
# 班级表
class Grade(db.Model):

    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    # 建立关联
    # 第一个参数： 关联的模型名（表）
    # 第二个参数： 反向引用的名称，grade对象，让student去反过来得到grade对象的名称
    # 第三个参数： 懒加载
    students = db.relationship('Student', backref='grade', lazy=True)


# 学生表
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)
    # 外键: 与Grade表中的id字段关联
    gradeid = db.Column(db.Integer, db.ForeignKey(Grade.id))


# --------------多对多----------------- #
# 用户收藏电影
# 用户:电影 = N:M

# 中间表:收藏表
collect = db.Table(
    'collects',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
)


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)


# 电影表
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    # 关联
    # secondary=collect : 设置中间表
    users = db.relationship('User', backref='movies', lazy='dynamic', secondary=collect)

    # lazy属性：
    #     懒加载，可以延迟再使用关联属性的时候才建立关联
    #     lazy='dynamic': 会返回一个query对象（查询集）, 可以继续使用其他查询方法，如 all()
    #     lazy='select': 首次访问到属性的时候，就会全部加载该属性的数据
    #     lazy='joined': 在对关联的两个表进行join操作，从而获取到所有相关的对象
    #     lazy=True : 返回一个可用的列表对象，同select