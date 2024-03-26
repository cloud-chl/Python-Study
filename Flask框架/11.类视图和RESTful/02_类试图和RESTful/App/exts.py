# exts.py  插件管理
# 扩展第三方插件

# 导包
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate()
api = Api()

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    api.init_app(app=app)