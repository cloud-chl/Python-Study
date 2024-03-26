from flask_restful import Resource, fields, marshal_with, reqparse
from flask import jsonify
from .models import *


# 类视图： CBV  Class Based View
# 视图函数：FBC  Function Based View
class helloResource(Resource):
    def get(self):
        return jsonify({'msg': 'get请求'})

    def post(self):
        return jsonify({'msg': 'post请求'})


# Flask RESTful
# 字段格式化： 定义返回给前端的数据格式
ret_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    # 'data': fields.String,
    'like': fields.String(default='ball'),
    'like2': fields.String(),
    'data2': fields.String(attribute='data')  # 使用data的值
}


class UserResource(Resource):
    @marshal_with(ret_fields)
    def get(self):
        return {
            'status': 1,
            'msg': 'OK',
            'data': 'Welcome to China'
        }


# ----------------------字段格式化--------------------------------#
user_fields = {
    # 'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'url': fields.Url(endpoint='id', absolute=True)
}
ret_fields2 = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}


class User2Resource(Resource):
    @marshal_with(ret_fields2)
    def get(self):
        user = User.query.first()
        return {
            'status': 1,
            'msg': 'OK',
            'data': user
        }


# ----------------------字段格式化--------------------------------#
user_fields2 = {
    'name': fields.String,
    'age': fields.Integer,
}

ret_fields3 = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_fields2))
}


class User3Resource(Resource):
    @marshal_with(ret_fields3)
    def get(self):
        users = User.query.all()
        return {
            'status': 1,
            'msg': 'OK',
            'data': users
        }

# ----------------------参数解析--------------------------------#
# 参数解析：获取前端发送过来的数据
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name是必须参数')
parser.add_argument('age', type=int, action='append') # 可以有多个age
parser.add_argument('key', type=str, location='cookies')

class User4Resource(Resource):
    def get(self):
        # 获取参数
        args = parser.parse_args()
        name = args.get('name')
        age = args.get('age')
        key = args.get('key')

        return jsonify({'name': name, 'age': age, 'key': key})