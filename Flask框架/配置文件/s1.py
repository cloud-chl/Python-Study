# 需要创建一个web应用，而Flask中创建应用的对象是Flask
from flask import Flask
import settings

# 创建对象
app = Flask(__name__)
app.config.from_object("settings.DevelopmentConfig")

# 路由地址
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "hello world!"

if __name__ == "__main__":
    # 启动web应用服务
    app.run(port=8080) 