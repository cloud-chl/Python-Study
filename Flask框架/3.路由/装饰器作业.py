from flask import Flask, render_template, redirect
import functools
app = Flask(__name__)

def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("befoer")
        return func(*args, **kwargs)
    return inner


@app.route('/', methods=['GET', 'POST'])
@wapper
def index():
    return "index"

@app.route('/', methods=['GET', 'POST'])
@wapper
def order():
    return "order"

if __name__ == '__main__':
    app.run()