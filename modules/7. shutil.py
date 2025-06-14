import shutil

# 把dir/1.txt移动到dir2

# shutil.move("dir1/1.txt", "dir2")



# 复制两个文件句柄
# f1 = open("dir1/1.txt", mode="rb")
# f2 = open("dir2/2.txt", mode="wb")
# shutil.copyfileobj(f1, f2)

# 复制文件内容
# shutil.copyfile("dir1/1.txt", "dir2/3.txt")
# 复制文件内容 + 文件的权限一起复制
# shutil.copy("dir2/1.txt", "dir1/4.txt")
# 复制文件内容 + 修改时间
# shutil.copy2("dir2/1.txt", "dir1/5.txt")

# 修改时间， 权限的复制, 不复制内容
shutil.copystat("dir1/1.txt", "dir2/5.txt")

# 只拷贝权限
shutil.copymode(".", "dir2/5.txt")

# 复制文件夹
shutil.copytree("dir1", "dir3")

# 删除文件夹
shutil.rmtree("dir3")