from flask import Flask, render_template,redirect

app = Flask(__name__)
app.config['SERVER_NAME'] = 'old.com:5000'


@app.route('/index', subdomain="<username>")
def xxxxxx(username):
    print(username)
    return "xxx"


if __name__ == '__main__':
    app.run(debug=True)