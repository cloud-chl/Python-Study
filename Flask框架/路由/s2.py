from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'], endpoint='n1')
def index():
    v1 = url_for('n1')
    v2 = url_for('n2')
    v3 = url_for('n3')
    print(v1,v2,v3)
    return "Index"

@app.route('/login', methods=['GET', 'POST'], endpoint='n2')
def index():
    return "Login"

@app.route('/logout', methods=['GET', 'POST'], endpoint='n3')
def index():
    return "Logout"

if __name__ == '__main__':
    app.run()