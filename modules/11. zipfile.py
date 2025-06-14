import zipfile

# 创建压缩包

# f = zipfile.ZipFile('test.zip', mode='w')
# f.write("app.log")
# f.write("debug.log")
#
# f.close()

f = zipfile.ZipFile("test.zip", mode="r")
# 全部解压缩
# f.extractall("zip_dir/")
# 一个一个解压缩
for name in f.namelist():
    f.extract(name, path="zip_dir/")