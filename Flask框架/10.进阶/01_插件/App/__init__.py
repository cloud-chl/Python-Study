# __init__.py : 初始化文件，创建Flask应用


from flask import Flask
from .views import blue
from .exts import init_exts
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f'BASEDIR: {BASE_DIR}')

def create_app():
    # static_folder = '../static'
    # template_folder = '../templates'
    static_folder = os.path.join(BASE_DIR, 'static')
    template_folder = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    db_uri = 'sqlite:///sqlite3.db' # sqlite 配置
    # db_uri = 'mysql+pymysql://root:admin%40123@localhost:3306/flask-demo4'
    # 密码：admin@123, 其中@符号需要用百分号编码形式，@对应 %40
    # db_uri = 'mysql://root:admin@123@localhost/flask-demo1'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app=app)

    return app