# views.py : 路由 + 视图函数

from flask import Blueprint
from .models import *


# 蓝图
blue = Blueprint('user', __name__)
# blue2 = Blueprint('product', __name__)


@blue.route('/', methods=['GET','POST'])
def index():

    return 'Index'


# @blue2.route('/goods/', methods=['GET','POST'])
# def index():
#
#     return 'Index'