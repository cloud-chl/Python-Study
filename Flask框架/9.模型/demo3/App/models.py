# models.py  : 模型,数据库


from .exts import db

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer, default=1)

    def __repr__(self):
        return self.name



# db.Column:   表示字段
# db.Integer： 表示整数
# primary_key： 表示主键
# autoincrement :自动递增
# db.String(30) 可变字符串
# unique=True : 唯一约束
# index=true : 普通索引
# nullable=False 是否允许为空