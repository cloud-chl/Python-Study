from datetime import date, datetime

# datetime: 年月日 时分秒
# date： 年月日
# time：时分秒

# 格式化一个时间
t = datetime.now()
print(t)
print(t.strftime("%Y-%m-%d %H:%M:%S"))  # 把是将格式化成一个字符串


# 把字符串转换成 时间
# s1 = input("请输入第一个时间(yyyy-MM-dd HH:MM:SS): ")
# s2 = input("请输入第一个时间(yyyy-MM-dd HH:MM:SS): ")
#
# t1 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
# t2 = datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")
# print(t2-t1)

# date
print(date.today())

# 需要掌握的
# now() 系统时间
# datetime(year, month, day, hour, min, second)
# strftime("%Y-%m-%d %H:%M:%S") 把时间格式化成字符串
# strptime(str, %Y-%m-%d %H:%M:%S) 把字符串转换成时间
# date.today() 今天的日期