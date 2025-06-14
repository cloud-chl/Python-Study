# try:
#     print(1/0)
# except:
#     print("error")

"""
try:
    try-代码
except 错误1 as 变量1:
    except1代码
except 错误2 as 变量2:
    except2代码
except Exception as 变量3:
    最终
"""

# try:
#     print(1/0)
# except ZeroDivisionError as z:
#     print("除数为0")
# except FileNotFoundError as f:
#     print("file is not found")
# except Exception as e:
#     print("系统错误")
#
# finally:
#     print("收尾")

def func(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        # 抛出异常
        raise Exception("数据类型不是int，无法计算")
func(1, "a")