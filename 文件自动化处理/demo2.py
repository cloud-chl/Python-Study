import os

# 要查看的路径
path = r'E:\windows\下载\鬼刀合集\年度壁纸包'

file_list = os.listdir(path)

for file in file_list:
    new_path = os.path.join(path, file)
    if os.path.isdir(new_path):
        for image_file in os.listdir(new_path):
            image_file = os.path.join(new_path, image_file)
            print(image_file)
    elif os.path.isfile(new_path):
        print(new_path)


