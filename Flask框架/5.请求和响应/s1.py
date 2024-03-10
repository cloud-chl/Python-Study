from flask import Flask, request,render_template, jsonify,make_response, Response,redirect, url_for

app = Flask(__name__)


def context():
    # 请求相关信息
    # request.method    请求方法
    # request.args      GET请求参数
    # request.form      POST请求参数
    # request.cookies   请求中的cookie
    # request.headers   请求头
    # request.path      路由中的路径
    # request.files     文件上传
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))
    # request.values
    # request.full_path
    # request.script_root
    # request.url       完整请求地址
    # request.base_url  去掉GET参数的URL
    # request.url_root
    # request.host_url  只有主机鹤和口号的URL
    # request.host

    # 响应相关信息
    # return "字符串"
    # return json.dumps({})  # return jsonify({})
    # return render_template('index.html', n1=123)
    # return redirect('/index.html')

    # response = make_response(render_template('index.html'))
    # response = make_response(render_template("xxx")
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response

    return None


# Request: 客户端向服务器发送的请求
@app.route('/request/', methods=['GET', 'POST'])
def get_request():
    # 请求方式, 'GET' or 'POST'
    print(request.method)

    # GET请求参数
    # ImmutableMultiDict: 类字典对象，区别是可以出现重复的key
    print(request.args) # ImmutableMultiDict([('name', 'lisi'), ('name', 'Cai'), ('age', '33')])
    # print(request.args['name'], request.args['age']) # lisi 33
    # print(request.args.get('name')) # list
    # print(request.args.getlist('name')) # ['lisi', 'Cai']

    # POST请求参数
    print(request.form) # ImmutableMultiDict([('name', 'Cai'), ('age', '24')])
    # print(request.form.get('name')) # Cai

    # cookie
    print(request.cookies)

    # 路径
    print(request.path)     # /request/
    print(request.url)      # http://127.0.0.1:5000/request/?name=lisi&age=33&name=Cai
    print(request.base_url) # http://127.0.0.1:5000/request/
    print(request.host_url) # http://127.0.0.1:5000/
    print(request.remote_addr) # 127.0.0.1

    print(request.files) # 文件内容, ImmutableMultiDict([])
    print(request.headers) # 请求头
    print(request.user_agent) # 用户代理，包括浏览器和操作系统的信息，python-requests/2.31.0

    return 'Request OK!'


# Response：服务器向客户端发送的响应
@app.route('/response/', methods = ['GET', 'POST'])
def get_response():
    pass
    # 响应的几种方式
    # 1. 返回字符串（不常用）
    # return "response ok!"

    # 2.模板渲染（前后端不分离）
    # return render_template('index.html', name='Cai', age=24)

    # 3.返回json数据（前后端分离）
    data = {'name': 'Cai', 'age': 24}
    # return data
    # return jsonify(data) # 序列化，字典=>字符串

    # 4.自定义Response对象
    html = render_template('index.html', name='张三', age=24)
    print(html, type(html))

    # res = make_response(html, 200)
    res = Response(html)
    return res


# Redirect：重定向
@app.route('/redirect/', methods = ['GET', 'POST'])
def make_redirect():

    # 重定向的几种方式
    # return redirect('https://www.baidu.com')
    # return redirect('/response')

    # 反向解析
    # url_for('蓝图名称.视图函数名'）
    # ret = url_for('get_response')
    # print('url_for:', ret)

    # url_for传参
    ret2 = url_for('get_response', name='Cai', age=24)

    return redirect(ret2)


if __name__ == '__main__':
    app.run()
