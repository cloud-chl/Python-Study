import hashlib

# # md5对象
# obj = hashlib.md5()
# # 把要加密的信息传给obj
# obj.update("66666".encode("utf-8"))
# # 从obj中拿到密文
# mi = obj.hexdigest()
# print(mi)
#
# obj = hashlib.md5(b'qweasd')
# obj.update("66666".encode("utf-8"))
# print(obj.hexdigest())


def func(salt, s):
    obj = hashlib.md5()
    obj.update(s.encode('utf-8'))
    return obj.hexdigest()
#
# username = input("输入用户名:")
# password = input("输入密码:")
# mi_passwd = func(username.encode("utf-8"), password)
# f = open('user.txt', mode="w", encoding='utf-8')
# f.write(username)
# f.write("\n")
# f.write(mi_passwd)

username = input("用户名：")
password = input("密码：")
password = func(username.encode('utf-8'), password)
f = open('user.txt', mode="r", encoding='utf-8')
uname = f.readline().strip()
upwd = f.readline().strip()
if username == uname and password == upwd:
    print("success")

