from math import trunc

from pymysql import Connection

conn = None
try:
    conn = Connection(
        host='localhost',
        port=3306,
        user='root',
        password='admin@123',
        database='test',
        autocommit=True,
    )
    # 创建游标对象
    cursor = conn.cursor()

    # SQL
    # sql="""
    #     CREATE TABLE `t_student2` (
    #     `id` int(11) NOT NULL AUTO_INCREMENT,
    #     `name` varchar(255) NOT NULL,
    #     `age` int(3) NOT NULL,
    #     `gender` varchar(10) NOT NULL,
    #     PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    # """

    # # 选择要操作的数据库
    # conn.select_db('test')

    # 使用游标对象执行sql
    # cursor.execute(sql)

    # 查询
    # cursor.execute("SELECT * FROM t_student")
    # # 获取查询所有结果
    # res = cursor.fetchall()
    # for row in res:
    #     print(row)

    # 插入
    # cursor.execute("INSERT INTO t_student (name, age, gender) VALUES ('Tom', 20, '男')")
    # print(f"主键id: {conn.insert_id()}")

    # 更新
    # cursor.execute("UPDATE t_student SET age = age + 1 WHERE id = 1")

    # 删除
    cursor.execute("DELETE FROM t_student WHERE id = 5")

except Exception as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    conn.close()



