from fastapi import APIRouter
from models import *
student_api = APIRouter()

@student_api.get('/')
async def getAllStudent():
    # (1) 查询所有 all方法
    # students = await Student.all() # Student <tortoise.queryset.QuerySet object at 0x000001EDBD7D8BF0>
    # students[0].name
    # for stu in students:
    #     print(stu.name, stu.sno)

    # (2) 过滤查询 filter
    # students = await Student.filter(name="cai")
    # students = await Student.filter(clas_id=7)
    # print("students", students)

    # (3) 过滤查询 get：返回模型类型对象
    # stu = await Student.get(id=1)
    # print(stu.name)

    # (4) 模糊查询
    # stus = await Student.filter(sno__gt=2001)
    # stus = await Student.filter(sno__in=[2001, 2002])
    # print(stus) # [<Student: 2>, <Student: 3>]

    # (5) values查询
    # stus = await Student.all().values("name", "sno")
    # print(stus)

    return {
        "学生": stus
    }

@student_api.post('/')
def addStudent():
    return {
        "操作": "添加一个学生"
    }

@student_api.get('/{student_id}')
def addStudent(student_id:int):
    return {
        "操作": f"查看id={student_id}学生"
    }

@student_api.put('/{student_id}')
def PutStudent(student_id:int):
    return {
        "操作": f"更新id={student_id}学生"
    }

@student_api.delete('/{student_id}')
def DelStudent(student_id:int):
    return {
        "操作": f"删除id={student_id}学生"
    }