# views.py : 路由 + 视图函数

from flask import Blueprint, request, render_template
from sqlalchemy import desc, and_, or_, not_

from .models import *


blue = Blueprint('user', __name__)


@blue.route('/', methods=['GET','POST'])
def index():

    return 'Index'


# 分页，翻页
# 1.手动翻页
#   offset().limit()
#   数据： 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#   页码： page
#   每一页显示数量：per_page=5
#    page=1: 1,2,3,4,5          => offset(0).limit(5)
#    page=2: 6,7,8,9,10         => offset(5).limit(5)
#    page=3: 11,12,13,14,15     => offset(10).limit(5)
#    page=4: 16,17,18,19,20     => offset(15).limit(5)
#    ...
#    page=n:                    => offset((page-1)*per_page).limit(per_page)

@blue.route('/paginate/', methods=['GET', 'POST'])
def get_paginte():
    # 页码: 默认显示第一页
    page = int(request.args.get('page', 1))
    # per_page: 每一页显示数量
    per_page = int(request.args.get('per_page', 5))
    # print(page, type(page))
    # print(per_page, type(per_page))

    # paginate()
    p = User.query.paginate(page=page, per_page=per_page, error_out=False)
    # paginate对象的属性:
    # items: 返回当前页的内容列表
    print(p.items)
    # has_next:是否还有下一页
    # print(p.has_next)
    # has_prev: 是否还有上一页
    # print(p.has_prev)
    # next(error_out = False):返回下一页的Pagination对象
    # print(p.next(error_out = False).items)
    # prev(error_out = False):返回上一页的Pagination对象
    # print(p.prev(error_out=False).items)
    # page: 当前页的页码(从1开始)
    print(p.page)
    # pages: 总页数
    print(p.pages)
    # per_page: 每页显示的数量
    # print(p.per_page)
    # prev_num: 上一页页码数
    # print(p.prev_num)
    # next_num: 下一页页码数
    # print(p.next_num)
    # total: 查询返回的记录总数
    print(p.total)

    return render_template('paginate.html', p=p)