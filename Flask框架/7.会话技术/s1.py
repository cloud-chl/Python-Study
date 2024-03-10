from flask import Flask, render_template, redirect, request, make_response, session
import datetime

app = Flask(__name__)
# app.config.from_pyfile('settings.py')
app.config.from_object('settings.BaseConfigure')
# session 配置
# app.config['SECRET_KEY'] = 'qweasd'

# 首页
@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def home():
    # 4. 获取cookie
    # username = request.cookies.get('user')

    # 获取session
    username = session.get('user')

    return render_template('home.html', username=username)


# 登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # GET: 访问登录页面
    if request.method == 'GET':
        return render_template('login.html')

    # POST: 实现登录
    elif request.method == 'POST':
        pass
        # 1. 获取前端提交过来的数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 2. 模拟登录: 用户名和密码验证
        if username == 'Cai' and password == 'qwe':
            # 登录成功
            response = redirect('/home/')

            # 3. 设置cookie
            #   cookie 不能用中文
            # response.set_cookie('user', username) # 默认浏览器关闭则cookie失效
            # 过期时间
            #   max_age: 秒
            #   expires: 指定datetime日期
            # response.set_cookie('user', username, max_age=3600*24*7)
            # response.set_cookie('user', username, expires=datetime.datetime(2024, 3, 11))

            # 设置session
            session['user'] = username
            session.permanent = True

            return response
        else:
            print('用户名或密码错误')
            return render_template('login.html', error_messages='用户名或密码错误')


# 注销
@app.route('/logout/')
def logout():
    response = redirect('/home/')
    # 5. 删除cookie
    # response.delete_cookie('user')

    # 删除session
    session.pop('user')
    # session.clear()  慎用，会删除服务器下所有session

    return response



if __name__ == '__main__':
    app.run()
