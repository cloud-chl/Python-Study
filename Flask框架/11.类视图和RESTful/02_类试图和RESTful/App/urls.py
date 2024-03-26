# urls.py 路由文件

from .exts import api
from .apis import *


api.add_resource(helloResource, '/hello/')
api.add_resource(UserResource, '/user/')
api.add_resource(User2Resource, '/user2/', endpoint='id')
api.add_resource(User3Resource, '/user3/')
api.add_resource(User4Resource, '/user4/')