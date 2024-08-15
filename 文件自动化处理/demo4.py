import os


def rename(path, prefix):
    # prefix = 'new_' # 重命名的前缀

    file_list = os.listdir(path)
    i = 1
    for file in file_list:

        old_path = os.path.join(path, file)
        # 获取旧文件后缀
        suffix = os.path.splitext(old_path)[-1]
        new_path = os.path.join(path, prefix+str(i)+suffix)
        # print(new_path)
        os.rename(old_path, new_path)
        i += 1


path = r'E:\windows\下载\demo4'

rename(path, 'new_q_')