# models.py  : 模型,数据库


from .exts import db

# 模型 ==> 数据库
# 类   ==> 表结构
# 类属性 ==> 表字段
# 一个对象 ==> 表的一行数据

# 模型： 类
# 必须继承 db.Model
class User(db.Model):
    # 表名
    __tablename__ = 'tb_users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, index=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Integer, default=10000, nullable=False)
    salary2 = db.Column(db.Integer, default=10000, nullable=False)




# db.Column:   表示字段
# db.Integer： 表示整数
# primary_key： 表示主键
# autoincrement :自动递增
# db.String(30) 可变字符串
# unique=True : 唯一约束
# index=true : 普通索引
# nullable=False 是否允许为空