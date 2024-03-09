from flask import Flask, redirect,render_template,request,jsonify,make_response

app = Flask(__name__)

def index():
    # 请求相关信息
    # request.method
    # request.args
    # request.form
    # request.values
    # request.cookies
    # request.headers
    # request.path
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))


    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host


    # 响应相关信息
    return "字符串"
    return json.dumps({}) # return jsonify({})
    return render_template('index.html', n1=123)
    return redirect('/index.html')

    # response = make_response(render_template('index.html'))
    # response = make_response(render_template("xxx")
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response

    return None

if __name__ == '__main__':
    app.run()