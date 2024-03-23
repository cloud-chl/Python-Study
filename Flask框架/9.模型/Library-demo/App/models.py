from .exts import db

#创建一个项目，用来说明出版社，书籍和作者的关系。
# 假定关系:作者:书籍=>1:n (一本书由一个作者完成，一个作者可以创作多本书)
#         出版社:书籍=>n:n (一个出版社可以出版多本书，一本书可以由多个出版社出版)

# 作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(200))
    # 关系：
    books = db.relationship('Book', backref='author', lazy='dynamic')


# 书籍
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True)
    date = db.Column(db.DateTime)
    # 1对多，外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


# 中间表（书籍-出版社）
book_publisher = db.Table('book_publisher',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'), primary_key=True)
)


# 出版社
class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(100))
    # 多对多，关联book表
    books = db.relationship('Book', backref='publishers', secondary=book_publisher, lazy='dynamic')