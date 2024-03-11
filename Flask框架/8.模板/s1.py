from flask import Flask, render_template ,redirect, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    pass

    data = {
        'name': 'cai cai cai',
        'age': 24,
        'likes': ['ball', 'sing', 'dance', 'code'],
    }

    # return render_template('home.html', **data)
    # return render_template('home.html', name='Cai', age=24, likes=['ball', 'sing', 'dance'])

    # return render_template('base.html')
    return render_template('child2.html', **data)

if __name__ == '__main__':
    app.run(debug=True)