import os
import sys
import requests
import subprocess
from requests.auth import HTTPBasicAuth
from .print_color import print_color_text, RED, BLUE, GREEN
from .database_manage import MySQLManager
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError


class UnlockAccount:
    """解锁账户和IP地址"""

    def cmc_and_cas(db_name):

        # 建立MySQL对象
        cmc_conn = MySQLManager()
        # 连接指定数据库
        cmc_conn.connection(db_name)
        # 解锁账户 SQL
        sql = """UPDATE bs_common_user SET status='enable' WHERE user_name="admin";"""

        try:
            cmc_conn.execute_sql(sql)
            print_color_text(f"账户 admin 已解锁", BLUE)

        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

        cmc_conn.close()

    def upm():
        try:
            with MongoClient("mongodb://127.0.0.1:27017/", username="upm", password="Y6*(T^7d") as client:
                db = client["upm"]
                collection = db["loginLog"]
                # 删除loginLog下面所有的记录
                collection.delete_many({})
                print_color_text(f"账户/IP 已解锁", BLUE)
        # mongo认证失败
        except OperationFailure as e:
            # print_color_text(f"ERROR: {e}", RED)
            with MongoClient("mongodb://127.0.0.1:27017/") as client:
                db = client["upm"]
                collection = db["loginLog"]
                # 删除loginLog下面所有的记录
                collection.delete_many({})
                print_color_text(f"账户/IP 已解锁", BLUE)

        # 27017端口不存
        except ServerSelectionTimeoutError as e:
            # print_color_text(f"ERROR: {e}", RED)
            opensearch_url = "http://localhost:9200/"
            index_name = "upm-login_log"
            username = "elastic"
            password = "N*(T#^72d"

            # 组成完整url
            url = f"{opensearch_url}/{index_name}/_delete_by_query"
            # 查询条件
            query = {"query": {"match_all": {}}}

            # 发送删除请求
            response = requests.post(
                url,
                auth=HTTPBasicAuth(username, password),
                json=query,
                headers={"Content-Type": "application/json"},
            )

            if response.status_code in (200, 201):
                print_color_text(
                    f"账户/IP 已解锁, 成功删除索引中的数据: {response.json()}", BLUE)
            else:
                print_color_text(
                    f"账户/IP 解锁失败，状态码：{response.status_code}, 响应内容：{response.json()}",
                    RED,
                )

        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

    def ras():
        res = subprocess.run(
            ["/usr/sbin/appclient", "restart", "httpapp"],
            capture_output=True,
            text=True,
        )
        if res.returncode == 0:
            print_color_text(f"账户/IP 已解锁", BLUE)
        else:
            print_color_text(f"账户/IP 解锁失败，{res.stderr}", RED)
