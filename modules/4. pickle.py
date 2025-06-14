import pickle

# lst = ["A", "B", "C", "D"]
# bs = pickle.dumps(lst)
# print(bs)
#
# bs = pickle.loads(bs)
# print(bs)

# 把数据存储到文件中
lst = ["A", "B", "C", "D"]
pickle.dump(lst, open("lst.txt", "wb"))


# 读取序列化之后的文件
dic = pickle.load(open("lst.txt", "rb"))
print(dic)

"""
dumps  把对象(数据)转换成字节
loads  把字节转换辉对象(数据)
dump   把对象序列化成字节之后写入文件
load   把文件中的反序列化成对象
"""