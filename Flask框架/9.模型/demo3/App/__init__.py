# __init__.py : 初始化文件，创建Flask应用


from flask import Flask
from .views import blue
from .exts import init_exts

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    # db_uri = 'sqlite:///sqlite3.db' # sqlite 配置
    db_uri = 'mysql+pymysql://root:admin%40123@localhost:3306/flask-demo3'
    # 密码：admin@123, 其中@符号需要用百分号编码形式，@对应 %40
    # db_uri = 'mysql://root:admin@123@localhost/flask-demo1'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app=app)

    return app