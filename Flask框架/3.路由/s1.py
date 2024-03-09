from flask import Flask, render_template,redirect

app = Flask(__name__)

# 第一种路由方式
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Index"

# 第二种路由方式
def order():
    return "Order"

app.add_url_rule('/order', view_func=order)
if __name__ == '__main__':
    app.run()