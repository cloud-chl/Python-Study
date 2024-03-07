from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/index/<int:nid>', methods=['GET', 'POST'])
def index(nid):
    print(nid)
    return "Index"

if __name__ == '__main__':
    app.run()