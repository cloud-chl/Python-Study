import random

# print(random.random()) # (0, 1)范围
#
# print(random.uniform(5, 9)) # 随机小数
#
# print(random.randint(3, 8)) # 随机整数，能够取到边界
#
# lst = ["Cai", "Hou", "Jie"]
# print(random.choice(lst))
# print(random.sample(lst, 2))

# 随机生成四位验证码
def rand_num():
    return str(random.randint(0, 9))

def rand_upper():
    return chr(random.randint(65, 90))

def rand_lower():
    return chr(random.randint(97, 122))

def rand_verify_code(n=4):
    lst = []
    for i in range(n):
        which = random.randint(1, 3)
        if which == 1:
            s = rand_num()
        elif which == 2:
            s = rand_upper()
        elif which == 3:
            s = rand_lower()
        lst.append(s)
    return "".join(lst)

print(rand_verify_code())