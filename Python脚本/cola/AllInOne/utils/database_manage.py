import mysql.connector
from mysql.connector import Error
from .print_color import print_color_text, RED


class MySQLManager:
    """MySQL manager"""
    def __init__(self):
        self.conn = None
        
    def connection(self, database):
        """建立数据库连接"""
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='!CSNTA@l23E8',
                database=database,
                autocommit=True,
            )
        except Error as e:
            print_color_text(f"Failed to connect to MySQL: {e}", RED)

    def execute_sql(self, sql):
        """执行 SQL"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                # print("SQL 执行成功")
        except Error as e:
            print_color_text(f"Failed to execute SQL: {e}", RED)
        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
