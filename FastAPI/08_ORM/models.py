from tortoise.models import Model
from tortoise import fields
# 选课
class  Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, description="姓名")
    pwd = fields.CharField(max_length=30, description="密码")
    sno = fields.IntField(description="学号")

    # 一对多
    clas = fields.ForeignKeyField("models.Clas", related_name="students")

    # 多对多
    courses = fields.ManyToManyField("models.Course", related_name="students")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher", )
    addr = fields.CharField(max_length=30, description="教室", default="")

class  Clas(Model):
    name = fields.CharField(max_length=30, description="班级名称")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, description="老师姓名")
    pwd = fields.CharField(max_length=30, description="密码")
    tno = fields.IntField(description="老师编号")