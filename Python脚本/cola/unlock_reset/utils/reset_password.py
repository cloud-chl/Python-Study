import subprocess
import requests
from requests.auth import HTTPBasicAuth
from mysql.connector import Error
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError
from urllib3.exceptions import InsecureRequestWarning
from .print_color import print_color_text, RED, BLUE
from .database_manage import MySQLManager


# 忽略自签证书的警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ResetPassword:
    """重置用户密码"""

    def update_db(db, authPass, sm3Password=None):
        """更新mongo"""

        update_fields = {"authPwd": authPass,
                         "pwdHistorys": [], "historySalt": []}

        # 含国密版本需要同时修改这个字段
        if sm3Password is not None:
            update_fields["sm3Password"] = sm3Password

        db.admin.update_one({"authIsRoot": True}, {"$set": update_fields})

    def cmc_and_cas(db_name):
        # 默认密码
        passStr = "csf@123"
        # 重置密码 SQL 语句
        sql = """update bs_common_user set password="$2a$07$g.L1NkBYZwzZffEZig/gUunnCNkVUYePaMvPZ5S4KwtTAbss3Rqem" where user_name="admin";"""
        # 建立 Mysql 对象
        conn = MySQLManager()
        # 连接指定数据库
        conn.connection(db_name)

        try:
            conn.execute_sql(sql)
            print_color_text(f"密码重置成功: {passStr}", BLUE)

        except Error as e:
            print_color_text(f"ERROR: {e}", RED)

        conn.close()

    def upm():
        # 默认密码
        new_pass = "!CSupm23"
        # 获取新密码字符串
        response = requests.get(
            f"https://127.0.0.1:8080/pub/secret.do?str={new_pass}", verify=False
        )
        auth_pass = response.json()["data"]
        # 国密版本需要进行dgst加密
        sm3_str = subprocess.run(
            ["/bin/echo", "-n", f"{auth_pass}",
                "|", "openssl", "dgst", "-sm3"],
            capture_output=True,
            text=True,
        )
        sm3_pass = sm3_str.stdout.split("=", 1)[1].strip()

        try:
            with MongoClient(
                "mongodb://127.0.0.1:27017/", username="upm", password="Y6*(T^7d"
            ) as client:
                db = client["upm"]
                # 确认是否国密版本
                doc = db.admin.find_one({"sm3Password": {"$exists": True}})
                ResetPassword.update_db(
                    db, auth_pass, sm3_pass if doc is not None else None
                )
                print_color_text(f"密码重置成功: {new_pass}", BLUE)
        # 账号密码错误 或 未开启认证
        except OperationFailure as ofe:
            with MongoClient("mongodb://127.0.0.1:27017/") as client:
                db = client["upm"]
                # 确认是否国密版本
                doc = db.admin.find_one({"sm3Password": {"$exists": True}})
                ResetPassword.update_db(
                    db, auth_pass, sm3_pass if doc is not None else None
                )
                print_color_text(f"密码重置成功: {new_pass}", BLUE)
        # 端口不对 或 不存在, 执行OS操作
        except ServerSelectionTimeoutError as e:
            # print_color_text(f"ERROR: {e}", RED)
            opensearch_url = "http://localhost:9201/"
            index_name = "upm-admin"
            username = "elastic"
            password = "N*(T#^72d"
            # 组成完整url
            url = f"{opensearch_url}/{index_name}/_update_by_query?conflicts=proceed"
            # 修改对象
            authPwd_query = {
                "script": {
                    "source": "ctx._source.authPwd = params.authPwd; ctx._source.pwdHistorys = params.pwdHistorys; ctx._source.historySalt = params.historySalt",
                    "lang": "painless",
                    "params": {
                        "authPwd": auth_pass,
                        "pwdHistorys": [],
                        "historySalt": [],
                    },
                },
                # 查询条件
                "query": {"bool": {"must": [{"term": {"authIsRoot": True}}]}},
            }
            # 修改对象
            sm3Pwd_query = {
                "script": {
                    "source": "ctx._source.sm3Password = params.sm3Password; ctx._source.pwdHistorys = params.pwdHistorys; ctx._source.historySalt = params.historySalt",
                    "lang": "painless",
                    "params": {
                        "sm3Password": sm3_pass,
                        "pwdHistorys": [],
                        "historySalt": [],
                    },
                },
                # 查询条件
                "query": {"bool": {"must": [{"term": {"authIsRoot": True}}]}},
            }

            # 发送修改请求
            auth_response = requests.post(
                url,
                auth=HTTPBasicAuth(username, password),
                json=authPwd_query,
                headers={"Content-Type": "application/json"},
            )
            sm3_response = requests.post(
                url,
                auth=HTTPBasicAuth(username, password),
                json=sm3Pwd_query,
                headers={"Content-Type": "application/json"},
            )

            if auth_response.status_code in (200, 201) and sm3_response.status_code in (
                200,
                201,
            ):
                print_color_text(f"密码重置成功: {new_pass}", BLUE)
            else:
                print_color_text(f"密码重置失败: {new_pass}", BLUE)

        except Exception as e:
            print_color_text(f"ERROR: {e}", RED)

    def ras():
        account = subprocess.run(
            ["/bin/cat", "/etc/csrass/account.v1.conf", "|", "grep", "admin"],
            capture_output=True,
            text=True,
        )
        output = account.stdout.strip()

        if "csadmin" in output:
            res = subprocess.run(
                ["/usr/local/bin/csrass/tools", "-U", "csadmin@local"],
                capture_output=True,
                text=True,
            )
            print_color_text(res.stdout, BLUE)

        else:
            res = subprocess.run(
                ["/usr/local/bin/csrass/tools", "-U", "admin@local"],
                capture_output=True,
                text=True,
            )
            print_color_text(res.stdout, BLUE)
