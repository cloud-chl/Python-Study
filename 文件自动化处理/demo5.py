import os


path = r'E:\windows\下载\demo4'
file_list = os.listdir(path)
filename = '副本'
for file in file_list:
    new_path = os.path.join(path, file)
    # 判断文件是否为副本
    if filename in new_path:
        # print(new_path)
        os.remove(new_path)