import json

dic ={"id": 1, "name":"管理员", "usertype": 0}
s = json.dumps(dic, ensure_ascii=False)
print(s, type(s))

print(ascii("管理员"))

# str = {
#     "key" : "我爱你",
#     "key1" : "一生一世"
# }
#
# json.dump(str, open("data.txt", mode="w", encoding="utf-8"), ensure_ascii=False)

d = json.load(open("data.txt", mode="r", encoding="utf-8"))
print(d, type(d))