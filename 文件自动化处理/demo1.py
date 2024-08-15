import os

# 要查看的路径
path = r'E:\windows\下载\鬼刀合集\年度壁纸包'

file_list = os.listdir(path)

print(file_list)

for file in file_list:
    # 拼接完整路径
    new_path = os.path.join(path, file)
    print(new_path)

