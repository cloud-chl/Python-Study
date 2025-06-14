import re

# 从一个字符串中提取到所有的数字
# lst = re.findall(r"\d+", "我今年18岁，我有5个爱好")
# print(lst)

# 判断一句话中是否有数字
# search特点: 匹配字符串，匹配到第一个结果就返回，不会继续匹配
# res = re.search(r"\d+", "我今年18岁，我有5个爱好")
# print(res.group())

# finditer,所有数据都会匹配，返回迭代器
# it = re.finditer(r"\d+", "我今年18岁，我有5个爱好")
# for i in it:
#     print(i.group())

# match 从头开始匹配，
# res= re.match(r"\d+", "18岁，我有5个爱好")
# print(res.group())

# res= re.split(r"\d+", "我今年18岁，我有5个爱好")
# res= re.split("[我]", "我今年18岁我有5个爱好")
# print(res)

# res = re.sub(r"\d+", "_SB_", "我今年18岁我有5个爱好")
# res = re.subn(r"\d+", "_SB_", "我今年18岁我有5个爱好")
# print(res)

res = re.compile(r"\d+") # 先加载这个正则，后面可以直接用这个去匹配内容
lst = res.findall("我今年18岁，我有5个爱好")
print(lst)