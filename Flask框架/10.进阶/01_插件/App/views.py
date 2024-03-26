import random
from flask import Blueprint, request, render_template, g, session, current_app
from .models import *
from .exts import cache
import time

blue = Blueprint('user', __name__)


# 使用缓存
@blue.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=20)   # 给视图函数加一个缓存
def index():
    print('Index2')
    print('Index视图函数中：', g.star)

    time.sleep(2)
    return 'Index2'


# AOP: 切面编程

# 钩子：钩子函数
#   也叫中间件
# before_request: 每一次请求之前访问
@blue.before_request
def before():
    print('before_request')

    # request
    # print(request.path)
    # print(request.method)
    # print(request.remote_addr)  # 客户端ip

    # 简单的反爬
    # print(request.user_agent)
    # if 'python' in request.user_agent.string:
    #     return  "这是Python爬虫"

    # 针对IP做反爬
    ip = request.remote_addr
    # cache.get()
    # cache.set()
    if cache.get(ip):
        # 做了拦截，不会进入视图函数
        return "访问太频繁"
    else:
        # 对每个IP设置一个缓存，1秒内不让重复访问
        cache.set(ip, 'value', timeout=1)


    # Flask内置对象
    # request： 请求对象
    # session： 会话对象
    # g： global全局对象
    # current_app: Flask应用对象

    g.star = 'Cai'
    print(g.star)

    print(current_app)
    print(current_app.config)


# static何templates
@blue.route("/templates/", methods=["GET", "POST"])
def templates():
    return render_template('index.html')