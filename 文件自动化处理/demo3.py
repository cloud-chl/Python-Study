import os

def find_file(path, filename):

    file_list = os.listdir(path)

    for file in file_list:
        new_path = os.path.join(path, file)
        if filename in new_path:
            total.append(os.path.join(new_path))
        # 判断是否目录，是则再次进入查找
        if os.path.isdir(new_path):
            find_file(new_path, filename)

# 要查看的路径
path = r'E:\windows\下载\鬼刀合集\年度壁纸包'

# 存储符合我们要求的文件或目录的名称
total = []

filename = 'Dome8_4k_b5239.jpg'
find_file(path, filename)

for i in total:
    print(i)
