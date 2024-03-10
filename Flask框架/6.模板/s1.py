from flask import Flask, redirect,render_template,request,jsonify,make_response
from jinja2 import Markup
app = Flask(__name__)


def gen_input(value):
    # return f"""<input value="{value}" />"""
    return Markup("""<input value=123 />""")


@app.route('/index', methods=['GET', 'POST'])
def index():
    context = {
        'k1': 123,
        'k2': [11,22,33],
        'k3': {'name': 'oldboy', 'age': 84},
        'k4': lambda x: x+1,
        'k5': gen_input('123')
    }
    return render_template('index.html', **context)


@app.route('/x2', methods=['GET', 'POST'])
def order():
    context = {
        'k1': 123,
        'k2':[11,22,33],      
        'k3':{'name': 'oldboy', 'age': 84},
        'k4': lambda x: x+1,
        'k5': gen_input('123')
    }
    return None


if __name__ == '__main__':
    app.run()