from flask import Flask, render_template, redirect,views
import functools
app = Flask(__name__)

# FBV
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

""" 
class IndexView(views.View):
    methods = ["GET"]
    decorators = [wapper,]

    def dispatch_request(self):
        print("Index")
        return "Index!"
app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint
 """
# CBV
class IndexView(views.MethodView):
    methods = ["GET"]
    decorators = [wapper,]

    def get(self):
        return "Index.GET"
    
    def post(self):
        return "Index.POST"
app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint

if __name__ == '__main__':
    app.run()